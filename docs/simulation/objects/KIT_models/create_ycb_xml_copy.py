import os
import trimesh
import argparse
import shutil
import random

"""
Creates Mujoco compatible XML files from converted KIT data.
This looks through all the KIT objects you have downloaded in a particular 
folder, and creates Mujoco compatible XML files from a set of templates.
you can change resolution here from[800,5k,25k,Orig], we set the default resolution is origin[Orig].
Notice that not all Orig resolution have _tex_.obj
    XXX_Orig.(obj|wrl|mdl) - this is the original resolution, usually between 200,000 and 400,000 faces
    XXX_25k.(obj|wrl) - this is a reduced version to approximately 25,000 faces
    XXX_5k.(obj|wrl) - this is a reduced version to approximately 5,000 faces
    XXX_800.(obj|wrl) - this is the lowest resolution at approximately 800 faces
"""

# Define folders & paths
default_folder = "./objects"
default_template_folder = os.path.join("templates", "ycb")
default_resolution="Orig"
if __name__ == "__main__":

    print("Creating Mujoco compatible XML files...")

    # Parse arguments
    parser = argparse.ArgumentParser(description="Model Importer")
    parser.add_argument("--downsaargparsemple-ratio", type=float, default=1,
                        help="Mesh vertex downsample ratio (set to 1 to leave meshes as they are)")
    parser.add_argument("--template-folder", type=str, default=default_template_folder,
                        help="Location of YCB models (defaults to ./templates/ycb)")
    parser.add_argument("--mesh-folder", type=str, default=default_folder,
                        help="Location of YCB models (defaults to ./objects)")
    parser.add_argument("--resolution", type=str, default=default_resolution,
                        help="Orig/25k/5k/800 (defaults to Orig)")

    args = parser.parse_args()

    # Get the list of all downloaded mesh folders
    folder_names = os.listdir(args.mesh_folder)
    resolution=args.resolution
    # Get the template files to copy over
    model_template_file = os.path.join(args.template_folder, "template.xml")
    visual_template_file = os.path.join(args.template_folder, "visual.xml")
    with open(model_template_file, "r") as f:
        model_template_text = f.read()
    with open(visual_template_file, "r") as f:
        visual_template_text = f.read()

    #mass_list = {}
    #longitude_list = {}
    
    # Now loop through all the folders
    for folder in folder_names:
        if folder != "template" and folder != ".DS_Store" and folder!="extract_command.sh" and folder!="namelist.txt":
            try:
                print("Creating Mujoco XML files for {} ...".format(folder))
                # Extract model name, folder, ID
                model_long = folder
                model_short = folder[4:]
                model_folder = os.path.join(args.mesh_folder, model_long)

                #id_with_leading_zeroes = folder[:3]
                #id_strip = id_with_leading_zeroes.lstrip("0")
                #id = f'{int(id_strip):04d}'
                id = f'{int(folder[:3]):04d}'
                #/home/charles/KIT_models_tool/objects/191_OrangeMarmelade/OrangeMarmelade_Orig_tex.stl
                mesh_file = os.path.join(model_folder,model_short+"_"+resolution+"_tex.stl")
                print("mesh_file:"+mesh_file)
                texture_file = os.path.join(model_folder,model_short+"_"+resolution+"_tex.png")          
                mesh = trimesh.load(mesh_file)
                print("test here")    
                
                # keep objects  0.1 kg <= mass <= 1 kg, 4 cm <= longitude = 7 cm
                mass_max = 1.0
                mass_min = 0.1
                longitude_max = 0.07
                longitude_min = 0.04

                mass = 1.1                

                if mass > mass_max:
                    mass = random.uniform(mass_min, mass_max)

                mass_text = str(mass)
                # mass_list[id]=mass
                height=0.08
                radius_x=0.08
                radius_y=0.09
                if height > longitude_max:
                    height_rand = random.uniform(longitude_min, longitude_max)
                else:
                    height_rand = height
                if radius_x > longitude_max:
                    radius_x_rand = random.uniform(longitude_min/2, longitude_max/2)
                else:
                    radius_x_rand = radius_x
                if radius_y > longitude_max:
                    radius_y_rand = random.uniform(longitude_min/2, longitude_max/2)
                else:
                    radius_y_rand = radius_y

                # given x, y, z, if(min(x,y,z))>=7cm, x'/y'/z'=rand() ,scale=R[x/y/z]= (x'/y'/z')/(x/y/z)
                min_longitude = min(radius_x, radius_y, height)
                longitude = {radius_x: radius_x_rand, radius_y: radius_y_rand, height: height_rand}
                ratio = longitude[min_longitude] / min_longitude

                # convert dimensions to strings for renaming templates
                bottom_text = str(-height_rand/2)
                upper_text = str(height_rand/2)
                radius_text = str(max(radius_x_rand, radius_y_rand))
                vertical_radius_text = str(height_rand)
                ratio_text = str(ratio)
                # longitude_list[id] = (height_rand, min(radius_x_rand, radius_y_rand)*2)

                # moments of inertia
                tf = mesh.principal_inertia_transform
                inertia = trimesh.inertia.transform_inertia(tf, mesh.moment_inertia)
                # Center of mass
                com_vec = mesh.center_mass.tolist()
                com_text = ' '.join(map(str, com_vec))
                com_text = str(com_text)

                # Create a downsampled mesh file with a subset of vertices and faces
                #if args.downsample_ratio < 1:
                #    mesh_pts = mesh.vertices.shape[0]
                #    num_pts = int(mesh_pts * args.downsample_ratio)
                #    (_, face_idx) = mesh.sample(num_pts, True)
                #    downsampled_mesh = mesh.submesh((face_idx,), append=True)
                #    with open(os.path.join(model_folder, "downsampled.obj"), "w") as f:
                #        downsampled_mesh.export(f, "obj")
                #    collision_mesh_text = model_long + "/downsampled.obj"
                #else:
                #    collision_mesh_text = model_long + "/" + mesh_type + "/textured.obj"


                texture_path = texture_file
                untextured_path = mesh_file

                # rename mesh and texture file as model_short.msh / model_short.png / untextured+model_short.stl
                
                texture_model_short_file = model_short + '.png'
                untex_mesh_model_short_file = mesh_file

                model_text = model_template_text.replace("$ID", id)
                model_text = model_text.replace("$MODEL_SHORT", model_short)
                model_text = model_text.replace("$MODEL_LONG", model_long)
                model_text = model_text.replace("$mesh_folder", args.mesh_folder)
                model_text = model_text.replace("$MASS", mass_text)
                model_text = model_text.replace("$BOTTOM", bottom_text)
                model_text = model_text.replace("$UPPER", upper_text)
                model_text = model_text.replace("$RADIUS", radius_text)
                model_text = model_text.replace("$VERTICAL_RADIUS", vertical_radius_text)
                model_text = model_text.replace("$RATIO", ratio_text)
                model_text = model_text.replace("$COM", com_text)
                model_text = model_text.replace("$IXX", str(inertia[0][0]))
                model_text = model_text.replace("$IYY", str(inertia[1][1]))
                model_text = model_text.replace("$IZZ", str(inertia[2][2]))
                model_text = model_text.replace("$IXY", str(inertia[0][1]))
                model_text = model_text.replace("$IXZ", str(inertia[0][2]))
                model_text = model_text.replace("$IYZ", str(inertia[1][2]))
                model_text = model_text.replace("$MESH_MODEL_SHORT_FILE", untex_mesh_model_short_file)
                model_text = model_text.replace("$TEXTURE_MODEL_SHORT_FILE", texture_model_short_file)

                # creating model_name.xml inside each model_folder
                model_text_name = model_text
                model_text_name = model_text_name.replace("$ADDRESS", ".")
                with open(os.path.join(model_folder, model_short + ".xml"), "w") as f:
                    f.write(model_text_name)
                # creating oXXXX.xml objects and put them inside the "objects" folder
                # ycb format is 001-072 but our encoding is 0001-1296
                model_text_oXXXX = model_text
                model_path = os.path.join( args.mesh_folder, model_long )
                model_text_oXXXX = model_text_oXXXX.replace("$ADDRESS", "../" + model_path)
                with open( os.path.join("./objects", "o" + id + ".xml"), "w") as f:
                    f.write(model_text_oXXXX)
                    
                # Copy and modify the visual file template
                visual_text = visual_template_text.replace("$ID", id)
                visual_text = visual_text.replace("$MODEL_SHORT", model_short)
                visual_text = visual_text.replace("$MODEL_LONG", model_long)
                visual_text = visual_text.replace("$MASS", mass_text)
                visual_text = visual_text.replace("$UPPER", upper_text)
                visual_text = visual_text.replace("$BOTTOM", bottom_text)
                visual_text = visual_text.replace("$RADIUS", radius_text)
                visual_text = visual_text.replace("$VERTICAL_RADIUS", vertical_radius_text)
                visual_text = visual_text.replace("$RATIO", ratio_text)
                visual_text = visual_text.replace("$UNTEX_MESH_MODEL_SHORT_FILE", untex_mesh_model_short_file)

                # creating model_name_visual.xml inside each model_folder
                visual_text_name = visual_text
                visual_text_name = visual_text_name.replace("$ADDRESS", ".")
                with open(os.path.join(model_folder, model_short + "v" + ".xml"), "w") as f:
                    f.write(visual_text)
                    
                # creating oXXXX_visual.xml objects and put them inside the "objects" folder
                visual_text_oXXXX = visual_text
                visual_text_oXXXX = visual_text_oXXXX.replace("$ADDRESS", "../" + model_path)
                with open( os.path.join("./objects", "o" + id + "v" + ".xml"), "w") as f:
                    f.write(visual_text_oXXXX)

               


            except:
                print("Error processing {}. Textured mesh likely does not exist for this object.".format(folder))
  
    print("Generation Completed.")
    #res1 = {key: val for key, val in sorted(mass_list.items(), key=lambda ele: ele[0])}
    #res2 = {key: val for key, val in sorted(longitude_list.items(), key=lambda ele: ele[0])}
    #print(res1)
    #print(res2)


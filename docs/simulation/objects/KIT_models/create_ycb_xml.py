import os
import trimesh
import argparse
import pandas as pd
import shutil
import random

# Define folders & paths
default_ycb_folder = "KIT_mesh"
default_template_folder = os.path.join("templates", "ycb")

#/home/charles/processed/       band_aid_sheer_strips/meshes/optimized_tsdf_texture_mapped_mesh.obj
#/home/charles/ycb/models/ycb/  001_chips_can/         tsdf          /textured.obj
#             /KIT_mesh\191_OrangeMarmelade\meshes\OrangeMarmelade_25k_tex.png
#             /KIT_mesh\191_OrangeMarmelade\meshes\OrangeMarmelade_25k_tex.obj
#             /templates\ycb\template.xml
if __name__ == "__main__":

    print("Creating files to use KIT objects in Mujoco...")

    # Parse arguments
    parser = argparse.ArgumentParser(description="YCB Model Importer")
    parser.add_argument("--downsaargparsemple-ratio", type=float, default=1,
                        help="Mesh vertex downsample ratio (set to 1 to leave meshes as they are)")
    parser.add_argument("--template-folder", type=str, default=default_template_folder,
                        help="Location of YCB models (defaults to ./templates/ycb)")
    parser.add_argument("--ycb-folder", type=str, default=default_ycb_folder,
                        help="Location of YCB models (defaults to ./models/ycb)")

    args = parser.parse_args()
    
    # Get the list of all downloaded mesh folders
    folder_names = os.listdir(args.ycb_folder)

    # Get the template files to copy over
    model_template_file = os.path.join(args.template_folder, "template.xml")
    visual_template_file = os.path.join(args.template_folder, "visual.xml")
    with open(model_template_file, "r") as f:
        model_template_text = f.read()
    with open(visual_template_file, "r") as f:
        visual_template_text = f.read()

    print (model_template_file,"\n")
    
    print ("args.ycb_folder:",args.ycb_folder)
    #print ()

    # Now loop through all the folders
    for folder in folder_names:
        #if folder != "template" and folder != ".DS_Store":
        #print ("tryyyyy")
        try:
            #print("tryyyyy")
            print("Creating Mujoco XML files for {} ...".format(folder))
                
                # Extract model name, folder, ID
            model_long = folder
            #print("tryyyyy1")
            model_short = folder[4:]
            #print("tryyyyy2")
            model_folder = os.path.join(args.ycb_folder, model_long)
            #print("tryyyyy3")
            id_with_leading_zeroes = folder[:3]
            #print("tryyyyy4")
            id_strip = id_with_leading_zeroes.lstrip("0")
            #print("tryyyyy5")
            id = f'{int(id_strip):04d}'
 
            mesh_file = os.path.join(model_folder, "meshes", model_short+"_25k_tex.obj")
            texture_file = model_short+"_25k_texh.png"
            print ("mesh_file:",mesh_file,"\n")
            print ("model_folder:",model_folder,"\n")
            print ("id:",id,"\n")

            mesh = trimesh.load(mesh_file)

            # keep objects  0.1 kg <= mass <= 1 kg, 4 cm <= longitude = 7 cm
            mass_max = 1.0
            mass_min = 0.1
            longitude_max = 0.07
            longitude_min = 0.04

            mass=1.1
            if mass > mass_max:
                mass = random.uniform(mass_min, mass_max)

            mass_text = str(mass)
                # mass_list[id]=mass

                # given object id , get dimensions (m) from excel
                #if df.longitude3[excel_id] != 0:
                #    height = df.longitude3[excel_id]/1000.0
                #    radius_x = df.longitude1[excel_id]/2000.0
                #    radius_y = df.longitude2[excel_id]/2000.0
                #elif df.longitude3[excel_id] == 0 and df.longitude2[excel_id] != 0:
                #    height = df.longitude2[excel_id]/1000.0
                #    radius_x = radius_y = df.longitude1[excel_id]/2000.0
                #else:
                #    height = df.longitude1[excel_id]/1000.0
                #    radius_x = radius_y = df.longitude1[excel_id]/2000.0
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
            #print("tryyyyy8")
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
            #print("tryyyyy9")
            print("9:",args.ycb_folder)
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
            #/home/charles/processed/       band_aid_sheer_strips/meshes/optimized_tsdf_texture_mapped_mesh.obj
            collision_mesh_text = model_long + "/" + "meshes" + "/"+model_short+"_25k_tex.obj"
            #print("tryyyyy10")        
                # Convert_obj_2_mujoco_msh
            mujoco_mesh_text = os.path.join(args.ycb_folder, collision_mesh_text)
            print(mujoco_mesh_text)
            command = 'python3 convert_obj_to_mujoco_msh.py' + ' ' + "./" + mujoco_mesh_text
            os.system(command)

            mesh_file = os.path.join(model_folder, "meshes",model_short+"_25k_tex.msh")
            texture_path = os.path.join(model_folder, "meshes", model_short+"_25k_tex.png")
                #untextured_path = os.path.join(model_folder, "tsdf", "nontextured.stl")

                # rename mesh and texture file as model_short.msh / model_short.png / untextured+model_short.stl

            mesh_model_short_file = model_long
            texture_model_short_file = model_long

                #untex_mesh_model_short_file = 'untextured_' + model_short + '.stl'
            

            print("model_long:",model_long)
            print("model_short:",model_short)
            print("mesh_model_short_file:",mesh_model_short_file)
            print("model_folder:",model_folder)
            print("texture_model_short_file:",texture_model_short_file)
            #model_long:            191_OrangeMarmelade
            #model_short:               OrangeMarmelade
            #mesh_model_short_file: 191_OrangeMarmelade
            #model_folder: KIT_mesh/191_OrangeMarmelade
            #texture_model_short_file: 191_OrangeMarmelade


            model_text = model_template_text.replace("$ID", id)
            model_text = model_text.replace("$MODEL_SHORT", model_short)
            model_text = model_text.replace("$MODEL_SHORT_mesh", model_short)
            model_text = model_text.replace("$MODEL_LONG", model_long)
            model_text = model_text.replace("$YCB_FOLDER", args.ycb_folder)
            model_text = model_text.replace("$MESH_TYPE", mesh_type)
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
            model_text = model_text.replace("$MESH_MODEL_SHORT_FILE", mesh_model_short_file)
            model_text = model_text.replace("$TEXTURE_MODEL_SHORT_FILE", texture_model_short_file)
            
                # creating model_name.xml inside each model_folder
            model_text_name = model_text
            #model_text_name = model_text_name.replace("$ADDRESS", ".")
            #print("tryyyyy13")
            print(os.path.join("processed",model_folder, model_short + ".xml"))
            with open(os.path.join(model_folder, model_short + ".xml"), "w") as f:
                f.write(model_text_name)
            #print("tryyyyy14")        
                # creating oXXXX.xml objects and put them inside the "objects" folder
                # ycb format is 001-072 but our encoding is 0001-1296
            model_text_oXXXX = model_text
            model_path = os.path.join( args.ycb_folder, model_long )
            model_text_oXXXX = model_text_oXXXX.replace("$ADDRESS", "../" + model_path)
            with open( os.path.join("./objects", "o" + id + ".xml"), "w") as f:
                f.write(model_text_oXXXX)
                    
                # Copy and modify the visual file template
                #visual_text = visual_template_text.replace("$ID", id)
                #visual_text = visual_text.replace("$MODEL_SHORT", model_short)
                #visual_text = visual_text.replace("$MODEL_LONG", model_long)
                #visual_text = visual_text.replace("$MESH_TYPE", mesh_type)
                #visual_text = visual_text.replace("$MASS", mass_text)
                #visual_text = visual_text.replace("$UPPER", upper_text)
                #visual_text = visual_text.replace("$BOTTOM", bottom_text)
                #visual_text = visual_text.replace("$RADIUS", radius_text)
                #visual_text = visual_text.replace("$VERTICAL_RADIUS", vertical_radius_text)
                #visual_text = visual_text.replace("$RATIO", ratio_text)
                #visual_text = visual_text.replace("$UNTEX_MESH_MODEL_SHORT_FILE", untex_mesh_model_short_file)

                # creating model_name_visual.xml inside each model_folder
                #visual_text_name = visual_text
                #visual_text_name = visual_text_name.replace("$ADDRESS", ".")
                #with open(os.path.join(model_folder, model_short + "v" + ".xml"), "w") as f:
                #    f.write(visual_text)
                    
                # creating oXXXX_visual.xml objects and put them inside the "objects" folder
                #visual_text_oXXXX = visual_text
                #visual_text_oXXXX = visual_text_oXXXX.replace("$ADDRESS", "../" + model_path)
                #with open( os.path.join("./objects", "o" + id + "v" + ".xml"), "w") as f:
                #    f.write(visual_text_oXXXX)

                # copy files
            original_mesh = mesh_file
            target_mesh = './objects/meshes/' + mesh_model_short_file
            shutil.copyfile(original_mesh, target_mesh)

                #original_untextured_mesh = untextured_path
                #target_untextured_mesh = './objects/meshes/' + untex_mesh_model_short_file
                #shutil.copyfile(original_untextured_mesh, target_untextured_mesh)

            original_texture = texture_path
            target_texture = './textures/' + texture_model_short_file
            shutil.copyfile(original_texture, target_texture)


        except:
            print("Error processing {}. Textured mesh likely does not exist for this object.".format(folder))
  
    print("Generation Completed.")
    #res1 = {key: val for key, val in sorted(mass_list.items(), key=lambda ele: ele[0])}
    #res2 = {key: val for key, val in sorted(longitude_list.items(), key=lambda ele: ele[0])}
    #print(res1)
    #print(res2)


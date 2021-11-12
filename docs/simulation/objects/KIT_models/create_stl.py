import os


# Define folders & paths
mesh_folder = "KIT_mesh"
default_template_folder = os.path.join("templates", "ycb")
default_resolution="Orig"
resolution=default_resolution 
#you can change resolution here from[800,5k,25k,Orig]
#   Notice that not all Orig resolution have _tex_.obj
#    XXX_Orig.(obj|wrl|mdl) - this is the original resolution, usually between 200,000 and 400,000 faces
#    XXX_25k.(obj|wrl) - this is a reduced version to approximately 25,000 faces
#    XXX_5k.(obj|wrl) - this is a reduced version to approximately 5,000 faces
#    XXX_800.(obj|wrl) - this is the lowest resolution at approximately 800 faces

if __name__=="__main__":
    print("Creating STL files from KIT database's OBJ...")
    folder_names = os.listdir(mesh_folder)
    for folder in folder_names:
        try:
            print("Creating STL files for {} ...".format(folder))

            model_long = folder            
            model_short = folder[4:]            
            
            stl_text = "KIT_mesh/"+model_long + "/" + "meshes" + "/"+model_short+"_"+resolution+"_tex.stl"
            png_text = "KIT_mesh/"+model_long + "/" + "meshes" + "/"+model_short+"_"+resolution+"_tex.png"
            mesh_text = "KIT_mesh/"+model_long + "/" + "meshes" + "/mesh.obj"
            stl_final_location="objects/"+model_long + "/"+model_short+"_"+resolution+"_tex.stl"
            png_final_location="objects/"+model_long + "/"+model_short+"_"+resolution+"_tex.png"
            mujoco_mesh_text = "./"+mesh_folder+"/"+model_long + "/" + "meshes" + "/"+model_short+"_"+resolution+"_tex.obj"
            
            print("obj mesh location:"+mujoco_mesh_text)
            commandMv1="mv ./"+mujoco_mesh_text+" "+mesh_text
            os.system(commandMv1)
            
            command = 'python3 ./obj2stl/convert.py -i ./' + mesh_text+' -o ./'+stl_text+" -t obj"
            commandMv2="mv ./"+mesh_text+" "+mujoco_mesh_text
            commandCp1 = 'cp ./'+stl_text+' ./'+stl_final_location
            commandCp2 = 'cp ./'+png_text+' ./'+png_final_location

            os.system(command)
            os.system(commandMv2)
            
            #move stl and png file to the ./objects
            os.system(commandCp1)
            os.system(commandCp2)


        except:
            print("Creating Failed for {}.",format(folder))
    print ("Finishe creating .STL")
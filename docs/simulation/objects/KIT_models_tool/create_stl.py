import os


#The script is written by Python3. Ruby are needed to execute part of script.
# Define folders & paths
mesh_folder = "KIT_mesh"
default_template_folder = os.path.join("templates", "ycb")
default_resolution="Orig"
default_target_folder="objects"
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
            ruby_text = "convertSTL.rb"
            stl_final_location=default_target_folder+"/"+model_long + "/"+model_short+"_"+resolution+"_tex.stl"
            png_final_location=default_target_folder+"/"+model_long + "/"+model_short+"_"+resolution+"_tex.png"
            ruby_final_location=default_target_folder+"/"+model_long + "/"+"convertSTL.rb"
            mujoco_mesh_text = "./"+mesh_folder+"/"+model_long + "/" + "meshes" + "/"+model_short+"_"+resolution+"_tex.obj"
            
            print("obj mesh location:"+mujoco_mesh_text)
            commandMv1="mv ./"+mujoco_mesh_text+" "+mesh_text
            os.system(commandMv1)
            
            #use external python3 script to create ASCII stl
            command = 'python3 ./obj2stl/convert.py -i ./' + mesh_text+' -o ./'+stl_text+" -t obj"
            #use ruby script to convert ASCII stl to Binary.
            commandBinary ='cd '+ 'ruby ./convertSTL.rb ./'+stl_text
            commandMv2="mv ./"+mesh_text+" "+mujoco_mesh_text
            commandCp1 = 'cp ./'+stl_text+' ./'+stl_final_location
            commandCp2 = 'cp ./'+png_text+' ./'+png_final_location
            commandCp3 = 'cp ./'+ruby_text+" ./"+ruby_final_location
            commandBinary = 'cd ./objects/'+model_long+'\n ruby ./convertSTL.rb '+model_short+"_"+resolution+"_tex.stl"
            commandRM = 'cd ./objects/'+model_long+'\n rm -f convertSTL.rb'
            os.system(command)
                        
            #os.system(commandBinary)
            os.system(commandMv2)
            
            #move stl and png file to the ./objects
            os.system(commandCp1)
            os.system(commandCp2)

            #convert ASCII stl files to BINARY (only binary meshes can be used in Mujoco) 
            os.system(commandCp3)
            os.system(commandBinary)
            os.system(commandRM)
        except:
            print("Creating Failed for {}.",format(folder))
    print ("Finished creating .STL")
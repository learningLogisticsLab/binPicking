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
            print("Creating XML files for {} ...".format(folder))
        except:
            print("Creating Failed for {}.",format(folder))
    print ("Finishe creating .XML")
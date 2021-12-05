import os
"""
Please place xml_tester.py inside mujoco bin directory "~/.mujoco/mujoco200/bin" where the executable "simulate.exe" is located. The folder "objects_visuals_oXXXX" should also be placed in the mujoco200 directory "~/.mujoco/mujoco200". This script will then simulate all oXXXX objects inside objects_visuals_oXXXX on mujoco automatically. The user can close the simulator to view the next xml object.
"""

# Define folders
default_ycb_folder = os.path.join("models", "ycb")
default_template_folder = os.path.join("templates", "ycb")

if __name__ == "__main__":

    print("Montage of Mujoco XML objects...")

    # Get the list of all downloaded mesh folders
    objects = os.listdir("../objects_visuals_oXXXX")
    
    # Now loop through all the folders
    for object in objects:
        if object[6:12] != "visual":
            try:
                print("Showing Mujoco XML files for {} ...".format(object))
                    
                command = './simulate' + ' ' + "../objects_visuals_oXXXX" + "/" + object
                os.system(command)
                
            except:
                print("Error processing {}. Textured mesh likely does not exist for this object.".format(object))
 
    print("Generation Completed.")

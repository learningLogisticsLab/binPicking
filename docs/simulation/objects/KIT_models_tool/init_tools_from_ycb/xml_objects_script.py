import os
import argparse

"""
Imports xml_objects 
"""

# Define folders
default_object_folder = "./objects"
default_template_folder = os.path.join("templates", "ycb")

if __name__ == "__main__":

    print("Importing xml_objects...")

    # Parse arguments
    parser = argparse.ArgumentParser(description="YCB Model Importer")
    parser.add_argument("--template-folder", type=str, default=default_template_folder,
                        help="Location of YCB models (defaults to ./templates/ycb)")
    parser.add_argument("--object-folder", type=str, default=default_object_folder,
                        help="Location of YCB models (defaults to ./objects)")

    args = parser.parse_args()

    # Get the list of all downloaded mesh folders
    folder_names = os.listdir(args.object_folder)
    folder_names.sort()

    # Get the template files to copy over
    object_template_file = os.path.join(args.template_folder, "xml_objects_template.py")
    object_header_file = os.path.join(args.template_folder, "objects_header.py")
    with open(object_template_file, "r") as f:
        object_template_text = f.read()
    with open(object_header_file, "r") as f:
        object_header_text = f.read()
    
    # write file header to include libraries
    with open( "xml_objects_created.py" , "w") as f:
                    f.write(object_header_text)
    
    # Now loop through all the oXXXX folders
    for folder in folder_names:
        if folder[5] != "v" and folder != "meshes" and folder != ".DS_Store":
            ID = folder[:5]
            print(folder)
            model_file = os.path.join(args.object_folder, folder)
            model_visual_file = os.path.join(args.object_folder, ID + "v.xml")
            
            # copy and modify object template file
            object_text = object_template_text.replace("$ObjectName", ID)
            object_text = object_text.replace("$VisualObjectName", ID + "v")
            object_text = object_text.replace("$LocationXML", model_file)
            object_text = object_text.replace("$LocationVisualXML", model_visual_file)
                    
            with open( "xml_objects_created.py" , "a") as f:
                    f.write(object_text)
            
    print("Generation Completed.")

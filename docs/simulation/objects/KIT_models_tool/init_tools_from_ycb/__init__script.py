import os
import argparse

"""
Append header
Append template
Loop through all folders and Append "tab+objects"
Append bottom
"""

# Define folders
default_init_folder = "./objects"
default_template_folder = os.path.join("templates", "ycb")

if __name__ == "__main__":

    print("Adding objects list to __init__.py...")

    # Parse arguments
    parser = argparse.ArgumentParser(description="YCB Model Importer")
    parser.add_argument("--template-folder", type=str, default=default_template_folder,
                        help="Location of YCB models (defaults to ./templates/ycb)")
    parser.add_argument("--init-folder", type=str, default=default_init_folder,
                        help="Location of YCB models (defaults to ./objects_visuals_oXXXX)")

    args = parser.parse_args()

    # Get the list of all downloaded mesh folders
    folder_names = os.listdir(args.init_folder)
    folder_names.sort()

    # Get the template files to copy over
    init_header_file = os.path.join(args.template_folder, "init_header.py")
    init_template_file = os.path.join(args.template_folder, "init_template.py")
    init_bottom_file = os.path.join(args.template_folder, "init_bottom.py")
    with open(init_header_file, "r") as f:
        init_header_text = f.read()
    with open(init_template_file, "r") as f:
        init_template_text = f.read()
    with open(init_bottom_file, "r") as f:
        init_bottom_text = f.read()
        
    # write file header to include libraries
    with open( "__init__created.py" , "w") as f:
                    f.write(init_header_text)
    
    # append body template
    with open( "__init__created.py" , "a") as f:
                    f.write(init_template_text)
                    
    # Now loop through all the oXXXX folders
    for folder in folder_names:
        if folder[5] != "v" and folder != "meshes" and folder != ".DS_Store":
            ID = folder[:5]
            object_text = "    " + ID + "," + "\n"
            visual_text = "    " + ID + "v" + "," + "\n"
            
            # append oXXXX to the list
            with open( "__init__created.py" , "a") as f:
                    f.write(object_text)
            
            # append oXXXX visual to the list
            with open( "__init__created.py" , "a") as f:
                    f.write(visual_text)
            
            
                    
    # append bottom file to import dependencies
    with open( "__init__created.py" , "a") as f:
                    f.write(init_bottom_text)
            
    print("Generation Completed.")

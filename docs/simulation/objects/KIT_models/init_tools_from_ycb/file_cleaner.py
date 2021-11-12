import os
import argparse
import shutil

default_ycb_folder = os.path.join("models", "ycb")

if __name__ == "__main__":
    print("Copying textures, meshes, to fit in robosuite directory...")

    # Parse arguments
    parser = argparse.ArgumentParser(description="Parser")
    parser.add_argument("--ycb-folder", type=str, default=default_ycb_folder,
                        help="Location of YCB models (defaults to ./models/ycb)")

    args = parser.parse_args()

    # Get the list of all downloaded mesh folders
    folder_names = os.listdir(args.ycb_folder)

    for folder in folder_names:
        model_long = folder
        model_short = folder[4:]
        folder_path = os.path.join(args.ycb_folder, model_long)

        try:
            # Check if there are Google meshes; else use the TSDF folder
            if "google_16k" in os.listdir(folder_path):
                mesh_type = "google_16k"
            else:
                mesh_type = "tsdf"

            # Extract key data from the mesh
            if mesh_type == "google_16k":
                mesh_file = os.path.join(folder_path, "google_16k", "textured.msh")
                texture_file = os.path.join(folder_path, "google_16k", "texture_map.png")
            elif mesh_type == "tsdf":
                mesh_file = os.path.join(folder_path, "tsdf", "textured.msh")
                texture_file = os.path.join(folder_path, "tsdf", "textured.png")

            original_mesh = mesh_file
            target_mesh = './objects/meshes/' + model_short + '.msh'
            shutil.copyfile(original_mesh, target_mesh)

            original_texture = texture_file
            target_texture = './textures/' + model_short + '.png'
            shutil.copyfile(original_texture, target_texture)

        except:
            print("{} trash file found, please ignore.". format(folder))


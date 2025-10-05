import os
import shutil
import argparse

def copy_folder_to_subfolders(src_folder, target_dir, subfolder_name):
    """
    Copy the specified folder into a new subfolder within each subdirectory of the target directory.

    Args:
        src_folder (str): Path to the source folder to copy.
        target_dir (str): Path to the target directory where the subfolders reside.
        subfolder_name (str): Name of the subfolder to create within each subdirectory.
    """
    for subdir in os.listdir(target_dir):
        subdir_path = os.path.join(target_dir, subdir)
        
        if os.path.isdir(subdir_path):  # Ensure it's a directory
            # Define the new subfolder path using the specified name
            new_subfolder_path = os.path.join(subdir_path, subfolder_name)
            os.makedirs(new_subfolder_path, exist_ok=True)  # Create the folder if it doesn't exist

            # Define the destination folder path within the new subfolder
            dest_folder_path = os.path.join(new_subfolder_path, os.path.basename(src_folder))
            
            # Copy the source folder to the destination
            try:
                shutil.copytree(src_folder, dest_folder_path)
                print(f"Copied {src_folder} to {dest_folder_path}")
            except FileExistsError:
                print(f"{dest_folder_path} already exists. Skipping copy.")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Copy a folder to a subfolder within each subdirectory of the target directory."
    )
    parser.add_argument(
        "src_folder",
        type=str,
        help="Path to the source folder to copy."
    )
    parser.add_argument(
        "target_dir",
        type=str,
        help="Path to the target directory where the subfolders reside."
    )
    parser.add_argument(
        "subfolder_name",
        type=str,
        help="Name of the subfolder to create within each subdirectory."
    )

    args = parser.parse_args()

    # Call the function with parsed arguments
    copy_folder_to_subfolders(args.src_folder, args.target_dir, args.subfolder_name)

if __name__ == "__main__":
    main()

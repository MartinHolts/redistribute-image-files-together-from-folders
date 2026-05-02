import os
import shutil
import sys

def consolidate_images():
    # Get the directory where the EXE or script is running
    if getattr(sys, 'frozen', False):
        current_dir = os.path.dirname(sys.executable)
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))

    output_folder_name = "All_Images_Combined"
    output_path = os.path.join(current_dir, output_folder_name)

    # Common image extensions
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Walk through all directories and files
    for root, dirs, files in os.walk(current_dir):
        # Skip the output folder itself to avoid infinite loops
        if output_path in root:
            continue

        for file in files:
            if file.lower().endswith(valid_extensions):
                source_file_path = os.path.join(root, file)
                
                # Handle duplicate filenames by appending a number
                dest_file_path = os.path.join(output_path, file)
                filename, extension = os.path.splitext(file)
                counter = 1
                
                while os.path.exists(dest_file_path):
                    dest_file_path = os.path.join(output_path, f"{filename}_{counter}{extension}")
                    counter += 1

                try:
                    shutil.copy2(source_file_path, dest_file_path)
                except:
                    pass

if __name__ == "__main__":
    consolidate_images()
    # The script ends here and the window will close automatically

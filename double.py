import os

directory_path = "../The_file_path_for_the_music_files_to_be_modified"

# Dictionnaire pour suivre les noms de fichiers identique
seen_file_names = {}

# Iterate through all files in the directory
for file_name in os.listdir(directory_path):
    full_path = os.path.join(directory_path, file_name)

    # Check if the item is a file and not a directory
    if os.path.isfile(full_path):
        if file_name in seen_file_names:
            # Duplicate file, delete it
            os.remove(full_path)
            print(f"Duplicated file removed: {file_name}")
        else:
            seen_file_names[file_name] = True

print("Duplicate file removal completed")

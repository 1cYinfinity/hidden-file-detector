import os
import concurrent.futures
import imghdr
import magic
import hashlib
import logging

logging.basicConfig(level=logging.INFO)

def calculate_file_hash(file_path):
    try:
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        logging.error(f"Error calculating hash for file {file_path}: {e}")
        return None

def process_file(file_path):
    try:
        file_hash = calculate_file_hash(file_path)
        if file_hash:
            with open(file_path, 'rb') as file:
                file_content = file.read(8192)  # Read a larger chunk of file content
                file_type = magic.from_buffer(file_content, mime=True)
                if 'image' in file_type or 'audio' in file_type or 'video' in file_type:
                    return file_path, file_type
                elif imghdr.what(file_path) is not None:
                    return file_path, "image/" + imghdr.what(file_path)
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
    return None, None  # Return None values in case of error

def main():
    directory = input("Enter the path of the directory to search for hidden files: ")
    hidden_files_found = []

    print("Searching for hidden files...")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for entry in os.scandir(directory):
            if entry.is_file():
                result = executor.submit(process_file, entry.path)
                hidden_files_found.append(result)

    print("Hidden files found:")
    for result in concurrent.futures.as_completed(hidden_files_found):
        file_path, file_type = result.result()
        if file_path:
            print(f"File: {file_path}, Type: {file_type}")

if __name__ == "__main__":
    main()

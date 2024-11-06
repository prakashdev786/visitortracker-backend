from flask import request
from werkzeug.utils import secure_filename
import os


def get_request_data():

    if request.is_json:  # If request has JSON content-type
        return request.get_json()
    else:  # For form data (application/x-www-form-urlencoded or multipart/form-data)
        data = request.form.to_dict()

        files = request.files.to_dict()  # Convert files to a dictionary

        data.update(files)
        return data




def save_image(image_data, fileName=None, folderName=None):
    if not image_data:
        return None

    # Base folder path
    base_folder = 'static/uploads'
    folder = base_folder  


    if folderName:
        folder = os.path.join(base_folder, folderName)

    # Create the directory if it does not exist
    os.makedirs(folder, exist_ok=True)


    filename = fileName if fileName else secure_filename(image_data.filename)


    filepath = os.path.join(folder, filename)


    image_data.save(filepath)


    return f"{folderName}/{filename}" if folderName else f"{filename}"

def remove_file(file_path):
    base_folder = 'static/uploads'
    new_file_path = os.path.join(base_folder, file_path)
    if os.path.isfile(new_file_path):
        try:
            print(new_file_path, 'new_file_path')
            os.remove(new_file_path)
        except Exception as e:
            print(f"Error removing file {new_file_path}: {str(e)}")
    else:
        print(f"File not found: {new_file_path}, cannot remove it.")


class DictToObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
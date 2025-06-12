import os
def get_files_info(working_directory, directory=None):

    working_directory = os.path.abspath(working_directory)
    
    if directory is None:
        directory = working_directory
    else:
        directory = os.path.abspath(f"{working_directory}/{directory}")
        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a valid directory'
    if not directory.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    file_info_template = f"-[file_name]: file_size:[file_size] bytes, is_dir=[is_dir_bool]"
    files_dict = {}
    files_in_dir = os.listdir(directory)

    for file in files_in_dir:
        file_name = file
        file_size = os.path.getsize(directory + "/" + file)
        is_dir_bool = os.path.isdir(directory + "/" + file)

        files_dict[file_name] = f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir_bool}"

    output_str = ""
    for file in files_dict.values():
        output_str += file + "\n"
        
    return output_str


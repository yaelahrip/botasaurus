import json
from os import path, makedirs, getcwd
from urllib.parse import urlparse

def remove_paths_from_url(url):
    """
    Removes the paths from a given URL.
    
    Args:
        url (str): The URL to remove paths from.
        
    Returns:
        str: The URL with the paths removed.
    """
    parsed_url = urlparse(url)
    
    # Construct the new URL with only the scheme, netloc, and port (if present)
    new_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    
    return new_url

def relative_path(target_path, goback=0):
    levels = [".."] * (goback + -1)
    return path.abspath(path.join(getcwd(), *levels, target_path.strip()))

def create_directory_if_not_exists(passed_path):
    dir_path = relative_path(passed_path, 0)
    if not path.exists(dir_path):
        makedirs(dir_path)

output_directory_created = False
def create_output_directory_if_not_exists():
    global output_directory_created
    # Check if output directory exists, if not, create it
    if not output_directory_created:
        create_directory_if_not_exists("output")
        create_directory_if_not_exists("output/responses")
        output_directory_created = True

 
def write_json_response(path, data,  indent=4):
    create_output_directory_if_not_exists()
    with open(path, 'w', encoding="utf-8") as fp:
        json.dump(data, fp, indent=indent)



def get_filename_from_response_headers(response):
    content_disposition = response.headers.get('Content-Disposition')
    filename = content_disposition.split('filename=')[1].strip('"')
    return filename
        
def write_file_response(file_path, filename, content ):
    create_output_directory_if_not_exists()
    
    fullpath = file_path + filename
    with open(fullpath, 'wb') as file:
        file.write(content)
    return fullpath
import guerilla
import os


def get_reference_file(dir_path):
    filelist = []
    for elements in os.listdir(dir_path):
        filepath = os.path.join(dir_path, elements)
        filelist.append(filepath)
    return filelist

def check_node_exists(node_full_path):
    """
    Check if node exist with full path
    """
    try:
        a = guerilla.pynode(node_full_path)
        test = True
    except:
        test = False
    return test


def get_Document_children(type, recursive=True):
    """
    Get all the current Document children recursively
    """
    document = guerilla.Document()
    names = []
    for node in guerilla.listchildren(document, type, recursive):
        names.append(node.name)
    return names


def get_data_from_asset_string(string_asset):
    """
    Return asset string as a dict
    """
    list = string_asset.split('/')
    data_dict = {'asset_category':list[0],
                 'asset_family':list[1],
                 'asset_name':list[2],
                 'asset_stage': list[3],
                 'asset_variant':list[4]}

    return data_dict


def print_reference_data(stage_name,
                         referenced_stage_name,
                         referenced_files_dir,
                         namespace,
                         new_objects,
                         string_asset,
                         referenced_string_asset):
    """
    Print references from hook reference
    """
    print("stage name", stage_name)
    print("referenced_stage_name", referenced_stage_name)
    print("referenced_files_dir name", referenced_files_dir)
    print("namespace", namespace)
    print("new_objects", new_objects)
    print("string_asset", string_asset)
    print("referenced_string_asset", referenced_string_asset)

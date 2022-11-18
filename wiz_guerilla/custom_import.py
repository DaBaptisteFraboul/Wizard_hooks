import guerilla

def get_new_name_from_data(data_dict):
    """
    Generate a custom new name from asset data
    """
    data = [data_dict['asset_family'],
            data_dict['asset_name'],
            data_dict['asset_variant']]

    parent_name = '_'.join(data)
    return parent_name

def create_custom_parent(parent_name):
    """
    Create custom node parent with name from reference data
    """
    custom = guerilla.pynode('CUSTOM')

    with guerilla.Modifier() as mod :
        parent_node = guerilla.Node.create(parent_name, 'SceneGraphNode', custom)

    return parent_node


def move_namespace_data(name_space, new_parent):
    """
    Move node with namespace
    """
    node = guerilla.pynode('CUSTOM|'+name_space)
    for graphs in node.children():
        graphs.move(new_parent)
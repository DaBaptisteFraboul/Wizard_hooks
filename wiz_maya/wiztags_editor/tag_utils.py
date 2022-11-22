import maya.cmds as cmds

# Module related to wizardTags attribute and selection


def get_cameras_transform_in_scene():
    """
    Get camera transforms in scene to blacklist them
    :return:
    """
    selection =cmds.ls(selection=False,  cameras=True)
    transforms = []
    for camera_shape in selection:
        cam_transform = cmds.listRelatives(camera_shape, parent=True)
        transforms.append(cam_transform[0])
    return transforms


def get_clean_selection(mode, object_blacklist) -> list:
    """
    Get a selection with only transforms and direct children transform if checked
    :param get_children:
    :return:
    """
    selection = []
    if mode == 'selection':
        selection = cmds.ls(selection=True, tr=True, objectsOnly = True, cameras=False)
    if mode == 'children':
        selection = cmds.ls(selection=True, tr=True, objectsOnly =True, cameras=False)
        for obj in selection :
            for children in cmds.listRelatives(obj, allDescendents = True):

                if cmds.nodeType(children) == 'transform' and children not in selection:
                    selection.append(children)
    if mode == 'all':
        selection = cmds.ls(tr = True,  cameras = False)
    print(object_blacklist, "objectblacklist")
    for blacklisted in object_blacklist:
        if blacklisted in selection:
            print("blacklisted", blacklisted)
            selection.remove(blacklisted)
    print("Selection", selection)
    return selection


def get_obj_material(obj: str) -> str:
    shader_groups = cmds.listConnections(cmds.listHistory(obj))
    if shader_groups :
        material = [mat for mat in cmds.ls(cmds.listConnections(shader_groups), materials = True)][0]
        return material

# Tags related functions


def create_wtags_attribute(obj) -> None:
    """
    Create 'wizardTags' attribute on obj
    :return:
    """
    cmds.addAttr(obj, longName='wizardTags', dataType="string")


def has_wtags_attribute(obj: str) -> bool:
    """
    Check whether wizardTags attribute exist on given object
    :param obj:
    :return:
    """
    return cmds.attributeQuery("wizardTags", node=obj, exists=True)


def get_wtags_attribute(obj: str) -> str:
    """
    Get wizardTags attributes from given object
    :param obj:
    :return: string
    """
    return cmds.getAttr(f'{obj}.wizardTags')


def set_wtags_attribute(obj: str, wtags: str) -> None:
    """
    Set wizardTags on object
    :param obj:
    :param wtags:
    :return:
    """
    cmds.setAttr(f'{obj}.wizardTags', wtags, typ='string')


def convert_wtags_in_list(guerilla_tags: str) -> list:
    """
    Convert wtags string into a clean list
    :param guerilla_tags:
    :return:
    """
    tags = guerilla_tags.replace(" ", "")
    wtags_list = tags.split(",")
    return wtags_list


def convert_wtags_in_string(guerilla_tags: list) -> str:
    """
    Convert a list of tags into the attribute string
    :param guerilla_tags:
    :return:
    """
    wtags_string = str()
    for tags in guerilla_tags:
        if tags == guerilla_tags[0]:
            wtags_string += tags
        else:
            wtags_string += ', ' + tags
    return wtags_string


def is_wtags_empty(obj) -> bool:
    """
    Check if wtags is empty on object with the wizardTags attribute
    :param obj:
    :return:
    """
    if not cmds.getAttr(f'{obj}.wizardTags'):
        return True
    else:
        return False


def add_gtag_to_attr(obj: str, tags: str) -> None:
    """
    Add tag to existing wizardTags on given object
    :param obj:
    :param tags:
    :return:
    """
    old_tags = get_wtags_attribute(obj)
    if not old_tags:
        new_tags = tags
    else:
        new_tags = old_tags + ', ' + tags
    set_wtags_attribute(obj, new_tags)

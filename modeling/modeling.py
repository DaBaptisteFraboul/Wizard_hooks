import maya.cmds as cmds


def generate_export_groups() -> None:
    """
    Generate the group LOD1 for modeling export at world root
    if it doesn't exist already
    """
    if not cmds.objExists('modeling_GRP_LOD1') :
        print("Missing LOD1 for modeling export, creating group...")
        cmds.group(name='modeling_GRP_LOD1', world=True, empty=True)
        print("... Done")
    else :
        print("LOD1 for modeling export already present, pass")


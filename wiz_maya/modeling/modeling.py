
# Maya python modules
import maya.cmds as cmds
import pymel.core as pm

# Wizard Python module
import wizard_communicate
from maya_wizard import wizard_tools
from maya_wizard import wizard_export

#Python modules
import os
import traceback
import logging
logger = logging.getLogger(__name__)

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


def custom_export():
    try:
        group_dict = {'modeling_GRP_LOD1':'LOD1'}
        for grp_name in group_dict:
            grp_obj = pm.PyNode(grp_name)
            asset_name = os.environ['wizard_asset_name']
            grp_obj.rename(asset_name)
            object_list = [grp_obj] + pm.listRelatives(grp_obj,
                                                       allDescendents=True)
            # Clear namespace
            objects_dic = wizard_tools.remove_LOD_from_names(object_list)
            export_name = 'TEXTURING'
            exported_string_asset = wizard_communicate.get_string_variant_from_work_env_id(
                os.environ['wizard_work_env_id'])
            export_GRP_list = [grp_obj]

            # TODO: Make custom FBX EXPORT here => without trigger hook
            additionnal_objects = wizard_export.trigger_before_export_hook('modeling', exported_string_asset)
            wizard_tools.apply_tags(export_GRP_list)
            grp_obj.rename(grp_name)
            wizard_tools.reassign_old_name_to_objects(objects_dic)

    except:
        logger.error(str(traceback.format_exc()))


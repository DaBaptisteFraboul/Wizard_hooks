# coding: utf-8
# Wizard hook
import pymel.core as pm
import maya.cmds as cmds
import logging

from wiz_maya.modeling import modeling
from wiz_maya.layout import layout
from wiz_maya import maya_utils
from wiz_maya.wiztags_editor import path_utils, start_editor

from maya_wizard import wizard_export
logger = logging.getLogger(__name__)


def after_scene_openning(stage_name, string_asset):
    ''' This function is triggered
		when you open the software.

		The "stage_name" argument is the name
		of the exported stage

		The "string_asset" argument is the current
		asset represented as string

		The "scene_path" argument is the scene path, 
		if there is no scene, it will be 'None' '''
    logger.info(f"Current stage : {stage_name}")
    maya = maya_utils.find_wizard_menu()
    fraboul_box = maya_utils.add_fraboulbox_to_wizard(maya)
    cmds.menuItem(parent=fraboul_box,
                  c=start_editor.test,
                  image=path_utils.get_abspath("icons/guerilla_render.png"),
                  label='wizardTags Editor')
    if stage_name == 'modeling':
        cmds.evalDeferred(modeling.generate_export_groups)
    if stage_name == 'layout':
        cmds.evalDeferred(layout.generate_export_groups)
    if stage_name == 'animation':
        maya_utils.set_project_aspect_ratio()
    if stage_name == 'layout':
        maya_utils.set_project_aspect_ratio()


def after_save(stage_name, string_asset, scene_path):
    ''' This function is triggered
		after an incremental save.

		The "stage_name" argument is the name
		of the exported stage

		The "string_asset" argument is the current
		asset represented as string

		The "scene_path" argument is the saved 
		incremental file'''
    pass


def sanity(stage_name, string_asset, exported_string_asset):
    ''' This function is triggered
		before the export and will stop the
		export process if the returned data is 
		"False"
		
		The "stage_name" argument is the name
		of the exported stage

		The "string_asset" argument is the current
		asset represented as string

		The "exported_string_asset" argument is the
		asset wizard will export represented as string'''
    return True


def before_export(stage_name, string_asset, exported_string_asset):
    ''' This function is triggered
		before the export 

		The "stage_name" argument is the name
		of the exported stage

		The "string_asset" argument is the current
		asset represented as string

		You can return a list of objects 
		that wizard will add to the export

		The "exported_string_asset" argument is the
		asset wizard will export represented as string'''
    print(f"Stage : {stage_name}")
    extra_object = []
    if stage_name == 'rigging':
        if cmds.objExists("ControlSet") :
            print("ControlSet found !")
            logger.info("ControlSet found !")
            extra_object.append("ControlSet")
        else :
            print("ControlSet not found!")
            logger.info("ControlSet not found!")
    # Export camrig for Houdini FX stage in layout
    if stage_name == 'layout':
        print(f"String asset : {exported_string_asset}")
        if cmds.objExists("CAMRIG"):
            # Trouver un moyen de recuperer le frame range de la l'asset export
            wizard_export.export(stage_name, "Houdini_cam", string_asset,["|CAMRIG"] ,frange = [0,500],custom_work_env_id = None, percent_factor=(0,1))
        else :
            logger.info("No CAMRIG TO export")
    return extra_object


def after_export(stage_name, export_dir, string_asset, exported_string_asset):
    ''' This function is triggered
		after the export

		The "stage_name" argument is the name
		of the exported stage

		The "export_dir" argument is the path wher wizard exported the
		file as string

		The "string_asset" argument is the current
		asset represented as string

		The "exported_string_asset" argument is the
		asset wizard just exported represented as string'''
    pass


def after_reference(stage_name,
                    referenced_stage_name,
                    referenced_files_dir,
                    namespace,
                    new_objects,
                    string_asset,
                    referenced_string_asset):
    ''' This function is triggered
		after referencing from wizard

		The "stage_name" argument is the name
		of the exported stage

		The "referenced_stage_name" argument is the name
		of the referenced stage

		The "referenced_files_dir" argument is the directory where the
		referenced files comes from

		The "namespace" argument is the namespace of the reference

		The "new_objects" argument is a list of the new objects added
		to the current scene after the reference

		The "string_asset" argument is the current
		asset represented as string

		The "referenced_string_asset" argument is the
		asset wizard just imported represented as string'''
    pass

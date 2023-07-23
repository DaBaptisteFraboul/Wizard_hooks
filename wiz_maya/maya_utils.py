import maya.cmds as cmds
import pymel.core as pm
from wiz_maya.wiztags_editor import start_editor
from wiz_maya.wiztags_editor import path_utils

def find_wizard_menu():
    """
    Get the wizard tab menu
    """
    default_wizard = 'MayaWindow|menu29'
    # We check that menu29 is labelled Wizard to spare time if needed
    if pm.menu(default_wizard, label=True, query=True) == 'Wizard':
        print(f"Found Wizard menu : {default_wizard}")
        return default_wizard
    else:
        maya_main_window = pm.language.melGlobals['gMainWindow']
        window_children = pm.window(maya_main_window, menuArray=True, query=True)
        for child in window_children :
            if pm.menu(child, label=True, query=True) == 'Wizard':
                print(f"Found Wizard menu : {child}")
                return child


def add_fraboulbox_to_wizard(wizard_menu):
    fraboulbox = pm.menuItem(parent = wizard_menu, subMenu=True, label='FraboulBox')
    return fraboulbox


def set_project_aspect_ratio():
    """
    Set Maya scene resolution and aspect ratio for camera
    """
    cmds.setAttr("defaultResolution.aspectLock", 0)
    cmds.setAttr("defaultResolution.width", 1920)
    cmds.setAttr("defaultResolution.height", 1080)
    cmds.setAttr("defaultResolution.pixelAspect", 1)
    cmds.setAttr("defaultResolution.deviceAspectRatio", 1.777)
    cmds.setAttr("defaultResolution.aspectLock", 1)

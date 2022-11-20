import maya.cmds as cmds
import pymel.core as pm

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


def add_submenu_to_wizard(wizard_menu):
    submenu = pm.menuItem(parent = wizard_menu, subMenu=True, label='FraboulBox')

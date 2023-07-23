from wiz_maya.wiztags_editor import gui
import importlib

importlib.reload(gui)

def test(*args):
    importlib.reload(gui)
    window = gui.wizardTagsEditor()
    window.show()
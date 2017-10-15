import sys
sys.path.append("..")
from pandaeditor import *

class MenuToggler():

    def __init__(self):
        self.is_editor = True
        self.target = None


    def input(self, key):
        if key == 'left mouse down':
            if self.entity.hovered:

                # close menus before opening a new one
                if self.entity.parent == scene.editor.toolbar:
                    for button in scene.editor.toolbar.children:
                        if button.menu_toggler:
                            button.menu_toggler.target.enabled = False

                self.target.enabled = not self.target.enabled

            else:
                print(mouse.hovered_entitiy)
                # self.target.enabled = False

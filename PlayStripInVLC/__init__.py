# Copyright (c) 2025, Mirko Barthauer
# All rights reserved.
# This source code is licensed under the MIT-style license found in the
# LICENSE file in the same directory of this source tree.

import bpy
from .control import menu_func, VSE_OT_PlayStripOperator_AddonPreferences, VSE_OT_PlayStripOperator

bl_info = {
    "name": "PlayStripInVLC",
    "description": "Open video or Audio strip in VLC starting from the current time cursor",
    "author": "Mirko Barthauer <m.barthauer@t-online.de>",
    "version": (0, 0, 1),
    "blender": (4, 5, 0),
    "location": "Video Sequence Editor > Right-click menu",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Sequencer"
}

classes = (VSE_OT_PlayStripOperator_AddonPreferences, VSE_OT_PlayStripOperator)

def register():
    for cls in classes:
        print("register %s" % str(cls))
        bpy.utils.register_class(cls)
    bpy.types.SEQUENCER_MT_context_menu.append(menu_func)

def unregister():
    bpy.types.SEQUENCER_MT_context_menu.remove(menu_func)
    for cls in reversed(classes):
        print("unregister %s" % str(cls))
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
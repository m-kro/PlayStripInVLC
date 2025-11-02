# Copyright (c) 2025, Mirko Barthauer
# All rights reserved.

# This source code is licensed under the MIT-style license found in the
# LICENSE file in the same directory of this source tree.
import os
import bpy
import subprocess
from urllib.request import pathname2url

# Define addon preferences (to store settings permanently)
class VSE_OT_PlayStripOperator_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__
    vlcPath: bpy.props.StringProperty(
        name="Path to VLC media player executable / VLC call",
        description="Call of VLC media player (start time and file data is appended by the addon)",
        default="vlc"
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "vlcPath")

def getStartTime(strip, useCursor = True):
    # check if the cursor is within the bounds of the strip
    startFrame = strip.frame_offset_start
    if useCursor:
        startFrame += bpy.context.scene.frame_current - strip.frame_final_start
    
    # compute the start time and call VLC
    startTime = round(startFrame / bpy.context.scene.render.fps * bpy.context.scene.render.fps_base, 1)
    return startTime

# Define strip menu operator
class VSE_OT_PlayStripOperator(bpy.types.Operator):
    """My Custom VSE Operator"""
    bl_idname = "sequencer.playstripoperator"
    bl_label = "Play strip in VLC from strip begin"
    bl_options = {'REGISTER'}

    useCursor : bpy.props.BoolProperty(name = "Use time cursor", description= "Start the strip from the time cursor position", default=False)

    def execute(self, context):
        strip = context.scene.sequence_editor.active_strip
        startTime = getStartTime(strip, useCursor=self.useCursor)
        filePath = bpy.path.abspath(strip.sound.filepath if strip.type == 'SOUND' else strip.filepath)
        cmd = [bpy.context.preferences.addons[__package__].preferences.vlcPath]
        cmd.extend(["--start-time", "%.1f" % startTime, "file:%s" % pathname2url(filePath)])
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return {'FINISHED'}

# Menu function (called when the user right-clicks on a strip)
def menu_func(self, context):
    layout = self.layout
    strip = context.scene.sequence_editor.active_strip if context.scene.sequence_editor else None

    # Only show for MOVIE AND SOUND strips
    if strip and strip.type in {'MOVIE', 'SOUND'}:
        layout.separator()
        layout.operator(VSE_OT_PlayStripOperator.bl_idname, text= "Play in VLC from start", icon="PLAY")
        cursorWithinStrip = strip.frame_final_start < bpy.context.scene.frame_current < strip.frame_final_end
        if cursorWithinStrip:
            layout.operator(VSE_OT_PlayStripOperator.bl_idname, text = "Play in VLC from current frame", icon="PLAY").useCursor = True

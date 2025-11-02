# License
This work is licensed under the MIT license.

# Description
VSE (sequencer) is the Blender tool for editing videos and related audio strips. Audio strips are displayed with some waveform but sometimes it is not easy 
to say whether you cut at the end of the sentence or one word early / late. Due to cuts in the audio strip some basic calculation is needed to find the corresponding 
time in the audio file. Obviously one can keep a media player or audio editing tool open in parallel and do this manually, but it seems convenient to let Blender help you 
in this context.
This Blender VSE addon adds strip context menu entries to start playing the audio of the strip in VLC. It translates the cut offset and optionally the position of the current frame 
into the corresponding time of the audio file in VLC using its command line option `--start-time`.

# Installation
The folder ./PlayStripInVLC contains all the necessary files. Make a zip archive from it and you are ready to 
install in in the Blender UI: 
`Menu > Edit > Preferences > Addons > Install...`.

Ensure VLC can be called by editing the addon settings inside the Preferences menu. By default VLC is expected to be included in the *PATH* environment variable.

# How to use it

- Open a .blend file with video or audio strips in the Blender VSE. 
- Select the one you want to listen to by clicking on it.
- Open the strip context menu on right click.
- Choose either "Play in VLC from start" (Start the audio at the point where the strip starts) or "Play in VLC from current frame" (Start the audio at the current frame).


# Compatibility
Developed using Blender 4.5.
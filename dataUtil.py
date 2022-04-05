import os
# for dev
# from typing import TypedDict

# for dev
# class ApaintTemp(TypedDict):
#     toggle_eraser: bool
#     brush_blend: str
#     is_draw: bool
#     is_line: bool
#     is_stamp: bool

def load_icon():
    import bpy.utils.previews
    if not hasattr(bpy.utils, 'previews'): return
    global custom_icons
    custom_icons = bpy.utils.previews.new()
    dir = os.path.join(os.path.dirname(__file__), "icons")
    for entry in os.scandir(dir):
        if entry.name.endswith(".png"):
            name = os.path.splitext(entry.name)[0]
            custom_icons.load(name.upper(), entry.path, "IMAGE")

def unload_icon():
    global custom_icons
    import bpy.utils.previews
    bpy.utils.previews.remove(custom_icons)

def c_icon(name:str) :
    global custom_icons
    return custom_icons[name].icon_id

# for dev
# apaint_temp : ApaintTemp = {'toggle_eraser': False}

apaint_temp  = {'toggle_eraser': False}


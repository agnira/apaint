from bpy import types
from . import dataUtil

temp = dataUtil.apaint_temp

class APAINT_MT_palette(types.Menu):
    bl_idname = "APAINT_MT_palette"
    bl_label = "Palletes"
    def draw(self, context: types.Context):
        layout = self.layout
        layout.operator("apaint.palette_operator", text="-").palette_name = "-"
        for palette in context.blend_data.palettes:
           layout.operator("apaint.palette_operator", text=palette.name).palette_name = palette.name
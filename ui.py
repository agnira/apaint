from bpy import types
from . import dataUtil

temp = dataUtil.apaint_temp
c_icon = dataUtil.c_icon

def apaint_menu(self, context : types.Context):
    ip: types.ImagePaint = context.tool_settings.image_paint
    b = ip.brush

    layout:types.UILayout = self.layout
    temp["toggle_eraser"] = bool(b.blend == "ERASE_ALPHA")
    temp["is_draw"] = bool(b.stroke_method == "SPACE")
    temp["is_line"] = bool(b.stroke_method == "LINE")
    temp["is_stamp"] = bool(b.stroke_method == "ANCHORED")

    row = layout.row(align=True)
    row.operator("apaint.toggle_eraser", depress=temp["toggle_eraser"], text="", icon_value=c_icon("ERASER"))
    row.operator("apaint.toggle_alpha_lock", depress= not b.use_alpha, text="", icon_value=c_icon("ALPHA LOCK"))
    row.separator()
    row.operator("apaint.toggle_occlude", depress=ip.use_occlude, text="", icon="SELECT_EXTEND")
    row.operator("apaint.toggle_culling", depress=ip.use_backface_culling, text="", icon="SELECT_SET")
    row.separator()
    row.operator("apaint.toggle_draw", depress=temp["is_draw"], text="", icon="GREASEPENCIL")
    row.operator("apaint.toggle_line", depress=temp["is_line"], text="", icon="IPO_LINEAR")
    row.operator("apaint.toggle_stamp", depress=temp["is_stamp"], text="", icon_value=c_icon("STAMP"))

    if temp["is_draw"] :
        row = layout.row(align=True)
        row.operator("apaint.toggle_smooth", depress=b.use_smooth_stroke, text="", icon="IPO_EASE_IN_OUT")

    row = layout.row(align=True)
    row.menu("APAINT_MT_palette")

    row = layout.row(align=True)
    col = row.column()
    col.template_palette(ip, "palette", color=False)
    
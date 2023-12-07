from bpy import types
from . import dataUtil

temp = dataUtil.apaint_temp
c_icon = dataUtil.c_icon


def apaint_menu(self, context: types.Context):
    ip: types.ImagePaint = context.tool_settings.image_paint
    b = ip.brush

    layout: types.UILayout = self.layout
    temp["toggle_eraser"] = bool(b.blend == "ERASE_ALPHA")
    temp["is_draw"] = bool(b.stroke_method == "SPACE")
    temp["is_line"] = bool(b.stroke_method == "LINE")
    temp["is_stamp"] = bool(b.stroke_method == "ANCHORED")

    temp["is_fallof_custom"] = bool(b.curve_preset == "CUSTOM")
    temp["is_fallof_smooth"] = bool(b.curve_preset == "SMOOTH")
    temp["is_fallof_smoother"] = bool(b.curve_preset == "SMOOTHER")
    temp["is_fallof_sphere"] = bool(b.curve_preset == "SPHERE")
    temp["is_fallof_root"] = bool(b.curve_preset == "ROOT")
    temp["is_fallof_sharp"] = bool(b.curve_preset == "SHARP")
    temp["is_fallof_lin"] = bool(b.curve_preset == "LIN")
    temp["is_fallof_pow4"] = bool(b.curve_preset == "POW4")
    temp["is_fallof_invsquare"] = bool(b.curve_preset == "INVSQUARE")
    temp["is_fallof_constant"] = bool(b.curve_preset == "CONSTANT")

    row = layout.row(align=True)
    row.operator("apaint.toggle_eraser",
                 depress=temp["toggle_eraser"], text="", icon_value=c_icon("ERASER"))
    row.operator("apaint.toggle_alpha_lock", depress=not b.use_alpha,
                 text="", icon_value=c_icon("ALPHA LOCK"))
    row.separator()
    row.operator("apaint.toggle_occlude", depress=ip.use_occlude,
                 text="", icon="SELECT_EXTEND")
    row.operator("apaint.toggle_culling",
                 depress=ip.use_backface_culling, text="", icon="SELECT_SET")
    row.separator()
    row.operator("apaint.toggle_draw",
                 depress=temp["is_draw"], text="", icon="GREASEPENCIL")
    row.operator("apaint.toggle_line",
                 depress=temp["is_line"], text="", icon="IPO_LINEAR")
    row.operator("apaint.toggle_stamp",
                 depress=temp["is_stamp"], text="", icon_value=c_icon("STAMP"))

    if temp["is_draw"] :
        row = layout.row(align=True)
        row.operator("apaint.toggle_smooth", depress=b.use_smooth_stroke, text="", icon="IPO_EASE_IN_OUT")

    row = layout.row(align=True)
    row.operator("apaint.toggle_fallof_custom",
                 depress=temp["is_fallof_custom"], text="", icon="RNDCURVE")
    row.operator("apaint.toggle_fallof_smooth",
                 depress=temp["is_fallof_smooth"], text="", icon="SMOOTHCURVE")
    row.operator("apaint.toggle_fallof_smoother",
                 depress=temp["is_fallof_smoother"], text="", icon="SMOOTHCURVE")
    row.operator("apaint.toggle_fallof_sphere",
                 depress=temp["is_fallof_sphere"], text="", icon="SPHERECURVE")
    row.operator("apaint.toggle_fallof_root",
                 depress=temp["is_fallof_root"], text="", icon="ROOTCURVE")
    row.operator("apaint.toggle_fallof_sharp",
                 depress=temp["is_fallof_sharp"], text="", icon="SHARPCURVE")
    row.operator("apaint.toggle_fallof_lin",
                 depress=temp["is_fallof_lin"], text="", icon="LINCURVE")
    row.operator("apaint.toggle_fallof_pow4",
                 depress=temp["is_fallof_pow4"], text="", icon="SHARPCURVE")
    row.operator("apaint.toggle_fallof_invsquare",
                 depress=temp["is_fallof_invsquare"], text="", icon="INVERSESQUARECURVE")
    row.operator("apaint.toggle_fallof_constant",
                 depress=temp["is_fallof_constant"], text="", icon="NOCURVE")

    row = layout.row(align=True)
    row.menu("APAINT_MT_palette")

    row = layout.row(align=True)
    col = row.column()
    col.template_palette(ip, "palette", color=False)

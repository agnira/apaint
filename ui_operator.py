from bpy import types, props
from . import dataUtil

temp = dataUtil.apaint_temp

class APAINT_OT_toggle_eraser(types.Operator):
    bl_idname = "apaint.toggle_eraser"
    bl_label = "Toggle Eraser"
    bl_description = "Toggle bursh blend to eraser"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["toggle_eraser"]:
            temp["brush_blend"] = b.blend
            b.blend = "ERASE_ALPHA"
        else:
            if not temp.get("brush_blend"):
                temp["brush_blend"] = "MIX"
            b.blend = temp["brush_blend"]
        return {'FINISHED'}

class APAINT_OT_toggle_alpha_lock(types.Operator):
    bl_idname = "apaint.toggle_alpha_lock"
    bl_label = "Toggle Alpha Lock"
    bl_description = "Toggle Alpha Lock"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if b.use_alpha :
            b.use_alpha = False
        else :
            b.use_alpha = True
        return {'FINISHED'}

class APAINT_OT_toggle_occlude(types.Operator):
    bl_idname = "apaint.toggle_occlude"
    bl_label = "Toggle Occlude"
    bl_description = "Toggle Occlude"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if ip.use_occlude :
            ip.use_occlude = False
        else :
            ip.use_occlude = True
        return {'FINISHED'}

class APAINT_OT_toggle_culling(types.Operator):
    bl_idname = "apaint.toggle_culling"
    bl_label = "Toggle Culling"
    bl_description = "Toggle Backface Culling"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if ip.use_backface_culling :
            ip.use_backface_culling = False
        else :
            ip.use_backface_culling = True
        return {'FINISHED'}

class APAINT_OT_toggle_draw(types.Operator):
    bl_idname = "apaint.toggle_draw"
    bl_label = "Draw Tool"
    bl_description = "Use Draw Tool"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_draw"]:
            temp["is_draw"] = True
            b.stroke_method = "SPACE"
        return {'FINISHED'}

class APAINT_OT_toggle_line(types.Operator):
    bl_idname = "apaint.toggle_line"
    bl_label = "Line Tool"
    bl_description = "Use Line Tool"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_line"]:
            temp["is_line"] = True
            b.stroke_method = "LINE"
        return {'FINISHED'}

class APAINT_OT_toggle_stamp(types.Operator):
    bl_idname = "apaint.toggle_stamp"
    bl_label = "Stamp Tool"
    bl_description = "Use Stamp Tool"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_stamp"]:
            temp["is_stamp"] = True
            b.stroke_method = "ANCHORED"
        return {'FINISHED'}

class APAINT_OT_palette_operator(types.Operator):
    bl_idname = "apaint.palette_operator"
    bl_label = "Palletes"
    bl_description = "Select Palletes"
    
    palette_name : props.StringProperty(name="pallete_name")
    @classmethod
    def poll(cls, context):
        return context.object is not None
    def execute(self, context: types.Context):
        ip = context.tool_settings.image_paint
        if self.palette_name == "-" :
            ip.palette = None
        else :
            print(self.palette_name)
            ip.palette = context.blend_data.palettes[self.palette_name]
        return {'FINISHED'}

class APAINT_OT_toggle_smooth(types.Operator):
    bl_idname = "apaint.toggle_smooth"
    bl_label = "use smooth brush"
    bl_description = "use smooth brush"

    def execute(self, context: types.Context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if b.use_smooth_stroke:
            b.use_smooth_stroke = False
        else:
            b.use_smooth_stroke = True
        return {'FINISHED'}

class APAINT_OT_toggle_fallof_custom(types.Operator):
    bl_idname = "apaint.toggle_fallof_custom"
    bl_label = "custom fallof"
    bl_description = "Use Custom Fallof"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_fallof_custom"]:
            temp["is_fallof_custom"] = True
            b.curve_preset = "CUSTOM"
        return {'FINISHED'}

class APAINT_OT_toggle_fallof_smooth(types.Operator):
    bl_idname = "apaint.toggle_fallof_smooth"
    bl_label = "smooth fallof"
    bl_description = "Use Smooth Fallof"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_fallof_smooth"]:
            temp["is_fallof_smooth"] = True
            b.curve_preset = "SMOOTH"
        return {'FINISHED'}
    
class APAINT_OT_toggle_fallof_smoother(types.Operator):
    bl_idname = "apaint.toggle_fallof_smoother"
    bl_label = "smoother fallof"
    bl_description = "Use Smoother Fallof"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_fallof_smoother"]:
            temp["is_fallof_smoother"] = True
            b.curve_preset = "SMOOTHER"
        return {'FINISHED'}

class APAINT_OT_fallof_sphere(types.Operator):
    bl_idname = "apaint.toggle_fallof_sphere"
    bl_label = "sphere fallof"
    bl_description = "Use Sphere Fallof"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_fallof_sphere"]:
            temp["is_fallof_sphere"] = True
            b.curve_preset = "SPHERE"
        return {'FINISHED'}

class APAINT_OT_toggle_fallof_root(types.Operator):
    bl_idname = "apaint.toggle_fallof_root"
    bl_label = "root fallof"
    bl_description = "Use Root Fallof"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_fallof_root"]:
            temp["is_fallof_root"] = True
            b.curve_preset = "ROOT"
        return {'FINISHED'}

class APAINT_OT_toggle_fallof_sharp(types.Operator):
    bl_idname = "apaint.toggle_fallof_sharp"
    bl_label = "sharp fallof"
    bl_description = "Use Sharp Fallof"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_fallof_sharp"]:
            temp["is_fallof_sharp"] = True
            b.curve_preset = "SHARP"
        return {'FINISHED'}
    
class APAINT_OT_toggle_fallof_lin(types.Operator):
    bl_idname = "apaint.toggle_fallof_lin"
    bl_label = "lin fallof"
    bl_description = "Use Lin Fallof"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_fallof_lin"]:
            temp["is_fallof_lin"] = True
            b.curve_preset = "LIN"
        return {'FINISHED'}
    
class APAINT_OT_toggle_fallof_pow4(types.Operator):
    bl_idname = "apaint.toggle_fallof_pow4"
    bl_label = "pow fallof"
    bl_description = "Use Pow4 Fallof"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_fallof_pow4"]:
            temp["is_fallof_pow4"] = True
            b.curve_preset = "POW4"
        return {'FINISHED'}
    
class APAINT_OT_toggle_fallof_invsquare(types.Operator):
    bl_idname = "apaint.toggle_fallof_invsquare"
    bl_label = "invsquare fallof"
    bl_description = "Use Invsquare Fallof"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_fallof_invsquare"]:
            temp["is_fallof_invsquare"] = True
            b.curve_preset = "INVSQUARE"
        return {'FINISHED'}
    
class APAINT_OT_toggle_fallof_constant(types.Operator):
    bl_idname = "apaint.toggle_fallof_constant"
    bl_label = "constant fallof"
    bl_description = "Use Constant Fallof"

    def execute(self, context):
        ip = context.tool_settings.image_paint
        b = ip.brush
        if not temp["is_fallof_constant"]:
            temp["is_fallof_constant"] = True
            b.curve_preset = "CONSTANT"
        return {'FINISHED'}

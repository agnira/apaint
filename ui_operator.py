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
    
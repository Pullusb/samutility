"""
Operator to tweak viewport quicker
"""

import bpy


##Only render (shamelessly stolen from Pablo Vasquez's Amaranth great addon)
#Alt+Shift+Z toggle Only Render

class SAMT_VIEW3D_OT_show_only_render(bpy.types.Operator):
    bl_idname = "samutils.show_only_render"
    bl_label = "Show Only Render"

    def execute(self, context):
        space = bpy.context.space_data

        if space.show_only_render:
            space.show_only_render = False
        else:
            space.show_only_render = True
        return {"FINISHED"}




#Alt+Shift+C toggleLock Cam to view

class SAMT_VIEW3D_OT_lock_camera_to_view(bpy.types.Operator):
    bl_idname = "samutils.lock_cam_to_view"
    bl_label = "Lock camera to view"

    def execute(self, context):
        #TODO (only if in view is in cam else, detect view)
        
        space = bpy.context.space_data
        #space.show_only_render = not space.lock_camera
        if space.show_only_render:
            space.lock_camera = True
        else:
            space.show_only_render = True
        return {"FINISHED"}
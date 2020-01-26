bl_info = {
    "name": "TimeSavers",
    "author": "Citrine's Animations",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "Side Bar",
    "description": "Nice little time savers",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}

import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )

bpy.types.Object.Start = bpy.props.IntProperty(default=0, min=0) 
bpy.types.Object.End = bpy.props.IntProperty(default=1, min=0) 

class Helpfullsh(bpy.types.Panel):
    bl_label = "TimeSavers"
    bl_idname = "TimeSavers"
    bl_category = "TimeSavers"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row(align=True)
        row.operator('oi.oi', text='2s')
        row = layout.row(align=True)
        row.prop(obj, "Start")
        row.operator('smeared.s')
        row.prop(obj, "End")
    


class oiOi(bpy.types.Operator):
    bl_idname = "oi.oi"
    bl_label = "2s"


    def execute(self, context):
        #self.report({'INFO'}, "Hello world!")
        obj = bpy.context.selected_objects
        
        for heh in obj:
            fcurve = heh.animation_data.action.fcurves
            for jeff in fcurve:
                jeff.modifiers.new(type='STEPPED')
            return {'FINISHED'}
        
class smearedS(bpy.types.Operator):
    bl_idname = "smeared.s"
    bl_label = "Smear"


    def execute(self, context):
        #self.report({'INFO'}, "Hello world!")
        obj = bpy.context.selected_objects[0]
        bruv = bpy.context.scene.frame_current-obj.Start
        bruv2 = bpy.context.scene.frame_current+obj.End+1
        bruv3 = bpy.context.scene.frame_current-obj.Start-1
        obj.hide_render = True
        obj.hide_viewport = True
        obj.keyframe_insert(data_path="hide_render", frame = bruv3)
        obj.keyframe_insert(data_path="hide_viewport", frame = bruv3)
        obj.hide_render = False
        obj.hide_viewport = False
        obj.keyframe_insert(data_path="hide_render", frame = bruv)
        obj.keyframe_insert(data_path="hide_viewport", frame = bruv)
        obj.hide_render = True
        obj.hide_viewport = True
        obj.keyframe_insert(data_path="hide_render", frame = bruv2)
        obj.keyframe_insert(data_path="hide_viewport", frame = bruv2)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(oiOi)
    bpy.utils.register_class(smearedS)
    bpy.utils.register_class(Helpfullsh)

    
def unregister():
    bpy.utils.unregister_class(Helpfullsh)
    bpy.utils.unregister_class(oiOi)
    bpy.utils.unregister_class(smearedS)

if __name__ == '__main__':
    register()



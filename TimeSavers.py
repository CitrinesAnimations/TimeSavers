bl_info = {
    "name": "TimeSavers",
    "author": "Citrine's Animations",
    "version": (1, 1, 0),
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

def mbColourPickerUp(context, self):
    bpy.context.object.mbColour = bpy.context.scene.obie.mbColour
    bpy.context.scene.obie = None

bpy.types.Object.Start = bpy.props.IntProperty(default=0, min=0) 
bpy.types.Object.End = bpy.props.IntProperty(default=1, min=0) 
bpy.types.Scene.obie = bpy.props.PointerProperty(type=bpy.types.Object, name="", update=mbColourPickerUp)

def mbColourUpdate(context, self):
    bpy.context.object.material_slots[0].material.node_tree.nodes["Group.004"].inputs[0].default_value = bpy.context.object.mbColour
    bpy.context.object.material_slots[0].material.diffuse_color = bpy.context.object.mbColour



bpy.types.Object.mbColour = bpy.props.FloatVectorProperty(name = "",subtype = "COLOR",size = 4,min = 0.0,max = 1.0, default = (0,0,0,1),update=mbColourUpdate) 

class fixedUpdateC(bpy.types.Operator):
    bl_idname = "fix.updatec"
    bl_label = "Reload Colours"
    
    def execute(self, context):
        for objs in bpy.data.objects:
            if objs.type == 'MESH':
                if objs.material_slots[0].material.node_tree.nodes.find("Group.004") > 0:
                    objs.mbColour = objs.material_slots[0].material.node_tree.nodes["Group.004"].inputs[0].default_value
        return {'FINISHED'}

class indentmats(bpy.types.Operator):
    bl_idname = "indent.mats"
    bl_label = "SU"
    
    def execute(self, context):
        bpy.context.object.material_slots[0].material = bpy.context.object.material_slots[0].material.copy()
        return {'FINISHED'}
    
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
        row = layout.row(align=True)
        row.split()
        row = layout.row(align=True)
        row.operator('fix.updatec')
        row.operator('indent.mats', text="", icon='RESTRICT_INSTANCED_ON')
        row = layout.row(align=True)
        row.prop(obj, 'mbColour')
        row.prop(context.scene, 'obie')
    


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
        obj = bpy.context.selected_objects
        for afaf in obj:
            bruv = bpy.context.scene.frame_current-afaf.Start
            bruv2 = bpy.context.scene.frame_current+afaf.End+1
            bruv3 = bpy.context.scene.frame_current-afaf.Start-1
            afaf.hide_render = True
            afaf.hide_viewport = True
            afaf.keyframe_insert(data_path="hide_render", frame = bruv3)
            afaf.keyframe_insert(data_path="hide_viewport", frame = bruv3)
            afaf.hide_render = False
            afaf.hide_viewport = False
            afaf.keyframe_insert(data_path="hide_render", frame = bruv)
            afaf.keyframe_insert(data_path="hide_viewport", frame = bruv)
            afaf.hide_render = True
            afaf.hide_viewport = True
            afaf.keyframe_insert(data_path="hide_render", frame = bruv2)
            afaf.keyframe_insert(data_path="hide_viewport", frame = bruv2)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(oiOi)
    bpy.utils.register_class(smearedS)
    bpy.utils.register_class(Helpfullsh)
    bpy.utils.register_class(fixedUpdateC)
    bpy.utils.register_class(indentmats)
    
def unregister():
    bpy.utils.unregister_class(Helpfullsh)
    bpy.utils.unregister_class(oiOi)
    bpy.utils.unregister_class(smearedS)
    bpy.utils.unregister_class(fixedUpdateC)
    bpy.utils.unregister_class(indentmats)
    
if __name__ == '__main__':
    register()



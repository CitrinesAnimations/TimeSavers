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

class Helpfullsh(bpy.types.Panel):
    bl_label = "TimeSavers"
    bl_idname = "TimeSavers"
    bl_category = "TimeSavers"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    
    def draw(self, context):
        layout = self.layout
        layout.operator('oi.oi', text='2s')
    


class oiOi(bpy.types.Operator):
    bl_idname = "oi.oi"
    bl_label = "2s"


    def execute(self, context):
        #self.report({'INFO'}, "Hello world!")
        obj = bpy.context.selected_objects[0]
    
        #again = obj.animation_data.action
        # pick the fcurve to add to
        fcurve = obj.animation_data.action.fcurves
    
        # add a modifier and get a reference.
        for jeff in fcurve:
            jeff.modifiers.new(type='STEPPED')
        return {'FINISHED'}

def register():
    bpy.utils.register_class(oiOi)
    bpy.utils.register_class(Helpfullsh)

    
def unregister():
    bpy.utils.unregister_class(Helpfullsh)
    bpy.utils.unregister_class(oiOi)

if __name__ == '__main__':
    register()



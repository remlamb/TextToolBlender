bl_info = {
    "name": "New Object",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > UI > Text Tool Tab",
    "description": "Adds a new Text Object with user defined properties",
    "warning": "",
    "doc_url": "",
    "category": "Add Text",
}

import bpy


class HelloTextTool(bpy.types.Panel):
    # """Creates a Panel in the Object properties window"""
    bl_label = "Hello Text Tool"
    bl_idname = "HelloTextTool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Text Tool"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Custom Text for the 3D View.")
        row = layout.row()
        row = layout.split(factor=0.45)
        row.label(text="")
        row.operator("wm.textop", text="Add Text", icon='OUTLINER_OB_FONT')



class WM_OT_textOp(bpy.types.Operator):
    bl_label = "Text Tool Operator"
    bl_idname = "wm.textop"
    text: bpy.props.StringProperty(name="Enter Text:", default="")
    scale: bpy.props.FloatProperty(name="Scale:", default=1)
    center: bpy.props.BoolProperty(name="Center Origin", default=False)
    extrude: bpy.props.BoolProperty(name="Extrude", default=False)
    extrude_amout: bpy.props.FloatProperty(name="Extrude Amout:", default=0.06)

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context) -> None:

        t = self.text
        s = self.scale
        c = self.center
        e = self.extrude
        ea = self.extrude_amout

        bpy.ops.object.text_add(enter_editmode=True)
        bpy.ops.font.delete(type='PREVIOUS_WORD')
        bpy.ops.font.text_insert(text=t)
        bpy.ops.object.editmode_toggle()
        bpy.context.object.data.size = s

        if c == True:
            bpy.context.object.data.align_x = 'CENTER'
            bpy.context.object.data.align_y = 'CENTER'

        if e == True:
            bpy.context.object.data.extrude = ea

        return {'FINISHED'}


def register():
    bpy.utils.register_class(HelloTextTool)
    bpy.utils.register_class(WM_OT_textOp)


def unregister():
    bpy.utils.unregister_class(HelloTextTool)
    bpy.utils.unregister_class(WM_OT_textOp)


if __name__ == "__main__":
    register()

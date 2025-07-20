我来为您翻译Blender 4.0.3的Context Access (bpy.context)完整文档：

# Blender 4.0.3 Context Access (bpy.context) 上下文访问

## 概述
上下文成员的可访问性取决于当前访问的Blender区域。

注意：所有上下文值都是只读的，但可以通过数据API或运行操作符来修改。

## 全局上下文 (Global Context)
这些属性在任何上下文中都可用。

### bpy.context.area
**类型**: `bpy.types.Area` (只读)
当前区域

### bpy.context.asset
**类型**: `bpy.types.AssetRepresentation` (只读)
当前资产

### bpy.context.blend_data
**类型**: `bpy.types.BlendData` (只读)
混合数据

### bpy.context.collection
**类型**: `bpy.types.Collection` (只读)
当前集合

### bpy.context.engine
**类型**: `string`, 默认 `""` (只读, 永不为None)
当前渲染引擎

### bpy.context.gizmo_group
**类型**: `bpy.types.GizmoGroup` (只读)
当前小工具组

### bpy.context.layer_collection
**类型**: `bpy.types.LayerCollection` (只读)
当前层集合

### bpy.context.mode
**类型**: `enum in Context Mode Items`, 默认 `'EDIT_MESH'` (只读)
当前模式

### bpy.context.preferences
**类型**: `bpy.types.Preferences` (只读)
用户偏好设置

### bpy.context.region
**类型**: `bpy.types.Region` (只读)
当前区域

### bpy.context.region_data
**类型**: `bpy.types.RegionView3D` (只读)
区域数据

### bpy.context.scene
**类型**: `bpy.types.Scene` (只读)
当前场景

### bpy.context.screen
**类型**: `bpy.types.Screen` (只读)
当前屏幕

### bpy.context.space_data
当前空间，在后台模式、光标在窗口外或使用菜单搜索时可能为None
**类型**: `bpy.types.Space` (只读)

### bpy.context.tool_settings
**类型**: `bpy.types.ToolSettings` (只读)
工具设置

### bpy.context.view_layer
**类型**: `bpy.types.ViewLayer` (只读)
当前视图层

### bpy.context.window
**类型**: `bpy.types.Window` (只读)
当前窗口

### bpy.context.window_manager
**类型**: `bpy.types.WindowManager` (只读)
窗口管理器

### bpy.context.workspace
**类型**: `bpy.types.WorkSpace` (只读)
当前工作空间

## 按钮上下文 (Buttons Context)

### bpy.context.texture_slot
**类型**: `bpy.types.TextureSlot`
纹理槽

### bpy.context.scene
**类型**: `bpy.types.Scene`
场景

### bpy.context.world
**类型**: `bpy.types.World`
世界

### bpy.context.object
**类型**: `bpy.types.Object`
对象

### bpy.context.mesh
**类型**: `bpy.types.Mesh`
网格

### bpy.context.armature
**类型**: `bpy.types.Armature`
骨骼

### bpy.context.lattice
**类型**: `bpy.types.Lattice`
晶格

### bpy.context.curve
**类型**: `bpy.types.Curve`
曲线

### bpy.context.meta_ball
**类型**: `bpy.types.MetaBall`
元球

### bpy.context.light
**类型**: `bpy.types.Light`
灯光

### bpy.context.speaker
**类型**: `bpy.types.Speaker`
扬声器

### bpy.context.lightprobe
**类型**: `bpy.types.LightProbe`
光照探针

### bpy.context.camera
**类型**: `bpy.types.Camera`
相机

### bpy.context.material
**类型**: `bpy.types.Material`
材质

### bpy.context.material_slot
**类型**: `bpy.types.MaterialSlot`
材质槽

### bpy.context.texture
**类型**: `bpy.types.Texture`
纹理

### bpy.context.texture_user
**类型**: `bpy.types.ID`
纹理用户

### bpy.context.texture_user_property
**类型**: `bpy.types.Property`
纹理用户属性

### bpy.context.bone
**类型**: `bpy.types.Bone`
骨骼

### bpy.context.edit_bone
**类型**: `bpy.types.EditBone`
编辑骨骼

### bpy.context.pose_bone
**类型**: `bpy.types.PoseBone`
姿态骨骼

### bpy.context.particle_system
**类型**: `bpy.types.ParticleSystem`
粒子系统

### bpy.context.particle_system_editable
**类型**: `bpy.types.ParticleSystem`
可编辑粒子系统

### bpy.context.particle_settings
**类型**: `bpy.types.ParticleSettings`
粒子设置

### bpy.context.cloth
**类型**: `bpy.types.ClothModifier`
布料

### bpy.context.soft_body
**类型**: `bpy.types.SoftBodyModifier`
软体

### bpy.context.fluid
**类型**: `bpy.types.FluidSimulationModifier`
流体

### bpy.context.collision
**类型**: `bpy.types.CollisionModifier`
碰撞

### bpy.context.brush
**类型**: `bpy.types.Brush`
笔刷

### bpy.context.dynamic_paint
**类型**: `bpy.types.DynamicPaintModifier`
动态绘制

### bpy.context.line_style
**类型**: `bpy.types.FreestyleLineStyle`
线条样式

### bpy.context.collection
**类型**: `bpy.types.LayerCollection`
集合

### bpy.context.gpencil
**类型**: `bpy.types.GreasePencil`
蜡笔

### bpy.context.grease_pencil
**类型**: `bpy.types.GreasePencilv3`
蜡笔v3

### bpy.context.curves
**类型**: `Hair Curves`
头发曲线

### bpy.context.volume
**类型**: `bpy.types.Volume`
体积

## 剪辑上下文 (Clip Context)

### bpy.context.edit_movieclip
**类型**: `bpy.types.MovieClip`
编辑电影剪辑

### bpy.context.edit_mask
**类型**: `bpy.types.Mask`
编辑遮罩

## 文件上下文 (File Context)

### bpy.context.active_file
**类型**: `bpy.types.FileSelectEntry`
活动文件

### bpy.context.selected_files
**类型**: `sequence of bpy.types.FileSelectEntry`
选中的文件

### bpy.context.asset_library_reference
**类型**: `bpy.types.AssetLibraryReference`
资产库引用

### bpy.context.selected_assets
**类型**: `sequence of bpy.types.AssetRepresentation`
选中的资产

### bpy.context.id
**类型**: `bpy.types.ID`
ID

### bpy.context.selected_ids
**类型**: `sequence of bpy.types.ID`
选中的ID

## 图像上下文 (Image Context)

### bpy.context.edit_image
**类型**: `bpy.types.Image`
编辑图像

### bpy.context.edit_mask
**类型**: `bpy.types.Mask`
编辑遮罩

## 节点上下文 (Node Context)

### bpy.context.selected_nodes
**类型**: `sequence of bpy.types.Node`
选中的节点

### bpy.context.active_node
**类型**: `bpy.types.Node`
活动节点

### bpy.context.light
**类型**: `bpy.types.Light`
灯光

### bpy.context.material
**类型**: `bpy.types.Material`
材质

### bpy.context.world
**类型**: `bpy.types.World`
世界

## 屏幕上下文 (Screen Context)

### bpy.context.scene
**类型**: `bpy.types.Scene`
场景

### bpy.context.view_layer
**类型**: `bpy.types.ViewLayer`
视图层

### bpy.context.visible_objects
**类型**: `sequence of bpy.types.Object`
可见对象

### bpy.context.selectable_objects
**类型**: `sequence of bpy.types.Object`
可选择对象

### bpy.context.selected_objects
**类型**: `sequence of bpy.types.Object`
选中的对象

### bpy.context.editable_objects
**类型**: `sequence of bpy.types.Object`
可编辑对象

### bpy.context.selected_editable_objects
**类型**: `sequence of bpy.types.Object`
选中的可编辑对象

### bpy.context.objects_in_mode
**类型**: `sequence of bpy.types.Object`
模式中的对象

### bpy.context.objects_in_mode_unique_data
**类型**: `sequence of bpy.types.Object`
模式中具有唯一数据的对象

### bpy.context.visible_bones
**类型**: `sequence of bpy.types.EditBone`
可见骨骼

### bpy.context.editable_bones
**类型**: `sequence of bpy.types.EditBone`
可编辑骨骼

### bpy.context.selected_bones
**类型**: `sequence of bpy.types.EditBone`
选中的骨骼

### bpy.context.selected_editable_bones
**类型**: `sequence of bpy.types.EditBone`
选中的可编辑骨骼

### bpy.context.visible_pose_bones
**类型**: `sequence of bpy.types.PoseBone`
可见姿态骨骼

### bpy.context.selected_pose_bones
**类型**: `sequence of bpy.types.PoseBone`
选中的姿态骨骼

### bpy.context.selected_pose_bones_from_active_object
**类型**: `sequence of bpy.types.PoseBone`
来自活动对象的选中姿态骨骼

### bpy.context.active_bone
**类型**: `bpy.types.EditBone`
活动骨骼

### bpy.context.active_pose_bone
**类型**: `bpy.types.PoseBone`
活动姿态骨骼

### bpy.context.active_object
**类型**: `bpy.types.Object`
活动对象

### bpy.context.object
**类型**: `bpy.types.Object`
对象

### bpy.context.edit_object
**类型**: `bpy.types.Object`
编辑对象

### bpy.context.sculpt_object
**类型**: `bpy.types.Object`
雕刻对象

### bpy.context.vertex_paint_object
**类型**: `bpy.types.Object`
顶点绘制对象

### bpy.context.weight_paint_object
**类型**: `bpy.types.Object`
权重绘制对象

### bpy.context.image_paint_object
**类型**: `bpy.types.Object`
图像绘制对象

### bpy.context.particle_edit_object
**类型**: `bpy.types.Object`
粒子编辑对象

### bpy.context.pose_object
**类型**: `bpy.types.Object`
姿态对象

### bpy.context.active_sequence_strip
**类型**: `bpy.types.Sequence`
活动序列条

### bpy.context.sequences
**类型**: `sequence of bpy.types.Sequence`
序列

### bpy.context.selected_sequences
**类型**: `sequence of bpy.types.Sequence`
选中的序列

### bpy.context.selected_editable_sequences
**类型**: `sequence of bpy.types.Sequence`
选中的可编辑序列

### bpy.context.active_nla_track
**类型**: `bpy.types.NlaTrack`
活动NLA轨道

### bpy.context.active_nla_strip
**类型**: `bpy.types.NlaStrip`
活动NLA条

### bpy.context.selected_nla_strips
**类型**: `sequence of bpy.types.NlaStrip`
选中的NLA条

### bpy.context.selected_movieclip_tracks
**类型**: `sequence of bpy.types.MovieTrackingTrack`
选中的电影剪辑轨道

### bpy.context.gpencil_data
**类型**: `bpy.types.GreasePencil`
蜡笔数据

### bpy.context.gpencil_data_owner
**类型**: `bpy.types.ID`
蜡笔数据所有者

### bpy.context.annotation_data
**类型**: `bpy.types.GreasePencil`
注释数据

### bpy.context.annotation_data_owner
**类型**: `bpy.types.ID`
注释数据所有者

### bpy.context.visible_gpencil_layers
**类型**: `sequence of bpy.types.GPencilLayer`
可见蜡笔层

### bpy.context.editable_gpencil_layers
**类型**: `sequence of bpy.types.GPencilLayer`
可编辑蜡笔层

### bpy.context.editable_gpencil_strokes
**类型**: `sequence of bpy.types.GPencilStroke`
可编辑蜡笔笔画

### bpy.context.active_gpencil_layer
**类型**: `sequence of bpy.types.GPencilLayer`
活动蜡笔层

### bpy.context.active_gpencil_frame
**类型**: `sequence of bpy.types.GreasePencilLayer`
活动蜡笔帧

### bpy.context.active_annotation_layer
**类型**: `bpy.types.GPencilLayer`
活动注释层

### bpy.context.active_operator
**类型**: `bpy.types.Operator`
活动操作符

### bpy.context.active_action
**类型**: `bpy.types.Action`
活动动作

### bpy.context.selected_visible_actions
**类型**: `sequence of bpy.types.Action`
选中的可见动作

### bpy.context.selected_editable_actions
**类型**: `sequence of bpy.types.Action`
选中的可编辑动作

### bpy.context.visible_fcurves
**类型**: `sequence of bpy.types.FCurve`
可见F曲线

### bpy.context.editable_fcurves
**类型**: `sequence of bpy.types.FCurve`
可编辑F曲线

### bpy.context.selected_visible_fcurves
**类型**: `sequence of bpy.types.FCurve`
选中的可见F曲线

### bpy.context.selected_editable_fcurves
**类型**: `sequence of bpy.types.FCurve`
选中的可编辑F曲线

### bpy.context.active_editable_fcurve
**类型**: `bpy.types.FCurve`
活动可编辑F曲线

### bpy.context.selected_editable_keyframes
**类型**: `sequence of bpy.types.Keyframe`
选中的可编辑关键帧

### bpy.context.ui_list
**类型**: `bpy.types.UIList`
UI列表

### bpy.context.property
**类型**: `(bpy.types.ID, string, int)`
获取与悬停按钮关联的属性。返回数据块、属性数据路径和数组索引的元组。

**示例**：为悬停的属性插入关键帧
```python
active_property = bpy.context.property
if active_property:
    datablock, data_path, index = active_property
    datablock.keyframe_insert(data_path=data_path, index=index, frame=1)
```

### bpy.context.asset_library_reference
**类型**: `bpy.types.AssetLibraryReference`
资产库引用

## 序列器上下文 (Sequencer Context)

### bpy.context.edit_mask
**类型**: `bpy.types.Mask`
编辑遮罩

## 文本上下文 (Text Context)

### bpy.context.edit_text
**类型**: `bpy.types.Text`
编辑文本

## 3D视图上下文 (View3D Context)

### bpy.context.active_object
**类型**: `bpy.types.Object`
活动对象

### bpy.context.selected_ids
**类型**: `sequence of bpy.types.ID`
选中的ID

## 实用示例

```python
import bpy

# 获取当前上下文信息
def print_context_info():
    print("=== Blender 上下文信息 ===")
    print(f"当前场景: {bpy.context.scene.name}")
    print(f"当前模式: {bpy.context.mode}")
    print(f"活动对象: {bpy.context.active_object.name if bpy.context.active_object else '无'}")
    print(f"选中对象数量: {len(bpy.context.selected_objects)}")
    print(f"渲染引擎: {bpy.context.engine}")
    print(f"当前视图层: {bpy.context.view_layer.name}")

# 获取选中对象信息
def print_selected_objects():
    print("\n=== 选中的对象 ===")
    for obj in bpy.context.selected_objects:
        print(f"对象: {obj.name}, 类型: {obj.type}, 位置: {obj.location}")

# 检查当前区域
def check_current_area():
    print(f"\n=== 当前区域 ===")
    print(f"区域类型: {bpy.context.area.type if bpy.context.area else '无区域'}")
    print(f"空间类型: {bpy.context.space_data.type if bpy.context.space_data else '无空间'}")

# 运行示例
print_context_info()
print_selected_objects()
check_current_area()
```

这个翻译涵盖了Blender 4.0.3中bpy.context的所有属性和功能，为中文用户提供了完整的上下文访问参考。
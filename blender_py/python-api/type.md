我来为您翻译Blender的bpy.types模块中的这些类型定义：

# Blender Python API 类型定义 (bpy.types)

## 纹理节点类型 (TextureNode)

### 基础纹理节点
- **TextureNode** - 纹理节点基类
- **TextureNodeAt** - 纹理坐标节点
- **TextureNodeBricks** - 砖块纹理节点
- **TextureNodeChecker** - 棋盘格纹理节点
- **TextureNodeCompose** - 合成纹理节点
- **TextureNodeCoordinates** - 坐标纹理节点
- **TextureNodeCurveRGB** - RGB曲线纹理节点
- **TextureNodeCurveTime** - 时间曲线纹理节点
- **TextureNodeDecompose** - 分解纹理节点
- **TextureNodeDistance** - 距离纹理节点
- **TextureNodeGroup** - 纹理节点组
- **TextureNodeHueSaturation** - 色相饱和度纹理节点
- **TextureNodeImage** - 图像纹理节点
- **TextureNodeInvert** - 反转纹理节点
- **TextureNodeMath** - 数学纹理节点
- **TextureNodeMixRGB** - RGB混合纹理节点
- **TextureNodeOutput** - 输出纹理节点
- **TextureNodeRGBToBW** - RGB转黑白纹理节点
- **TextureNodeRotate** - 旋转纹理节点
- **TextureNodeScale** - 缩放纹理节点
- **TextureNodeSeparateColor** - 分离颜色纹理节点
- **TextureNodeTexture** - 纹理节点
- **TextureNodeTranslate** - 平移纹理节点
- **TextureNodeValToNor** - 值转法线纹理节点
- **TextureNodeValToRGB** - 值转RGB纹理节点
- **TextureNodeViewer** - 查看器纹理节点

### 程序化纹理节点
- **TextureNodeTexBlend** - 混合纹理节点
- **TextureNodeTexClouds** - 云彩纹理节点
- **TextureNodeTexDistNoise** - 距离噪声纹理节点
- **TextureNodeTexMagic** - 魔法纹理节点
- **TextureNodeTexMarble** - 大理石纹理节点
- **TextureNodeTexMusgrave** - Musgrave纹理节点
- **TextureNodeTexNoise** - 噪声纹理节点
- **TextureNodeTexStucci** - 凹凸纹理节点
- **TextureNodeTexVoronoi** - Voronoi纹理节点
- **TextureNodeTexWood** - 木纹纹理节点

### 颜色处理节点
- **TextureNodeCombineColor** - 组合颜色纹理节点

## 主题系统 (Theme)

### 界面主题
- **Theme** - 主题基类
- **ThemeUserInterface** - 用户界面主题
- **ThemeStyle** - 样式主题
- **ThemeFontStyle** - 字体样式主题
- **ThemeGradientColors** - 渐变颜色主题
- **ThemeWidgetColors** - 控件颜色主题
- **ThemeWidgetStateColors** - 控件状态颜色主题
- **ThemePanelColors** - 面板颜色主题
- **ThemeStripColor** - 条带颜色主题
- **ThemeCollectionColor** - 集合颜色主题
- **ThemeBoneColorSet** - 骨骼颜色集主题

### 编辑器主题
- **ThemeView3D** - 3D视图主题
- **ThemeGraphEditor** - 图形编辑器主题
- **ThemeNodeEditor** - 节点编辑器主题
- **ThemeImageEditor** - 图像编辑器主题
- **ThemeTextEditor** - 文本编辑器主题
- **ThemeConsole** - 控制台主题
- **ThemeInfo** - 信息主题
- **ThemeFileBrowser** - 文件浏览器主题
- **ThemeOutliner** - 大纲视图主题
- **ThemeProperties** - 属性主题
- **ThemePreferences** - 偏好设置主题
- **ThemeSpreadsheet** - 电子表格主题
- **ThemeStatusBar** - 状态栏主题
- **ThemeTopBar** - 顶部栏主题

### 动画编辑器主题
- **ThemeDopeSheet** - 摄影表主题
- **ThemeNLAEditor** - 非线性动画编辑器主题
- **ThemeSequenceEditor** - 序列编辑器主题
- **ThemeClipEditor** - 剪辑编辑器主题

### 空间主题
- **ThemeSpaceGeneric** - 通用空间主题
- **ThemeSpaceGradient** - 渐变空间主题
- **ThemeSpaceListGeneric** - 通用列表空间主题

### 特殊主题
- **ThemeAssetShelf** - 资产架主题

## 修改器类型 (Modifier)

### 几何体修改器
- **TriangulateModifier** - 三角化修改器
- **UVProjectModifier** - UV投影修改器
- **UVWarpModifier** - UV扭曲修改器
- **VolumeDisplaceModifier** - 体积置换修改器
- **VolumeToMeshModifier** - 体积转网格修改器
- **WarpModifier** - 扭曲修改器
- **WaveModifier** - 波浪修改器
- **WeightedNormalModifier** - 加权法线修改器
- **WeldModifier** - 焊接修改器
- **WireframeModifier** - 线框修改器

### 顶点权重修改器
- **VertexWeightEditModifier** - 顶点权重编辑修改器
- **VertexWeightMixModifier** - 顶点权重混合修改器
- **VertexWeightProximityModifier** - 顶点权重邻近修改器

### 约束类型 (Constraint)
- **TrackToConstraint** - 跟踪约束
- **TransformCacheConstraint** - 变换缓存约束
- **TransformConstraint** - 变换约束

## 蜡笔修改器 (GpencilModifier)
- **TextureGpencilModifier** - 纹理蜡笔修改器
- **ThickGpencilModifier** - 厚度蜡笔修改器
- **TimeGpencilModifier** - 时间蜡笔修改器
- **TintGpencilModifier** - 着色蜡笔修改器
- **WeightAngleGpencilModifier** - 角度权重蜡笔修改器
- **WeightProxGpencilModifier** - 邻近权重蜡笔修改器

## 时间相关
- **TimelineMarker** - 时间线标记
- **TimelineMarkers** - 时间线标记集合
- **Timer** - 计时器
- **TimeGpencilModifierSegment** - 时间蜡笔修改器段

## 变换系统
- **TransformOrientation** - 变换方向
- **TransformOrientationSlot** - 变换方向槽
- **TransformSequence** - 变换序列

## 工具设置
- **ToolSettings** - 工具设置
- **UnifiedPaintSettings** - 统一绘制设置

## 单位设置
- **UnitSettings** - 单位设置

## 用户相关
- **UserAssetLibrary** - 用户资产库
- **UserExtensionRepo** - 用户扩展仓库
- **UserExtensionRepoCollection** - 用户扩展仓库集合
- **UserSolidLight** - 用户实体灯光

## 资产系统
- **VIEW3D_AST_pose_library** - 3D视图姿态库资产架
- **VIEW3D_AST_sculpt_brushes** - 3D视图雕刻笔刷资产架

## UI列表
- **UIList** - UI列表
- **UI_UL_list** - UI列表基类
- **USERPREF_UL_asset_libraries** - 偏好设置资产库列表
- **USERPREF_UL_extension_repos** - 偏好设置扩展仓库列表
- **VIEWLAYER_UL_aov** - 视图层AOV列表
- **VIEWLAYER_UL_linesets** - 视图层线条集列表
- **VOLUME_UL_grids** - 体积网格列表

## 几何体数据
- **UVLoopLayers** - UV循环层
- **UVProjector** - UV投影器
- **VertexGroup** - 顶点组
- **VertexGroupElement** - 顶点组元素
- **VertexGroups** - 顶点组集合

## 绘制系统
- **VertexPaint** - 顶点绘制
- **Paint** - 绘制基类

## 视图系统
- **View2D** - 2D视图
- **View3DCursor** - 3D光标
- **View3DOverlay** - 3D覆盖层
- **View3DShading** - 3D着色
- **ViewLayer** - 视图层
- **ViewLayerEEVEE** - 视图层EEVEE
- **ViewLayers** - 视图层集合

## 查看器路径
- **ViewerPath** - 查看器路径
- **ViewerPathElem** - 查看器路径元素
- **ViewerNodeViewerPathElem** - 查看器节点查看器路径元素

## 体积系统
- **Volume** - 体积
- **VolumeDisplay** - 体积显示
- **VolumeGrid** - 体积网格
- **VolumeGrids** - 体积网格集合
- **VolumeRender** - 体积渲染

## 纹理
- **VoronoiTexture** - Voronoi纹理
- **WoodTexture** - 木纹纹理

## 导航
- **WalkNavigation** - 行走导航

## 窗口管理
- **Window** - 窗口
- **WindowManager** - 窗口管理器

## 工作区
- **WorkSpace** - 工作区
- **WorkSpaceTool** - 工作区工具

## 世界
- **World** - 世界
- **WorldLighting** - 世界照明
- **WorldMistSettings** - 世界雾效设置

## XR系统
- **XrActionMap** - XR动作映射
- **XrActionMapBinding** - XR动作映射绑定
- **XrActionMapBindings** - XR动作映射绑定集合
- **XrActionMapItem** - XR动作映射项
- **XrActionMapItems** - XR动作映射项集合
- **XrActionMaps** - XR动作映射集合
- **XrComponentPath** - XR组件路径
- **XrComponentPaths** - XR组件路径集合
- **XrEventData** - XR事件数据
- **XrSessionSettings** - XR会话设置
- **XrSessionState** - XR会话状态
- **XrUserPath** - XR用户路径
- **XrUserPaths** - XR用户路径集合

## 序列效果
- **WipeSequence** - 擦除序列

## 字体
- **VectorFont** - 矢量字体

## 其他类型
- **UDIMTile** - UDIM瓦片
- **UDIMTiles** - UDIM瓦片集合
- **UILayout** - UI布局
- **UIPieMenu** - UI饼状菜单
- **UIPopover** - UI弹出框
- **UIPopupMenu** - UI弹出菜单
- **USDHook** - USD钩子
- **UnknownType** - 未知类型
- **bpy_prop_collection** - bpy属性集合
- **bpy_struct** - bpy结构体
- **wmOwnerID** - 窗口管理器所有者ID
- **wmOwnerIDs** - 窗口管理器所有者ID集合
- **wmTools** - 窗口管理器工具

## 使用示例

### 1. **创建纹理节点**
```python
import bpy

# 创建纹理节点树
texture_tree = bpy.data.textures.new("MyTexture", type='NODE_TREE')

# 添加噪声纹理节点
noise_node = texture_tree.nodes.new('TextureNodeTexNoise')
noise_node.location = (0, 0)

# 添加颜色映射节点
color_ramp = texture_tree.nodes.new('TextureNodeValToRGB')
color_ramp.location = (200, 0)

# 连接节点
texture_tree.links.new(noise_node.outputs[0], color_ramp.inputs[0])
```

### 2. **应用修改器**
```python
import bpy

# 获取活动对象
obj = bpy.context.active_object

if obj and obj.type == 'MESH':
    # 添加线框修改器
    wireframe = obj.modifiers.new(name="Wireframe", type='WIREFRAME')
    wireframe.thickness = 0.1
    
    # 添加加权法线修改器
    weighted_normal = obj.modifiers.new(name="WeightedNormal", type='WEIGHTED_NORMAL')
    weighted_normal.keep_sharp = True
```

### 3. **设置主题**
```python
import bpy

# 获取当前主题
theme = bpy.context.preferences.themes[0]

# 修改3D视图主题
theme.view_3d.space.gradients.high = (0.8, 0.8, 0.8)
theme.view_3d.space.gradients.low = (0.2, 0.2, 0.2)

# 修改节点编辑器主题
theme.node_editor.space.back = (0.1, 0.1, 0.1)
theme.node_editor.space.grid = (0.3, 0.3, 0.3)
```

### 4. **创建顶点组**
```python
import bpy

obj = bpy.context.active_object

if obj and obj.type == 'MESH':
    # 创建新的顶点组
    vertex_group = obj.vertex_groups.new(name="MyVertexGroup")
    
    # 添加顶点到组
    vertices = [0, 1, 2, 3]  # 顶点索引
    vertex_group.add(vertices, 1.0, 'REPLACE')
```

### 5. **设置变换方向**
```python
import bpy

# 创建自定义变换方向
transform_orientation = bpy.context.scene.transform_orientation_slots[0]
transform_orientation.type = 'GIMBAL'

# 或者使用全局方向
bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'
```

这个翻译涵盖了Blender Python API中主要的类型定义，为中文用户提供了完整的类型参考。

我来为您翻译Blender的Utilities (bpy.utils)文档并保存到指定目录：

我已经成功为您翻译了Blender的Utilities (bpy.utils)文档并保存到了`blender_py/python-api/Utilities (bpy.utils).md`文件中。

这个文档包含了以下主要内容：

## 主要功能模块

1. **文件路径处理** - `blend_paths()`函数用于获取外部文件路径
2. **字符串处理** - `escape_identifier()`, `unescape_identifier()`, `flip_name()`等函数
3. **类注册管理** - `register_class()`, `unregister_class()`等函数
4. **资源路径管理** - `resource_path()`, `user_resource()`等函数
5. **脚本管理** - `load_scripts()`, `modules_from_path()`等函数
6. **预设管理** - `preset_find()`, `preset_paths()`等函数
7. **工具注册** - `register_tool()`, `unregister_tool()`等函数
8. **时间格式转换** - `smpte_from_frame()`, `smpte_from_seconds()`等函数
9. **文件执行** - `execfile()`函数

## 实用示例

文档还包含了6个完整的使用示例：
1. 完整的插件注册示例
2. 资源路径管理示例
3. 预设管理示例
4. 时间格式转换示例
5. 脚本路径管理示例
6. 工具注册示例

这个翻译为中文用户提供了完整的bpy.utils模块参考，包含了所有函数的详细说明、参数、返回值和实际使用示例。
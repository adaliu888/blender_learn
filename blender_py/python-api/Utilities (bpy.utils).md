# Utilities (bpy.utils) 实用工具

## 概述
此模块包含特定于Blender的实用函数，但不与Blender的内部数据关联。

## 子模块

- **bpy.utils.previews** - 预览子模块
- **bpy.utils.units** - 单位子模块

## 核心函数

### 文件路径处理

#### bpy.utils.blend_paths()
返回由加载的.blend文件引用的外部文件路径列表。

**参数：**
- `absolute` (boolean) - 当为true时，返回的路径将变为绝对路径
- `packed` (boolean) - 当为true时跳过打包数据的文件路径
- `local` (boolean) - 当为true时跳过链接库路径

**返回：**
- 路径列表

**返回类型：**
- 字符串列表

```python
import bpy

# 获取所有外部文件路径
paths = bpy.utils.blend_paths()
print("外部文件路径:", paths)

# 获取绝对路径
absolute_paths = bpy.utils.blend_paths(absolute=True)
print("绝对路径:", absolute_paths)
```

### 字符串处理

#### bpy.utils.escape_identifier(string)
用于动画路径的简单字符串转义函数。

**参数：**
- `string` (string) - 文本

**返回：**
- 转义后的字符串

**返回类型：**
- string

#### bpy.utils.unescape_identifier(string)
用于动画路径的简单字符串反转义函数。执行escape_identifier的反向操作。

**参数：**
- `string` (string) - 文本

**返回：**
- 反转义后的字符串

**返回类型：**
- string

```python
import bpy

# 转义标识符
escaped = bpy.utils.escape_identifier("my.property")
print("转义后:", escaped)

# 反转义标识符
unescaped = bpy.utils.unescape_identifier(escaped)
print("反转义后:", unescaped)
```

#### bpy.utils.flip_name(name, strip_digits=False)
在左/右侧之间翻转名称，对镜像骨骼名称很有用。

**参数：**
- `name` (string) - 要翻转的骨骼名称
- `strip_digits` (bool) - 是否移除.###后缀

**返回：**
- 翻转后的名称

**返回类型：**
- string

```python
import bpy

# 翻转骨骼名称
original_name = "arm.L"
flipped_name = bpy.utils.flip_name(original_name)
print(f"原始名称: {original_name}")
print(f"翻转后: {flipped_name}")

# 带数字后缀的翻转
name_with_digits = "finger.L.001"
flipped_with_digits = bpy.utils.flip_name(name_with_digits, strip_digits=True)
print(f"带数字后缀翻转: {flipped_with_digits}")
```

### 类注册管理

#### bpy.utils.register_class(cls)
注册Blender类型类的子类。

**参数：**
- `cls` (class) - Blender类型类，包括：bpy.types.Panel, bpy.types.UIList, bpy.types.Menu, bpy.types.Header, bpy.types.Operator, bpy.types.KeyingSetInfo, bpy.types.RenderEngine, bpy.types.AssetShelf

**异常：**
- ValueError - 如果类不是可注册的blender类的子类

**注意：**
如果类有register类方法，它将在注册前被调用。

#### bpy.utils.unregister_class(cls)
从blender中卸载Python类。

如果类有unregister类方法，它将在注销前被调用。

```python
import bpy

# 定义自定义操作符
class MyCustomOperator(bpy.types.Operator):
    bl_idname = "object.my_custom_operator"
    bl_label = "我的自定义操作符"
    
    def execute(self, context):
        print("执行自定义操作符")
        return {'FINISHED'}

# 注册类
bpy.utils.register_class(MyCustomOperator)

# 注销类
bpy.utils.unregister_class(MyCustomOperator)
```

### 资源路径管理

#### bpy.utils.resource_path(type, major=bpy.app.version[0], minor=bpy.app.version[1])
返回存储系统文件的基础路径。

**参数：**
- `type` (string) - 字符串，可选值：['USER', 'LOCAL', 'SYSTEM']
- `major` (int) - 主版本号，默认为当前版本
- `minor` (string) - 次版本号，默认为当前版本

**返回：**
- 资源路径（不一定存在）

**返回类型：**
- string

```python
import bpy

# 获取用户资源路径
user_path = bpy.utils.resource_path('USER')
print(f"用户资源路径: {user_path}")

# 获取系统资源路径
system_path = bpy.utils.resource_path('SYSTEM')
print(f"系统资源路径: {system_path}")

# 获取本地资源路径
local_path = bpy.utils.resource_path('LOCAL')
print(f"本地资源路径: {local_path}")
```

### 脚本管理

#### bpy.utils.load_scripts()
加载脚本并运行每个模块的register函数。

**参数：**
- `reload_scripts` (bool) - 导致所有脚本在加载前调用其unregister方法
- `refresh_scripts` (bool) - 仅加载尚未作为模块加载的脚本
- `extensions` (bool) - 加载附加脚本（插件和应用程序模板）

```python
import bpy

# 加载所有脚本
bpy.utils.load_scripts()

# 重新加载脚本
bpy.utils.load_scripts(reload_scripts=True)

# 仅刷新脚本
bpy.utils.load_scripts(refresh_scripts=True)
```

#### bpy.utils.modules_from_path(path, loaded_modules)
加载路径中的所有模块并将它们作为列表返回。

**参数：**
- `path` (string) - 扫描脚本和包的路径
- `loaded_modules` (set) - 已加载的模块名称，匹配这些名称的文件将被忽略

**返回：**
- 所有加载的模块

**返回类型：**
- list

```python
import bpy

# 从路径加载模块
loaded_modules = set()
modules = bpy.utils.modules_from_path("/path/to/scripts", loaded_modules)
print(f"加载了 {len(modules)} 个模块")
```

#### bpy.utils.refresh_script_paths()
在创建新脚本路径后运行此函数以更新sys.path

```python
import bpy

# 刷新脚本路径
bpy.utils.refresh_script_paths()
```

### 预设管理

#### bpy.utils.preset_find(name, preset_path, *, display_name=False, ext='.py')
查找预设文件。

#### bpy.utils.preset_paths(subdir)
返回特定预设的路径列表。

**参数：**
- `subdir` (string) - 预设子目录（不能是绝对路径）

**返回：**
- 脚本路径

**返回类型：**
- list

```python
import bpy

# 获取预设路径
preset_paths = bpy.utils.preset_paths("operators")
print("预设路径:", preset_paths)
```

### 应用程序模板

#### bpy.utils.app_template_paths(*, path=None)
返回有效的应用程序模板路径。

**参数：**
- `path` (string) - 可选的子目录

**返回：**
- 应用程序模板路径

**返回类型：**
- generator

```python
import bpy

# 获取应用程序模板路径
template_paths = list(bpy.utils.app_template_paths())
print("应用程序模板路径:", template_paths)
```

### 工具注册

#### bpy.utils.register_tool(tool_cls, *, after=None, separator=False, group=False)
在工具栏中注册工具。

**参数：**
- `tool_cls` (bpy.types.WorkSpaceTool subclass) - 工具子类
- `after` (collection of strings or None) - 此工具将在其后添加的可选标识符
- `separator` (bool) - 当为true时，在此工具前添加分隔符
- `group` (bool) - 当为true时，添加新的嵌套工具组

#### bpy.utils.unregister_tool(tool_cls)
注销工具。

```python
import bpy

# 定义自定义工具
class MyCustomTool(bpy.types.WorkSpaceTool):
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    
    bl_idname = "view3d.my_custom_tool"
    bl_label = "我的自定义工具"
    bl_description = "这是一个自定义工具"
    
    def draw_settings(self, context, layout):
        layout.label(text="工具设置")

# 注册工具
bpy.utils.register_tool(MyCustomTool, separator=True)

# 注销工具
bpy.utils.unregister_tool(MyCustomTool)
```

### RNA路径创建

#### bpy.utils.make_rna_paths(struct_name, prop_name, enum_name)
从给定名称创建RNA"路径"。

**参数：**
- `struct_name` (string) - RNA结构名称（如"Scene"）
- `prop_name` (string) - RNA结构属性的名称
- `enum_name` (string) - RNA枚举标识符的名称

**返回：**
- 三个"RNA路径"的三元组（最完整路径，"struct.prop"，"struct.prop:'enum'"）。如果没有给出enum_name，第三个元素将始终为空。

**返回类型：**
- tuple of strings

```python
import bpy

# 创建RNA路径
paths = bpy.utils.make_rna_paths("Scene", "frame_current", "REPEAT")
print("RNA路径:", paths)
```

### 手册映射

#### bpy.utils.register_manual_map(manual_hook)
注册手册映射。

#### bpy.utils.unregister_manual_map(manual_hook)
注销手册映射。

#### bpy.utils.manual_map()
获取手册映射。

#### bpy.utils.manual_language_code(default='en')
返回基于当前语言用户偏好的用户手册URL组件使用的语言代码，在不可用时回退到默认值。

**返回：**
- 语言代码

**返回类型：**
- str

```python
import bpy

# 获取手册语言代码
lang_code = bpy.utils.manual_language_code()
print(f"手册语言代码: {lang_code}")
```

### 脚本路径管理

#### bpy.utils.script_path_user()
返回环境变量，如果不可用则回退到主目录或None

#### bpy.utils.script_paths(*, subdir=None, user_pref=True, check_all=False, use_user=True)
返回有效脚本路径的列表。

**参数：**
- `subdir` (string) - 可选的子目录
- `user_pref` (bool) - 包含用户偏好脚本路径
- `check_all` (bool) - 包含本地、用户和系统路径，而不仅仅是Blender使用的路径

**返回：**
- 脚本路径

**返回类型：**
- list

```python
import bpy

# 获取脚本路径
script_paths = bpy.utils.script_paths()
print("脚本路径:", script_paths)

# 获取用户脚本路径
user_script_path = bpy.utils.script_path_user()
print("用户脚本路径:", user_script_path)
```

### 时间格式转换

#### bpy.utils.smpte_from_frame(frame, *, fps=None, fps_base=None)
从帧返回SMPTE格式字符串：HH:MM:SS:FF。

如果未给出fps和fps_base，则使用当前场景。

**参数：**
- `frame` (int or float) - 帧号

**返回：**
- 帧字符串

**返回类型：**
- string

#### bpy.utils.smpte_from_seconds(time, *, fps=None, fps_base=None)
从时间返回SMPTE格式字符串：HH:MM:SS:FF。

如果未给出fps和fps_base，则使用当前场景。

**参数：**
- `time` (int, float or datetime.timedelta) - 秒为单位的时间

**返回：**
- 帧字符串

**返回类型：**
- string

```python
import bpy

# 从帧转换为SMPTE格式
frame = 125
smpte_frame = bpy.utils.smpte_from_frame(frame)
print(f"帧 {frame} 的SMPTE格式: {smpte_frame}")

# 从秒转换为SMPTE格式
time_seconds = 5.5
smpte_time = bpy.utils.smpte_from_seconds(time_seconds)
print(f"时间 {time_seconds}秒 的SMPTE格式: {smpte_time}")
```

### 用户资源管理

#### bpy.utils.user_resource(resource_type, *, path='', create=False)
返回用户资源路径（通常来自用户的主目录）。

**参数：**
- `resource_type` (string) - 资源类型，可选值：['DATAFILES', 'CONFIG', 'SCRIPTS', 'AUTOSAVE']
- `path` (string) - 可选的子目录
- `create` (boolean) - 将路径视为目录，如果不存在则创建它

**返回：**
- 路径

**返回类型：**
- string

```python
import bpy

# 获取用户数据文件路径
data_path = bpy.utils.user_resource('DATAFILES')
print(f"用户数据文件路径: {data_path}")

# 获取用户配置路径
config_path = bpy.utils.user_resource('CONFIG')
print(f"用户配置路径: {config_path}")

# 获取用户脚本路径
scripts_path = bpy.utils.user_resource('SCRIPTS')
print(f"用户脚本路径: {scripts_path}")

# 获取自动保存路径
autosave_path = bpy.utils.user_resource('AUTOSAVE')
print(f"自动保存路径: {autosave_path}")
```

### 文件执行

#### bpy.utils.execfile(filepath, *, mod=None)
将文件路径作为Python脚本执行。

**参数：**
- `filepath` (string) - 要执行的脚本路径
- `mod` (Module or None) - 可选的缓存模块，之前执行的结果

**返回：**
- 可以作为mod传递回的模块

**返回类型：**
- ModuleType

```python
import bpy

# 执行Python脚本文件
try:
    module = bpy.utils.execfile("/path/to/script.py")
    print("脚本执行成功")
except Exception as e:
    print(f"脚本执行失败: {e}")
```

### 实用函数工厂

#### bpy.utils.register_classes_factory(classes)
创建register和unregister函数的实用函数，这些函数简单地注册和注销类序列。

```python
import bpy

# 定义多个类
class MyPanel(bpy.types.Panel):
    bl_label = "我的面板"
    bl_idname = "VIEW3D_PT_my_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '工具'

class MyOperator(bpy.types.Operator):
    bl_idname = "object.my_operator"
    bl_label = "我的操作符"
    
    def execute(self, context):
        return {'FINISHED'}

# 创建注册和注销函数
classes = [MyPanel, MyOperator]
register, unregister = bpy.utils.register_classes_factory(classes)

# 注册类
register()

# 注销类
unregister()
```

#### bpy.utils.register_submodule_factory(module_name, submodule_names)
创建register和unregister函数的实用函数，这些函数简单地加载子模块，调用它们的register和unregister函数。

**注意：**
模块按给定顺序注册，按相反顺序注销。

**参数：**
- `module_name` (string) - 模块名称，通常是__name__
- `submodule_names` (list of strings) - 要加载和卸载的子模块名称列表

**返回：**
- register和unregister函数

**返回类型：**
- tuple pair of functions

```python
import bpy

# 创建子模块注册函数
submodules = ['panel', 'operator', 'menu']
register, unregister = bpy.utils.register_submodule_factory(__name__, submodules)

# 注册子模块
register()

# 注销子模块
unregister()
```

### 键盘配置

#### bpy.utils.keyconfig_init()
初始化键盘配置。

#### bpy.utils.keyconfig_set(filepath, *, report=None)
设置键盘配置文件。

```python
import bpy

# 初始化键盘配置
bpy.utils.keyconfig_init()

# 设置键盘配置文件
bpy.utils.keyconfig_set("/path/to/keyconfig.py")
```

## 使用示例

### 1. **完整的插件注册示例**
```python
import bpy

# 定义面板
class MyPanel(bpy.types.Panel):
    bl_label = "我的工具面板"
    bl_idname = "VIEW3D_PT_my_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '我的工具'
    
    def draw(self, context):
        layout = self.layout
        layout.operator("object.my_operator")

# 定义操作符
class MyOperator(bpy.types.Operator):
    bl_idname = "object.my_operator"
    bl_label = "我的操作符"
    
    def execute(self, context):
        print("执行我的操作符")
        return {'FINISHED'}

# 定义菜单
class MyMenu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_my_menu"
    bl_label = "我的菜单"
    
    def draw(self, context):
        layout = self.layout
        layout.operator("object.my_operator")

# 注册所有类
classes = [MyPanel, MyOperator, MyMenu]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

# 注册插件
register()
```

### 2. **资源路径管理示例**
```python
import bpy
import os

def setup_resource_paths():
    """设置资源路径"""
    
    # 获取用户资源路径
    user_path = bpy.utils.user_resource('SCRIPTS', create=True)
    print(f"用户脚本路径: {user_path}")
    
    # 创建自定义脚本目录
    custom_scripts_dir = os.path.join(user_path, "my_scripts")
    if not os.path.exists(custom_scripts_dir):
        os.makedirs(custom_scripts_dir)
        print(f"创建自定义脚本目录: {custom_scripts_dir}")
    
    # 获取系统资源路径
    system_path = bpy.utils.resource_path('SYSTEM')
    print(f"系统资源路径: {system_path}")

setup_resource_paths()
```

### 3. **预设管理示例**
```python
import bpy

def manage_presets():
    """管理预设"""
    
    # 获取预设路径
    preset_paths = bpy.utils.preset_paths("operators")
    print("操作符预设路径:", preset_paths)
    
    # 查找特定预设
    preset_name = "my_preset"
    preset_file = bpy.utils.preset_find(preset_name, "operators")
    if preset_file:
        print(f"找到预设文件: {preset_file}")
    else:
        print(f"未找到预设: {preset_name}")

manage_presets()
```

### 4. **时间格式转换示例**
```python
import bpy

def time_conversion_examples():
    """时间格式转换示例"""
    
    # 设置场景帧率
    scene = bpy.context.scene
    scene.render.fps = 24
    
    # 从帧转换为SMPTE
    frames = [0, 24, 48, 72, 96, 120]
    for frame in frames:
        smpte = bpy.utils.smpte_from_frame(frame)
        print(f"帧 {frame:3d} -> {smpte}")
    
    # 从秒转换为SMPTE
    times = [0, 1, 2, 5, 10]
    for time in times:
        smpte = bpy.utils.smpte_from_seconds(time)
        print(f"时间 {time}秒 -> {smpte}")

time_conversion_examples()
```

### 5. **脚本路径管理示例**
```python
import bpy

def script_path_management():
    """脚本路径管理"""
    
    # 获取所有脚本路径
    all_paths = bpy.utils.script_paths(check_all=True)
    print("所有脚本路径:")
    for path in all_paths:
        print(f"  {path}")
    
    # 获取用户偏好脚本路径
    user_paths = bpy.utils.script_paths(user_pref=True)
    print("\n用户偏好脚本路径:")
    for path in user_paths:
        print(f"  {path}")
    
    # 获取特定子目录的路径
    addon_paths = bpy.utils.script_paths(subdir="addons")
    print("\n插件路径:")
    for path in addon_paths:
        print(f"  {path}")

script_path_management()
```

### 6. **工具注册示例**
```python
import bpy

# 定义自定义工具
class MyCustomTool(bpy.types.WorkSpaceTool):
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'OBJECT'
    
    bl_idname = "view3d.my_custom_tool"
    bl_label = "我的自定义工具"
    bl_description = "这是一个用于对象操作的自定义工具"
    
    def draw_settings(self, context, layout):
        layout.label(text="工具设置")
        layout.prop(context.scene, "my_tool_property")
    
    def draw_settings_advanced(self, context, layout):
        layout.label(text="高级设置")
    
    def draw_cursor(self, context):
        # 绘制自定义光标
        pass

def register_tool():
    """注册工具"""
    bpy.utils.register_tool(MyCustomTool, separator=True, group=True)
    print("自定义工具已注册")

def unregister_tool():
    """注销工具"""
    bpy.utils.unregister_tool(MyCustomTool)
    print("自定义工具已注销")

# 注册工具
register_tool()
```

这个文档涵盖了bpy.utils模块的所有主要功能，为中文用户提供了完整的实用工具参考。 
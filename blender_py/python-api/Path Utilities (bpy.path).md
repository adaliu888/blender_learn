# Path Utilities (bpy.path) 路径实用工具

## 概述
此模块与os.path具有类似的作用域，包含用于处理Blender中路径的实用函数。

## 核心函数

### 路径转换

#### bpy.path.abspath(path, *, start=None, library=None)
返回相对于当前blend文件的绝对路径，使用"//"前缀。

**参数：**
- `path` (string or bytes) - 要转换的路径
- `start` (string or bytes) - 相对于此路径，未设置时使用当前文件名
- `library` (bpy.types.Library) - 此路径来自的库。这仅为了方便而包含，当库不为None时，其路径替换start

**返回：**
- 绝对路径

**返回类型：**
- string

```python
import bpy

# 获取绝对路径
relative_path = "//textures/my_texture.png"
absolute_path = bpy.path.abspath(relative_path)
print(f"相对路径: {relative_path}")
print(f"绝对路径: {absolute_path}")

# 使用自定义起始路径
custom_start = "/path/to/blend/file"
absolute_path = bpy.path.abspath(relative_path, start=custom_start)
print(f"自定义起始路径的绝对路径: {absolute_path}")
```

#### bpy.path.relpath(path, *, start=None)
返回相对于当前blend文件的路径，使用"//"前缀。

**参数：**
- `path` (string or bytes) - 绝对路径
- `start` (string or bytes) - 相对于此路径，未设置时使用当前文件名

**返回：**
- 相对路径

**返回类型：**
- string

```python
import bpy

# 获取相对路径
absolute_path = "/home/user/project/textures/my_texture.png"
relative_path = bpy.path.relpath(absolute_path)
print(f"绝对路径: {absolute_path}")
print(f"相对路径: {relative_path}")

# 使用自定义起始路径
custom_start = "/home/user/project"
relative_path = bpy.path.relpath(absolute_path, start=custom_start)
print(f"自定义起始路径的相对路径: {relative_path}")
```

### 路径组件处理

#### bpy.path.basename(path)
等同于os.path.basename，但跳过"//"前缀。

用于Windows兼容性。

**参数：**
- `path` (string) - 路径

**返回：**
- 给定路径的基本名称

**返回类型：**
- string

```python
import bpy

# 获取基本名称
path = "//textures/my_texture.png"
basename = bpy.path.basename(path)
print(f"路径: {path}")
print(f"基本名称: {basename}")

# 带前缀的路径
path_with_prefix = "//models/character.blend"
basename = bpy.path.basename(path_with_prefix)
print(f"带前缀路径: {path_with_prefix}")
print(f"基本名称: {basename}")
```

### 名称清理和显示

#### bpy.path.clean_name(name, *, replace='_')
返回一个名称，其中可能在各种情况下（如写入文件时）造成问题的字符被替换。

除了A-Z/a-z、0-9之外的所有字符都被替换为"_"或定义的replace参数。

**参数：**
- `name` (string or bytes) - 路径名称
- `replace` (string) - 非有效字符的替换字符

**返回：**
- 清理后的名称

**返回类型：**
- string

```python
import bpy

# 清理文件名
dirty_name = "My File (with spaces) & symbols!.txt"
clean_name = bpy.path.clean_name(dirty_name)
print(f"原始名称: {dirty_name}")
print(f"清理后: {clean_name}")

# 使用自定义替换字符
clean_name_custom = bpy.path.clean_name(dirty_name, replace='-')
print(f"自定义替换: {clean_name_custom}")

# 处理特殊字符
special_name = "file@#$%^&*()"
clean_special = bpy.path.clean_name(special_name)
print(f"特殊字符: {special_name}")
print(f"清理后: {clean_special}")
```

#### bpy.path.display_name(name, *, has_ext=True, title_case=True)
从名称创建显示字符串，用于菜单和用户界面。适用于文件名和模块名。

**参数：**
- `name` (string) - 用于显示用户界面的名称
- `has_ext` (boolean) - 从名称中移除文件扩展名
- `title_case` (boolean) - 将小写名称转换为标题大小写

**返回：**
- 显示字符串

**返回类型：**
- string

```python
import bpy

# 创建显示名称
filename = "my_texture_file.png"
display_name = bpy.path.display_name(filename)
print(f"文件名: {filename}")
print(f"显示名称: {display_name}")

# 保留扩展名
display_with_ext = bpy.path.display_name(filename, has_ext=False)
print(f"保留扩展名: {display_with_ext}")

# 不转换为标题大小写
display_lower = bpy.path.display_name(filename, title_case=False)
print(f"小写显示: {display_lower}")

# 处理下划线
underscore_name = "my_texture_file_with_underscores.png"
display_underscore = bpy.path.display_name(underscore_name)
print(f"下划线文件名: {underscore_name}")
print(f"显示名称: {display_underscore}")
```

#### bpy.path.display_name_to_filepath(name)
执行display_name的反向操作，使用文件路径中不支持的字符的字面版本。

**参数：**
- `name` (string) - 要转换的显示名称

**返回：**
- 文件路径

**返回类型：**
- string

```python
import bpy

# 显示名称转文件路径
display_name = "My Texture File"
filepath = bpy.path.display_name_to_filepath(display_name)
print(f"显示名称: {display_name}")
print(f"文件路径: {filepath}")

# 处理特殊字符
special_display = "File with Spaces & Symbols"
special_filepath = bpy.path.display_name_to_filepath(special_display)
print(f"特殊显示名称: {special_display}")
print(f"文件路径: {special_filepath}")
```

#### bpy.path.display_name_from_filepath(name)
返回去除目录和扩展名的路径，确保与utf8兼容。

**参数：**
- `name` (string) - 要转换的文件路径

**返回：**
- 显示名称

**返回类型：**
- string

```python
import bpy

# 从文件路径获取显示名称
filepath = "/path/to/my_texture_file.png"
display_name = bpy.path.display_name_from_filepath(filepath)
print(f"文件路径: {filepath}")
print(f"显示名称: {display_name}")

# 处理复杂路径
complex_path = "/home/user/projects/textures/character_diffuse_map.jpg"
display_complex = bpy.path.display_name_from_filepath(complex_path)
print(f"复杂路径: {complex_path}")
print(f"显示名称: {display_complex}")
```

### 扩展名处理

#### bpy.path.ensure_ext(filepath, ext, *, case_sensitive=False)
如果尚未设置，则返回添加了扩展名的路径。

**参数：**
- `filepath` (string) - 文件路径
- `ext` (string) - 要检查的扩展名，可以是复合扩展名。应以点开头，如'.blend'或'.tar.gz'
- `case_sensitive` (boolean) - 比较扩展名时检查匹配的大小写

**返回：**
- 具有给定扩展名的文件路径

**返回类型：**
- string

```python
import bpy

# 确保扩展名
filepath = "/path/to/my_file"
filepath_with_ext = bpy.path.ensure_ext(filepath, ".blend")
print(f"原始路径: {filepath}")
print(f"添加扩展名: {filepath_with_ext}")

# 已有扩展名的情况
filepath_with_ext_already = "/path/to/my_file.blend"
result = bpy.path.ensure_ext(filepath_with_ext_already, ".blend")
print(f"已有扩展名: {filepath_with_ext_already}")
print(f"结果: {result}")

# 复合扩展名
filepath_tar = "/path/to/archive"
filepath_tar_gz = bpy.path.ensure_ext(filepath_tar, ".tar.gz")
print(f"原始路径: {filepath_tar}")
print(f"复合扩展名: {filepath_tar_gz}")

# 大小写敏感
filepath_upper = "/path/to/file.BLEND"
result_sensitive = bpy.path.ensure_ext(filepath_upper, ".blend", case_sensitive=True)
print(f"大小写敏感检查: {filepath_upper}")
print(f"结果: {result_sensitive}")
```

### 路径验证和解析

#### bpy.path.is_subdir(path, directory)
如果路径是目录的子目录，则返回true。两个路径都必须是绝对路径。

**参数：**
- `path` (string or bytes) - 绝对路径
- `directory` (string or bytes) - 要检查的目录

**返回：**
- 路径是否为子目录

**返回类型：**
- boolean

```python
import bpy

# 检查子目录
parent_dir = "/home/user/projects"
subdir = "/home/user/projects/textures"
not_subdir = "/home/user/documents"

is_sub = bpy.path.is_subdir(subdir, parent_dir)
is_not_sub = bpy.path.is_subdir(not_subdir, parent_dir)

print(f"路径: {subdir}")
print(f"父目录: {parent_dir}")
print(f"是子目录: {is_sub}")

print(f"路径: {not_subdir}")
print(f"父目录: {parent_dir}")
print(f"是子目录: {is_not_sub}")
```

#### bpy.path.resolve_ncase(path)
在区分大小写的系统上解析不区分大小写的路径，如果找到则返回带有路径的字符串，否则返回原始路径。

**参数：**
- `path` (string) - 要解析的路径名称

**返回：**
- 解析后的路径

**返回类型：**
- string

```python
import bpy

# 解析不区分大小写的路径
path = "/path/to/MyFile.txt"
resolved_path = bpy.path.resolve_ncase(path)
print(f"原始路径: {path}")
print(f"解析后路径: {resolved_path}")

# 处理不存在的情况
non_existent = "/path/to/nonexistent/file.txt"
resolved_non_existent = bpy.path.resolve_ncase(non_existent)
print(f"不存在路径: {non_existent}")
print(f"解析结果: {resolved_non_existent}")
```

### 路径分隔符处理

#### bpy.path.native_pathsep(path)
用系统的原生os.sep替换路径分隔符。

**参数：**
- `path` (string) - 要替换的路径

**返回：**
- 具有系统原生分隔符的路径

**返回类型：**
- string

```python
import bpy

# 转换路径分隔符
unix_path = "/home/user/file.txt"
windows_path = "C:\\Users\\user\\file.txt"

native_unix = bpy.path.native_pathsep(unix_path)
native_windows = bpy.path.native_pathsep(windows_path)

print(f"Unix路径: {unix_path}")
print(f"原生路径: {native_unix}")

print(f"Windows路径: {windows_path}")
print(f"原生路径: {native_windows}")
```

### 目录处理

#### bpy.path.reduce_dirs(dirs)
给定目录序列，移除重复项和嵌套在其他路径中的任何目录。（对递归路径搜索有用）

**参数：**
- `dirs` (sequence of strings) - 目录路径序列

**返回：**
- 唯一路径列表

**返回类型：**
- list of strings

```python
import bpy

# 减少目录列表
dirs = [
    "/home/user/projects",
    "/home/user/projects/textures",
    "/home/user/projects/models",
    "/home/user/documents",
    "/home/user/documents/work"
]

reduced_dirs = bpy.path.reduce_dirs(dirs)
print("原始目录列表:")
for dir in dirs:
    print(f"  {dir}")

print("\n减少后的目录列表:")
for dir in reduced_dirs:
    print(f"  {dir}")

# 处理重复项
duplicate_dirs = [
    "/path/to/dir",
    "/path/to/dir",
    "/path/to/dir/subdir",
    "/path/to/dir/subdir/deeper"
]

reduced_duplicates = bpy.path.reduce_dirs(duplicate_dirs)
print("\n重复目录列表:")
for dir in duplicate_dirs:
    print(f"  {dir}")

print("\n减少后的重复目录:")
for dir in reduced_duplicates:
    print(f"  {dir}")
```

### 模块名称处理

#### bpy.path.module_names(path, *, recursive=False, package='')
返回可以从路径导入的模块列表。

**参数：**
- `path` (string) - 要扫描的目录
- `recursive` (bool) - 也为包返回子模块名称
- `package` (string) - 可选的字符串，用作模块名称的前缀（不带尾随"."）

**返回：**
- 字符串对列表（module_name, module_file）

**返回类型：**
- list of strings

```python
import bpy
import os

# 获取模块名称
script_path = bpy.utils.script_paths()[0]  # 获取第一个脚本路径
module_names = bpy.path.module_names(script_path)

print(f"扫描路径: {script_path}")
print("可导入的模块:")
for module_name, module_file in module_names:
    print(f"  模块: {module_name}")
    print(f"  文件: {module_file}")

# 递归扫描
if os.path.exists(script_path):
    recursive_modules = bpy.path.module_names(script_path, recursive=True)
    print(f"\n递归扫描结果:")
    for module_name, module_file in recursive_modules:
        print(f"  模块: {module_name}")
        print(f"  文件: {module_file}")
```

## 使用示例

### 1. **完整的路径处理示例**
```python
import bpy
import os

def path_processing_example():
    """路径处理示例"""
    
    # 创建测试路径
    test_path = "//textures/my_texture.png"
    
    # 转换为绝对路径
    abs_path = bpy.path.abspath(test_path)
    print(f"绝对路径: {abs_path}")
    
    # 转换为相对路径
    rel_path = bpy.path.relpath(abs_path)
    print(f"相对路径: {rel_path}")
    
    # 获取基本名称
    basename = bpy.path.basename(test_path)
    print(f"基本名称: {basename}")
    
    # 清理文件名
    dirty_name = "My File (with spaces) & symbols!.txt"
    clean_name = bpy.path.clean_name(dirty_name)
    print(f"清理后的名称: {clean_name}")
    
    # 创建显示名称
    display_name = bpy.path.display_name("my_texture_file.png")
    print(f"显示名称: {display_name}")
    
    # 确保扩展名
    filepath = "/path/to/my_file"
    filepath_with_ext = bpy.path.ensure_ext(filepath, ".blend")
    print(f"带扩展名的路径: {filepath_with_ext}")

path_processing_example()
```

### 2. **文件路径管理示例**
```python
import bpy

def file_path_management():
    """文件路径管理示例"""
    
    # 处理Blender相对路径
    relative_paths = [
        "//textures/diffuse.png",
        "//models/character.blend",
        "//scripts/my_script.py"
    ]
    
    print("相对路径处理:")
    for rel_path in relative_paths:
        abs_path = bpy.path.abspath(rel_path)
        print(f"  相对: {rel_path}")
        print(f"  绝对: {abs_path}")
        print()
    
    # 处理文件名清理
    problematic_names = [
        "My File (with spaces).txt",
        "file@#$%^&*().blend",
        "texture with spaces & symbols.png"
    ]
    
    print("文件名清理:")
    for name in problematic_names:
        clean_name = bpy.path.clean_name(name)
        print(f"  原始: {name}")
        print(f"  清理: {clean_name}")
        print()

file_path_management()
```

### 3. **目录结构处理示例**
```python
import bpy

def directory_structure_processing():
    """目录结构处理示例"""
    
    # 模拟目录列表
    directories = [
        "/home/user/projects",
        "/home/user/projects/textures",
        "/home/user/projects/models",
        "/home/user/projects/textures/diffuse",
        "/home/user/projects/textures/normal",
        "/home/user/documents",
        "/home/user/documents/work",
        "/home/user/documents/personal"
    ]
    
    # 减少目录列表
    reduced_dirs = bpy.path.reduce_dirs(directories)
    
    print("原始目录列表:")
    for dir in directories:
        print(f"  {dir}")
    
    print("\n减少后的目录列表:")
    for dir in reduced_dirs:
        print(f"  {dir}")
    
    # 检查子目录关系
    parent_dir = "/home/user/projects"
    subdirs = [
        "/home/user/projects/textures",
        "/home/user/projects/models",
        "/home/user/documents"
    ]
    
    print(f"\n检查子目录关系 (父目录: {parent_dir}):")
    for subdir in subdirs:
        is_sub = bpy.path.is_subdir(subdir, parent_dir)
        print(f"  {subdir}: {'是' if is_sub else '不是'} 子目录")

directory_structure_processing()
```

### 4. **跨平台路径处理示例**
```python
import bpy

def cross_platform_path_handling():
    """跨平台路径处理示例"""
    
    # 不同平台的路径
    paths = [
        "/home/user/file.txt",           # Unix风格
        "C:\\Users\\user\\file.txt",     # Windows风格
        "//relative/path/file.blend",    # Blender相对路径
        "mixed\\path/with/different\\separators"  # 混合分隔符
    ]
    
    print("跨平台路径处理:")
    for path in paths:
        native_path = bpy.path.native_pathsep(path)
        basename = bpy.path.basename(path)
        
        print(f"  原始路径: {path}")
        print(f"  原生路径: {native_path}")
        print(f"  基本名称: {basename}")
        print()
    
    # 处理不区分大小写的路径
    case_paths = [
        "/path/to/MyFile.txt",
        "/path/to/myfile.txt",
        "/PATH/TO/FILE.TXT"
    ]
    
    print("大小写解析:")
    for path in case_paths:
        resolved = bpy.path.resolve_ncase(path)
        print(f"  原始: {path}")
        print(f"  解析: {resolved}")
        print()

cross_platform_path_handling()
```

### 5. **显示名称处理示例**
```python
import bpy

def display_name_processing():
    """显示名称处理示例"""
    
    # 文件名到显示名称
    filenames = [
        "my_texture_file.png",
        "character_diffuse_map.jpg",
        "scene_01_final_render.exr",
        "animation_keyframes.blend"
    ]
    
    print("文件名到显示名称:")
    for filename in filenames:
        display_name = bpy.path.display_name(filename)
        print(f"  文件名: {filename}")
        print(f"  显示名: {display_name}")
        print()
    
    # 显示名称到文件路径
    display_names = [
        "My Texture File",
        "Character Diffuse Map",
        "Scene 01 Final Render",
        "Animation Keyframes"
    ]
    
    print("显示名称到文件路径:")
    for display_name in display_names:
        filepath = bpy.path.display_name_to_filepath(display_name)
        print(f"  显示名: {display_name}")
        print(f"  文件路径: {filepath}")
        print()
    
    # 从文件路径获取显示名称
    filepaths = [
        "/path/to/my_texture_file.png",
        "/home/user/projects/character_diffuse_map.jpg",
        "C:\\Users\\user\\scene_01_final_render.exr"
    ]
    
    print("从文件路径获取显示名称:")
    for filepath in filepaths:
        display_name = bpy.path.display_name_from_filepath(filepath)
        print(f"  文件路径: {filepath}")
        print(f"  显示名称: {display_name}")
        print()

display_name_processing()
```

### 6. **扩展名处理示例**
```python
import bpy

def extension_handling():
    """扩展名处理示例"""
    
    # 确保扩展名
    filepaths = [
        "/path/to/my_file",
        "/path/to/my_file.blend",
        "/path/to/archive",
        "/path/to/archive.tar.gz"
    ]
    
    extensions = [".blend", ".blend", ".tar.gz", ".tar.gz"]
    
    print("扩展名处理:")
    for filepath, ext in zip(filepaths, extensions):
        result = bpy.path.ensure_ext(filepath, ext)
        print(f"  原始路径: {filepath}")
        print(f"  扩展名: {ext}")
        print(f"  结果: {result}")
        print()
    
    # 大小写敏感检查
    case_sensitive_paths = [
        "/path/to/file.BLEND",
        "/path/to/file.blend",
        "/path/to/file.Blend"
    ]
    
    print("大小写敏感检查:")
    for filepath in case_sensitive_paths:
        result_sensitive = bpy.path.ensure_ext(filepath, ".blend", case_sensitive=True)
        result_insensitive = bpy.path.ensure_ext(filepath, ".blend", case_sensitive=False)
        
        print(f"  路径: {filepath}")
        print(f"  大小写敏感: {result_sensitive}")
        print(f"  大小写不敏感: {result_insensitive}")
        print()

extension_handling()
```

这个文档涵盖了bpy.path模块的所有主要功能，为中文用户提供了完整的路径处理工具参考。 
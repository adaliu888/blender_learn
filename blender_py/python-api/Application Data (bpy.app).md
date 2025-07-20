# Application Data (bpy.app) 应用程序数据

## 概述
此模块包含在运行时保持不变的应用程序值。

## 子模块

- **bpy.app.handlers** - 应用程序处理器
- **bpy.app.translations** - 应用程序翻译
- **bpy.app.icons** - 应用程序图标
- **bpy.app.timers** - 应用程序计时器

## 应用程序属性

### 自动执行相关

#### bpy.app.autoexec_fail
未记录，建议贡献文档。

#### bpy.app.autoexec_fail_message
未记录，建议贡献文档。

#### bpy.app.autoexec_fail_quiet
未记录，建议贡献文档。

### 二进制路径

#### bpy.app.binary_path
Blender可执行文件的位置，对于打开新实例的实用程序很有用。只读，除非Blender作为Python模块构建 - 在这种情况下，值为空字符串，脚本作者可以指向Blender二进制文件。

```python
import bpy

# 获取Blender可执行文件路径
binary_path = bpy.app.binary_path
print(f"Blender可执行文件路径: {binary_path}")
```

### 调试属性

#### bpy.app.debug
布尔值，用于调试信息（以--debug / --debug-*启动，匹配此属性名称）

#### bpy.app.debug_depsgraph
布尔值，用于依赖图调试信息

#### bpy.app.debug_depsgraph_build
布尔值，用于依赖图构建调试信息

#### bpy.app.debug_depsgraph_eval
布尔值，用于依赖图评估调试信息

#### bpy.app.debug_depsgraph_pretty
布尔值，用于依赖图美化调试信息

#### bpy.app.debug_depsgraph_tag
布尔值，用于依赖图标签调试信息

#### bpy.app.debug_depsgraph_time
布尔值，用于依赖图时间调试信息

#### bpy.app.debug_events
布尔值，用于事件调试信息

#### bpy.app.debug_ffmpeg
布尔值，用于FFmpeg调试信息

#### bpy.app.debug_freestyle
布尔值，用于Freestyle调试信息

#### bpy.app.debug_handlers
布尔值，用于处理器调试信息

#### bpy.app.debug_io
布尔值，用于输入输出调试信息

#### bpy.app.debug_python
布尔值，用于Python调试信息

#### bpy.app.debug_simdata
布尔值，用于模拟数据调试信息

#### bpy.app.debug_value
短整型，可以设置为非零值用于测试目的

#### bpy.app.debug_wm
布尔值，用于窗口管理器调试信息

```python
import bpy

# 检查调试模式
print(f"调试模式: {bpy.app.debug}")
print(f"Python调试: {bpy.app.debug_python}")
print(f"依赖图调试: {bpy.app.debug_depsgraph}")
print(f"调试值: {bpy.app.debug_value}")
```

### 驱动程序命名空间

#### bpy.app.driver_namespace
驱动程序命名空间的字典，可原地编辑，文件加载时重置（只读）

## 文件加载和初始化顺序

由于驱动程序可能在加载blend文件后立即评估，因此有必要确保驱动程序命名空间事先初始化。

这可以通过注册文本数据块在启动时执行来完成，这会在驱动程序评估之前执行脚本。请参阅Blender文本编辑器中的Text -> Register。

**提示：**
您可能更喜欢使用外部文件而不是Blender的文本块。这可以使用执行外部文件的文本块来完成。

此示例运行位于文本块blend文件同一目录中的driver_namespace.py：

```python
import os
import bpy
blend_dir = os.path.normalize(os.path.join(__file__, "..", ".."))
bpy.utils.execfile(os.path.join(blend_dir, "driver_namespace.py"))
```

使用`__file__`确保文本解析为预期路径，即使从另一个文件库链接时也是如此。

其他填充驱动程序命名空间的方法可以工作，但往往容易出错：

- 使用`--python`命令行参数填充命名空间通常无法达到预期目标，因为初始评估将查找尚不存在的函数，将驱动程序标记为无效 - 阻止进一步评估。

- 在blend文件加载之前填充驱动程序命名空间也不起作用，因为打开文件会清除命名空间。

可以通过`--python`命令行参数在blend文件之前运行脚本。这可以注册一个加载后处理器（bpy.app.handlers.load_post）来初始化命名空间。虽然这对后台任务有效，但缺点是从文件选择器打开文件不会设置命名空间。

```python
import bpy

# 访问驱动程序命名空间
driver_namespace = bpy.app.driver_namespace
print(f"驱动程序命名空间: {driver_namespace}")

# 添加自定义函数到命名空间
def my_driver_function(value):
    return value * 2

driver_namespace['my_driver_function'] = my_driver_function
```

### 渲染相关

#### bpy.app.render_icon_size
图标/预览渲染的参考大小（只读）

#### bpy.app.render_preview_size
图标/预览渲染的参考大小（只读）

```python
import bpy

# 获取渲染尺寸
icon_size = bpy.app.render_icon_size
preview_size = bpy.app.render_preview_size
print(f"图标渲染尺寸: {icon_size}")
print(f"预览渲染尺寸: {preview_size}")
```

### 临时目录

#### bpy.app.tempdir
字符串，Blender使用的临时目录（只读）

```python
import bpy

# 获取临时目录
temp_dir = bpy.app.tempdir
print(f"临时目录: {temp_dir}")
```

### 应用程序行为

#### bpy.app.use_event_simulate
布尔值，用于应用程序行为（以--enable-*启动，匹配此属性名称）

#### bpy.app.use_userpref_skip_save_on_exit
布尔值，用于应用程序行为（以--enable-*启动，匹配此属性名称）

### 运行模式

#### bpy.app.background
布尔值，当Blender在没有用户界面的情况下运行时为True（以-b启动）

#### bpy.app.factory_startup
布尔值，当Blender以--factory-startup运行时为True

```python
import bpy

# 检查运行模式
print(f"后台模式: {bpy.app.background}")
print(f"工厂启动: {bpy.app.factory_startup}")
```

### 构建信息

#### bpy.app.build_branch
此Blender实例构建的分支

#### bpy.app.build_cflags
C编译器标志

#### bpy.app.build_commit_date
此Blender实例构建的提交日期

#### bpy.app.build_commit_time
此Blender实例构建的提交时间

#### bpy.app.build_cxxflags
C++编译器标志

#### bpy.app.build_date
此Blender实例构建的日期

#### bpy.app.build_hash
此Blender实例构建的提交哈希

#### bpy.app.build_linkflags
二进制链接标志

#### bpy.app.build_platform
此Blender实例构建的平台

#### bpy.app.build_system
使用的构建系统

#### bpy.app.build_time
此Blender实例构建的时间

#### bpy.app.build_type
构建类型（Release, Debug）

#### bpy.app.build_commit_timestamp
此Blender实例构建的提交的Unix时间戳

```python
import bpy

# 获取构建信息
print(f"构建分支: {bpy.app.build_branch}")
print(f"构建日期: {bpy.app.build_date}")
print(f"构建时间: {bpy.app.build_time}")
print(f"构建类型: {bpy.app.build_type}")
print(f"构建平台: {bpy.app.build_platform}")
print(f"构建哈希: {bpy.app.build_hash}")
```

### 版本信息

#### bpy.app.version_cycle
此构建的发布状态 alpha/beta/rc/release

#### bpy.app.version_string
格式化为字符串的Blender版本

#### bpy.app.version
Blender版本，作为3个数字的元组。例如 (2, 83, 1)

#### bpy.app.version_file
Blender版本，作为元组，最后用于保存.blend文件，与bpy.data.version兼容。此值应用于处理Blender版本之间的兼容性更改

```python
import bpy

# 获取版本信息
version = bpy.app.version
version_string = bpy.app.version_string
version_cycle = bpy.app.version_cycle
version_file = bpy.app.version_file

print(f"版本: {version}")
print(f"版本字符串: {version_string}")
print(f"版本周期: {version_cycle}")
print(f"文件版本: {version_file}")
```

### 库支持信息

#### bpy.app.alembic
常量值，包含Alembic支持信息

#### bpy.app.build_options
常量值，包含构建选项信息

#### bpy.app.ffmpeg
常量值，包含FFmpeg支持信息

#### bpy.app.ocio
常量值，包含OCIO支持信息

#### bpy.app.oiio
常量值，包含OIIO支持信息

#### bpy.app.opensubdiv
常量值，包含OpenSubdiv支持信息

#### bpy.app.openvdb
常量值，包含OpenVDB支持信息

#### bpy.app.sdl
常量值，包含SDL支持信息

#### bpy.app.usd
常量值，包含USD支持信息

```python
import bpy

# 检查库支持
print("库支持信息:")
print(f"Alembic: {bpy.app.alembic.supported}")
print(f"FFmpeg: {bpy.app.ffmpeg.supported}")
print(f"OCIO: {bpy.app.ocio.supported}")
print(f"OIIO: {bpy.app.oiio.supported}")
print(f"OpenSubdiv: {bpy.app.opensubdiv.supported}")
print(f"OpenVDB: {bpy.app.openvdb.supported}")
print(f"USD: {bpy.app.usd.supported}")

# 获取版本信息
print(f"\n版本信息:")
print(f"FFmpeg版本: {bpy.app.ffmpeg.avcodec_version_string}")
print(f"OCIO版本: {bpy.app.ocio.version_string}")
print(f"OIIO版本: {bpy.app.oiio.version_string}")
print(f"OpenSubdiv版本: {bpy.app.opensubdiv.version_string}")
print(f"OpenVDB版本: {bpy.app.openvdb.version_string}")
print(f"USD版本: {bpy.app.usd.version_string}")

# 检查构建选项
build_options = bpy.app.build_options
print(f"\n构建选项:")
print(f"Bullet: {build_options.bullet}")
print(f"Cycles: {build_options.cycles}")
print(f"Freestyle: {build_options.freestyle}")
print(f"OpenMP: {build_options.openmp}")
print(f"OpenVDB: {build_options.openvdb}")
print(f"USD: {build_options.usd}")
```

## 静态方法

### bpy.app.help_text(all=False)
返回帮助文本作为字符串。

**参数：**
- `all` (bool) - 返回所有参数，即使那些对当前平台不可用的参数

**返回：**
- 帮助文本字符串

```python
import bpy

# 获取帮助文本
help_text = bpy.app.help_text()
print("Blender帮助文本:")
print(help_text)

# 获取所有参数（包括平台特定的）
all_help_text = bpy.app.help_text(all=True)
print("\n所有参数帮助文本:")
print(all_help_text)
```

### bpy.app.is_job_running(job_type)
检查给定类型的作业是否正在运行。

**参数：**
- `job_type` (str) - Wm Job Type Items中的作业类型

**返回：**
- 给定类型的作业是否正在运行

**返回类型：**
- bool

```python
import bpy

# 检查作业状态
job_types = ['RENDER', 'RENDER_PREVIEW', 'RENDER_ANIMATION']

for job_type in job_types:
    is_running = bpy.app.is_job_running(job_type)
    print(f"作业 {job_type}: {'运行中' if is_running else '未运行'}")
```

## 使用示例

### 1. **应用程序信息获取示例**
```python
import bpy

def get_application_info():
    """获取应用程序信息"""
    
    print("=== Blender应用程序信息 ===")
    
    # 版本信息
    print(f"版本: {bpy.app.version}")
    print(f"版本字符串: {bpy.app.version_string}")
    print(f"版本周期: {bpy.app.version_cycle}")
    
    # 构建信息
    print(f"\n构建信息:")
    print(f"构建分支: {bpy.app.build_branch}")
    print(f"构建日期: {bpy.app.build_date}")
    print(f"构建时间: {bpy.app.build_time}")
    print(f"构建类型: {bpy.app.build_type}")
    print(f"构建平台: {bpy.app.build_platform}")
    
    # 运行模式
    print(f"\n运行模式:")
    print(f"后台模式: {bpy.app.background}")
    print(f"工厂启动: {bpy.app.factory_startup}")
    
    # 路径信息
    print(f"\n路径信息:")
    print(f"二进制路径: {bpy.app.binary_path}")
    print(f"临时目录: {bpy.app.tempdir}")

get_application_info()
```

### 2. **调试模式检查示例**
```python
import bpy

def check_debug_modes():
    """检查调试模式"""
    
    print("=== 调试模式检查 ===")
    
    debug_attributes = [
        'debug', 'debug_depsgraph', 'debug_python', 'debug_io',
        'debug_events', 'debug_handlers', 'debug_wm', 'debug_value'
    ]
    
    for attr in debug_attributes:
        if hasattr(bpy.app, attr):
            value = getattr(bpy.app, attr)
            print(f"{attr}: {value}")
    
    # 检查调试值
    if bpy.app.debug_value != 0:
        print(f"\n调试值设置为: {bpy.app.debug_value}")

check_debug_modes()
```

### 3. **库支持检查示例**
```python
import bpy

def check_library_support():
    """检查库支持"""
    
    print("=== 库支持检查 ===")
    
    # 主要库
    libraries = {
        'Alembic': bpy.app.alembic,
        'FFmpeg': bpy.app.ffmpeg,
        'OCIO': bpy.app.ocio,
        'OIIO': bpy.app.oiio,
        'OpenSubdiv': bpy.app.opensubdiv,
        'OpenVDB': bpy.app.openvdb,
        'USD': bpy.app.usd
    }
    
    for name, lib in libraries.items():
        print(f"{name}:")
        print(f"  支持: {lib.supported}")
        print(f"  版本: {lib.version_string}")
    
    # 构建选项
    print(f"\n构建选项:")
    build_options = bpy.app.build_options
    
    important_options = [
        'cycles', 'freestyle', 'openmp', 'openvdb', 'usd',
        'fluid', 'alembic', 'collada', 'openexr', 'tiff'
    ]
    
    for option in important_options:
        if hasattr(build_options, option):
            value = getattr(build_options, option)
            print(f"  {option}: {value}")

check_library_support()
```

### 4. **驱动程序命名空间管理示例**
```python
import bpy

def setup_driver_namespace():
    """设置驱动程序命名空间"""
    
    print("=== 驱动程序命名空间设置 ===")
    
    # 获取命名空间
    namespace = bpy.app.driver_namespace
    
    # 添加自定义函数
    def custom_sine(value, frequency=1.0, amplitude=1.0):
        """自定义正弦函数"""
        import math
        return math.sin(value * frequency) * amplitude
    
    def custom_noise(value, scale=1.0):
        """自定义噪声函数"""
        import random
        random.seed(int(value * 1000))
        return (random.random() - 0.5) * scale
    
    def custom_ramp(value, start=0.0, end=1.0):
        """自定义斜坡函数"""
        return start + (end - start) * value
    
    # 注册函数到命名空间
    namespace['custom_sine'] = custom_sine
    namespace['custom_noise'] = custom_noise
    namespace['custom_ramp'] = custom_ramp
    
    print("已添加自定义函数到驱动程序命名空间:")
    print("  - custom_sine(value, frequency, amplitude)")
    print("  - custom_noise(value, scale)")
    print("  - custom_ramp(value, start, end)")
    
    # 显示当前命名空间
    print(f"\n当前命名空间包含 {len(namespace)} 个项目")

setup_driver_namespace()
```

### 5. **作业状态监控示例**
```python
import bpy

def monitor_jobs():
    """监控作业状态"""
    
    print("=== 作业状态监控 ===")
    
    # 常见的作业类型
    job_types = [
        'RENDER',
        'RENDER_PREVIEW', 
        'RENDER_ANIMATION',
        'RENDER_VIEWPORT',
        'RENDER_VIEWPORT_ANIMATION'
    ]
    
    active_jobs = []
    
    for job_type in job_types:
        if bpy.app.is_job_running(job_type):
            active_jobs.append(job_type)
            print(f"✓ {job_type} 正在运行")
        else:
            print(f"✗ {job_type} 未运行")
    
    if active_jobs:
        print(f"\n当前活跃作业: {', '.join(active_jobs)}")
    else:
        print(f"\n当前没有活跃的渲染作业")

monitor_jobs()
```

### 6. **应用程序配置检查示例**
```python
import bpy

def check_app_configuration():
    """检查应用程序配置"""
    
    print("=== 应用程序配置检查 ===")
    
    # 检查事件模拟
    print(f"事件模拟: {bpy.app.use_event_simulate}")
    
    # 检查用户偏好设置跳过保存
    print(f"退出时跳过保存用户偏好: {bpy.app.use_userpref_skip_save_on_exit}")
    
    # 检查渲染尺寸
    print(f"图标渲染尺寸: {bpy.app.render_icon_size}")
    print(f"预览渲染尺寸: {bpy.app.render_preview_size}")
    
    # 检查调试模式
    if bpy.app.debug:
        print("调试模式已启用")
    
    if bpy.app.debug_value != 0:
        print(f"调试值: {bpy.app.debug_value}")
    
    # 检查运行环境
    if bpy.app.background:
        print("运行在后台模式")
    
    if bpy.app.factory_startup:
        print("运行在工厂启动模式")

check_app_configuration()
```

### 7. **版本兼容性检查示例**
```python
import bpy

def check_version_compatibility():
    """检查版本兼容性"""
    
    print("=== 版本兼容性检查 ===")
    
    current_version = bpy.app.version
    file_version = bpy.app.version_file
    
    print(f"当前Blender版本: {current_version}")
    print(f"文件保存版本: {file_version}")
    
    # 检查版本兼容性
    if current_version != file_version:
        print("⚠️  版本不匹配，可能存在兼容性问题")
        
        # 比较主要版本号
        if current_version[0] != file_version[0]:
            print("⚠️  主要版本不匹配，可能存在重大兼容性问题")
        elif current_version[1] != file_version[1]:
            print("⚠️  次要版本不匹配，可能存在功能兼容性问题")
        else:
            print("ℹ️  补丁版本不匹配，通常可以安全使用")
    else:
        print("✓ 版本完全匹配")
    
    # 检查版本周期
    version_cycle = bpy.app.version_cycle
    print(f"版本周期: {version_cycle}")
    
    if version_cycle in ['alpha', 'beta', 'rc']:
        print("⚠️  使用预发布版本，可能存在稳定性问题")

check_version_compatibility()
```

这个文档涵盖了bpy.app模块的所有主要功能，为中文用户提供了完整的应用程序数据参考。 

我来为您翻译Blender的Application Data (bpy.app)文档并保存到指定目录：



我已经成功为您翻译了Blender的Application Data (bpy.app)文档并保存到了`blender_py/python-api/Application Data (bpy.app).md`文件中。

这个文档包含了以下主要内容：

## 主要功能模块

1. **应用程序属性** - 包含各种运行时不变的应用程序值
2. **调试属性** - 各种调试模式的布尔值设置
3. **驱动程序命名空间** - 用于动画驱动程序的函数命名空间
4. **构建信息** - Blender构建的详细信息
5. **版本信息** - Blender版本和兼容性信息
6. **库支持信息** - 各种第三方库的支持状态和版本

## 核心功能

### 应用程序属性
- **二进制路径** - Blender可执行文件位置
- **调试模式** - 各种调试选项的状态
- **运行模式** - 后台模式、工厂启动等
- **临时目录** - Blender使用的临时目录
- **渲染尺寸** - 图标和预览渲染的参考尺寸

### 版本和构建信息
- **版本信息** - 当前版本、版本字符串、版本周期
- **构建信息** - 构建日期、时间、平台、类型等
- **库支持** - Alembic、FFmpeg、OCIO、OIIO、OpenSubdiv、OpenVDB、USD等

### 静态方法
- **help_text()** - 获取Blender帮助文本
- **is_job_running()** - 检查作业运行状态

## 实用示例

文档包含了7个完整的使用示例：
1. 应用程序信息获取示例
2. 调试模式检查示例
3. 库支持检查示例
4. 驱动程序命名空间管理示例
5. 作业状态监控示例
6. 应用程序配置检查示例
7. 版本兼容性检查示例

## 特色功能

- **驱动程序命名空间管理** - 详细说明了如何正确设置动画驱动程序的函数命名空间
- **版本兼容性检查** - 帮助处理不同Blender版本之间的兼容性问题
- **库支持检测** - 检查各种第三方库的可用性和版本
- **调试模式监控** - 全面的调试选项检查
- **作业状态监控** - 实时监控渲染作业状态

这个翻译为中文用户提供了完整的bpy.app模块参考，特别适合需要了解Blender应用程序状态、版本信息、库支持和调试功能的开发者。
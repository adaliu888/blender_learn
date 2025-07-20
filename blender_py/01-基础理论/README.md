# Blender Python API 基础理论

## 1. Blender架构与Python集成原理

### 1.1 Blender架构概述
Blender采用模块化架构，主要组件包括：
- **数据层 (Data Layer)**: 存储场景、对象、材质等数据
- **操作层 (Operator Layer)**: 提供用户界面操作
- **脚本层 (Scripting Layer)**: Python API接口
- **渲染层 (Rendering Layer)**: 渲染引擎

### 1.2 Python集成机制
```python
import bpy

# Python通过bpy模块访问Blender内部数据
# bpy.data - 访问数据
# bpy.context - 访问当前上下文
# bpy.ops - 执行操作
# bpy.types - 类型定义
```

## 2. bpy模块核心概念

### 2.1 数据访问 (bpy.data)
```python
# 访问场景数据
scenes = bpy.data.scenes
objects = bpy.data.objects
meshes = bpy.data.meshes
materials = bpy.data.materials
```

### 2.2 上下文操作 (bpy.context)
```python
# 获取当前活动对象
active_object = bpy.context.active_object

# 获取选中的对象
selected_objects = bpy.context.selected_objects

# 获取当前场景
current_scene = bpy.context.scene
```

### 2.3 操作接口 (bpy.ops)
```python
# 执行Blender操作
bpy.ops.mesh.primitive_cube_add()
bpy.ops.object.delete()
bpy.ops.transform.translate()
```

## 3. 数据流与操作模式

### 3.1 数据流模式
1. **读取模式**: 从bpy.data读取现有数据
2. **修改模式**: 通过bpy.ops或直接属性修改
3. **创建模式**: 通过bpy.ops创建新对象
4. **删除模式**: 通过bpy.ops删除对象

### 3.2 操作模式
```python
# 对象模式
bpy.context.view_layer.objects.active = obj
bpy.ops.object.mode_set(mode='OBJECT')

# 编辑模式
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')

# 姿态模式
bpy.ops.object.mode_set(mode='POSE')
```

## 4. 核心数据类型

### 4.1 对象类型
- **Object**: 场景中的对象
- **Mesh**: 网格数据
- **Material**: 材质数据
- **Texture**: 纹理数据
- **Armature**: 骨骼数据

### 4.2 数据结构
```python
# 对象层次结构
scene = bpy.context.scene
objects = scene.objects

# 网格数据结构
mesh = obj.data
vertices = mesh.vertices
edges = mesh.edges
faces = mesh.polygons
```

## 5. 脚本执行环境

### 5.1 脚本编辑器
- 在Blender中打开文本编辑器
- 创建新文本文件
- 编写Python代码
- 点击"运行脚本"执行

### 5.2 外部脚本
```python
# 从外部文件执行脚本
import bpy
exec(open("path/to/script.py").read())
```

## 6. 错误处理与调试

### 6.1 常见错误
```python
# 检查对象是否存在
if obj in bpy.data.objects:
    print("对象存在")

# 检查属性是否存在
if hasattr(obj, 'location'):
    print("属性存在")
```

### 6.2 调试技巧
```python
# 打印对象信息
print(f"对象名称: {obj.name}")
print(f"对象类型: {obj.type}")
print(f"对象位置: {obj.location}")

# 使用Blender的控制台输出
import bpy
bpy.app.debug = True
```

## 7. 性能优化

### 7.1 批量操作
```python
# 批量选择对象
for obj in bpy.data.objects:
    obj.select_set(True)

# 批量修改属性
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        obj.location.z += 1.0
```

### 7.2 内存管理
```python
# 清理未使用的数据
bpy.ops.outliner.orphans_purge(do_recursive=True)

# 释放内存
import gc
gc.collect()
```

## 8. 最佳实践

### 8.1 代码组织
- 使用函数封装重复操作
- 添加适当的注释
- 遵循PEP 8代码规范
- 使用异常处理

### 8.2 脚本设计
```python
def create_cube(name, location, size):
    """创建立方体的函数"""
    try:
        bpy.ops.mesh.primitive_cube_add(
            size=size,
            location=location
        )
        cube = bpy.context.active_object
        cube.name = name
        return cube
    except Exception as e:
        print(f"创建立方体失败: {e}")
        return None

# 使用函数
cube = create_cube("MyCube", (0, 0, 0), 2.0)
```

## 9. 学习资源

### 9.1 官方文档
- [Blender Python API 文档](https://docs.blender.org/api/current/)
- [Blender Python 教程](https://docs.blender.org/manual/en/latest/advanced/scripting/index.html)

### 9.2 社区资源
- Blender Stack Exchange
- BlenderArtists 论坛
- GitHub 上的开源项目

### 9.3 实践项目
- 创建简单的几何体
- 批量重命名对象
- 自动化材质应用
- 创建自定义修改器 
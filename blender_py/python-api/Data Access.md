我来为您翻译Blender的Data Access (bpy.data)文档：

# Data Access (bpy.data) 数据访问

## 概述
此模块用于所有Blender/Python数据访问。

## bpy.data.data
访问Blender的内部数据

**类型**: `bpy.types.BlendData`

## 使用示例

```python
import bpy

# 打印所有对象
for obj in bpy.data.objects:
    print(obj.name)

# 以列表形式打印所有场景名称
print(bpy.data.scenes.keys())

# 删除名为"Cube"的网格
if "Cube" in bpy.data.meshes:
    mesh = bpy.data.meshes["Cube"]
    print("正在删除网格", mesh)
    bpy.data.meshes.remove(mesh)

# 将图像信息写入blend文件旁边的文本文件
import os
with open(os.path.splitext(bpy.data.filepath)[0] + ".txt", 'w') as fs:
    for image in bpy.data.images:
        fs.write("%s %d x %d\n" % (image.filepath, image.size[0], image.size[1]))
```

## 详细说明

### 1. **访问所有对象**
```python
# 遍历所有对象
for obj in bpy.data.objects:
    print(f"对象名称: {obj.name}")
    print(f"对象类型: {obj.type}")
    print(f"对象位置: {obj.location}")
```

### 2. **访问场景数据**
```python
# 获取所有场景
scenes = bpy.data.scenes
print(f"场景数量: {len(scenes)}")

# 遍历所有场景
for scene in scenes:
    print(f"场景名称: {scene.name}")
    print(f"帧范围: {scene.frame_start} - {scene.frame_end}")
```

### 3. **访问网格数据**
```python
# 获取所有网格
meshes = bpy.data.meshes
print(f"网格数量: {len(meshes)}")

for mesh in meshes:
    print(f"网格名称: {mesh.name}")
    print(f"顶点数量: {len(mesh.vertices)}")
    print(f"面数量: {len(mesh.polygons)}")
```

### 4. **访问材质数据**
```python
# 获取所有材质
materials = bpy.data.materials
print(f"材质数量: {len(materials)}")

# 遍历所有材质
for material in materials:
    print(f"材质名称: {material.name}")
    print(f"使用节点: {material.use_nodes}")
```

### 5. **访问图像数据**
```python
# 获取所有图像
images = bpy.data.images
print(f"图像数量: {len(images)}")

# 遍历所有图像
for image in images:
    print(f"图像名称: {image.name}")
    print(f"图像路径: {image.filepath}")
    print(f"图像尺寸: {image.size[0]} x {image.size[1]}")
```

### 6. **数据清理示例**
```python
# 删除未使用的数据
def cleanup_unused_data():
    """清理未使用的数据"""
    
    # 删除未使用的网格
    for mesh in bpy.data.meshes:
        if mesh.users == 0:
            print(f"删除未使用的网格: {mesh.name}")
            bpy.data.meshes.remove(mesh)
    
    # 删除未使用的材质
    for material in bpy.data.materials:
        if material.users == 0:
            print(f"删除未使用的材质: {material.name}")
            bpy.data.materials.remove(material)
    
    # 删除未使用的纹理
    for texture in bpy.data.textures:
        if texture.users == 0:
            print(f"删除未使用的纹理: {texture.name}")
            bpy.data.textures.remove(texture)
    
    # 删除未使用的图像
    for image in bpy.data.images:
        if image.users == 0:
            print(f"删除未使用的图像: {image.name}")
            bpy.data.images.remove(image)
    
    print("数据清理完成!")

# 运行清理
cleanup_unused_data()
```

### 7. **数据统计示例**
```python
def print_data_statistics():
    """打印数据统计信息"""
    print("=== Blender 数据统计 ===")
    print(f"对象数量: {len(bpy.data.objects)}")
    print(f"场景数量: {len(bpy.data.scenes)}")
    print(f"网格数量: {len(bpy.data.meshes)}")
    print(f"材质数量: {len(bpy.data.materials)}")
    print(f"纹理数量: {len(bpy.data.textures)}")
    print(f"图像数量: {len(bpy.data.images)}")
    print(f"动作数量: {len(bpy.data.actions)}")
    print(f"相机数量: {len(bpy.data.cameras)}")
    print(f"灯光数量: {len(bpy.data.lights)}")

# 运行统计
print_data_statistics()
```

### 8. **数据导出示例**
```python
def export_data_info():
    """导出数据信息到文件"""
    import os
    
    # 获取blend文件路径
    blend_path = bpy.data.filepath
    if blend_path:
        # 创建输出文件路径
        output_path = os.path.splitext(blend_path)[0] + "_data_info.txt"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=== Blender 数据信息 ===\n\n")
            
            # 写入对象信息
            f.write("对象信息:\n")
            for obj in bpy.data.objects:
                f.write(f"  {obj.name} ({obj.type})\n")
            
            # 写入材质信息
            f.write("\n材质信息:\n")
            for material in bpy.data.materials:
                f.write(f"  {material.name}\n")
            
            # 写入图像信息
            f.write("\n图像信息:\n")
            for image in bpy.data.images:
                f.write(f"  {image.name}: {image.size[0]} x {image.size[1]}\n")
        
        print(f"数据信息已导出到: {output_path}")
    else:
        print("请先保存blend文件")

# 运行导出
export_data_info()
```

### 9. **数据验证示例**
```python
def validate_data():
    """验证数据完整性"""
    print("=== 数据验证 ===")
    
    # 检查对象数据
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and not obj.data:
            print(f"警告: 网格对象 '{obj.name}' 没有网格数据")
        
        if obj.type == 'ARMATURE' and not obj.data:
            print(f"警告: 骨骼对象 '{obj.name}' 没有骨骼数据")
    
    # 检查材质数据
    for material in bpy.data.materials:
        if material.use_nodes and not material.node_tree:
            print(f"警告: 材质 '{material.name}' 启用了节点但没有节点树")
    
    print("数据验证完成!")

# 运行验证
validate_data()
```

## 常用数据访问模式

### 1. **按名称访问**
```python
# 按名称获取对象
cube = bpy.data.objects.get("Cube")
if cube:
    print(f"找到对象: {cube.name}")

# 按名称获取材质
material = bpy.data.materials.get("Material")
if material:
    print(f"找到材质: {material.name}")
```

### 2. **按类型过滤**
```python
# 获取所有网格对象
mesh_objects = [obj for obj in bpy.data.objects if obj.type == 'MESH']
print(f"网格对象数量: {len(mesh_objects)}")

# 获取所有相机对象
camera_objects = [obj for obj in bpy.data.objects if obj.type == 'CAMERA']
print(f"相机对象数量: {len(camera_objects)}")
```

### 3. **数据创建和删除**
```python
# 创建新材质
new_material = bpy.data.materials.new(name="NewMaterial")

# 创建新网格
new_mesh = bpy.data.meshes.new(name="NewMesh")

# 删除数据
if "OldMaterial" in bpy.data.materials:
    bpy.data.materials.remove(bpy.data.materials["OldMaterial"])
```

这个翻译涵盖了bpy.data模块的核心功能和使用方法，为中文用户提供了完整的数据访问参考。
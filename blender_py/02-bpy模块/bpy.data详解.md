# bpy.data 详解

## 概述
`bpy.data` 是Blender Python API中的数据访问模块，提供了对所有Blender数据的直接访问。它包含了场景、对象、网格、材质、纹理、骨骼等所有数据类型。

## 1. 核心数据集合

### 1.1 场景数据
```python
import bpy

# 场景集合
scenes = bpy.data.scenes
current_scene = bpy.data.scenes[0]  # 第一个场景

# 创建新场景
new_scene = bpy.data.scenes.new(name="MyScene")

# 删除场景
bpy.data.scenes.remove(scene_to_remove)

# 重命名场景
scene.name = "NewSceneName"
```

### 1.2 对象数据
```python
# 对象集合
objects = bpy.data.objects

# 按类型获取对象
mesh_objects = [obj for obj in bpy.data.objects if obj.type == 'MESH']
armature_objects = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']

# 按名称获取对象
my_object = bpy.data.objects.get("MyObject")

# 创建新对象
new_object = bpy.data.objects.new("NewObject", mesh_data)
```

### 1.3 网格数据
```python
# 网格集合
meshes = bpy.data.meshes

# 创建新网格
new_mesh = bpy.data.meshes.new("NewMesh")

# 删除网格
bpy.data.meshes.remove(mesh_to_remove)

# 复制网格
copied_mesh = mesh.copy()
```

## 2. 数据创建与管理

### 2.1 创建基础对象
```python
def create_basic_objects():
    """创建基础几何体"""
    # 创建立方体
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.active_object
    
    # 创建球体
    bpy.ops.mesh.primitive_uv_sphere_add()
    sphere = bpy.context.active_object
    
    # 创建圆柱体
    bpy.ops.mesh.primitive_cylinder_add()
    cylinder = bpy.context.active_object
    
    return cube, sphere, cylinder

def create_custom_mesh():
    """创建自定义网格"""
    # 创建新网格数据
    mesh = bpy.data.meshes.new("CustomMesh")
    
    # 创建顶点
    vertices = [
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (0, 1, 0)
    ]
    
    # 创建面
    faces = [(0, 1, 2, 3)]
    
    # 构建网格
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    
    # 创建对象
    obj = bpy.data.objects.new("CustomObject", mesh)
    bpy.context.scene.collection.objects.link(obj)
    
    return obj
```

### 2.2 材质管理
```python
def create_material(name, color=(1, 1, 1, 1)):
    """创建材质"""
    # 检查材质是否已存在
    material = bpy.data.materials.get(name)
    if material is None:
        material = bpy.data.materials.new(name=name)
    
    # 启用节点
    material.use_nodes = True
    nodes = material.node_tree.nodes
    
    # 清除默认节点
    nodes.clear()
    
    # 创建输出节点
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    output_node.location = (300, 0)
    
    # 创建漫反射节点
    diffuse_node = nodes.new(type='ShaderNodeBsdfDiffuse')
    diffuse_node.location = (0, 0)
    diffuse_node.inputs[0].default_value = color
    
    # 连接节点
    material.node_tree.links.new(diffuse_node.outputs[0], output_node.inputs[0])
    
    return material

def assign_material_to_object(obj, material):
    """为对象分配材质"""
    if obj.data.materials:
        obj.data.materials[0] = material
    else:
        obj.data.materials.append(material)
```

## 3. 数据查询与过滤

### 3.1 按条件查询
```python
def find_objects_by_type(object_type):
    """按类型查找对象"""
    return [obj for obj in bpy.data.objects if obj.type == object_type]

def find_objects_by_name_pattern(pattern):
    """按名称模式查找对象"""
    return [obj for obj in bpy.data.objects if pattern in obj.name]

def find_objects_by_location(min_z=0):
    """按位置查找对象"""
    return [obj for obj in bpy.data.objects if obj.location.z >= min_z]

def find_objects_by_scale(min_scale=1.0):
    """按缩放查找对象"""
    return [obj for obj in bpy.data.objects 
            if obj.scale.x >= min_scale or obj.scale.y >= min_scale or obj.scale.z >= min_scale]
```

### 3.2 数据统计
```python
def get_scene_statistics():
    """获取场景统计信息"""
    stats = {
        'total_objects': len(bpy.data.objects),
        'mesh_objects': len([obj for obj in bpy.data.objects if obj.type == 'MESH']),
        'armature_objects': len([obj for obj in bpy.data.objects if obj.type == 'ARMATURE']),
        'camera_objects': len([obj for obj in bpy.data.objects if obj.type == 'CAMERA']),
        'light_objects': len([obj for obj in bpy.data.objects if obj.type == 'LIGHT']),
        'total_materials': len(bpy.data.materials),
        'total_textures': len(bpy.data.textures),
        'total_meshes': len(bpy.data.meshes)
    }
    return stats

def print_scene_info():
    """打印场景信息"""
    stats = get_scene_statistics()
    print("场景统计信息:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
```

## 4. 数据清理与优化

### 4.1 清理未使用数据
```python
def cleanup_unused_data():
    """清理未使用的数据"""
    # 清理未使用的网格
    for mesh in bpy.data.meshes:
        if mesh.users == 0:
            bpy.data.meshes.remove(mesh)
    
    # 清理未使用的材质
    for material in bpy.data.materials:
        if material.users == 0:
            bpy.data.materials.remove(material)
    
    # 清理未使用的纹理
    for texture in bpy.data.textures:
        if texture.users == 0:
            bpy.data.textures.remove(texture)
    
    # 清理未使用的图像
    for image in bpy.data.images:
        if image.users == 0:
            bpy.data.images.remove(image)

def remove_orphaned_data():
    """移除孤立数据"""
    bpy.ops.outliner.orphans_purge(do_recursive=True)
```

### 4.2 数据验证
```python
def validate_mesh_data(mesh):
    """验证网格数据"""
    issues = []
    
    if not mesh.vertices:
        issues.append("网格没有顶点")
    
    if not mesh.polygons:
        issues.append("网格没有面")
    
    # 检查是否有孤立的顶点
    used_vertices = set()
    for polygon in mesh.polygons:
        for vertex_index in polygon.vertices:
            used_vertices.add(vertex_index)
    
    if len(used_vertices) != len(mesh.vertices):
        issues.append("存在孤立的顶点")
    
    return issues

def validate_object_data(obj):
    """验证对象数据"""
    issues = []
    
    if obj.type == 'MESH' and not obj.data:
        issues.append("网格对象没有网格数据")
    
    if obj.type == 'ARMATURE' and not obj.data:
        issues.append("骨骼对象没有骨骼数据")
    
    return issues
```

## 5. 批量操作

### 5.1 批量重命名
```python
def batch_rename_objects(prefix="", suffix="", pattern="", replacement=""):
    """批量重命名对象"""
    for obj in bpy.data.objects:
        new_name = obj.name
        
        if prefix:
            new_name = prefix + new_name
        
        if suffix:
            new_name = new_name + suffix
        
        if pattern and replacement:
            new_name = new_name.replace(pattern, replacement)
        
        obj.name = new_name

def batch_rename_by_type():
    """按类型批量重命名"""
    type_counts = {}
    
    for obj in bpy.data.objects:
        obj_type = obj.type.lower()
        if obj_type not in type_counts:
            type_counts[obj_type] = 0
        type_counts[obj_type] += 1
        
        obj.name = f"{obj_type}_{type_counts[obj_type]:03d}"
```

### 5.2 批量变换
```python
def batch_transform_objects(translation=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """批量变换对象"""
    for obj in bpy.data.objects:
        # 应用平移
        obj.location.x += translation[0]
        obj.location.y += translation[1]
        obj.location.z += translation[2]
        
        # 应用旋转
        obj.rotation_euler.x += rotation[0]
        obj.rotation_euler.y += rotation[1]
        obj.rotation_euler.z += rotation[2]
        
        # 应用缩放
        obj.scale.x *= scale[0]
        obj.scale.y *= scale[1]
        obj.scale.z *= scale[2]

def batch_apply_modifiers():
    """批量应用修改器"""
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.modifiers:
            # 切换到对象模式
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='OBJECT')
            
            # 应用所有修改器
            for modifier in obj.modifiers[:]:  # 使用切片创建副本
                bpy.ops.object.modifier_apply(modifier=modifier.name)
```

## 6. 数据导入导出

### 6.1 数据导出
```python
def export_object_data(obj, filepath):
    """导出对象数据"""
    import json
    
    data = {
        'name': obj.name,
        'type': obj.type,
        'location': list(obj.location),
        'rotation': list(obj.rotation_euler),
        'scale': list(obj.scale),
        'dimensions': list(obj.dimensions)
    }
    
    if obj.type == 'MESH':
        mesh = obj.data
        data['mesh'] = {
            'vertices': [[v.co.x, v.co.y, v.co.z] for v in mesh.vertices],
            'polygons': [[p.vertices[i] for i in range(len(p.vertices))] for p in mesh.polygons]
        }
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def export_scene_data(filepath):
    """导出场景数据"""
    import json
    
    scene_data = {
        'scenes': [],
        'objects': [],
        'materials': []
    }
    
    # 导出场景
    for scene in bpy.data.scenes:
        scene_data['scenes'].append({
            'name': scene.name,
            'frame_start': scene.frame_start,
            'frame_end': scene.frame_end
        })
    
    # 导出对象
    for obj in bpy.data.objects:
        scene_data['objects'].append({
            'name': obj.name,
            'type': obj.type,
            'location': list(obj.location),
            'rotation': list(obj.rotation_euler),
            'scale': list(obj.scale)
        })
    
    # 导出材质
    for material in bpy.data.materials:
        scene_data['materials'].append({
            'name': material.name,
            'use_nodes': material.use_nodes
        })
    
    with open(filepath, 'w') as f:
        json.dump(scene_data, f, indent=2)
```

### 6.2 数据导入
```python
def import_object_data(filepath):
    """导入对象数据"""
    import json
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    if data['type'] == 'MESH':
        # 创建网格
        mesh = bpy.data.meshes.new(data['name'])
        
        # 创建顶点
        mesh.from_pydata(data['mesh']['vertices'], [], data['mesh']['polygons'])
        mesh.update()
        
        # 创建对象
        obj = bpy.data.objects.new(data['name'], mesh)
        bpy.context.scene.collection.objects.link(obj)
        
        # 设置变换
        obj.location = data['location']
        obj.rotation_euler = data['rotation']
        obj.scale = data['scale']
        
        return obj
    
    return None
```

## 7. 性能优化

### 7.1 数据缓存
```python
def optimize_data_access():
    """优化数据访问"""
    # 缓存常用数据
    objects = list(bpy.data.objects)
    meshes = list(bpy.data.meshes)
    materials = list(bpy.data.materials)
    
    # 使用缓存的数据而不是重复访问bpy.data
    for obj in objects:
        if obj.type == 'MESH':
            mesh = obj.data
            if mesh in meshes:
                # 处理网格
                pass
```

### 7.2 批量数据处理
```python
def batch_process_meshes():
    """批量处理网格"""
    # 收集所有需要处理的网格
    meshes_to_process = []
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data:
            meshes_to_process.append(obj.data)
    
    # 批量处理
    for mesh in meshes_to_process:
        # 处理网格数据
        mesh.calc_normals()
        mesh.update()
```

## 8. 最佳实践

### 8.1 数据管理
- 总是检查数据是否存在再访问
- 使用try-except处理数据访问错误
- 及时清理未使用的数据
- 使用有意义的名称

### 8.2 性能考虑
- 缓存频繁访问的数据
- 使用批量操作而不是逐个处理
- 避免在循环中重复访问bpy.data
- 合理使用数据验证

### 8.3 错误处理
- 检查数据有效性
- 提供有意义的错误消息
- 在出错时清理状态
- 使用安全的数据访问方法 
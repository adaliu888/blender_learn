# bpy.context 详解

## 概述
`bpy.context` 是Blender Python API中最重要的模块之一，提供了对当前Blender状态和上下文的访问。它包含了当前选中的对象、活动对象、场景、视图层等信息。

## 1. 核心属性

### 1.1 场景相关
```python
import bpy

# 当前场景
current_scene = bpy.context.scene

# 所有场景
all_scenes = bpy.context.scenes

# 当前视图层
view_layer = bpy.context.view_layer

# 当前窗口
window = bpy.context.window

# 当前区域
area = bpy.context.area

# 当前空间
space = bpy.context.space_data
```

### 1.2 对象相关
```python
# 当前活动对象
active_object = bpy.context.active_object

# 选中的对象列表
selected_objects = bpy.context.selected_objects

# 选中的可编辑对象
selected_editable_objects = bpy.context.selected_editable_objects

# 可见对象
visible_objects = bpy.context.visible_objects
```

### 1.3 编辑模式相关
```python
# 当前编辑模式
mode = bpy.context.mode

# 编辑模式下的选中元素
if bpy.context.mode == 'EDIT_MESH':
    # 选中的顶点
    selected_vertices = bpy.context.selected_vertices
    
    # 选中的边
    selected_edges = bpy.context.selected_edges
    
    # 选中的面
    selected_faces = bpy.context.selected_faces
```

## 2. 上下文管理

### 2.1 临时上下文
```python
# 临时设置活动对象
with bpy.context.temp_override(active_object=my_object):
    # 在这个上下文中，my_object是活动对象
    bpy.ops.object.delete()

# 临时设置选中对象
with bpy.context.temp_override(selected_objects=[obj1, obj2]):
    # 在这个上下文中，obj1和obj2被选中
    bpy.ops.transform.translate(value=(1, 0, 0))
```

### 2.2 上下文覆盖
```python
# 设置活动对象
bpy.context.view_layer.objects.active = my_object

# 设置选中对象
for obj in objects_to_select:
    obj.select_set(True)
```

## 3. 实用函数

### 3.1 对象选择与激活
```python
def select_and_activate_object(obj):
    """选择并激活对象"""
    # 取消所有选择
    bpy.ops.object.select_all(action='DESELECT')
    
    # 选择指定对象
    obj.select_set(True)
    
    # 设置为活动对象
    bpy.context.view_layer.objects.active = obj

def select_multiple_objects(objects):
    """选择多个对象"""
    for obj in objects:
        obj.select_set(True)
    
    # 设置第一个对象为活动对象
    if objects:
        bpy.context.view_layer.objects.active = objects[0]
```

### 3.2 模式切换
```python
def switch_to_object_mode():
    """切换到对象模式"""
    bpy.ops.object.mode_set(mode='OBJECT')

def switch_to_edit_mode():
    """切换到编辑模式"""
    bpy.ops.object.mode_set(mode='EDIT')

def switch_to_pose_mode():
    """切换到姿态模式"""
    bpy.ops.object.mode_set(mode='POSE')
```

## 4. 高级用法

### 4.1 遍历上下文
```python
def process_selected_objects():
    """处理所有选中的对象"""
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            print(f"处理网格对象: {obj.name}")
            # 处理网格对象
        elif obj.type == 'ARMATURE':
            print(f"处理骨骼对象: {obj.name}")
            # 处理骨骼对象

def process_visible_objects():
    """处理所有可见对象"""
    for obj in bpy.context.visible_objects:
        if obj.hide_viewport:
            continue
        print(f"可见对象: {obj.name}")
```

### 4.2 上下文验证
```python
def validate_context():
    """验证当前上下文是否有效"""
    if not bpy.context.active_object:
        print("警告: 没有活动对象")
        return False
    
    if not bpy.context.selected_objects:
        print("警告: 没有选中的对象")
        return False
    
    return True

def ensure_edit_mode():
    """确保在编辑模式下"""
    if bpy.context.mode != 'EDIT_MESH':
        bpy.ops.object.mode_set(mode='EDIT')
```

## 5. 常见应用场景

### 5.1 批量操作
```python
def batch_transform_objects(translation=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """批量变换选中的对象"""
    for obj in bpy.context.selected_objects:
        # 设置位置
        obj.location = (
            obj.location.x + translation[0],
            obj.location.y + translation[1],
            obj.location.z + translation[2]
        )
        
        # 设置旋转
        obj.rotation_euler = (
            obj.rotation_euler.x + rotation[0],
            obj.rotation_euler.y + rotation[1],
            obj.rotation_euler.z + rotation[2]
        )
        
        # 设置缩放
        obj.scale = (
            obj.scale.x * scale[0],
            obj.scale.y * scale[1],
            obj.scale.z * scale[2]
        )
```

### 5.2 智能选择
```python
def select_by_type(object_type):
    """按类型选择对象"""
    bpy.ops.object.select_all(action='DESELECT')
    
    for obj in bpy.context.scene.objects:
        if obj.type == object_type:
            obj.select_set(True)
    
    # 设置第一个匹配的对象为活动对象
    matching_objects = [obj for obj in bpy.context.scene.objects if obj.type == object_type]
    if matching_objects:
        bpy.context.view_layer.objects.active = matching_objects[0]

def select_by_name_pattern(pattern):
    """按名称模式选择对象"""
    bpy.ops.object.select_all(action='DESELECT')
    
    for obj in bpy.context.scene.objects:
        if pattern in obj.name:
            obj.select_set(True)
```

## 6. 错误处理

### 6.1 安全访问
```python
def safe_get_active_object():
    """安全获取活动对象"""
    try:
        return bpy.context.active_object
    except AttributeError:
        print("无法获取活动对象")
        return None

def safe_get_selected_objects():
    """安全获取选中的对象"""
    try:
        return bpy.context.selected_objects
    except AttributeError:
        print("无法获取选中的对象")
        return []
```

### 6.2 上下文检查
```python
def check_context_validity():
    """检查上下文有效性"""
    issues = []
    
    if not bpy.context.scene:
        issues.append("没有活动场景")
    
    if not bpy.context.view_layer:
        issues.append("没有视图层")
    
    if not bpy.context.window:
        issues.append("没有活动窗口")
    
    return issues
```

## 7. 性能优化

### 7.1 缓存上下文
```python
def optimize_context_access():
    """优化上下文访问"""
    # 缓存常用值
    scene = bpy.context.scene
    active_obj = bpy.context.active_object
    selected_objs = bpy.context.selected_objects
    
    # 使用缓存的值而不是重复访问
    for obj in selected_objs:
        if obj != active_obj:
            # 处理非活动对象
            pass
```

### 7.2 批量上下文操作
```python
def batch_context_operations():
    """批量上下文操作"""
    # 收集所有需要操作的对象
    objects_to_process = []
    
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH' and obj.hide_viewport == False:
            objects_to_process.append(obj)
    
    # 批量处理
    with bpy.context.temp_override(selected_objects=objects_to_process):
        if objects_to_process:
            bpy.context.view_layer.objects.active = objects_to_process[0]
            # 执行批量操作
            bpy.ops.object.delete()
```

## 8. 最佳实践

### 8.1 上下文管理
- 总是检查上下文的有效性
- 使用临时上下文进行批量操作
- 在操作完成后恢复原始状态

### 8.2 错误处理
- 使用try-except块处理可能的错误
- 提供有意义的错误消息
- 在出错时清理状态

### 8.3 性能考虑
- 缓存频繁访问的上下文值
- 避免在循环中重复访问上下文
- 使用批量操作而不是逐个操作 
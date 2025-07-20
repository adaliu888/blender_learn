我来为您翻译Blender的Operators (bpy.ops)文档：

# Operators (bpy.ops) 操作符

## 调用操作符

提供Python访问调用操作符的功能，包括用C、Python或宏编写的操作符。

只能使用关键字参数来传递操作符属性。

操作符没有您可能期望的返回值，而是返回一个由以下元素组成的集合：`{'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'}`。常见的返回值是`{'FINISHED'}`和`{'CANCELLED'}`，后者表示操作符执行被中止，没有进行任何更改或保存撤销历史记录。

在错误的上下文中调用操作符会引发`RuntimeError`，有一个`poll()`方法可以避免这个问题。

注意，在这个例子中操作符ID（bl_idname）是`mesh.subdivide`，`bpy.ops`只是Python的访问路径。

## 关键字和位置参数

对于调用操作符，关键字用于操作符属性，位置参数用于定义如何调用操作符。

有2个可选的位置参数（下面详细记录）。

```python
bpy.ops.test.operator(execution_context, undo)
```

- `execution_context` - str (枚举)
- `undo` - bool类型

这些参数中的每一个都是可选的，但必须按上述顺序给出。

## 使用示例

```python
import bpy

# 调用操作符
bpy.ops.mesh.subdivide(number_cuts=3, smoothness=0.5)

# 检查poll()以避免异常
if bpy.ops.object.mode_set.poll():
    bpy.ops.object.mode_set(mode='EDIT')
```

## 覆盖上下文

可以覆盖操作符看到的上下文成员，使它们作用于指定的数据而不是选中的或活动的数据，或者在用户界面的不同部分执行操作符。

上下文覆盖作为字典传递，键匹配`bpy.context`中的上下文成员名称。例如，要覆盖`bpy.context.active_object`，您需要将`{'active_object': object}`传递给`bpy.types.Context.temp_override`。

**注意**：您几乎总是希望使用实际当前上下文的副本作为基础（否则，您必须自己查找和收集所有需要的数据）。

```python
# 删除场景中的所有对象而不是选中的对象
import bpy
from bpy import context
context_override = context.copy()
context_override["selected_objects"] = list(context.scene.objects)
with context.temp_override(**context_override):
    bpy.ops.object.delete()
```

## 执行上下文

调用操作符时，您可能希望传递执行上下文。

这决定了为操作符运行提供的上下文，以及是否调用`invoke()`或仅调用`execute()`。

默认使用`EXEC_DEFAULT`，仅运行`execute()`方法，但您可能希望操作符通过`INVOKE_DEFAULT`进行用户交互，如果存在的话也会调用`invoke()`。

执行上下文是以下之一：

- `INVOKE_DEFAULT`
- `INVOKE_REGION_WIN`
- `INVOKE_REGION_CHANNELS`
- `INVOKE_REGION_PREVIEW`
- `INVOKE_AREA`
- `INVOKE_SCREEN`
- `EXEC_DEFAULT`
- `EXEC_REGION_WIN`
- `EXEC_REGION_CHANNELS`
- `EXEC_REGION_PREVIEW`
- `EXEC_AREA`
- `EXEC_SCREEN`

```python
# 集合添加弹出窗口
import bpy
bpy.ops.object.collection_instance_add('INVOKE_DEFAULT')
```

也可以在用户界面的特定部分运行操作符。为此，我们需要传递窗口、区域，有时还需要传递区域。

```python
# 在所有窗口中最大化3D视图
import bpy
from bpy import context

for window in context.window_manager.windows:
    screen = window.screen
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            with context.temp_override(window=window, area=area):
                bpy.ops.screen.screen_full_area()
            break
```

## 子模块

### 操作符分类

**动画相关操作符：**
- Action Operators (动作操作符)
- Anim Operators (动画操作符)
- Nla Operators (非线性动画操作符)
- Pose Operators (姿态操作符)
- Poselib Operators (姿态库操作符)

**建模相关操作符：**
- Mesh Operators (网格操作符)
- Curve Operators (曲线操作符)
- Curves Operators (曲线系统操作符)
- Surface Operators (曲面操作符)
- Geometry Operators (几何体操作符)
- Sculpt Operators (雕刻操作符)
- Sculpt Curves Operators (雕刻曲线操作符)

**骨骼和约束：**
- Armature Operators (骨骼操作符)
- Constraint Operators (约束操作符)
- Rigidbody Operators (刚体操作符)

**材质和纹理：**
- Material Operators (材质操作符)
- Texture Operators (纹理操作符)
- Paint Operators (绘制操作符)

**渲染和输出：**
- Render Operators (渲染操作符)
- Cycles Operators (Cycles渲染器操作符)
- Export Operators (导出操作符)
- Import Operators (导入操作符)

**界面和工具：**
- Object Operators (对象操作符)
- Transform Operators (变换操作符)
- View3D Operators (3D视图操作符)
- View2D Operators (2D视图操作符)
- Screen Operators (屏幕操作符)
- Workspace Operators (工作区操作符)

**文件和数据：**
- File Operators (文件操作符)
- Scene Operators (场景操作符)
- Collection Operators (集合操作符)
- Asset Operators (资产操作符)

**特殊功能：**
- Node Operators (节点操作符)
- Script Operators (脚本操作符)
- Console Operators (控制台操作符)
- Text Operators (文本操作符)
- Info Operators (信息操作符)

**其他专业功能：**
- Camera Operators (相机操作符)
- Light Operators (灯光操作符)
- World Operators (世界操作符)
- Particle Operators (粒子操作符)
- Fluid Operators (流体操作符)
- Cloth Operators (布料操作符)
- Boid Operators (群体操作符)
- Cachefile Operators (缓存文件操作符)
- Clip Operators (剪辑操作符)
- Mask Operators (遮罩操作符)
- Marker Operators (标记操作符)
- Palette Operators (调色板操作符)
- Sound Operators (声音操作符)
- Sequencer Operators (序列编辑器操作符)
- Spreadsheet Operators (电子表格操作符)

## 实用示例

### 1. **基本操作符调用**
```python
import bpy

# 添加立方体
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))

# 添加球体
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(3, 0, 0))

# 添加圆柱体
bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=2, location=(-3, 0, 0))
```

### 2. **检查操作符可用性**
```python
def safe_operator_call():
    """安全地调用操作符"""
    
    # 检查是否可以进入编辑模式
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='EDIT')
        print("已进入编辑模式")
    else:
        print("无法进入编辑模式")
    
    # 检查是否可以细分网格
    if bpy.ops.mesh.subdivide.poll():
        bpy.ops.mesh.subdivide(number_cuts=2)
        print("网格已细分")
    else:
        print("无法细分网格")

safe_operator_call()
```

### 3. **使用上下文覆盖**
```python
def operate_on_specific_objects():
    """对特定对象执行操作"""
    import bpy
    from bpy import context
    
    # 获取所有网格对象
    mesh_objects = [obj for obj in bpy.data.objects if obj.type == 'MESH']
    
    if mesh_objects:
        # 创建上下文覆盖
        context_override = context.copy()
        context_override["selected_objects"] = mesh_objects
        context_override["active_object"] = mesh_objects[0]
        
        # 在覆盖的上下文中执行操作
        with context.temp_override(**context_override):
            # 删除所有选中的对象
            bpy.ops.object.delete()
            print(f"已删除 {len(mesh_objects)} 个网格对象")

operate_on_specific_objects()
```

### 4. **使用执行上下文**
```python
def invoke_operator_with_context():
    """使用特定执行上下文调用操作符"""
    import bpy
    
    # 使用INVOKE_DEFAULT显示用户界面
    bpy.ops.object.collection_instance_add('INVOKE_DEFAULT')
    
    # 使用EXEC_DEFAULT直接执行
    bpy.ops.mesh.primitive_cube_add('EXEC_DEFAULT', location=(0, 0, 0))

invoke_operator_with_context()
```

### 5. **批量操作示例**
```python
def batch_operations():
    """批量操作示例"""
    import bpy
    
    # 创建多个对象
    for i in range(5):
        x = i * 2
        bpy.ops.mesh.primitive_cube_add(location=(x, 0, 0))
    
    # 选择所有对象
    bpy.ops.object.select_all(action='SELECT')
    
    # 合并所有选中的对象
    if bpy.ops.object.join.poll():
        bpy.ops.object.join()
        print("所有对象已合并")
    
    # 添加细分表面修改器
    active_obj = bpy.context.active_object
    if active_obj and active_obj.type == 'MESH':
        modifier = active_obj.modifiers.new(name="Subdivision", type='SUBSURF')
        modifier.levels = 2
        print("已添加细分表面修改器")

batch_operations()
```

### 6. **错误处理示例**
```python
def safe_operator_execution():
    """安全的操作符执行"""
    import bpy
    
    try:
        # 尝试执行操作符
        result = bpy.ops.mesh.subdivide(number_cuts=3)
        
        # 检查结果
        if 'FINISHED' in result:
            print("操作符执行成功")
        elif 'CANCELLED' in result:
            print("操作符执行被取消")
        elif 'RUNNING_MODAL' in result:
            print("操作符正在模态运行")
        else:
            print("操作符执行结果未知")
            
    except RuntimeError as e:
        print(f"操作符执行失败: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")

safe_operator_execution()
```

### 7. **自定义操作符调用**
```python
def custom_operator_call():
    """自定义操作符调用"""
    import bpy
    
    # 设置操作符参数
    operator_params = {
        'number_cuts': 2,
        'smoothness': 0.5,
        'quadtri': False,
        'quadcorner': 'INNER_VERT'
    }
    
    # 调用操作符
    if bpy.ops.mesh.subdivide.poll():
        result = bpy.ops.mesh.subdivide(**operator_params)
        print(f"细分操作结果: {result}")
    else:
        print("细分操作不可用")

custom_operator_call()
```

这个翻译涵盖了bpy.ops模块的核心概念和使用方法，为中文用户提供了完整的操作符调用参考。
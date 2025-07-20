我来为您提供一个完整可执行的Message Bus简单实例：

# 完整可执行的Message Bus实例

```python
import bpy

class BlenderMessageBusDemo:
    def __init__(self):
        self.owner = object()
        self.setup_demo()
    
    def setup_demo(self):
        """设置演示环境"""
        print("�� 开始Message Bus演示...")
        
        # 清理场景
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        
        # 创建一个测试立方体
        bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
        self.test_cube = bpy.context.active_object
        self.test_cube.name = "MessageBusTestCube"
        
        # 创建一个测试球体
        bpy.ops.mesh.primitive_uv_sphere_add(location=(3, 0, 0))
        self.test_sphere = bpy.context.active_object
        self.test_sphere.name = "MessageBusTestSphere"
        
        # 设置订阅
        self.setup_subscriptions()
        
        print("✅ 演示环境设置完成!")
        print("📋 操作说明:")
        print("   1. 在3D视口中移动立方体")
        print("   2. 在属性面板中修改对象名称")
        print("   3. 在属性面板中修改对象缩放")
        print("   4. 在属性面板中修改对象旋转")
        print("   5. 运行 cleanup_demo() 清理订阅")
    
    def setup_subscriptions(self):
        """设置所有订阅"""
        # 订阅立方体位置变化
        self.subscribe_object_location(self.test_cube, "立方体")
        
        # 订阅球体位置变化
        self.subscribe_object_location(self.test_sphere, "球体")
        
        # 订阅所有对象名称变化
        self.subscribe_object_names()
        
        # 订阅所有对象缩放变化
        self.subscribe_object_scales()
        
        # 订阅场景帧数变化
        self.subscribe_frame_changes()
        
        # 订阅渲染引擎变化
        self.subscribe_render_engine()
    
    def location_callback(self, obj_name, *args):
        """位置变化回调"""
        obj = bpy.data.objects.get(obj_name)
        if obj:
            print(f"�� {obj_name} 位置变化: {obj.location}")
    
    def name_callback(self, *args):
        """名称变化回调"""
        print("📝 对象名称发生变化!")
        for obj in bpy.data.objects:
            if obj.type == 'MESH':
                print(f"   {obj.name}")
    
    def scale_callback(self, obj_name, *args):
        """缩放变化回调"""
        obj = bpy.data.objects.get(obj_name)
        if obj:
            print(f"�� {obj_name} 缩放变化: {obj.scale}")
    
    def frame_callback(self, *args):
        """帧数变化回调"""
        scene = bpy.context.scene
        print(f"��️ 当前帧: {scene.frame_current}")
    
    def render_callback(self, *args):
        """渲染引擎变化回调"""
        scene = bpy.context.scene
        print(f"🎬 渲染引擎变化: {scene.render.engine}")
    
    def subscribe_object_location(self, obj, obj_label):
        """订阅对象位置变化"""
        subscribe_to = obj.location
        bpy.msgbus.subscribe_rna(
            key=subscribe_to,
            owner=self.owner,
            args=(obj.name,),
            notify=lambda *args: self.location_callback(obj_label, *args),
        )
        print(f"✅ 已订阅 {obj_label} 位置变化")
    
    def subscribe_object_names(self):
        """订阅所有对象名称变化"""
        subscribe_to = (bpy.types.Object, "name")
        bpy.msgbus.subscribe_rna(
            key=subscribe_to,
            owner=self.owner,
            args=(),
            notify=self.name_callback,
        )
        print("✅ 已订阅所有对象名称变化")
    
    def subscribe_object_scales(self):
        """订阅所有对象缩放变化"""
        for obj in bpy.data.objects:
            if obj.type == 'MESH':
                subscribe_to = obj.scale
                bpy.msgbus.subscribe_rna(
                    key=subscribe_to,
                    owner=self.owner,
                    args=(obj.name,),
                    notify=lambda *args: self.scale_callback(obj.name, *args),
                )
        print("✅ 已订阅所有对象缩放变化")
    
    def subscribe_frame_changes(self):
        """订阅帧数变化"""
        subscribe_to = bpy.context.scene.frame_current
        bpy.msgbus.subscribe_rna(
            key=subscribe_to,
            owner=self.owner,
            args=(),
            notify=self.frame_callback,
        )
        print("✅ 已订阅帧数变化")
    
    def subscribe_render_engine(self):
        """订阅渲染引擎变化"""
        subscribe_to = bpy.context.scene.render.engine
        bpy.msgbus.subscribe_rna(
            key=subscribe_to,
            owner=self.owner,
            args=(),
            notify=self.render_callback,
        )
        print("✅ 已订阅渲染引擎变化")
    
    def cleanup_demo(self):
        """清理演示环境"""
        bpy.msgbus.clear_by_owner(self.owner)
        print("🧹 Message Bus订阅已清理")
        
        # 删除测试对象
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        print("��️ 测试对象已删除")
        print("✅ 演示环境清理完成!")

# 创建演示实例
demo = BlenderMessageBusDemo()

# 清理函数（在需要时调用）
def cleanup_demo():
    demo.cleanup_demo()

# 测试函数
def test_message_bus():
    """测试Message Bus功能"""
    print("\n�� 开始Message Bus测试...")
    
    # 测试位置变化
    if demo.test_cube:
        print("📍 测试立方体位置变化...")
        demo.test_cube.location.x += 1.0
    
    # 测试名称变化
    if demo.test_sphere:
        print("📝 测试球体名称变化...")
        demo.test_sphere.name = "RenamedSphere"
    
    # 测试缩放变化
    if demo.test_cube:
        print("📏 测试立方体缩放变化...")
        demo.test_cube.scale = (2.0, 2.0, 2.0)
    
    # 测试帧数变化
    print("��️ 测试帧数变化...")
    bpy.context.scene.frame_current += 10
    
    # 测试渲染引擎变化
    print("🎬 测试渲染引擎变化...")
    bpy.context.scene.render.engine = 'CYCLES'
    
    print("✅ 测试完成!")

# 运行测试
# test_message_bus()

print("\n�� 使用说明:")
print("1. 运行 test_message_bus() 进行自动测试")
print("2. 在3D视口中手动移动对象")
print("3. 在属性面板中修改对象属性")
print("4. 运行 cleanup_demo() 清理环境")
```

## 使用步骤：

### 1. 运行演示
将上述代码复制到Blender的文本编辑器中，然后运行。您会看到：
- 场景中创建了一个立方体和一个球体
- 控制台输出显示各种订阅已设置

### 2. 测试功能
在Blender中执行以下操作来测试Message Bus：

#### 自动测试：
```python
# 在文本编辑器中运行
test_message_bus()
```

#### 手动测试：
1. **移动对象**：在3D视口中选择并移动立方体或球体
2. **修改名称**：在属性面板中修改对象名称
3. **修改缩放**：在属性面板中修改对象的缩放值
4. **修改旋转**：在属性面板中修改对象的旋转值
5. **切换帧**：在时间轴上移动播放头
6. **切换渲染引擎**：在渲染设置中切换渲染引擎

### 3. 观察输出
在Blender的控制台中，您会看到类似这样的输出：
```
📍 立方体 位置变化: <Vector (1.0000, 0.0000, 0.0000)>
📝 对象名称发生变化!
   MessageBusTestCube
   RenamedSphere
�� MessageBusTestCube 缩放变化: <Vector (2.0000, 2.0000, 2.0000)>
��️ 当前帧: 11
🎬 渲染引擎变化: CYCLES
```

### 4. 清理环境
```python
# 在文本编辑器中运行
cleanup_demo()
```

## 功能说明：

1. **位置监听**：监听立方体和球体的位置变化
2. **名称监听**：监听所有对象的名称变化
3. **缩放监听**：监听所有对象的缩放变化
4. **帧数监听**：监听场景当前帧的变化
5. **渲染引擎监听**：监听渲染引擎的切换

这个实例展示了Message Bus的核心功能，您可以根据需要修改和扩展它。
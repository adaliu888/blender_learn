# Property Definitions (bpy.props) 属性定义

## 概述
此模块定义属性以扩展Blender的内部数据。这些函数的结果用于将属性分配给在Blender中注册的类，不能直接使用。

**注意：**
这些函数的所有参数必须作为关键字传递。

## 分配给现有类

自定义属性可以添加到任何ID、Bone和PoseBone的子类。

这些属性可以像Blender的现有属性一样进行动画化、通过用户界面和Python访问。

**警告：**
对这些属性的访问可能在多线程上下文中发生，在每数据块级别。在使用访问器或更新回调时必须仔细考虑这一点。

通常，这些回调不应影响其数据块拥有的任何其他数据。当访问外部非Blender数据时，应考虑线程安全机制。

```python
import bpy

# 为现有类型分配自定义属性
bpy.types.Material.custom_float = bpy.props.FloatProperty(name="测试属性")

# 测试属性是否存在
bpy.data.materials[0].custom_float = 5.0
```

## 操作符示例

自定义属性的常见用途是用于基于Python的操作符类。通过在文本编辑器中运行此代码或在3D视口的工具面板中点击按钮来测试此代码。后者将在重做面板中显示属性并允许您更改它们。

```python
import bpy

class OBJECT_OT_property_example(bpy.types.Operator):
    bl_idname = "object.property_example"
    bl_label = "属性示例"
    bl_options = {'REGISTER', 'UNDO'}

    my_float: bpy.props.FloatProperty(name="一些浮点数")
    my_bool: bpy.props.BoolProperty(name="切换选项")
    my_string: bpy.props.StringProperty(name="字符串值")

    def execute(self, context):
        self.report(
            {'INFO'}, 'F: %.2f  B: %s  S: %r' %
            (self.my_float, self.my_bool, self.my_string)
        )
        print('我的浮点数:', self.my_float)
        print('我的布尔值:', self.my_bool)
        print('我的字符串:', self.my_string)
        return {'FINISHED'}

class OBJECT_PT_property_example(bpy.types.Panel):
    bl_idname = "object_PT_property_example"
    bl_label = "属性示例"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "工具"

    def draw(self, context):
        # 您可以设置用户按下UI中的按钮时应该使用的属性值
        props = self.layout.operator('object.property_example')
        props.my_bool = True
        props.my_string = "不应该是47吗？"

        # 您可以动态设置属性：
        if context.object:
            props.my_float = context.object.location.x
        else:
            props.my_float = 327

bpy.utils.register_class(OBJECT_OT_property_example)
bpy.utils.register_class(OBJECT_PT_property_example)

# 演示调用。确保也在3D视口中测试
bpy.ops.object.property_example(
    my_float=47,
    my_bool=True,
    my_string="不应该是327吗？",
)
```

## PropertyGroup示例

PropertyGroups可用于将自定义设置收集到一个值中，以避免许多单独的设置混合在一起。

```python
import bpy

class MaterialSettings(bpy.types.PropertyGroup):
    my_int: bpy.props.IntProperty()
    my_float: bpy.props.FloatProperty()
    my_string: bpy.props.StringProperty()

bpy.utils.register_class(MaterialSettings)

bpy.types.Material.my_settings = bpy.props.PointerProperty(type=MaterialSettings)

# 测试新设置是否工作
material = bpy.data.materials[0]

material.my_settings.my_int = 5
material.my_settings.my_float = 3.0
material.my_settings.my_string = "Foo"
```

## 集合示例

自定义属性可以添加到任何ID、Bone和PoseBone的子类。

```python
import bpy

# 分配集合
class SceneSettingItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="测试属性", default="未知")
    value: bpy.props.IntProperty(name="测试属性", default=22)

bpy.utils.register_class(SceneSettingItem)

bpy.types.Scene.my_settings = bpy.props.CollectionProperty(type=SceneSettingItem)

# 假设选择了骨骼对象
print("添加2个值！")

my_item = bpy.context.scene.my_settings.add()
my_item.name = "Spam"
my_item.value = 1000

my_item = bpy.context.scene.my_settings.add()
my_item.name = "Eggs"
my_item.value = 30

for my_item in bpy.context.scene.my_settings:
    print(my_item.name, my_item.value)
```

## 更新示例

当属性更改时执行操作可能很有用，可用于更新其他属性或与外部数据同步。

除CollectionProperty外，所有属性都定义更新函数。

**警告：**
请记住，这些回调可能在多线程上下文中执行。

**警告：**
如果属性属于操作符，更新回调的第一个参数将是OperatorProperties实例，而不是操作符本身的实例。这意味着您无法访问操作符的其他内部函数，只能访问其其他属性。

```python
import bpy

def update_func(self, context):
    print("我的测试函数", self)

bpy.types.Scene.testprop = bpy.props.FloatProperty(update=update_func)

bpy.context.scene.testprop = 11.0

# >>> 我的测试函数 <bpy_struct, Scene("Scene")>
```

## Getter/Setter示例

Getter/setter函数可用于布尔、整数、浮点、字符串和枚举属性。如果定义了这些回调，属性将不会自动存储在ID属性中。相反，当从API读取或写入属性时，将调用get和set函数。

**警告：**
请记住，这些回调可能在多线程上下文中执行。

```python
import bpy

# 从ID属性简单读取/写入属性
# 这是RNA内部会做的事情
def get_float(self):
    return self["testprop"]

def set_float(self, value):
    self["testprop"] = value

bpy.types.Scene.test_float = bpy.props.FloatProperty(get=get_float, set=set_float)

# 只读字符串属性，返回当前日期
def get_date(self):
    import datetime
    return str(datetime.datetime.now())

bpy.types.Scene.test_date = bpy.props.StringProperty(get=get_date)

# 布尔数组。Set函数存储单个布尔值，作为第二个组件返回
# 数组getter必须返回列表或元组
# 数组大小必须与属性向量大小完全匹配
def get_array(self):
    return (True, self["somebool"])

def set_array(self, values):
    self["somebool"] = values[0] and values[1]

bpy.types.Scene.test_array = bpy.props.BoolVectorProperty(size=2, get=get_array, set=set_array)

# 枚举属性
# 注意：getter/setter回调必须使用整数标识符！
test_items = [
    ("RED", "红色", "", 1),
    ("GREEN", "绿色", "", 2),
    ("BLUE", "蓝色", "", 3),
    ("YELLOW", "黄色", "", 4),
]

def get_enum(self):
    import random
    return random.randint(1, 4)

def set_enum(self, value):
    print("设置值", value)

bpy.types.Scene.test_enum = bpy.props.EnumProperty(items=test_items, get=get_enum, set=set_enum)

# 测试属性：
scene = bpy.context.scene

scene.test_float = 12.34
print('test_float:', scene.test_float)

scene.test_array = (True, False)
print('test_array:', tuple(scene.test_array))

# scene.test_date = "blah"   # 这会失败，属性是只读的
print('test_date:', scene.test_date)

scene.test_enum = 'BLUE'
print('test_enum:', scene.test_enum)

# 上述输出：
# test_float: 12.34000015258789
# test_array: (True, False)
# test_date: 2018-03-14 11:36:53.158653
# 设置值 3
# test_enum: GREEN
```

## 属性定义函数

### bpy.props.BoolProperty()
返回新的布尔属性定义。

**参数：**
- `name` (string) - 用户界面中使用的名称
- `description` (string) - 用于工具提示和API文档的文本
- `translation_context` (string) - 用作上下文以消除翻译歧义的文本
- `default` (bool) - 默认值，默认为False
- `options` (set) - Property Flag Items中的枚举器
- `override` (set) - Property Override Flag Items中的枚举器
- `tags` (set) - 由父类定义的标签枚举器
- `subtype` (string) - Property Subtype Number Items中的枚举器
- `update` (function) - 修改此值时调用的函数，此函数必须接受2个值(self, context)并返回None。警告：没有安全检查来避免无限递归
- `get` (function) - "读取"此值时调用的函数，此函数必须接受1个值(self)并返回属性的值
- `set` (function) - "写入"此值时调用的函数，此函数必须接受2个值(self, value)并返回None

```python
import bpy

# 创建布尔属性
bpy.types.Scene.my_bool = bpy.props.BoolProperty(
    name="我的布尔属性",
    description="这是一个布尔属性",
    default=True
)
```

### bpy.props.BoolVectorProperty()
返回新的向量布尔属性定义。

**参数：**
- `name` (string) - 用户界面中使用的名称
- `description` (string) - 用于工具提示和API文档的文本
- `translation_context` (string) - 用作上下文以消除翻译歧义的文本
- `default` (sequence) - 长度为size的布尔序列
- `options` (set) - Property Flag Items中的枚举器
- `override` (set) - Property Override Flag Items中的枚举器
- `tags` (set) - 由父类定义的标签枚举器
- `subtype` (string) - Property Subtype Number Array Items中的枚举器
- `size` (int or int sequence) - 向量维度在[1, 32]中。可以使用int序列定义多维数组
- `update` (function) - 修改此值时调用的函数
- `get` (function) - "读取"此值时调用的函数
- `set` (function) - "写入"此值时调用的函数

```python
import bpy

# 创建布尔向量属性
bpy.types.Scene.my_bool_vector = bpy.props.BoolVectorProperty(
    name="我的布尔向量",
    description="这是一个布尔向量属性",
    default=(True, False, True),
    size=3
)
```

### bpy.props.CollectionProperty()
返回新的集合属性定义。

**参数：**
- `type` (class) - bpy.types.PropertyGroup的子类
- `name` (string) - 用户界面中使用的名称
- `description` (string) - 用于工具提示和API文档的文本
- `translation_context` (string) - 用作上下文以消除翻译歧义的文本
- `options` (set) - Property Flag Items中的枚举器
- `override` (set) - Property Override Flag Collection Items中的枚举器
- `tags` (set) - 由父类定义的标签枚举器

```python
import bpy

# 定义集合项类型
class MyCollectionItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="名称")
    value: bpy.props.IntProperty(name="值")

bpy.utils.register_class(MyCollectionItem)

# 创建集合属性
bpy.types.Scene.my_collection = bpy.props.CollectionProperty(type=MyCollectionItem)
```

### bpy.props.EnumProperty()
返回新的枚举器属性定义。

**参数：**
- `items` (sequence of string tuples or a function) - 格式化的枚举项序列：[(identifier, name, description, icon, number), ...]
- `name` (string) - 用户界面中使用的名称
- `description` (string) - 用于工具提示和API文档的文本
- `translation_context` (string) - 用作上下文以消除翻译歧义的文本
- `default` (string, integer or set) - 此枚举的默认值
- `options` (set) - Property Flag Enum Items中的枚举器
- `override` (set) - Property Override Flag Items中的枚举器
- `tags` (set) - 由父类定义的标签枚举器
- `update` (function) - 修改此值时调用的函数
- `get` (function) - "读取"此值时调用的函数
- `set` (function) - "写入"此值时调用的函数

```python
import bpy

# 创建枚举属性
enum_items = [
    ("OPTION_A", "选项A", "这是选项A", "", 1),
    ("OPTION_B", "选项B", "这是选项B", "", 2),
    ("OPTION_C", "选项C", "这是选项C", "", 3),
]

bpy.types.Scene.my_enum = bpy.props.EnumProperty(
    name="我的枚举",
    description="这是一个枚举属性",
    items=enum_items,
    default="OPTION_A"
)
```

### bpy.props.FloatProperty()
返回新的浮点（单精度）属性定义。

**参数：**
- `name` (string) - 用户界面中使用的名称
- `description` (string) - 用于工具提示和API文档的文本
- `translation_context` (string) - 用作上下文以消除翻译歧义的文本
- `default` (float) - 默认值，默认为0.0
- `min` (float) - 硬最小值，尝试分配低于此值的值将静默分配此最小值
- `max` (float) - 硬最大值，尝试分配高于此值的值将静默分配此最大值
- `soft_min` (float) - 软最小值(>= min)，用户在UI中无法将小部件拖到此值以下
- `soft_max` (float) - 软最大值(<= max)，用户在UI中无法将小部件拖到此值以上
- `step` (int) - UI中递增/递减的步长，在[1, 100]中，默认为3（警告：实际值是/100）
- `precision` (int) - 显示的最大小数位数，在[0, 6]中
- `options` (set) - Property Flag Items中的枚举器
- `override` (set) - Property Override Flag Items中的枚举器
- `tags` (set) - 由父类定义的标签枚举器
- `subtype` (string) - Property Subtype Number Items中的枚举器
- `unit` (string) - Property Unit Items中的枚举器
- `update` (function) - 修改此值时调用的函数
- `get` (function) - "读取"此值时调用的函数
- `set` (function) - "写入"此值时调用的函数

```python
import bpy

# 创建浮点属性
bpy.types.Scene.my_float = bpy.props.FloatProperty(
    name="我的浮点数",
    description="这是一个浮点属性",
    default=1.0,
    min=0.0,
    max=10.0,
    soft_min=0.0,
    soft_max=5.0,
    step=1,
    precision=2
)
```

### bpy.props.FloatVectorProperty()
返回新的向量浮点属性定义。

**参数：**
- `name` (string) - 用户界面中使用的名称
- `description` (string) - 用于工具提示和API文档的文本
- `translation_context` (string) - 用作上下文以消除翻译歧义的文本
- `default` (sequence) - 长度为size的浮点序列
- `min` (float) - 硬最小值
- `max` (float) - 硬最大值
- `soft_min` (float) - 软最小值
- `soft_max` (float) - 软最大值
- `options` (set) - Property Flag Items中的枚举器
- `override` (set) - Property Override Flag Items中的枚举器
- `tags` (set) - 由父类定义的标签枚举器
- `step` (int) - UI中递增/递减的步长
- `precision` (int) - 显示的最大小数位数
- `subtype` (string) - Property Subtype Number Array Items中的枚举器
- `unit` (string) - Property Unit Items中的枚举器
- `size` (int or int sequence) - 向量维度在[1, 32]中
- `update` (function) - 修改此值时调用的函数
- `get` (function) - "读取"此值时调用的函数
- `set` (function) - "写入"此值时调用的函数

```python
import bpy

# 创建浮点向量属性
bpy.types.Scene.my_float_vector = bpy.props.FloatVectorProperty(
    name="我的浮点向量",
    description="这是一个浮点向量属性",
    default=(1.0, 2.0, 3.0),
    min=0.0,
    max=10.0,
    size=3
)
```

### bpy.props.IntProperty()
返回新的整数属性定义。

**参数：**
- `name` (string) - 用户界面中使用的名称
- `description` (string) - 用于工具提示和API文档的文本
- `translation_context` (string) - 用作上下文以消除翻译歧义的文本
- `default` (int) - 默认值，默认为0
- `min` (int) - 硬最小值
- `max` (int) - 硬最大值
- `soft_min` (int) - 软最小值
- `soft_max` (int) - 软最大值
- `step` (int) - UI中递增/递减的步长，默认为1
- `options` (set) - Property Flag Items中的枚举器
- `override` (set) - Property Override Flag Items中的枚举器
- `tags` (set) - 由父类定义的标签枚举器
- `subtype` (string) - Property Subtype Number Items中的枚举器
- `update` (function) - 修改此值时调用的函数
- `get` (function) - "读取"此值时调用的函数
- `set` (function) - "写入"此值时调用的函数

```python
import bpy

# 创建整数属性
bpy.types.Scene.my_int = bpy.props.IntProperty(
    name="我的整数",
    description="这是一个整数属性",
    default=5,
    min=0,
    max=100,
    soft_min=0,
    soft_max=50
)
```

### bpy.props.IntVectorProperty()
返回新的向量整数属性定义。

**参数：**
- `name` (string) - 用户界面中使用的名称
- `description` (string) - 用于工具提示和API文档的文本
- `translation_context` (string) - 用作上下文以消除翻译歧义的文本
- `default` (sequence) - 长度为size的整数序列
- `min` (int) - 硬最小值
- `max` (int) - 硬最大值
- `soft_min` (int) - 软最小值
- `soft_max` (int) - 软最大值
- `step` (int) - UI中递增/递减的步长
- `options` (set) - Property Flag Items中的枚举器
- `override` (set) - Property Override Flag Items中的枚举器
- `tags` (set) - 由父类定义的标签枚举器
- `subtype` (string) - Property Subtype Number Array Items中的枚举器
- `size` (int or int sequence) - 向量维度在[1, 32]中
- `update` (function) - 修改此值时调用的函数
- `get` (function) - "读取"此值时调用的函数
- `set` (function) - "写入"此值时调用的函数

```python
import bpy

# 创建整数向量属性
bpy.types.Scene.my_int_vector = bpy.props.IntVectorProperty(
    name="我的整数向量",
    description="这是一个整数向量属性",
    default=(1, 2, 3),
    min=0,
    max=10,
    size=3
)
```

### bpy.props.PointerProperty()
返回新的指针属性定义。

**参数：**
- `type` (class) - bpy.types.PropertyGroup或bpy.types.ID的子类
- `name` (string) - 用户界面中使用的名称
- `description` (string) - 用于工具提示和API文档的文本
- `translation_context` (string) - 用作上下文以消除翻译歧义的文本
- `options` (set) - Property Flag Items中的枚举器
- `override` (set) - Property Override Flag Items中的枚举器
- `tags` (set) - 由父类定义的标签枚举器
- `poll` (function) - 用于确定项目是否对此属性有效的函数
- `update` (function) - 修改此值时调用的函数

```python
import bpy

# 定义指针属性类型
class MyPointerType(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="名称")
    value: bpy.props.FloatProperty(name="值")

bpy.utils.register_class(MyPointerType)

# 创建指针属性
bpy.types.Scene.my_pointer = bpy.props.PointerProperty(
    name="我的指针",
    description="这是一个指针属性",
    type=MyPointerType
)
```

### bpy.props.RemoveProperty()
移除动态定义的属性。

**参数：**
- `cls` (type) - 包含属性的类（必须是位置参数）
- `attr` (string) - 属性名称（必须作为关键字传递）

**注意：**
通常不需要直接访问此函数。而是使用del cls.attr

```python
import bpy

# 移除属性
bpy.props.RemoveProperty(bpy.types.Scene, attr="my_property")

# 或者使用del
del bpy.types.Scene.my_property
```

### bpy.props.StringProperty()
返回新的字符串属性定义。

**参数：**
- `name` (string) - 用户界面中使用的名称
- `description` (string) - 用于工具提示和API文档的文本
- `translation_context` (string) - 用作上下文以消除翻译歧义的文本
- `default` (string) - 初始化字符串
- `maxlen` (int) - 字符串的最大长度
- `options` (set) - Property Flag Items中的枚举器
- `override` (set) - Property Override Flag Items中的枚举器
- `tags` (set) - 由父类定义的标签枚举器
- `subtype` (string) - Property Subtype String Items中的枚举器
- `update` (function) - 修改此值时调用的函数
- `get` (function) - "读取"此值时调用的函数
- `set` (function) - "写入"此值时调用的函数
- `search` (function) - 用于显示此字符串候选的函数
- `search_options` (set) - 搜索选项集合

```python
import bpy

# 创建字符串属性
bpy.types.Scene.my_string = bpy.props.StringProperty(
    name="我的字符串",
    description="这是一个字符串属性",
    default="默认值",
    maxlen=100
)
```

## 使用示例

### 1. **基本属性创建示例**
```python
import bpy

def create_basic_properties():
    """创建基本属性"""
    
    # 为场景添加各种类型的属性
    bpy.types.Scene.my_bool = bpy.props.BoolProperty(
        name="我的布尔值",
        description="这是一个布尔属性",
        default=True
    )
    
    bpy.types.Scene.my_int = bpy.props.IntProperty(
        name="我的整数",
        description="这是一个整数属性",
        default=42,
        min=0,
        max=100
    )
    
    bpy.types.Scene.my_float = bpy.props.FloatProperty(
        name="我的浮点数",
        description="这是一个浮点属性",
        default=3.14,
        min=0.0,
        max=10.0
    )
    
    bpy.types.Scene.my_string = bpy.props.StringProperty(
        name="我的字符串",
        description="这是一个字符串属性",
        default="Hello World"
    )
    
    print("基本属性已创建")

create_basic_properties()
```

### 2. **向量属性示例**
```python
import bpy

def create_vector_properties():
    """创建向量属性"""
    
    # 创建浮点向量属性
    bpy.types.Scene.my_float_vector = bpy.props.FloatVectorProperty(
        name="我的浮点向量",
        description="这是一个3D浮点向量",
        default=(1.0, 2.0, 3.0),
        min=0.0,
        max=10.0,
        size=3
    )
    
    # 创建整数向量属性
    bpy.types.Scene.my_int_vector = bpy.props.IntVectorProperty(
        name="我的整数向量",
        description="这是一个3D整数向量",
        default=(1, 2, 3),
        min=0,
        max=10,
        size=3
    )
    
    # 创建布尔向量属性
    bpy.types.Scene.my_bool_vector = bpy.props.BoolVectorProperty(
        name="我的布尔向量",
        description="这是一个3D布尔向量",
        default=(True, False, True),
        size=3
    )
    
    print("向量属性已创建")

create_vector_properties()
```

### 3. **枚举属性示例**
```python
import bpy

def create_enum_properties():
    """创建枚举属性"""
    
    # 静态枚举项
    enum_items = [
        ("OPTION_A", "选项A", "这是第一个选项", "", 1),
        ("OPTION_B", "选项B", "这是第二个选项", "", 2),
        ("OPTION_C", "选项C", "这是第三个选项", "", 3),
        ("OPTION_D", "选项D", "这是第四个选项", "", 4),
    ]
    
    bpy.types.Scene.my_enum = bpy.props.EnumProperty(
        name="我的枚举",
        description="这是一个枚举属性",
        items=enum_items,
        default="OPTION_A"
    )
    
    # 动态枚举项（使用回调函数）
    def enum_items_callback(self, context):
        return [
            ("DYNAMIC_A", "动态选项A", "动态选项A的描述"),
            ("DYNAMIC_B", "动态选项B", "动态选项B的描述"),
            ("DYNAMIC_C", "动态选项C", "动态选项C的描述"),
        ]
    
    bpy.types.Scene.my_dynamic_enum = bpy.props.EnumProperty(
        name="我的动态枚举",
        description="这是一个动态枚举属性",
        items=enum_items_callback
    )
    
    print("枚举属性已创建")

create_enum_properties()
```

### 4. **PropertyGroup示例**
```python
import bpy

def create_property_groups():
    """创建属性组"""
    
    # 定义属性组
    class MySettings(bpy.types.PropertyGroup):
        name: bpy.props.StringProperty(name="名称", default="默认名称")
        value: bpy.props.FloatProperty(name="值", default=1.0)
        enabled: bpy.props.BoolProperty(name="启用", default=True)
        
        # 枚举属性
        enum_items = [
            ("TYPE_A", "类型A", "类型A的描述"),
            ("TYPE_B", "类型B", "类型B的描述"),
            ("TYPE_C", "类型C", "类型C的描述"),
        ]
        
        type: bpy.props.EnumProperty(
            name="类型",
            description="选择类型",
            items=enum_items,
            default="TYPE_A"
        )
    
    # 注册属性组
    bpy.utils.register_class(MySettings)
    
    # 为场景添加指针属性
    bpy.types.Scene.my_settings = bpy.props.PointerProperty(type=MySettings)
    
    # 为材质添加指针属性
    bpy.types.Material.my_settings = bpy.props.PointerProperty(type=MySettings)
    
    print("属性组已创建")

create_property_groups()
```

### 5. **集合属性示例**
```python
import bpy

def create_collection_properties():
    """创建集合属性"""
    
    # 定义集合项
    class MyCollectionItem(bpy.types.PropertyGroup):
        name: bpy.props.StringProperty(name="名称", default="项目")
        value: bpy.props.FloatProperty(name="值", default=0.0)
        enabled: bpy.props.BoolProperty(name="启用", default=True)
        
        # 颜色属性
        color: bpy.props.FloatVectorProperty(
            name="颜色",
            description="项目颜色",
            subtype='COLOR',
            default=(1.0, 1.0, 1.0),
            min=0.0,
            max=1.0,
            size=3
        )
    
    # 注册集合项
    bpy.utils.register_class(MyCollectionItem)
    
    # 为场景添加集合属性
    bpy.types.Scene.my_collection = bpy.props.CollectionProperty(type=MyCollectionItem)
    
    # 添加一些测试项
    scene = bpy.context.scene
    
    item1 = scene.my_collection.add()
    item1.name = "项目1"
    item1.value = 1.0
    item1.color = (1.0, 0.0, 0.0)  # 红色
    
    item2 = scene.my_collection.add()
    item2.name = "项目2"
    item2.value = 2.0
    item2.color = (0.0, 1.0, 0.0)  # 绿色
    
    print("集合属性已创建")

create_collection_properties()
```

### 6. **更新回调示例**
```python
import bpy

def create_update_callbacks():
    """创建更新回调"""
    
    def float_update_callback(self, context):
        """浮点属性更新回调"""
        print(f"浮点属性已更新: {self.my_float}")
        
        # 更新其他相关属性
        if hasattr(self, 'my_int'):
            self.my_int = int(self.my_float)
    
    def enum_update_callback(self, context):
        """枚举属性更新回调"""
        print(f"枚举属性已更新: {self.my_enum}")
        
        # 根据枚举值更新其他属性
        if self.my_enum == "OPTION_A":
            self.my_float = 1.0
        elif self.my_enum == "OPTION_B":
            self.my_float = 2.0
        elif self.my_enum == "OPTION_C":
            self.my_float = 3.0
    
    # 创建带更新回调的属性
    bpy.types.Scene.my_float = bpy.props.FloatProperty(
        name="我的浮点数",
        description="带更新回调的浮点属性",
        default=0.0,
        update=float_update_callback
    )
    
    enum_items = [
        ("OPTION_A", "选项A", "选项A的描述"),
        ("OPTION_B", "选项B", "选项B的描述"),
        ("OPTION_C", "选项C", "选项C的描述"),
    ]
    
    bpy.types.Scene.my_enum = bpy.props.EnumProperty(
        name="我的枚举",
        description="带更新回调的枚举属性",
        items=enum_items,
        default="OPTION_A",
        update=enum_update_callback
    )
    
    print("更新回调已创建")

create_update_callbacks()
```

### 7. **Getter/Setter示例**
```python
import bpy

def create_getter_setter():
    """创建Getter/Setter"""
    
    def get_float(self):
        """获取浮点值"""
        return self.get("my_float", 0.0)
    
    def set_float(self, value):
        """设置浮点值"""
        self["my_float"] = value
        print(f"浮点值已设置为: {value}")
    
    def get_readonly_string(self):
        """获取只读字符串"""
        import datetime
        return f"当前时间: {datetime.datetime.now()}"
    
    def get_enum(self):
        """获取枚举值"""
        import random
        return random.choice(["OPTION_A", "OPTION_B", "OPTION_C"])
    
    def set_enum(self, value):
        """设置枚举值"""
        print(f"枚举值已设置为: {value}")
    
    # 创建带getter/setter的属性
    bpy.types.Scene.my_float = bpy.props.FloatProperty(
        name="我的浮点数",
        description="带getter/setter的浮点属性",
        get=get_float,
        set=set_float
    )
    
    bpy.types.Scene.my_readonly_string = bpy.props.StringProperty(
        name="我的只读字符串",
        description="只读字符串属性",
        get=get_readonly_string
    )
    
    enum_items = [
        ("OPTION_A", "选项A", "选项A的描述"),
        ("OPTION_B", "选项B", "选项B的描述"),
        ("OPTION_C", "选项C", "选项C的描述"),
    ]
    
    bpy.types.Scene.my_enum = bpy.props.EnumProperty(
        name="我的枚举",
        description="带getter/setter的枚举属性",
        items=enum_items,
        get=get_enum,
        set=set_enum
    )
    
    print("Getter/Setter已创建")

create_getter_setter()
```

### 8. **搜索功能示例**
```python
import bpy

def create_search_properties():
    """创建带搜索功能的属性"""
    
    def search_callback(self, context, edit_text):
        """搜索回调函数"""
        # 模拟搜索结果
        candidates = [
            "apple",
            "banana", 
            "cherry",
            "date",
            "elderberry",
            "fig",
            "grape",
            "honeydew"
        ]
        
        # 过滤匹配的候选项
        results = []
        for candidate in candidates:
            if edit_text.lower() in candidate.lower():
                results.append(candidate)
        
        return results
    
    # 创建带搜索功能的字符串属性
    bpy.types.Scene.my_search_string = bpy.props.StringProperty(
        name="我的搜索字符串",
        description="带搜索功能的字符串属性",
        default="",
        search=search_callback,
        search_options={'SUGGESTION'}
    )
    
    print("搜索功能已创建")

create_search_properties()
```

这个文档涵盖了bpy.props模块的所有主要功能，为中文用户提供了完整的属性定义参考。 

我来为您翻译Blender的Property Definitions (bpy.props)文档并保存到指定目录：

Read file: blender_py/python-api/Property Definitions (bpy.props).md
我已经成功为您翻译了Blender的Property Definitions (bpy.props)文档并保存到了`blender_py/python-api/Property Definitions (bpy.props).md`文件中。

这个文档包含了以下主要内容：

## 主要功能模块

1. **属性定义基础** - 如何为Blender内部数据扩展属性
2. **操作符属性** - 在操作符类中使用自定义属性
3. **PropertyGroup** - 将相关设置组织成属性组
4. **集合属性** - 创建可动态添加/删除项的集合
5. **更新回调** - 属性值变化时的响应机制
6. **Getter/Setter** - 自定义属性的读取和写入逻辑

## 核心属性类型

### 基本类型
- **BoolProperty()** - 布尔属性
- **IntProperty()** - 整数属性
- **FloatProperty()** - 浮点属性
- **StringProperty()** - 字符串属性

### 向量类型
- **BoolVectorProperty()** - 布尔向量属性
- **IntVectorProperty()** - 整数向量属性
- **FloatVectorProperty()** - 浮点向量属性

### 复杂类型
- **EnumProperty()** - 枚举属性
- **CollectionProperty()** - 集合属性
- **PointerProperty()** - 指针属性

## 实用示例

文档包含了8个完整的使用示例：
1. 基本属性创建示例
2. 向量属性示例
3. 枚举属性示例
4. PropertyGroup示例
5. 集合属性示例
6. 更新回调示例
7. Getter/Setter示例
8. 搜索功能示例

## 特色功能

- **多线程安全** - 详细说明了在多线程环境下的注意事项
- **更新回调** - 属性值变化时的自动响应机制
- **自定义Getter/Setter** - 完全控制属性的读取和写入逻辑
- **搜索功能** - 为字符串属性提供智能搜索建议
- **属性组** - 将相关属性组织成逻辑单元
- **集合管理** - 动态添加、删除和管理属性集合

这个翻译为中文用户提供了完整的bpy.props模块参考，特别适合需要为Blender创建自定义属性、操作符和插件的开发者。
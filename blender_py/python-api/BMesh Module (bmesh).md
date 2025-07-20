# BMesh模块 (bmesh)

此模块提供对Blender的bmesh数据结构的访问。

## 介绍

此API提供对Blender内部网格编辑API的访问，具有几何连接数据和对编辑操作（如分割、分离、折叠和溶解）的访问权限。暴露的功能紧密跟随C API，为Python提供对Blender自身网格编辑工具使用的函数的访问。

有关BMesh数据类型及其如何相互引用的概述，请参见：BMesh设计文档。

**注意：** 磁盘和径向数据不通过Python API暴露，因为这是仅供内部使用的。

**警告**

TODO项目包括：
- 添加对BMesh遍历器的访问
- 添加自定义数据操作函数（添加、删除或重命名）

## 示例脚本

```python
# 此示例假设我们有一个选中的网格对象

import bpy
import bmesh

# 获取活动网格
me = bpy.context.object.data

# 获取BMesh表示
bm = bmesh.new()   # 创建空的BMesh
bm.from_mesh(me)   # 从Mesh填充它

# 修改BMesh，可以在这里做任何事情...
for v in bm.verts:
    v.co.x += 1.0

# 完成，将bmesh写回网格
bm.to_mesh(me)
bm.free()  # 释放并防止进一步访问
```

## 独立模块

BMesh模块被编写为独立的，除了用于顶点位置和法线的mathutils。唯一的其他例外是在将网格数据与bpy.types.Mesh之间转换时。

## 网格访问

有两种方式访问BMesh数据，您可以通过转换来自bpy.types.BlendData.meshes的网格来创建新的BMesh，或者通过访问当前的编辑模式网格。请参见：bmesh.types.BMesh.from_mesh和bmesh.from_edit_mesh。

当明确从网格数据转换时，Python拥有数据，这意味着网格只在Python持有对它的引用时存在。脚本负责在编辑完成后将其放回网格数据块中。

请注意，与bpy不同，BMesh不一定对应于当前打开的blend文件中的数据，BMesh可以在用户从未看到或访问过的情况下创建、编辑和释放。与编辑模式不同，BMesh模块可以同时使用多个BMesh实例。

在处理多个BMesh实例时要小心，因为网格数据可能使用大量内存。虽然Python脚本拥有的网格在脚本不持有对它的引用时会被释放，但调用bmesh.types.BMesh.free是好的做法，这将立即删除所有网格数据并禁用进一步访问。

## 编辑模式镶嵌

在编写操作编辑模式数据的脚本时，您通常希望在运行脚本后重新计算镶嵌，这需要明确调用。BMesh本身不存储三角化面，而是存储在bpy.types.Mesh中，要刷新镶嵌三角形，请调用bpy.types.Mesh.calc_loop_triangles。

## 自定义数据访问

BMesh有一种统一的方式来访问网格属性，如UV、顶点颜色、形状键、边折痕等。这是通过在BMesh数据序列上有一个layers属性来访问自定义数据层，然后可以用来访问每个顶点、边、面或循环上的实际数据。

以下是一些示例：

```python
uv_lay = bm.loops.layers.uv.active

for face in bm.faces:
    for loop in face.loops:
        uv = loop[uv_lay].uv
        print("循环UV: %f, %f" % uv[:])
        vert = loop.vert
        print("循环顶点: (%f,%f,%f)" % vert.co[:])

shape_lay = bm.verts.layers.shape["Key.001"]

for vert in bm.verts:
    shape = vert[shape_lay]
    print("顶点形状: %f, %f, %f" % (shape.x, shape.y, shape.z))

# 在此示例中使用活动顶点组索引，
# 这存储在对象中，而不是BMesh中
group_index = obj.vertex_groups.active_index

# 只有一个变形权重层
dvert_lay = bm.verts.layers.deform.active

for vert in bm.verts:
    dvert = vert[dvert_lay]

    if group_index in dvert:
        print("权重 %f" % dvert[group_index])
    else:
        print("设置权重")
        dvert[group_index] = 0.5
```

## 保持正确状态

在Blender中建模时，对网格状态有某些假设：

- 隐藏的几何体未被选中
- 当边被选中时，其顶点也被选中
- 当面被选中时，其边和顶点也被选中
- 重复的边/面不存在
- 面至少有三个顶点

为了给开发者灵活性，这些约定不被强制执行，但工具必须让网格处于有效状态，否则其他工具可能行为不正确。任何因不遵循这些约定而产生的错误都被认为是脚本中的错误，而不是Blender中的错误。

## 选择/刷新

如上所述，可能创建无效的选择状态（例如通过选择面然后取消选择其顶点之一），大多数情况下解决这个问题的最佳方法是在执行一系列编辑后刷新选择。这验证选择状态。

## 模块函数

### 子模块

- **BMesh操作符 (bmesh.ops)**
- **BMesh类型 (bmesh.types)**
- **BMesh工具 (bmesh.utils)**
- **BMesh几何工具 (bmesh.geometry)**

### bmesh.from_edit_mesh(mesh)

从此网格返回BMesh，当前网格必须已经在编辑模式中。

**参数：**
- `mesh` (bpy.types.Mesh) – 编辑模式网格

**返回：**
与此网格关联的BMesh

**返回类型：**
bmesh.types.BMesh

### bmesh.new(use_operators=True)

**参数：**
- `use_operators` (布尔值) – 支持在bmesh.ops中调用操作符（每个顶点/边/面使用一些额外内存）

**返回：**
返回新的、空的BMesh

**返回类型：**
bmesh.types.BMesh

### bmesh.update_edit_mesh(mesh, loop_triangles=True, destructive=True)

在编辑模式中对BMesh进行更改后更新网格，可选择重新计算n边形镶嵌。

**参数：**
- `mesh` (bpy.types.Mesh) – 编辑模式网格
- `loop_triangles` (布尔值) – 重新计算n边形镶嵌的选项
- `destructive` (布尔值) – 在几何体已添加或删除时使用 
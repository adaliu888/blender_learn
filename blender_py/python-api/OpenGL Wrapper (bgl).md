                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                # OpenGL Wrapper (bgl)

## 警告

此模块已被弃用，将在未来版本中移除，届时OpenGL将被Metal和Vulkan替代。请使用与图形API无关的gpu模块代替。

此模块封装了OpenGL常量和函数，使它们可以在Blender Python中使用。

完整列表可以通过列出模块内容来获取：`dir(bgl)`。在网络上进行简单搜索可以找到足够多的材料来教授OpenGL编程，从书籍到许多教程集合。

以下是一份综合书籍列表（非免费）。Learn OpenGL是学习现代OpenGL的最佳资源之一，opengl-tutorial.org提供了一套广泛的示例，包括高级功能。

## 注意

您可以使用`bpy.types.Image`类型来加载和设置纹理。例如，参见`bpy.types.Image.gl_load`和`bpy.types.Image.gl_free`。

## 函数参考

### glBindTexture(target, texture)
将命名纹理绑定到纹理目标

**参数：**
- `target` (枚举常量) – 指定纹理绑定的目标
- `texture` (无符号整数) – 指定纹理的名称

### glBlendFunc(sfactor, dfactor)
指定像素算术

**参数：**
- `sfactor` (枚举常量) – 指定如何计算红色、绿色、蓝色和alpha源混合因子
- `dfactor` (枚举常量) – 指定如何计算红色、绿色、蓝色和alpha目标混合因子

### glClear(mask)
将缓冲区清除为预设值

**参数：**
- `mask` (枚举常量) – 指示要清除的缓冲区的掩码的按位OR

### glClearColor(red, green, blue, alpha)
指定颜色缓冲区的清除值

**参数：**
- `red, green, blue, alpha` – 指定颜色缓冲区被清除时使用的红色、绿色、蓝色和alpha值。初始值都为0

### glClearDepth(depth)
指定深度缓冲区的清除值

**参数：**
- `depth` (整数) – 指定深度缓冲区被清除时使用的深度值。初始值为1

### glClearStencil(s)
指定模板缓冲区的清除值

**参数：**
- `s` (整数) – 指定模板缓冲区被清除时使用的索引。初始值为0

### glClipPlane(plane, equation)
指定一个平面，所有几何体都相对于该平面进行裁剪

**参数：**
- `plane` (枚举常量) – 指定正在定位的裁剪平面
- `equation` (bgl.Buffer对象，类型GL_FLOAT) – 指定四个双精度浮点值数组的地址。这些值被解释为平面方程

### glColorMask(red, green, blue, alpha)
启用和禁用帧缓冲区颜色分量的写入

**参数：**
- `red, green, blue, alpha` – 指定红色、绿色、蓝色和alpha是否可以写入帧缓冲区。初始值都为GL_TRUE，表示颜色分量可以写入

### glCopyTexImage2D(target, level, internalformat, x, y, width, height, border)
将像素复制到2D纹理图像中

**参数：**
- `target` (枚举常量) – 指定目标纹理
- `level` (整数) – 指定细节层次编号。级别0是基础图像级别。级别n是第n个mipmap缩减图像
- `internalformat` (整数) – 指定纹理中的颜色分量数量
- `x, y` – 指定从帧缓冲区复制的第一个像素的窗口坐标。此位置是像素矩形块的左下角
- `width` (整数) – 指定纹理图像的宽度。必须是2^n+2(border)的形式，其中n为某个整数。所有实现都支持至少64个纹素宽的纹理图像
- `height` (整数) – 指定纹理图像的高度。必须是2^m+2(border)的形式，其中m为某个整数。所有实现都支持至少64个纹素高的纹理图像
- `border` (整数) – 指定边框宽度。必须为0或1

### glCullFace(mode)
指定是否可以剔除正面或背面面片

**参数：**
- `mode` (枚举常量) – 指定正面或背面面片是否为剔除候选

### glDeleteTextures(n, textures)
删除命名纹理

**参数：**
- `n` (整数) – 指定要删除的纹理数量
- `textures` (bgl.Buffer GL_INT) – 指定要删除的纹理数组

### glDepthFunc(func)
指定用于深度缓冲区比较的值

**参数：**
- `func` (枚举常量) – 指定深度比较函数

### glDepthMask(flag)
启用或禁用深度缓冲区的写入

**参数：**
- `flag` (整数(布尔值)) – 指定是否启用深度缓冲区的写入。如果flag为GL_FALSE，则禁用深度缓冲区写入。否则启用。初始时，深度缓冲区写入是启用的

### glDepthRange(zNear, zFar)
指定从标准化设备坐标到窗口坐标的深度值映射

**参数：**
- `zNear` (整数) – 指定近裁剪平面到窗口坐标的映射。初始值为0
- `zFar` (整数) – 指定远裁剪平面到窗口坐标的映射。初始值为1

### glDisable(cap)
禁用服务器端GL功能

**参数：**
- `cap` (枚举常量) – 指定表示GL功能的符号常量

### glDrawBuffer(mode)
指定要绘制到的颜色缓冲区

**参数：**
- `mode` (枚举常量) – 指定要绘制到的最多四个颜色缓冲区

### glEdgeFlag(flag)
将边标记为边界或非边界

**参数：**
- `flag` (取决于函数原型) – 指定当前边标志值。初始值为GL_TRUE

### glEnable(cap)
启用服务器端GL功能

**参数：**
- `cap` (枚举常量) – 指定表示GL功能的符号常量

### glEvalCoord(u, v)
计算启用的一维和二维映射

**参数：**
- `u` (取决于函数原型) – 指定一个值，该值是域坐标u到在之前的glMap1或glMap2命令中定义的基础函数。如果函数原型以'v'结尾，则u指定指向包含一个或两个域坐标的数组的指针。第一个坐标是u。第二个坐标是v，仅在glEvalCoord2版本中存在
- `v` (取决于函数原型(仅限'2'原型)) – 指定一个值，该值是域坐标v到在之前的glMap2命令中定义的基础函数。此参数在glEvalCoord1命令中不存在

### glEvalMesh(mode, i1, i2)
计算一维或二维点或线网格

**参数：**
- `mode` (枚举常量) – 在glEvalMesh1中，指定是否计算一维点或线网格
- `i1, i2` – 为网格域变量i指定第一个和最后一个整数值

### glEvalPoint(i, j)
在网格中生成和计算单个点

**参数：**
- `i` (整数) – 为网格域变量i指定整数值
- `j` (整数(仅限'2'原型)) – 为网格域变量j指定整数值(仅限glEvalPoint2)

### glFeedbackBuffer(size, type, buffer)
控制反馈模式

**参数：**
- `size` (整数) – 指定可以写入缓冲区的最大值的数量
- `type` (枚举常量) – 指定描述将为每个顶点返回的信息的符号常量
- `buffer` (bgl.Buffer对象 GL_FLOAT) – 返回反馈数据

### glFinish()
阻塞直到所有GL执行完成

### glFlush()
强制在有限时间内执行GL命令

### glFog(pname, param)
指定雾参数

**参数：**
- `pname` (枚举常量) – 指定单值雾参数。如果函数原型以'v'结尾，则指定雾参数
- `param` (取决于函数原型) – 指定要分配给pname的值或值。GL_FOG_COLOR需要四个值的数组。所有其他参数接受仅包含单个值的数组

### glFrontFace(mode)
定义正面和背面多边形

**参数：**
- `mode` (枚举常量) – 指定正面多边形的方向

### glGenTextures(n, textures)
生成纹理名称

**参数：**
- `n` (整数) – 指定要生成的纹理名称数量
- `textures` (bgl.Buffer对象，类型GL_INT) – 指定存储生成的纹理名称的数组

### glGet(pname, param)
返回选定参数的值或值

**参数：**
- `pname` (枚举常量) – 指定要返回的参数值
- `param` (取决于函数原型) – 返回指定参数的值或值

### glGetError()
返回错误信息

### glGetLight(light, pname, params)
返回光源参数值

**参数：**
- `light` (枚举常量) – 指定光源。可能的灯光数量取决于实现，但至少支持八个灯光。它们由形式为GL_LIGHTi的符号名称标识，其中0 < i < GL_MAX_LIGHTS
- `pname` (枚举常量) – 为light指定光源参数
- `params` (bgl.Buffer对象，取决于函数原型) – 返回请求的数据

### glGetMap(target, query, v)
返回计算器参数

**参数：**
- `target` (枚举常量) – 指定映射的符号名称
- `query` (枚举常量) – 指定要返回的参数
- `v` (bgl.Buffer对象，取决于函数原型) – 返回请求的数据

### glGetMaterial(face, pname, params)
返回材质参数

**参数：**
- `face` (枚举常量) – 指定正在查询的两个材质中的哪一个，分别表示正面和背面材质
- `pname` (枚举常量) – 指定要返回的材质参数
- `params` (bgl.Buffer对象，取决于函数原型) – 返回请求的数据

### glGetPixelMap(map, values)
返回指定的像素映射

**参数：**
- `map` (枚举常量) – 指定要返回的像素映射的名称
- `values` (bgl.Buffer对象，取决于函数原型) – 返回像素映射内容

### glGetString(name)
返回描述当前GL连接的字符串

**参数：**
- `name` (枚举常量) – 指定符号常量

### glGetTexEnv(target, pname, params)
返回纹理环境参数

**参数：**
- `target` (枚举常量) – 指定纹理环境。必须为GL_TEXTURE_ENV
- `pname` (枚举常量) – 指定纹理环境参数的符号名称
- `params` (bgl.Buffer对象，取决于函数原型) – 返回请求的数据

### glGetTexGen(coord, pname, params)
返回纹理坐标生成参数

**参数：**
- `coord` (枚举常量) – 指定纹理坐标
- `pname` (枚举常量) – 指定要返回的值的符号名称
- `params` (bgl.Buffer对象，取决于函数原型) – 返回请求的数据

### glGetTexImage(target, level, format, type, pixels)
返回纹理图像

**参数：**
- `target` (枚举常量) – 指定要获取的纹理
- `level` (整数) – 指定所需图像的细节层次编号。级别0是基础图像级别。级别n是第n个mipmap缩减图像
- `format` (枚举常量) – 为返回的数据指定像素格式
- `type` (枚举常量) – 为返回的数据指定像素类型
- `pixels` (bgl.Buffer对象) – 返回纹理图像。应该是指向由type指定的类型数组的指针

### glGetTexLevelParameter(target, level, pname, params)
返回特定细节层次的纹理参数值

**参数：**
- `target` (枚举常量) – 指定目标纹理的符号名称
- `level` (整数) – 指定所需图像的细节层次编号。级别0是基础图像级别。级别n是第n个mipmap缩减图像
- `pname` (枚举常量) – 指定纹理参数的符号名称
- `params` (bgl.Buffer对象，取决于函数原型) – 返回请求的数据

### glGetTexParameter(target, pname, params)
返回纹理参数值

**参数：**
- `target` (枚举常量) – 指定目标纹理的符号名称
- `pname` (枚举常量) – 指定目标纹理的符号名称
- `params` (bgl.Buffer对象，取决于函数原型) – 返回纹理参数

### glHint(target, mode)
指定实现特定的提示

**参数：**
- `target` (枚举常量) – 指定指示要控制的行为的符号常量
- `mode` (枚举常量) – 指定指示所需行为的符号常量

### glIsEnabled(cap)
测试功能是否启用

**参数：**
- `cap` (枚举常量) – 指定表示GL功能的常量

### glIsTexture(texture)
确定名称是否对应于纹理

**参数：**
- `texture` (无符号整数) – 指定可能是纹理名称的值

### glLight(light, pname, param)
设置光源参数

**参数：**
- `light` (枚举常量) – 指定光源。灯光数量取决于实现，但至少支持八个灯光。它们由形式为GL_LIGHTi的符号名称标识，其中0 < i < GL_MAX_LIGHTS
- `pname` (枚举常量) – 为light指定单值光源参数
- `param` (取决于函数原型) – 指定光源light的参数pname将设置的值。如果函数原型以'v'结尾，则指定指向参数pname将设置的值或值的指针

### glLightModel(pname, param)
设置光照模型参数

**参数：**
- `pname` (枚举常量) – 指定单值光照模型参数
- `param` (取决于函数原型) – 指定param将设置的值。如果函数原型以'v'结尾，则指定指向param将设置的值或值的指针

### glLineWidth(width)
指定光栅化线的宽度

**参数：**
- `width` (浮点数) – 指定光栅化线的宽度。初始值为1

### glLoadMatrix(m)
用指定矩阵替换当前矩阵

**参数：**
- `m` (bgl.Buffer对象，取决于函数原型) – 指定指向16个连续值的指针，这些值用作4x4列主矩阵的元素

### glLogicOp(opcode)
为颜色索引渲染指定逻辑像素操作

**参数：**
- `opcode` (枚举常量) – 指定选择逻辑操作的符号常量

### glMap1(target, u1, u2, stride, order, points)
定义一维计算器

**参数：**
- `target` (枚举常量) – 指定由计算器生成的值的类型
- `u1, u2` – 指定u的线性映射，如呈现给glEvalCoord1，到由该命令指定的方程计算的变量
- `stride` (整数) – 指定数据结构中一个控制点开始与下一个控制点开始之间的浮点数或双精度浮点数。这允许控制点嵌入任意数据结构中。唯一的约束是特定控制点的值必须占据连续的内存位置
- `order` (整数) – 指定控制点数量。必须为正数
- `points` (bgl.Buffer对象，取决于函数原型) – 指定指向控制点数组的指针

### glMap2(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)
定义二维计算器

**参数：**
- `target` (枚举常量) – 指定由计算器生成的值的类型
- `u1, u2` – 指定u的线性映射，如呈现给glEvalCoord2，到由该命令指定的方程计算的变量。初始时u1为0，u2为1
- `ustride` (整数) – 指定控制点R开始与控制点R ij开始之间的浮点数或双精度浮点数，其中i和j分别是u和v控制点索引。这允许控制点嵌入任意数据结构中。唯一的约束是特定控制点的值必须占据连续的内存位置。ustride的初始值为0
- `uorder` (整数) – 指定u轴控制点数组的维度。必须为正数。初始值为1
- `v1, v2` – 指定v的线性映射，如呈现给glEvalCoord2，到由该命令指定的方程计算的两个变量之一。初始时，v1为0，v2为1
- `vstride` (整数) – 指定控制点R开始与控制点R ij开始之间的浮点数或双精度浮点数，其中i和j分别是u和v控制点索引。这允许控制点嵌入任意数据结构中。唯一的约束是特定控制点的值必须占据连续的内存位置。vstride的初始值为0
- `vorder` (整数) – 指定v轴控制点数组的维度。必须为正数。初始值为1
- `points` (bgl.Buffer对象，取决于函数原型) – 指定指向控制点数组的指针

### glMapGrid(un, u1, u2, vn, v1, v2)
定义一维或二维网格

**参数：**
- `un` (整数) – 指定网格范围间隔[u1, u2]中的分区数量。必须为正数
- `u1, u2` – 为整数网格域值i=0和i=un指定映射
- `vn` (整数) – 指定网格范围间隔[v1, v2]中的分区数量(仅限glMapGrid2)
- `v1, v2` – 为整数网格域值j=0和j=vn指定映射(仅限glMapGrid2)

### glMaterial(face, pname, params)
为光照模型指定材质参数

**参数：**
- `face` (枚举常量) – 指定正在更新的面或面。必须为以下之一：
- `pname` (枚举常量) – 指定正在更新的面或面的单值材质参数。必须为GL_SHININESS
- `params` (整数) – 指定参数GL_SHININESS将设置的值。如果函数原型以'v'结尾，则指定指向pname将设置的值或值的指针

### glMultMatrix(m)
将当前矩阵与指定矩阵相乘

**参数：**
- `m` (bgl.Buffer对象，取决于函数原型) – 指向16个连续值，这些值用作4x4列主矩阵的元素

### glNormal3(nx, ny, nz, v)
设置当前法向量

**参数：**
- `nx, ny, nz` – 指定新当前法向量的x、y和z坐标。当前法向量的初始值是单位向量(0, 0, 1)
- `v` (bgl.Buffer对象，取决于函数原型('v'原型)) – 指定指向三个元素数组的指针：新当前法向量的x、y和z坐标

### glPixelMap(map, mapsize, values)
设置像素传输映射

**参数：**
- `map` (枚举常量) – 指定符号映射名称
- `mapsize` (整数) – 指定正在定义的映射大小
- `values` (bgl.Buffer对象，取决于函数原型) – 指定mapsize值的数组

### glPixelStore(pname, param)
设置像素存储模式

**参数：**
- `pname` (枚举常量) – 指定要设置的参数的符号名称。六个值影响像素数据到内存的打包。另外六个影响像素数据从内存的解包
- `param` (取决于函数原型) – 指定pname设置的值

### glPixelTransfer(pname, param)
设置像素传输模式

**参数：**
- `pname` (枚举常量) – 指定要设置的像素传输参数的符号名称
- `param` (取决于函数原型) – 指定pname设置的值

### glPointSize(size)
指定光栅化点的直径

**参数：**
- `size` (浮点数) – 指定光栅化点的直径。初始值为1

### glPolygonMode(face, mode)
选择多边形光栅化模式

**参数：**
- `face` (枚举常量) – 指定mode应用的多边形。对于正面多边形必须为GL_FRONT，对于背面多边形必须为GL_BACK，对于正面和背面多边形必须为GL_FRONT_AND_BACK
- `mode` (枚举常量) – 指定多边形将如何光栅化。正面和背面多边形的初始值都是GL_FILL

### glPolygonOffset(factor, units)
设置用于计算深度值的比例和单位

**参数：**
- `factor` (浮点数) – 指定用于为每个多边形创建可变深度偏移的比例因子。初始值为0
- `units` (浮点数) – 乘以实现特定的值以创建恒定深度偏移。初始值为0

### glRasterPos(x, y, z, w)
为像素操作指定光栅位置

**参数：**
- `x, y, z, w` – 为光栅位置指定x、y、z和w对象坐标(如果存在)。如果函数原型以'v'结尾，则指定指向两个、三个或四个元素数组的指针，分别指定x、y、z和w坐标

**注意：**
如果您使用空间处理程序的Scriptlink绘制到3D视图，面板的缩放级别将按视图矩阵缩放glRasterPos。因此，X为10不会总是按预期偏移10个像素。

要解决此问题，请获取视图矩阵的缩放值并使用它来缩放像素值。

```python
import bgl
xval, yval = 100, 40
# 获取视图矩阵的缩放值
view_matrix = bgl.Buffer(bgl.GL_FLOAT, 16)
bgl.glGetFloatv(bgl.GL_MODELVIEW_MATRIX, view_matrix)
f = 1.0 / view_matrix[0]

# 而不是通常的glRasterPos2i(xval, yval)
bgl.glRasterPos2f(xval * f, yval * f)
```

### glReadBuffer(mode)
选择像素的颜色缓冲区源

**参数：**
- `mode` (枚举常量) – 指定颜色缓冲区

### glReadPixels(x, y, width, height, format, type, pixels)
从帧缓冲区读取像素块

**参数：**
- `x, y` – 指定从帧缓冲区读取的第一个像素的窗口坐标。此位置是像素矩形的左下角
- `width, height` – 指定像素矩形的尺寸。宽度和高度为1对应于单个像素
- `format` (枚举常量) – 指定像素数据的格式
- `type` (枚举常量) – 指定像素数据的类型
- `pixels` (bgl.Buffer对象) – 返回像素数据

### glRect(x1, y1, x2, y2, v1, v2)
绘制矩形

**参数：**
- `x1, y1` – 指定矩形的一个顶点
- `x2, y2` – 指定矩形的相对顶点
- `v1, v2` – 指定指向矩形一个顶点的指针和指向矩形相对顶点的指针

### glRotate(angle, x, y, z)
将当前矩阵与旋转矩阵相乘

**参数：**
- `angle` (取决于函数原型) – 以度为单位指定旋转角度
- `x, y, z` – 分别指定向量的x、y和z坐标

### glScale(x, y, z)
将当前矩阵与一般缩放矩阵相乘

**参数：**
- `x, y, z` – 分别指定沿x、y和z轴的缩放因子

### glScissor(x, y, width, height)
定义裁剪框

**参数：**
- `x, y` – 指定裁剪框的左下角。初始为(0, 0)
- `width, height` – 指定裁剪框的宽度和高度。当GL上下文首次附加到窗口时，宽度和高度设置为该窗口的尺寸

### glStencilFunc(func, ref, mask)
设置模板测试的函数和参考值

**参数：**
- `func` (枚举常量) – 指定测试函数
- `ref` (整数) – 为模板测试指定参考值。ref被限制在范围[0,2^n-1]内，其中n是模板缓冲区中的位平面数。初始值为0
- `mask` (无符号整数) – 指定在测试完成时与参考值和存储的模板值进行AND运算的掩码。初始值全为1

### glStencilMask(mask)
控制模板平面中各个位的写入

**参数：**
- `mask` (无符号整数) – 指定位掩码以启用和禁用模板平面中各个位的写入。初始时，掩码全为1

### glStencilOp(fail, zfail, zpass)
设置模板测试操作

**参数：**
- `fail` (枚举常量) – 指定模板测试失败时要采取的操作。初始值为GL_KEEP
- `zfail` (枚举常量) – 指定模板测试通过但深度测试失败时的模板操作。zfail接受与fail相同的符号常量。初始值为GL_KEEP
- `zpass` (枚举常量) – 指定模板测试和深度测试都通过，或模板测试通过且没有深度缓冲区或深度测试未启用时的模板操作。zpass接受与fail相同的符号常量。初始值为GL_KEEP

### glTexCoord(s, t, r, q, v)
设置当前纹理坐标

**参数：**
- `s, t, r, q` – 指定s、t、r和q纹理坐标。并非所有参数都存在于命令的所有形式中
- `v` (bgl.Buffer对象，取决于函数原型(仅限'v'原型)) – 指定指向一个、两个、三个或四个元素数组的指针，这些元素依次指定s、t、r和q纹理坐标

### glTexEnv(target, pname, param)
设置纹理环境参数

**参数：**
- `target` (枚举常量) – 指定纹理环境。必须为GL_TEXTURE_ENV
- `pname` (枚举常量) – 指定单值纹理环境参数的符号名称。必须为GL_TEXTURE_ENV_MODE
- `param` (取决于函数原型) – 指定单个符号常量。如果函数原型以'v'结尾，则指定包含单个符号常量或RGBA颜色的参数数组的指针

### glTexGen(coord, pname, param)
控制纹理坐标的生成

**参数：**
- `coord` (枚举常量) – 指定纹理坐标
- `pname` (枚举常量) – 指定纹理坐标生成函数的符号名称
- `param` (取决于函数原型) – 指定单值纹理生成参数。如果函数原型以'v'结尾，则指定指向纹理生成参数数组的指针。如果pname是GL_TEXTURE_GEN_MODE，则数组必须包含单个符号常量。否则，params保存由pname指定的纹理坐标生成函数的系数

### glTexImage1D(target, level, internalformat, width, border, format, type, pixels)
指定一维纹理图像

**参数：**
- `target` (枚举常量) – 指定目标纹理
- `level` (整数) – 指定细节层次编号。级别0是基础图像级别。级别n是第n个mipmap缩减图像
- `internalformat` (整数) – 指定纹理中的颜色分量数量
- `width` (整数) – 指定纹理图像的宽度。必须是2^n+2(border)的形式，其中n为某个整数。所有实现都支持至少64个纹素宽的纹理图像。1D纹理图像的高度为1
- `border` (整数) – 指定边框宽度。必须为0或1
- `format` (枚举常量) – 指定像素数据的格式
- `type` (枚举常量) – 指定像素数据的类型
- `pixels` (bgl.Buffer对象) – 指定内存中图像数据的指针

### glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)
指定二维纹理图像

**参数：**
- `target` (枚举常量) – 指定目标纹理
- `level` (整数) – 指定细节层次编号。级别0是基础图像级别。级别n是第n个mipmap缩减图像
- `internalformat` (整数) – 指定纹理中的颜色分量数量
- `width` (整数) – 指定纹理图像的宽度。必须是2^n+2(border)的形式，其中n为某个整数。所有实现都支持至少64个纹素宽的纹理图像
- `height` (整数) – 指定纹理图像的高度。必须是2^m+2(border)的形式，其中m为某个整数。所有实现都支持至少64个纹素高的纹理图像
- `border` (整数) – 指定边框宽度。必须为0或1
- `format` (枚举常量) – 指定像素数据的格式
- `type` (枚举常量) – 指定像素数据的类型
- `pixels` (bgl.Buffer对象) – 指定内存中图像数据的指针

### glTexParameter(target, pname, param)
设置纹理参数

**参数：**
- `target` (枚举常量) – 指定目标纹理
- `pname` (枚举常量) – 指定单值纹理参数的符号名称
- `param` (取决于函数原型) – 指定pname的值。如果函数原型以'v'结尾，则指定指向存储pname值或值的数组的指针

### glTranslate(x, y, z)
将当前矩阵与平移矩阵相乘

**参数：**
- `x, y, z` – 指定平移向量的x、y和z坐标

### glViewport(x, y, width, height)
设置视口

**参数：**
- `x, y` – 以像素为单位指定视口矩形的左下角。初始值为(0,0)
- `width, height` – 指定视口的宽度和高度。当GL上下文首次附加到窗口时，宽度和高度设置为该窗口的尺寸

### glUseProgram(program)
将程序对象安装为当前渲染状态的一部分

**参数：**
- `program` (整数) – 指定其可执行文件将用作当前渲染状态一部分的程序对象的句柄

### glValidateProgram(program)
验证程序对象

**参数：**
- `program` (整数) – 指定要验证的程序对象的句柄

### glLinkProgram(program)
链接程序对象

**参数：**
- `program` (整数) – 指定要链接的程序对象的句柄

### glActiveTexture(texture)
选择活动纹理单元

**参数：**
- `texture` (整数) – GL_TEXTURE0中的常量 0 - 8

### glAttachShader(program, shader)
将着色器对象附加到程序对象

**参数：**
- `program` (整数) – 指定着色器对象将附加到的程序对象
- `shader` (整数) – 指定要附加的着色器对象

### glCompileShader(shader)
编译着色器对象

**参数：**
- `shader` (整数) – 指定要编译的着色器对象

### glCreateProgram()
创建程序对象

**返回类型：** 整数

**返回：** 新程序或如果发生错误则为零

### glCreateShader(shaderType)
创建着色器对象

**参数：**
- `shaderType` (指定要创建的着色器类型。必须为GL_VERTEX_SHADER、GL_TESS_CONTROL_SHADER、GL_TESS_EVALUATION_SHADER、GL_GEOMETRY_SHADER或GL_FRAGMENT_SHADER之一)

**返回类型：** 整数

**返回：** 如果发生错误则为0

### glDeleteProgram(program)
删除程序对象

**参数：**
- `program` (整数) – 指定要删除的程序对象

### glDeleteShader(shader)
删除着色器对象

**参数：**
- `shader` (整数) – 指定要删除的着色器对象

### glDetachShader(program, shader)
从附加的程序对象中分离着色器对象

**参数：**
- `program` (整数) – 指定要从中分离着色器对象的程序对象
- `shader` (整数) – 指定要从其分离着色器对象的程序对象

### glGetAttachedShaders(program, maxCount, count, shaders)
返回附加到程序对象的着色器对象的句柄

**参数：**
- `program` (整数) – 指定要查询的程序对象
- `maxCount` (整数) – 指定用于存储返回对象名称的数组大小
- `count` (bgl.Buffer整数缓冲区) – 返回实际在objects中返回的名称数量
- `shaders` (bgl.Buffer整数缓冲区) – 指定用于返回附加着色器对象名称的数组

### glGetProgramInfoLog(program, maxLength, length, infoLog)
返回程序对象的信息日志

**参数：**
- `program` (整数) – 指定要查询其信息日志的程序对象
- `maxLength` (整数) – 指定用于存储返回信息日志的字符缓冲区大小
- `length` (bgl.Buffer整数缓冲区) – 返回infoLog中返回的字符串长度(不包括空终止符)
- `infoLog` (bgl.Buffer字符缓冲区) – 指定用于返回信息日志的字符数组

### glGetShaderInfoLog(program, maxLength, length, infoLog)
返回着色器对象的信息日志

**参数：**
- `shader` (整数) – 指定要查询其信息日志的着色器对象
- `maxLength` (整数) – 指定用于存储返回信息日志的字符缓冲区大小
- `length` (bgl.Buffer整数缓冲区) – 返回infoLog中返回的字符串长度(不包括空终止符)
- `infoLog` (bgl.Buffer字符缓冲区) – 指定用于返回信息日志的字符数组

### glGetProgramiv(program, pname, params)
从程序对象返回参数

**参数：**
- `program` (整数) – 指定要查询的程序对象
- `pname` (整数) – 指定对象参数
- `params` (bgl.Buffer整数缓冲区) – 返回请求的对象参数

### glIsShader(shader)
确定名称是否对应于着色器对象

**参数：**
- `shader` (整数) – 指定潜在的着色器对象

### glIsProgram(program)
确定名称是否对应于程序对象

**参数：**
- `program` (整数) – 指定潜在的程序对象

### glGetShaderSource(shader, bufSize, length, source)
从着色器对象返回源代码字符串

**参数：**
- `shader` (整数) – 指定要查询的着色器对象
- `bufSize` (整数) – 指定用于存储返回源代码字符串的字符缓冲区大小
- `length` (bgl.Buffer整数缓冲区) – 返回source中返回的字符串长度(不包括空终止符)
- `source` (bgl.Buffer字符) – 指定用于返回源代码字符串的字符数组

### glShaderSource(shader, shader_string)
替换着色器对象中的源代码

**参数：**
- `shader` (整数) – 指定其源代码将被替换的着色器对象的句柄
- `shader_string` (字符串) – 着色器字符串

## bgl.Buffer类

Buffer对象只是用户划定和初始化的内存块。许多OpenGL函数将数据返回到C风格指针，但由于这在python中不可能，因此可以使用Buffer对象来实现此目的。在OpenGL函数中使用指针表示法的地方，可以在其bgl包装器中使用Buffer对象。在某些情况下，Buffer对象需要用模板参数初始化，而在其他情况下，用户可能只想创建一个空白缓冲区，默认情况下会清零。

```python
import bgl

myByteBuffer = bgl.Buffer(bgl.GL_BYTE, [32, 32])
bgl.glGetPolygonStipple(myByteBuffer)

print(myByteBuffer.dimensions)
print(myByteBuffer.to_list())

sliceBuffer = myByteBuffer[0:16]
print(sliceBuffer)
```

### dimensions
缓冲区的维度数

### to_list()
缓冲区内容作为python列表

### __init__(type, dimensions, template = None)
这将创建一个新的Buffer对象，用于其他bgl OpenGL命令。只需要存储数据的参数类型和缓冲区维度。除非提供模板，否则缓冲区默认清零，在这种情况下，缓冲区将初始化为模板。

**参数：**
- `type` (整数) – 存储数据的格式。类型应该是GL_BYTE、GL_SHORT、GL_INT或GL_FLOAT之一
- `dimensions` (指定缓冲区维度的整数或序列对象) – 如果维度指定为整数，将为缓冲区创建线性数组。如果为维度传递序列，缓冲区变为n维，其中n等于序列中传递的参数数量。示例：[256,2]是二维缓冲区，而[256,256,4]创建三维缓冲区。您可以将每个附加维度视为左侧维度的子项。即[10,2]是10个元素的数组，每个都有2个子项。[(0,0), (0,1), (1,0), (1,1), (2,0), …]等
- `template` (python序列对象(可选)) – 匹配维度的序列，将用于初始化缓冲区。如果不传入模板，所有字段将初始化为0

**返回类型：** Buffer对象

**返回：** 新创建的缓冲区作为PyObject 
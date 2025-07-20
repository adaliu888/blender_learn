# 字体绘制 (blf)

此模块提供对Blender文本绘制函数的访问。

## Hello World 文本示例

使用blf模块的示例。对于此模块工作，我们还需要使用OpenGL包装器bgl。

```python
# 导入独立模块
import blf
import bpy

font_info = {
    "font_id": 0,
    "handler": None,
}


def init():
    """初始化函数 - 运行一次"""
    import os
    # 创建新的字体对象，使用外部ttf文件
    font_path = bpy.path.abspath('//Zeyada.ttf')
    # 存储字体索引 - 稍后使用
    if os.path.exists(font_path):
        font_info["font_id"] = blf.load(font_path)
    else:
        # 默认字体
        font_info["font_id"] = 0

    # 设置字体绘制例程每帧运行
    font_info["handler"] = bpy.types.SpaceView3D.draw_handler_add(
        draw_callback_px, (None, None), 'WINDOW', 'POST_PIXEL')


def draw_callback_px(self, context):
    """在视口中绘制"""
    # BLF绘制例程
    font_id = font_info["font_id"]
    blf.position(font_id, 2, 80, 0)
    blf.size(font_id, 50.0)
    blf.draw(font_id, "Hello World")


if __name__ == '__main__':
    init()
```

## 函数参考

### blf.aspect(fontid, aspect)
设置文本绘制的宽高比。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `aspect` (浮点数) – 用于文本绘制的宽高比

### blf.clipping(fontid, xmin, ymin, xmax, ymax)
设置裁剪，使用CLIPPING启用/禁用。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `xmin` (浮点数) – 通过这些边界裁剪绘制区域
- `ymin` (浮点数) – 通过这些边界裁剪绘制区域
- `xmax` (浮点数) – 通过这些边界裁剪绘制区域
- `ymax` (浮点数) – 通过这些边界裁剪绘制区域

### blf.color(fontid, r, g, b, a)
设置文本绘制的颜色。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `r` (浮点数) – 红色通道 0.0 - 1.0
- `g` (浮点数) – 绿色通道 0.0 - 1.0
- `b` (浮点数) – 蓝色通道 0.0 - 1.0
- `a` (浮点数) – alpha通道 0.0 - 1.0

### blf.dimensions(fontid, text)
返回文本的宽度和高度。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `text` (字符串) – 要绘制的文本

**返回：**
文本的宽度和高度

**返回类型：**
2个浮点数的元组

### blf.disable(fontid, option)
禁用选项。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `option` (整数) – ROTATION、CLIPPING、SHADOW或KERNING_DEFAULT之一

### blf.draw(fontid, text)
在当前上下文中绘制文本。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `text` (字符串) – 要绘制的文本

### blf.enable(fontid, option)
启用选项。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `option` (整数) – ROTATION、CLIPPING、SHADOW或KERNING_DEFAULT之一

### blf.load(filepath)
加载新字体。

**参数：**
- `filepath` (字符串或字节) – 字体文件路径

**返回：**
新字体的fontid，如果有错误则为-1

**返回类型：**
整数

### blf.position(fontid, x, y, z)
设置文本绘制的位置。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `x` (浮点数) – 绘制文本的X轴位置
- `y` (浮点数) – 绘制文本的Y轴位置
- `z` (浮点数) – 绘制文本的Z轴位置

### blf.rotation(fontid, angle)
设置文本旋转角度，使用ROTATION启用/禁用。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `angle` (浮点数) – 用于文本绘制的角度

### blf.shadow(fontid, level, r, g, b, a)
阴影选项，使用SHADOW启用/禁用。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `level` (整数) – 模糊级别，可以是3、5或0
- `r` (浮点数) – 阴影颜色（红色通道 0.0 - 1.0）
- `g` (浮点数) – 阴影颜色（绿色通道 0.0 - 1.0）
- `b` (浮点数) – 阴影颜色（蓝色通道 0.0 - 1.0）
- `a` (浮点数) – 阴影颜色（alpha通道 0.0 - 1.0）

### blf.shadow_offset(fontid, x, y)
设置阴影文本的偏移。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `x` (浮点数) – 垂直阴影偏移值（像素）
- `y` (浮点数) – 水平阴影偏移值（像素）

### blf.size(fontid, size)
设置文本绘制的大小。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `size` (浮点数) – 字体的点大小

### blf.unload(filepath)
卸载现有字体。

**参数：**
- `filepath` (字符串或字节) – 字体文件路径

### blf.word_wrap(fontid, wrap_width)
设置换行宽度，使用WORD_WRAP启用/禁用。

**参数：**
- `fontid` (整数) – 由blf.load()返回的字体ID，默认字体使用0
- `wrap_width` (整数) – 换行的宽度（像素）

## 常量

### blf.CLIPPING
常量值 2

### blf.MONOCHROME
常量值 128

### blf.ROTATION
常量值 1

### blf.SHADOW
常量值 4

### blf.WORD_WRAP
常量值 64 
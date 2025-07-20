# Blender Python API 知识体系

## 概述
本文档系统梳理Blender与Python的集成知识，包括API接口、自动化操作、建模、动画制作、渲染等核心功能。

## 目录结构

### 1. 基础理论
- [Blender Python API 基础理论](./01-基础理论/)
  - Blender架构与Python集成原理
  - bpy模块核心概念
  - 数据流与操作模式

### 2. 核心API模块
- [bpy模块详解](./02-bpy模块/)
  - bpy.context - 上下文操作
  - bpy.data - 数据访问
  - bpy.ops - 操作接口
  - bpy.types - 类型系统

### 3. 建模自动化
- [建模操作API](./03-建模操作/)
  - 几何体创建与编辑
  - 修改器应用
  - 材质与纹理
  - 骨骼与权重

### 4. 动画制作
- [动画制作API](./04-动画制作/)
  - 关键帧操作
  - 约束系统
  - 驱动系统
  - 动画曲线编辑

### 5. 渲染与输出
- [渲染API](./05-渲染输出/)
  - 渲染引擎配置
  - 材质与光照
  - 输出格式设置
  - 批量渲染

### 6. 实用工具
- [实用工具与脚本](./06-实用工具/)
  - 常用脚本模板
  - 性能优化技巧
  - 错误处理与调试
  - 最佳实践

## 学习路径
1. 从基础理论开始，理解Blender的架构
2. 掌握bpy模块的核心API
3. 学习建模自动化操作
4. 深入动画制作技术
5. 掌握渲染与输出
6. 实践实用工具开发

## 快速开始
```python
import bpy

# 清除场景
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 创建一个立方体
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))

# 添加细分表面修改器
cube = bpy.context.active_object
subdiv = cube.modifiers.new(name="Subdivision", type='SUBSURF')
subdiv.levels = 2
```

## 注意事项
- 所有脚本都需要在Blender的Python环境中运行
- 操作前建议备份场景
- 注意内存管理和性能优化
- 遵循Blender的最佳实践 
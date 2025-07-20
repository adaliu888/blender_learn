import bpy
import math

# -------------------------------------------------
# 公用函数
# -------------------------------------------------
def create_torus(location, name):
    bpy.ops.mesh.primitive_torus_add(location=location)
    torus = bpy.context.object
    torus.name = name
    bpy.ops.object.shade_smooth()
    return torus

def clear_screen():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def rotation(obj, first=1, last=250, angle_deg=360):
    """
    为对象 obj 设置绕 X 轴旋转 angle_deg 度的关键帧动画
    first / last：起始/结束帧
    """
    angle_rad = math.radians(angle_deg)
    obj.rotation_euler = (0, 0, 0)
    obj.keyframe_insert(data_path='rotation_euler', frame=first)
    obj.rotation_euler.x = angle_rad
    obj.keyframe_insert(data_path='rotation_euler', frame=last)

# -------------------------------------------------
# 主流程
# -------------------------------------------------
def main():
    clear_screen()

    # 环面 1
    torus1 = create_torus(location=(0, 0, 0), name="Rotation1")
    rotation(torus1, first=1, last=250, angle_deg=360)

    # 环面 2
    torus2 = create_torus(location=(4, 0, 0), name="Rotation2")
    rotation(torus2, first=1, last=250, angle_deg=360)

# -------------------------------------------------
# 运行
# -------------------------------------------------
if __name__ == "__main__":
    main()
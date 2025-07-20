import bpy
import math

def create_torus(location,name):
    bpy.ops.mesh.primitive_torus_add(location = location)
    torus = bpy.context.object
    torus.name = name
    bpy.ops.object.shade_smooth()
    return torus
def clear_screen():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
def rotation(obj,first =1,last=250,PImult=2):
    PImult = PImult*math.pi
    obj.rotation_euler = (0,0,0)
    obj.keyframe_insert(data_path = 'rotation_euler',
    frame=first)
    obj.rotation_euler.x = PImult
    obj.keyframe_insert(data_path='rotation_euler',
    frame = last)
def main():
    clear_screen()
    torus1 = create_torus(location=(0,0,0),name = "Rotation1")
    rotation(torus1,1,250,2)
    torus2 = create_torus(location=(4,0,0),name = "Rotation2")
    rotation(torus2,1,250,4)
main()
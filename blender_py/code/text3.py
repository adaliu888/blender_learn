'''
TH  
Write me a blender python script to add location keyframe to all selected objects, then add a noise F-curve modifier to all Z location curves for those objects. Set the strength to 0.04 and scale to 10.  

Sure! Below is a Blender Python script that accomplishes the specified task:  
python  
Copy code 
''' 
import bpy  

def add_location_keyframe(obj):  
    obj.keyframe_insert(data_path="location", frame=bpy.context.scene.frame_current)  

def add_noise_fcurve_modifier(obj):  
    fcurve = obj.animation_data.action.fcurves.find("location", index=2)  
    modifier = fcurve.modifiers.new("NOISE")  
    modifier.strength = 0.04  
    modifier.scale = 10  

def main():  
    selected_objects = bpy.context.selected_objects  
    if not selected_objects:  
        print("No objects selected.")  
        return  
    bpy.ops.object.mode_set(mode='OBJECT')  # Switch to object mode  
    for obj in selected_objects:  
        add_location_keyframe(obj)  
        add_noise_fcurve_modifier(obj)  

if __name__ == "__main__":  
    main()
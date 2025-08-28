import argparse
import bpy

def get_args():
  parser = argparse.ArgumentParser()
 
  # get all script args
  _, all_arguments = parser.parse_known_args()
  double_dash_index = all_arguments.index('--')
  script_args = all_arguments[double_dash_index + 1: ]
 
  # add parser rules
  parser.add_argument('-f', '--file', help="filepath of gcode")
  parsed_script_args, _ = parser.parse_known_args(script_args)
  return parsed_script_args

args = get_args()


bpy.ops.wm.open_mainfile(filepath="../B4V3P.blend")

bpy.context.scene.my_tool.split_layers = False

bpy.ops.wm.gcode_import(filepath=args.file, filter_glob="*.*")

printobj = bpy.data.objects['Gcode']

printobj.select_set(True)

bpy.context.view_layer.objects.active = bpy.data.objects['Gcode']

bpy.ops.object.convert(target='CURVE')

bpy.data.curves['Gcode'].bevel_mode = 'OBJECT'

bpy.data.curves['Gcode'].bevel_object = bpy.data.objects['PROFILE']

mat = bpy.data.materials.get("PLA")

printobj.data.materials.append(mat)

bpy.context.scene.render.filepath = args.file.rsplit('.', 1)[0] + '.jpg'
bpy.ops.render.render(write_still=True)

import sys,os
from PIL import Image
#grab first and second argments
'''
    storing the output in a seperate folder
'''
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check for exists or not if no then create it
if not os.path.exists(output_folder):
  os.makedirs(output_folder)
for filename  in os.listdir(image_folder):
  img = image.open(f'{{image_folder}{filename}')
  clean_name = os.path.splitext(filename)[0]
  img.save(f'{output_folder}{clean_name}.png','png')
#completed

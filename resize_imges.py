import os
from PIL import Image


fit_size=int(input('enter size: '))
output_folder=input('enter folder name to save new images in it: ')

for file_name in os.listdir('.'):
    if not file_name.endswith(('.png','.jpg')):
        continue
    imge=Image.open(file_name)
    
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    width,hight=imge.size

    # Check if image needs to be resized 
    if width>fit_size and hight>fit_size:
        # Calculate the new width and height to resize to
        if width>hight:
            hight=int((fit_size/width)*hight)
            width=fit_size
           
        else:
            width=int((fit_size/hight)*width)
            hight=fit_size
            
        imge=imge.resize((width,hight))
        imge=imge.save(os.path.join(output_folder,file_name))
        print("resize %s..."%(file_name))

print('we are Done --^-^--')
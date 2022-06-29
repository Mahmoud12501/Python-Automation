import os
from  shutil import copy

current_dir=os.path.dirname(os.path.realpath(__file__))
# print(current_dir)

#organize docs files
count=0
for filename in os.listdir(current_dir):
    
    if filename.endswith(('.pdf','.docx','.pptx')):
        if not os.path.exists('docs'):
             os.mkdir('docs')
        copy(filename,'docs')
        os.remove(filename)
        count+=1
print(f"done you add {count} docs files")    


#organize image files
count1=0
for filename in os.listdir(current_dir):
    
    if filename.endswith(('.jpg','.png')):
        if not os.path.exists('images'):
             os.mkdir('images')
        copy(filename,'images')
        os.remove(filename)
        count1+=1
print(f"done you add {count1} images files")    

#organize media file
count2=0
for filename in os.listdir(current_dir):
    
    if filename.endswith(('.mp4','.wmv')):
        if not os.path.exists('media'):
             os.mkdir('media')
        copy(filename,'media')
        os.remove(filename)
        count2+=1
print(f"done you add {count2} media files")    

#organize archive file
count3=0
for filename in os.listdir(current_dir):
    
    if filename.endswith(('.zip')):
        if not os.path.exists('archive'):
             os.mkdir('archive')
        copy(filename,'archive')
        os.remove(filename)
        count3+=1
print(f"done you add {count3} archive files")    


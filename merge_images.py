import numpy as np
from PIL import Image
import os

rg_front_dir = 'cnh_a_cropped'
rg_back_dir = 'cnh_b_cropped'

front_imgs    = []
back_imgs = []
work_imgs = []

front_imgs_count = 0
back_imgs_count = 0

imgs_limit = 1500
work_imgs_index = 0

#Opens one back and one front image. Doctype = RG
for front_filename in os.listdir(rg_front_dir):
    
    front_image = Image.open(rg_front_dir + "/" + front_filename)
    front_imgs.append(front_image)
    print('Appending front image: ' + front_filename)
    front_imgs_count = front_imgs_count + 1

for back_filename in os.listdir(rg_back_dir):
    back_image = Image.open(rg_back_dir + "/" + back_filename)
    back_imgs.append(back_image)
    print('Appending back image: ' + back_filename)
    back_imgs_count = back_imgs_count + 1

#Gets one img from each new array
while work_imgs_index < (imgs_limit - 1):
    work_imgs = [front_imgs[work_imgs_index], back_imgs[work_imgs_index]]

    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in work_imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in work_imgs ) )

    # save that beautiful picture
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save( 'fullrg' + str(work_imgs_index)+ '.jpg' )    

    # for a vertical stacking it is simple: use vstack
    imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in work_imgs ) )
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save( 'fullrg' + str(work_imgs_index)+ 'vertical' '.jpg'  )
    work_imgs_index = work_imgs_index + 1
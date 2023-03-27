# allow us to upload pictures

import os
from PIL import Image
from flask import url_for, current_app

def add_profile_pic(pic_upload,username):

    filename = pic_upload.filename
    ext_type = filename.split('.')[-1] # ex: jpg or png
    storage_filename = str(username) + '.' + ext_type # store the pic with 'username.jpg' new filename

    filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename) # static\profile_pics is the folder name

    output_size = (200,200) # 200*200 pixels

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size) # squeeze whatever pixel into output size
    pic.save(filepath)

    return storage_filename
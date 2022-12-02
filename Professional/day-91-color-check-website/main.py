import numpy as np
from flask_uploads import UploadSet, IMAGES
from numpy.random import random
import matplotlib.pyplot as plt
import scipy
import scipy.misc
import scipy.cluster
import binascii
import struct
from PIL import Image
from flask import Flask, flash, request, redirect, url_for, render_template,send_from_directory
from werkzeug.utils import secure_filename
import os
from flask_uploads import UploadSet, IMAGES,configure_uploads
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
import extcolors
from colormap import rgb2hex
import easydev

app= Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
app.config['SECRET_KEY'] = 'secret123@'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
chosen_photo = ''

def show_img_compar(img_1, img_2 ):
    f, ax = plt.subplots(1, 2, figsize=(10,10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off') #hide the axis
    ax[1].axis('off')
    f.tight_layout()
    plt.show()

class UploadForm(FlaskForm):
    photo= FileField(validators=[
        FileAllowed(photos, 'Only images are allowed'),
        FileRequired('File field should not be empty')
    ])
    submit= SubmitField('Submit')

color_dict = {}
initial_limit = 12
total = 0
def color_extraction(image, limit, dictionary):
    global total
    img = Image.open(rf"C:\\Users\\HP\\PycharmProjects\\day-91-color-check-website{image}")
    img.show()
    resize_width = 900
    w_percent = resize_width / float(img.size[0])
    h_size = int((float(img.size[1]) * float(w_percent)))
    img2 = img.resize((resize_width, h_size))

    # Color extraction
    colors = extcolors.extract_from_image(img2, tolerance=12, limit=limit)

    colors_pre_list = str(colors).replace('([(', '').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')', '') for i in colors_pre_list]

    # convert RGB to HEX code
    df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(", "")),
                           int(i.split(", ")[1]),
                           int(i.split(", ")[2].replace(")", ""))) for i in df_rgb]
    # GEt total of occurrence
    for x in df_percent:
        total += int(x)

    # convert to dictionary
    for key in df_color_up:
        for value in df_percent:
            dictionary[key] = round(int(value) / total, 8)
            df_percent.remove(value)
            break

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/', methods = ['GET', 'POST'])
def upload_photo():
    form = UploadForm()
    empty_dict= {}
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename= filename)
        if file_url:
            color_extraction(image=file_url, limit=initial_limit,dictionary=empty_dict)
    else:
        file_url = None
    return render_template('index.html', form= form, file_url=file_url,colors = empty_dict)

# @app.route('/openphotos')
# def openphotos():
#     path = file_url
#     im = Image.open(path)
#     return im.show()

if __name__ == '__main__':
    app.run(debug=True)

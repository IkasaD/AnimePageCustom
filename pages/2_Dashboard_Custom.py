import streamlit as st
from matplotlib import image
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import plotly.express as px
import os
from PIL import ImageEnhance




FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "Resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "pir.png")  
FONT_PATH = os.path.join(dir_of_interest, "font", "BlackItalic.ttf")


img = Image.open(IMAGE_PATH)
imgo = image.imread(IMAGE_PATH)
color_enhancer = ImageEnhance.Color(img)
st.image(img, width= 500)
option = st.selectbox(
         'Change Color',
        ('Grey','Red'))

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
    title = st.text_input('Want to custom your name on the image', 'Your Name')
    st.write('Your Name is', title)
    if st.button('Submit'):
        #if option == "Blue":
            #st.image(imgo, width= 800,channels= "BGR")
        if option == "Grey" : 
            grey = color_enhancer.enhance(0)
            img1 = grey.copy()
        elif option == "Red" : 
            img1 = img.copy()
            
        
        st.success('Sucess!!!!!!', icon="✅")
        st.write('You selected:', option,':skull:')


        
        DRAW = ImageDraw.Draw(img1)
        font = ImageFont.truetype(FONT_PATH, 36)
        TEXT = title


        DRAW.text((250, 350), text=TEXT, fill=(255, 255, 255),font=font,stroke_width = 0)

        st.image(img1, width= 500)
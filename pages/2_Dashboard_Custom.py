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





    
option = st.selectbox(
         'Choose Anime',
        ('One Piece','Dragon Ball','Naruto',"Upload"))
agree = st.checkbox('I agree')
if agree:
    title = st.text_input('Want to custom your name on the image', placeholder='Your Name')
    st.write('Your Name is', title)
    if option == "One Piece":
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "pir.png")
        img = Image.open(IMAGE_PATH)
        option = st.selectbox("Choose Color",("Original","Grey"))
        if option == "Original":   
            st.image(img, width= 800)
        elif option == "Grey" : 
                curr_bri = ImageEnhance.Color(img)
                new_bri = 0
                img = curr_bri.enhance(new_bri)
                st.image(img, width= 800)
        n = 250
        m = 350
        s = 36
        w = 800
        h = 800
    elif option == "Dragon Ball":
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "DBZ.jpg")
        img = Image.open(IMAGE_PATH)
        st.image(img, width= 800)
        n = 1500
        m = 600
        s = 72
        w = 1000
        h = 1000
    elif option == "Naruto":
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "N.jpg")
        img = Image.open(IMAGE_PATH)
        st.image(img, width= 800)
        n = 1000
        m = 1000
        s = 72
        w = 1000
        h = 1000
    else:
        image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
        confirm = st.text_input("Type Confirm",placeholder="Confirm")
        if confirm == "Confirm":
            img = Image.open(image_file)
            st.image(img)
            with open(os.path.join("Resources",image_file.name),"wb") as f:f.write((image_file).getbuffer())
            st.success("File Saved")
        n = 600
        m = 1000
        s = 72
        w = 1000
        h = 1000
    option = st.selectbox(
    'Change Font',
    ('Black Italic','Extra Bold'))
    if option == "Black Italic":
        FONT_PATH = os.path.join(dir_of_interest, "font", "BlackItalic.ttf")
    elif option == "Extra Bold":
        FONT_PATH = os.path.join(dir_of_interest, "font", "ExtraBold.ttf")
    
    if st.button('Submit'):
        st.success('Sucess!!!!!!', icon="✅")
        
        DRAW = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT_PATH,s)
        TEXT = title


        DRAW.text((n, m), text=TEXT, fill=(255, 255, 255),font=font,stroke_width = 0)
       
        col1 = st
        fig = px.imshow(img)
        fig.update_layout(
        autosize=False,
        width=w,
        height=h)
        st.image(img)
        #fig.update_xaxes(visible=False)
        #fig.update_yaxes(visible=False)
        col1.plotly_chart(fig)
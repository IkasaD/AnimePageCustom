import streamlit as st
from PIL import Image, ImageDraw, ImageFont
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
            img = img
        elif option == "Grey" : 
                curr_bri = ImageEnhance.Color(img)
                new_bri = 0
                img = curr_bri.enhance(new_bri)
        s = 36
    elif option == "Dragon Ball":
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "DBZ.jpg")
        img = Image.open(IMAGE_PATH)
        s = 72
    elif option == "Naruto":
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "N.jpg")
        img = Image.open(IMAGE_PATH)
        s = 72
    else:
        image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
        confirm = st.text_input("Type Confirm",placeholder="Confirm")
        if confirm == "Confirm":
            img = Image.open(image_file)
            with open(os.path.join("Resources",image_file.name),"wb") as f:f.write((image_file).getbuffer())
            st.success("We are Good to go!!!!!!")
        s = 72
    
    ok = st.checkbox("OK")
    if ok:
        width, height = img.size
        st.image(img, width=700)


    
        values = st.slider(
        'Select width', float(width))
        st.write('Values:', values)
        value = st.slider(
        'Select height', float(height))
        st.write('Values:', value)
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


        DRAW.text((values, value), text=TEXT, fill=(255, 255, 255),font=font,stroke_width = 0)
        img1 = img.convert("RGB") 
        st.image(img1)
        from io import BytesIO
        buf = BytesIO()
        img1.save(buf, format="JPEG")
        byte_im = buf.getvalue()
        btn = st.download_button(
        label="Download Image",
        data=byte_im,
        file_name="Custom.png",
        mime="image/jpeg",
        )
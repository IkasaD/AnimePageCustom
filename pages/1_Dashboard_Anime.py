import streamlit as st
from matplotlib import image
import os




# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "Resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "pir.png")


st.title("Dashboard - Pirates")

type = st.radio(
    "What\'s do you want",
    ('Image', 'Audio', 'Video'))



if type == 'Image':
    st.write('You selected Image.')
    
    imgo = image.imread(IMAGE_PATH)
    st.image(imgo, width= 800)
                
    option = st.selectbox(
         'Change Color',
        ('Blue','Grey'))
    
    agree = st.checkbox('I agree')
    if agree:
        st.write('Great!')
        if st.button('Submit'):
            st.write('Why hello there')
            if option == "Blue":
                st.image(imgo, width= 800,channels= "BGR")
                new_title = '<p style="text-align: center; color:blue; font-size: 42px;">One Piece</p>'
            elif option == "Grey" : 
                grey = imgo[:,:,0]
                st.image(grey, width= 800)
                new_title = '<p style="text-align: center; color:Grey; font-size: 42px;">One Piece</p>'       
            
        
            st.markdown(new_title, unsafe_allow_html=True)
            st.success('Sucessfully you changed the color!', icon="✅")
            st.write('You selected:', option,':skull:')

  


elif type == "Audio":
    st.write("You select Audio.")
    option = st.selectbox(
         'Choose BGM',
        ('One Piece','Dragon Ball','Naruto',"Bleach","Tokyo Ghoul"))
    if option == "One Piece":
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "OP.jpg")
        AUDIO_PATH = os.path.join(dir_of_interest, "Audio", "OP.mp3")
        img = image.imread(IMAGE_PATH)
        st.image(img, width= 800)
        audio_file = open(AUDIO_PATH, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg' )
    elif option == "Dragon Ball":
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "DBZ.jpg")
        AUDIO_PATH = os.path.join(dir_of_interest, "Audio", "DBZ.mp3")
        img = image.imread(IMAGE_PATH)
        st.image(img, width= 800)
        audio_file = open(AUDIO_PATH, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg' )
    elif option == "Naruto":
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "N.jpg")
        AUDIO_PATH = os.path.join(dir_of_interest, "Audio", "N.mp3")
        img = image.imread(IMAGE_PATH)
        st.image(img, width= 800)
        audio_file = open(AUDIO_PATH, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg' )
    
    elif option == "Bleach":
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "B.jpeg")
        AUDIO_PATH = os.path.join(dir_of_interest, "Audio", "B.mp3")
        img = image.imread(IMAGE_PATH)
        st.image(img, width= 800)
        audio_file = open(AUDIO_PATH, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg' )
    else:
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "TG.jpg")
        AUDIO_PATH = os.path.join(dir_of_interest, "Audio", "TG.mp3")
        img = image.imread(IMAGE_PATH)
        st.image(img, width= 800)
        audio_file = open(AUDIO_PATH, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg' )
    
    
elif type == "Video":
    tab1, tab2 = st.tabs(["ONE PIECE", "NARUTO"])
    with tab1:
        st.header("ONE PIECE")
        st.subheader("AMV 1")
        VIDEO_PATH = os.path.join(dir_of_interest, "Videos","OP1.mp4")
        video_file = open(VIDEO_PATH, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes, start_time=0)
        st.write("AMV Video [link](https://youtu.be/xmbxe0Jtxmc)")
        st.subheader("AMV 2")
        VIDEO_PATH = os.path.join(dir_of_interest, "Videos","OP2.mp4")
        video_file = open(VIDEO_PATH, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes, start_time=0)
        st.write("AMV Video [link](https://youtu.be/l4yVf28RfO4)")
    with tab2:
        st.header("NARUTO")
        VIDEO_PATH = os.path.join(dir_of_interest, "Videos","N1.mp4")
        video_file = open(VIDEO_PATH, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes, start_time=0)
        st.write("AMV Video [link](https://youtu.be/ND0UeXeHB4A)")
        st.header("ITACHI")
        st.subheader("AMV 1")
        VIDEO_PATH = os.path.join(dir_of_interest, "Videos","I1.mp4")
        video_file = open(VIDEO_PATH, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes, start_time=0)
        st.write("AMV Video [link](https://youtu.be/anGyMHsNEh0)")
        st.subheader("AMV 2")
        VIDEO_PATH = os.path.join(dir_of_interest, "Videos","I2.mp4")
        video_file = open(VIDEO_PATH, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes, start_time=0)
        st.write("AMV Video [link](https://youtu.be/QTmzUEDyG0U)")
    








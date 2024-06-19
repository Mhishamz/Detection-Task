import streamlit as st
import detector
from PIL import Image
import json
from streamlit_lottie import st_lottie



def process_image(uploaded_file):
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        returned_list=[]
        returned_list=detector.Predict(img)
        st.subheader("Images Categories:")
        for item in returned_list:
            st.write(f"- { item }")
        
    else:
        st.warning("No image to process. Please upload an image first.")
        return None  # Return None if no image is uploaded


# Initialize an empty list to store uploaded images
col1, col2 = st.columns([4, 2]) 

with col1:

    st.title("Welcome !")
    st.subheader("This app detects components from image")
    
    
    # File upload for image
    uploaded_file = st.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"])
    
    
    # Button to trigger image list appending
    if st.button("Analyse Image"):
        process_image(uploaded_file)

with col2:
    with open("Animation.json", "r") as f:
        lottie_data = json.load(f)
    
    
    # Display the Lottie animation
    st_lottie(lottie_data, key="my_lottie", height=200, width=200, loop=True)

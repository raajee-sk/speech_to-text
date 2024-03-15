import speech_recognition as sr
import streamlit as st
from PIL import Image
from googletrans import Translator
from streamlit_option_menu import option_menu

choice=option_menu(menu_title=None,
                            options=["About","Language Selection,Audio Input&Output Text"],orientation='horizontal')

r = sr.Recognizer() 

if choice=="About":

    col1,col2=st.columns(2)
    with col1:
        c=Image.open(r'C:\Users\SKAN\Downloads\th.jpeg')
        st.image(c)

    with col2:
        st.markdown(
            f"<h1 style='color:#F24C3D; font-size: 36px;'>SPEECH TO TEXT</h1>",
            unsafe_allow_html=True,)
   

    st.markdown(
        f"<h1 style='color:#33cc33; font-size: 30px;'>This is speech-to-text web application that accurately transcribes spoken audio into text.</h1>",
        unsafe_allow_html=True,)
    st.markdown(
        f"<h1 style='color:#33cc33; font-size: 30px;'>Capture audio input from the user's microphone and convert the Audio Input To Text.</h1>",
        unsafe_allow_html=True,)
   
   
elif choice=="Language Selection,Audio Input&Output Text":
    select=st.selectbox(':blue[**Select your Language:**]',['select','English','Tamil','Hindi','Telugu','Malayalam','Kannada','Marathi','Assamese','Bengali','Gujarathi','Oriya','Panjabi','Urdu']) 
    if select=="English":
        select='en-IN'
    elif select=="Tamil":
            select='ta-IN' 
    elif select=="Hindi":
            select='hi-IN'
    elif select=="Telugu":
            select='te-IN'  
    elif select=="Malayalam":
            select='ml-IN'  
    elif select=="Kannada":
            select='ka-IN' 
    elif select=="Marathi":
            select='mr-IN'  
    elif select=="Assamese":
            select='as-IN'
    elif select=="Bengali":
            select='bn-IN' 
    elif select=="Gujarathi":
            select='gu-IN'  
    elif select=="Oriya":
            select='or-IN'
    elif select=="Panjabi":
            select='pa-IN'  
    else:
            select='or-IN'      
               
        
    c1=Image.open(r'C:\Users\SKAN\Downloads\OIP (1).jpeg')
    st.image(c1)

    b=st.button(":blue[Start Dictating]")
    if b:            
        with sr.Microphone() as source:   
                r = sr.Recognizer()         
                audio_data = r.record(source,duration=10)

                c1=Image.open(r'C:\Users\SKAN\Downloads\OIP (2).jpeg')
                st.image(c1)
                           
                text = r.recognize_google(audio_data, language=select) 
                translator = Translator()
                translation = translator.translate(text)     
                col1,col2=st.columns(2)   
                with col1:       
                    st.markdown(
                f"<h1 style='color:#F24C3D; font-size: 36px;'>Your Text</h1>",
                unsafe_allow_html=True,)
                    st.write(text)
                with col2:       
                    st.markdown(
                f"<h1 style='color:#F24C3D; font-size: 36px;'>Your Translation Text</h1>",
                unsafe_allow_html=True,)
                    st.write(translation.text)
                                      
                                    
            

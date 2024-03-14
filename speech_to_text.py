import speech_recognition as sr
import streamlit as st
from PIL import Image
from googletrans import Translator
col1,col2=st.columns(2)
with col1:
    c=Image.open(r'C:\Users\SKAN\Downloads\th.jpeg')
    st.image(c)

with col2:
    st.markdown(
        f"<h1 style='color:#F24C3D; font-size: 36px;'>SPEECH TO TEXT</h1>",
        unsafe_allow_html=True,)
st.write(":red[Note: English:'en-IN, Tamil:'ta-IN',Telugu:'te-IN', Malayalm:'ml-IN', Kannada:'ka-IN', Hindi:'hi-IN', Marathi:'mr-IN', Assamese:'as-IN', Bengali (Bangla):'bn-IN', Gujarati:'gu-IN', Oriya:'or-IN', Punjabi:'pa-IN',Urdu:'ur-IN. And the Duration is 10 Seconds]")    
select=st.selectbox(':blue[**Select your Language:**]',['select','en-IN','ta-IN','te-IN','ml-IN','ka-IN','hi-IN','mr-IN','as-IN','bn-IN','gu-IN','or-IN','pa-IN','ur-IN'])    

if select != 'select':
    r = sr.Recognizer()
      
    with sr.Microphone() as source:
        c1=Image.open(r'C:\Users\SKAN\Downloads\OIP.jpeg')
        st.image(c1)
                      
    
        audio_data = r.record(source,duration=10)
        st.markdown(
        f"<h1 style='color:#F24C3D; font-size: 30px;'>Processing....</h1>",
        unsafe_allow_html=True,)
        

        # convert speech to text
        text = r.recognize_google(audio_data,language=str(select))
        st.markdown(
        f"<h1 style='color:#33cc33; font-size: 30px;'>YOUR TEXT IS</h1>",
        unsafe_allow_html=True,)
        st.write(text)     
        
        translator = Translator()
        translation = translator.translate(text)
        st.markdown(
        f"<h1 style='color:#33cc33; font-size: 30px;'>YOUR TRANSLATION TEXT IS</h1>",
        unsafe_allow_html=True,)
        st.write(translation.text)



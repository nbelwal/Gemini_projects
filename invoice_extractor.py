# from dotenv import load_dotenv
import streamlit as st
# import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
# load_dotenv()

# Configure the API key for Google Generative AI
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to interact with the model
def get_gemini_response(context, image, prompt):
    # Convert the image to bytes for processing
    return model.generate_content([context, image, prompt]).text

# Streamlit setup
st.set_page_config(page_title="Multilanguage Invoice Extractor")
st.header("Multi-language Invoice Extractor")
st.text('''🌍 The ultimate language-agnostic invoice extractor you need!
Got an invoice in Spanish, but not familiar with the language? No problem at all!😊''')
# User input for fields/info to extract
prompt = st.text_input("Ask anything about the uploaded invoice.")

# File uploader for invoice images
uploaded_file = st.file_uploader("Select Invoice", type=["jpg", "jpeg", "png"])

# Initialize image variable
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image=image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Let's Go")

# Setting model context 
context = '''extract the content of the image'''
'''
you are a multilanguage invoice extrator. Please tell all the information asked about the invoice. And first, check if the provided image is invoice or not, if not, then say "provided image is not an invoice". if the image is invoice then, check if the question asked about it is related to invoice or not, if not say "The question is not related to invoice". if it is related then, answer accordinly. and if no question is asked, provide all the info from the invoice
'''

# Handling submit button action
if submit:
    if image:
        response = get_gemini_response(context, image, prompt)
        st.subheader("Response")
        st.markdown(response)
    else:
        st.text("Please provide an invoice image.")








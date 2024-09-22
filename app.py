from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai
import base64


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input, pdf_content, prompt):
    model= genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf(uploaded_file):
    if uploaded_file is not None:
        pdf_content = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = pdf_content[0] 

        #convert_to_bytes

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]

        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded") 

#Streamlit

st.set_page_config(page_title="ATS Tracking", page_icon="🔮", layout="wide")
st.header("Yogi's ATS Helper")
input_text = st.text_area("Enter the Job Description", key= "input")
uploaded_file = st.file_uploader("Upload your Resume as PDF", type=["pdf"], key="file")


if uploaded_file is not None:
    st.write("Resume Uploaded Successfully")

submit1 = st.button("Tell me about the Resume")
submit2= st.button("Match with the Job Description")
submit3 = st.button("Percentage match and Suggestions")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Extract technical skills, soft skills, education details, and experience/project information directly from the resume. Only include information explicitly stated in the resume for each category.
"""

input_prompt2 = """Given a resume and a job description, 
generate a table illustrating the match. Use cues to represent high, medium, and low match areas, highlighting strengths and weaknesses."""

input_prompt3 = """
Consider yourself as a hiring manager and you know the ATS used in the job application process.You need to behave like a robust tool and provide the percentage match of the resume with the job description.
Analyze a resume and job description. Identify keywords and skills from the job description absent in the resume. Prioritize based on frequency and relevance to the job. 
Provide suggestions for integrating these keywords into the resume, emphasizing achievements and quantifiable results. Write this how this can be incoprated in the resume with suggestions.
"""


if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt1)
        st.subheader("Resume Analysis")
        st.write(response)
    else:
        st.write("Please upload the resume")

if submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt2)
        st.subheader("Resume Analysis")
        st.write(response)
    else:
        st.write("Please upload the resume")

if submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt3)
        st.subheader("Resume Analysis")
        st.write(response)
    else:
        st.write("Please upload the resume")



st.text("Keep grinding, because every 'NO' is just one step closer to that big 'YES'.- cheers to what's coming next!")
st.text("Made with ❤️ by Yogi")
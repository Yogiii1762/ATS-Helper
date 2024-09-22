# Yogi's ATS Helper

Yogi's ATS Helper is a streamlined tool built using Streamlit to evaluate resumes and job descriptions for job seekers. This application integrates various services such as Google Generative AI (`gemini-1.5-pro`) to help candidates analyze and match their resumes with specific job descriptions using artificial intelligence. The app also provides suggestions on how to improve resumes to match job descriptions more closely.

## Features

- **Resume Upload:** Upload your resume in PDF format.
- **Resume Analysis:** Get an in-depth review of the resume, focusing on technical skills, soft skills, education details, and experiences.
- **Job Description Matching:** Analyze the alignment between your resume and job description.
- **Percentage Match & Suggestions:** Get a percentage match of your resume with the job description and suggestions for improving alignment.
- **Human-Like Evaluations:** The AI acts as an experienced Technical HR Manager, providing professional evaluation and feedback.

## Tech Stack

- **Python**
- **Streamlit** for the web interface
- **dotenv** for handling environment variables
- **Google Generative AI** (Gemini model) for AI-powered content generation
- **pdf2image** for converting PDFs to images
- **Pillow (PIL)** for image processing
- **Base64** for encoding the PDF images
- **io** for in-memory byte stream handling

## Setup

### Requirements

To run this project, you need to have the following libraries installed:

- `streamlit`
- `Pillow`
- `pdf2image`
- `dotenv`
- `google-generativeai`

### API Key

This app uses the **Google Gemini Model**. Make sure you have your API key ready. Add your API key in a `.env` file in the root directory:


`GOOGLE_API_KEY=your-google-api-key `

### Running the App

To run the application, use the following command:

```bash
streamlit run app.py



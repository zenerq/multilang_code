import streamlit as st 
import os
import openai
import pybase64

LOGO_IMAGE = "logo.png"

st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-img {
        float:right;
	margin:auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{pybase64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
    </div>
    """,
    unsafe_allow_html=True
)


st.header("Code Translate Generator in different languages") 
language_option = st.selectbox(
    'In which language do you want your code solution?',
    ('Python', 'Java', 'C++','Javascript','Go','Ruby'))
question=st.text_area("Type Problem")
button= st.button("Generate code")

def gen_auto_response(question,language_option):

    openai.api_key = "YOUR_KEY"
    response = openai.Completion.create(
        model="code-cushman-001",
        prompt=f""""Given a {language_option} solution for the code question below 
                Question: {question} 
                {language_option} Solution: """,
        temperature=0,
        max_tokens=1124,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    return response.choices[0].text
	
if question and button and language_option:
    with st.spinner("Generating code, Please Wait"):
        reply=gen_auto_response(question,language_option)
        st.code(reply)

import streamlit as st
import requests

# Hide Streamlit's default menu and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Function to get data from Flask API
def get_data():
    response = requests.get('http://127.0.0.1:5000/api/data')
    if response.status_code == 200:
        return response.json()
    else:
        return {"message": "Failed to retrieve data"}

# Function to post data to Flask API
def post_data(new_message):
    response = requests.post('http://127.0.0.1:5000/api/data', json={"message": new_message})
    if response.status_code == 200:
        return response.json()
    else:
        return {"message": "Failed to post data"}

# Streamlit UI
st.title('Streamlit Frontend with Flask Backend')

st.header('Get Data from Flask')
if st.button('Get Data'):
    data = get_data()
    st.write(data)

st.header('Post Data to Flask')
new_message = st.text_input('Enter a new message:')
if st.button('Post Data'):
    updated_data = post_data(new_message)
    st.write(updated_data)

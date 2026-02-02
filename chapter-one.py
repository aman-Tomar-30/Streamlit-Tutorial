import streamlit as st

st.title("Chapter One")
st.subheader("Introduction to Streamlit")
st.text("Welcome to our interactive app built with streamlit")
st.write("Choose your favorite programming language from the options below:")

language = st.selectbox(
    "Select a programming language:", ["Python", "JavaScript", "Java", "C++", "Ruby"]
)
st.write(f"You selected: {language}")
st.success("This is a success message!")
st.error("This is an error message!")
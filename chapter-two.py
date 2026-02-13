import streamlit as st
import datetime 

st.title("Interactive Widgets")
if st.button("Click Me"):
    st.success("You clicked the button!")
    
check = st.checkbox("Check me out")
if check:
    choice = st.radio("Choose among these options:", ["Python", "Java", "C++"])
    st.write(f"You chose: {choice}")
    
option = st.selectbox("Select your favorite web framework:", ["Flask", "Django", "FastAPI"])
st.write(f"You selected: {option}")

if option:
    st.slider(f"Select a range as per your expertise in {option} Framework", 1, 5, 2)
    experience = st.number_input(f"Rate your experience with {option} Framework", min_value=0, max_value=10)
    st.write(f"You rated your experience with {option} Framework as: {experience}")

    your_name = st.text_input("Enter your name:")
    if your_name: 
        st.write(f"Hello, {your_name}!")
        st.text_area(f"Share your thoughts on {option} Framework")
        dob = st.date_input("Select your date of birth", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2027, 12, 31))
        today = datetime.datetime.now().year
        st.write(f"Your Age is: {(today - dob.year)} years")
    
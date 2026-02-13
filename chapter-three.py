import streamlit as st

st.title("Understanding of Grids")
col1, col2 = st.columns(2)
with col1:
    st.header("Now")
    st.write("A software developer with a passion for creating intuitive user interfaces. He has experience in various programming languages and frameworks, and enjoys working on projects that challenge his skills and creativity.")
    st.video("https://youtu.be/5jDegtLFE8Y")
with col2:    
    st.header("Then")
    st.write("A curious child who loved to explore the world around him.")
    st.image("https://cdn2.geckoandfly.com/wp-content/uploads/2017/08/thomas-edison-quote-02.jpg")
    
name = st.sidebar.text_input("Enter your Name:")
if name:
    st.sidebar.write(f"Hello, {name}!")
    comment = st.sidebar.text_area("Leave a comment:")
    if comment:
        st.sidebar.write("Thank you for your comment!")
        
with st.expander("Way to get ready for DSA"):
    st.write("1. Start with the basics: Make sure you have a solid understanding of fundamental data structures (like arrays, linked lists, stacks, queues) and algorithms (like sorting and searching).")
    st.write("2. Practice coding problems: Use platforms like LeetCode, HackerRank, or CodeSignal to practice solving coding problems. Start with easy problems and gradually move to more difficult ones.")
    st.write("3. Learn about time and space complexity: Understand how to analyze the efficiency of your code using Big O notation.")
    st.write("4. Study common algorithms: Familiarize yourself with common algorithms such as binary search, depth-first search, breadth-first search, dynamic programming, and greedy algorithms.")
    st.write("5. Participate in coding competitions: Join online coding competitions to challenge yourself and improve your problem-solving skills under time constraints.")
    
st.markdown("### Conclusion")
st.markdown("> World only remembers the Winner, So be the One")
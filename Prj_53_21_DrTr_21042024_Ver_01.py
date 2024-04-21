import streamlit as st

# Add a title and some text
st.title('My Streamlit App')
st.write("Here's our first attempt at using data to create a table:")


# Using a button to print a message
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
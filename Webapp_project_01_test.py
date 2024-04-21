import streamlit as st
import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
st.title('Vietnam Shapefile Viewer')
# File uploader allows user to add their own .mat file
uploaded_file = st.file_uploader("Choose a .mat file", type=['mat'])
if uploaded_file is not None:
    # Use the uploaded file instead of the hardcoded path
    data = loadmat(uploaded_file)
    try:
        # Assuming 'VN_shape' is the key in the .mat file containing the shape data
        VN_shape = data['VN_shape'][0]  # Adjust indexing based on your data structure
        fig, ax = plt.subplots()
        for shape in VN_shape:
            ax.plot(shape['X'][0], shape['Y'][0], 'k-')  # Adjust the indexing if necessary
        ax.set_xlabel('Easting (m)')
        ax.set_ylabel('Northing (m)')
        ax.set_title('UTM Projection of Vietnam Shapefile')
        ax.grid(True)
        st.pyplot(fig)
    except KeyError:
        st.error("Error: The key 'VN_shape' was not found in the .mat file. Please check the file and try again.")
else:
    st.warning("Please upload a .mat file to view the shapefile.")

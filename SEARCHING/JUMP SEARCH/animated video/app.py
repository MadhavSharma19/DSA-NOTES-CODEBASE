import streamlit as st
import subprocess
import sys

st.set_page_config(page_title="Jump Search Visualizer", layout="centered")

st.title("🐰 Jump Search Visualizer")

# Input array
arr_input = st.text_input("Enter sorted array (comma separated)", "1,3,5,7,9,11,13,15")
target = st.number_input("Enter target", value=9)

if st.button("▶️ Go"):
    arr = arr_input.replace(" ", "")
    
    # Pass data to turtle script
    subprocess.Popen([sys.executable, "turtle_jump.py", arr, str(target)])

    st.success("Visualization started in a new window 🚀")
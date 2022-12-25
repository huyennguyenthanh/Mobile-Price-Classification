import base64
from io import BytesIO
import streamlit as st
import os
import json
import requests
from PIL import Image



st.title("Phone Price Classification")
st.caption("Now, let describe your phone")


st.header("Phone's Utilities")
three_g = st.checkbox("3G available")
four_g = st.checkbox("4G available")
bluetooth = st.checkbox("Bluetooth available")
dual_sim = st.checkbox("Dual sim available")
wifi = st.checkbox("Wifi available")
touch_screen = st.checkbox("Touch screen available")


st.header("Phone's Specification")
battery_power = st.slider("Battery power (mAh)", 500, 2000)
clock_speed = st.slider("Clock speed", 0.5, 3.0)
int_memory = st.number_input("Memory sỉze (GB)", 4, 64, 4, 4)
n_cores = st.number_input("Number of CPU cores", 1, 10,1,1)


st.header("Phone's Design")

px_height = st.slider("Height (pixel)", 720, 4096)
px_width = st.slider("Width (pixel)", 720, 4096)


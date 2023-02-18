import streamlit as sl
from PIL import Image

sl.set_page_config(layout='wide')

image = Image.open('pictures/good-luck-blackboard-old-wooden-table-texture-123012816.jpg')

sl.header("Assignment\t2")
sl.subheader("Lev Sukherman")
sl.text("Math 7800")
sl.balloons()

sl.image(image, caption='')


sl.markdown("<h6 style='text-align: right; color: black;'>02.17.2023</h6>", unsafe_allow_html=True)

import streamlit as sl
from PIL import Image

sl.subheader("2. Seeds from supplier A have an 85 percent germination rate,"
             " and those from supplier B have 75 percent germination rate."
             "A company purchases 40 percent of its seeds from supplier A and 60 percent from supplier B.")

general_image = Image.open('pictures/Page_2.png')

sl.subheader("(a) Find the probability that a seed selected at random will germinate.")
sl.image(general_image, caption='')
sl.subheader("Answer: 0.34 + 0.45 = 0.79")
sl.subheader("(b) Given that a seed germinated, find the probability that the seed was from supplier A.")
sl.image(general_image, caption='')
sl.subheader("Answer: $$P(A|Yes) = \dfrac{P(A \cap Yes)}{P(Yes)}$$ = $$\dfrac{0.34}{0.34+0.45}$$ = 0.43")

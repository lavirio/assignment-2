import streamlit as sl
from PIL import Image

sl.subheader("3. At the emergency room, 20 percent of patients are classified as critical,"
             "30 percent are serious, and 50 are stable. Of the critical ones, 30 percent die;"
             "of the serious ones, 10 percent die; of the stable ones, 1 percent die.")

image = Image.open('pictures/Page_3.png')

sl.subheader("(a) Find the probability that a patient in this emergency room dies.")
sl.image(image, caption='')
sl.subheader("$$P(Yes) = 0.06 + 0.03 + 0.005 = 0.095$$")
sl.subheader("(b) Given that the patient died, what is the probability they were classified as critical.")
sl.image(image, caption='')
sl.subheader("$$P(A|Yes) = \dfrac{P(A \cap Yes)}{P(Yes)}$$ = $$\dfrac{0.06}{0.095} = 0.63$$")

import streamlit as sl
from PIL import Image

image = Image.open('pictures/good-luck-blackboard-old-wooden-table-texture-123012816.jpg')

sl.header("1. Let A and B be events.")
sl.subheader("(a) If A and B are mutually exclusive, can they be independent? Give an example to explain.")
sl.subheader("Mutually exclusice: $P(A \cap B)$ = 0")
sl.subheader("Independent: P(A|B) = P(A)")
sl.subheader("$$P(A|B) = \dfrac{P(A \cap B)} {P(B)}$$")
sl.subheader("$$P(A|B) = 0 \\neq\ P(A)$$")
sl.subheader("Therefore, A and B are dependent")
sl.subheader("(b) If A is a subset of B, can A and B be independent? Give an example to explain. ")
sl.subheader("A c B therefore, $$A \cap B = A$$")
sl.subheader("$$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{P(A)}{P(B)} \\neq\ P(A)$$")
sl.subheader("$$ P(B|A) = \dfrac{P(A \cap B)}{P(A)} = \dfrac{P(A)}{P(A)} = 1 \\neq\ P(B)$$")
sl.subheader("Therefore, A and B are dependent")

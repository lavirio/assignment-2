import math

import streamlit as sl
from PIL import Image

sl.subheader("8. Lets a random experiment be the rolling of two fair six-sided dice.")

image_8_1 = Image.open('pictures/Page_8-1.png')
image_8_2 = Image.open('pictures/Page_8-2.png')

sl.subheader("(a) Let X be the random variable that keeps track of the minimum of the two outcomes."
             " Find the pmf (probability mass function) of X. That is for each possible value i of X,"
             "find P(X = i).")
sl.image(image_8_1, caption='')
sl.subheader("(b) Find the expected value of X.")
Exp_x = (1 * 11 / 36) + (2 * 9 / 36) + (3 * 7 / 36) + (4 * 5 / 36) + (5 * 3 / 36) + (6 * 1 / 36)
sl.subheader("E(X) = " + str(Exp_x))
sl.subheader("(c) Find the variance of X. ")
Var_x = (1 * 11 / 36) + (4 * 9 / 36) + (9 * 7 / 36) + (16 * 5 / 36) + (25 * 3 / 36) + (6 * 1 / 36) - math.pow(Exp_x, 2)
sl.subheader("Var(X) = " + str(Var_x))
sl.subheader("(d) Let Y be the absolute value of the difference between the two rolls. Find the pmf of Y.")
sl.image(image_8_2, caption='')
sl.subheader("(e) Find the expected value of Y.")
Exp_y = (1 * 10 / 36) + (2 * 8 / 36) + (3 * 6 / 36) + (4 * 5 / 36) + (5 * 2 / 36)
sl.subheader("E(Y) = " + str(Exp_y))
sl.subheader("(e) Find the variance of Y.")
Var_y = (1 * 10 / 36) + (4 * 8 / 36) + (9 * 6 / 36) + (16 * 4 / 36) + (25 * 2 / 36) - math.pow(Exp_y, 2)
sl.subheader("Var(Y) = " + str(Var_y))

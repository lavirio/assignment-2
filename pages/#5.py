import streamlit as sl
import math
from PIL import Image

sl.subheader("5. A hand of 5 cards is drawn without replacement from a normal deck of 52 cards."
             "Find the probability that the 5 card hand is:")

image = Image.open('pictures/good-luck-blackboard-old-wooden-table-texture-123012816.jpg')

sl.subheader("$$\\binom{n}{k}\ = \dfrac{n!}{k!(n-k)!}$$")
sl.subheader("(a) four of a kind (four cards of equal value and one card of a different value).")
a = (math.comb(13, 1) * math.comb(4, 4) * math.comb(48, 1)) / math.comb(52, 5)
sl.subheader("$$\dfrac{\dbinom{13}{1} * \dbinom{4}{4} * \dbinom{48}{1}}{\dbinom{52}{5}} = $$ " + str(a))
sl.subheader("(b) full house (one pair and one triple of cards with equal value).")
b = (math.comb(13, 1) * math.comb(4, 2) * math.comb(12, 1) * math.comb(4, 3)) / math.comb(52, 5)
sl.subheader("$$\dfrac{\dbinom{13}{1} * \dbinom{4}{2} * \dbinom{12}{1} * \dbinom{4}{3}}{\dbinom{52}{5}} = $$ " + str(b))
sl.subheader("(c) three of a kind (three equal face values plus two cards of different values).")
c = (math.comb(13, 1) * math.comb(4, 3) * math.comb(12, 1) * math.comb(4, 1) * math.comb(11, 1) * math.comb(4,
                                                                                                            1)) / (math.comb(
    52, 5) * math.factorial(2))
sl.subheader(
    "$$\dfrac{\dbinom{13}{1} * \dbinom{4}{3} * \dbinom{12}{1}  * \dbinom{4}{1} * \dbinom{11}{1}  * \dbinom{4}{1} * \dfrac{1}{2!}}{\dbinom{52}{5}} = $$ " + str(
        c))
sl.subheader("(d) two pairs (two pairs of equal values plus one card of different value).")
d = (math.comb(13, 1) * math.comb(4, 2) * math.comb(12, 1) * math.comb(4, 2) * math.comb(11, 1) * math.comb(4,
                                                                                                            1)) / (
                math.comb(
                    52, 5) * math.factorial(2))
sl.subheader(
    "$$\dfrac{\dbinom{13}{1} * \dbinom{4}{2} * \dbinom{12}{1}  * \dbinom{4}{2} * \dbinom{11}{1}  * \dbinom{4}{1} * \dfrac{1}{2!}}{\dbinom{52}{5}} = $$ " + str(
        d))
sl.subheader("(e) one pair (one pair of equal value plus three cards of different values)")
e = (math.comb(13, 1) * math.comb(4, 2) * (math.comb(12, 1) * math.comb(4, 1)) * (
        math.comb(11, 1) * math.comb(4, 1)) * (math.comb(10, 1) * math.comb(4, 1))) / (
                math.comb(52, 5) * math.factorial(3))
sl.subheader(
    "$$\dfrac{\dbinom{13}{1} * \dbinom{4}{2} * \dbinom{12}{1}  * \dbinom{4}{1} * \dbinom{11}{1} * \dbinom{4}{1} * \dbinom{10}{1}  * \dbinom{4}{1} * \dfrac{1}{3!}}{\dbinom{52}{5}} = $$ " + str(
        e))

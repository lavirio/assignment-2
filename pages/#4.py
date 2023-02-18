import streamlit as sl
import math
import pandas as pd

sl.subheader("4. Find the rules of keno here.  https://www.masslottery.com/games/draw-and-instants/keno/how-to-play")
sl.subheader("There is a drop down menu in the how to win section.")

sl.subheader("$$\\binom{n}{k}\ = \dfrac{n!}{k!(n-k)!}$$")
sl.subheader("(a) In the 12 spot game, calculate the exact probability that you match 11 balls and win 25000 dollars.")
a = (math.comb(20, 11) * math.comb(60, 1)) / math.comb(80, 12)
sl.subheader("$$\dfrac{\dbinom{20}{11} * \dbinom{60}{1}}{\dbinom{80}{12}} = $$ " + str(a))
sl.subheader("(b) Find the expected value of the winning in the 7 spot game.")
Prob_1_7 = (math.comb(20, 7) * math.comb(60, 0)) / math.comb(80, 7)
Prob_2_7 = (math.comb(20, 6) * math.comb(60, 1)) / math.comb(80, 7)
Prob_3_7 = (math.comb(20, 5) * math.comb(60, 2)) / math.comb(80, 7)
Prob_4_7 = (math.comb(20, 4) * math.comb(60, 3)) / math.comb(80, 7)
Prob_5_7 = (math.comb(20, 3) * math.comb(60, 4)) / math.comb(80, 7)
Prob_6_7 = 1 - (Prob_5_7 + Prob_4_7 + Prob_3_7 + Prob_2_7 + Prob_1_7)
Exp_7 = (Prob_6_7 * 0) + (Prob_5_7 * 1) + (Prob_4_7 * 3) + (Prob_3_7 * 20) + (Prob_2_7 * 100) + (Prob_1_7 * 5000)
df_7 = pd.DataFrame([('X', '5000', '100', '20', '3', '1', '0'),
                   ('P(x)', "{:.7f}".format(Prob_1_7), "{:.4f}".format(Prob_2_7), "{:.4f}".format(Prob_3_7), "{:.4f}".format(Prob_4_7), "{:.4f}".format(Prob_5_7), "{:.4f}".format(Prob_6_7))],
                  columns=('', 'Match 7', 'Match 6', 'Match 5', 'Match 4', 'Match 3', 'Match <3'))
sl.dataframe(df_7)
sl.subheader("$$E(x) = $$ " + str(Exp_7))
sl.subheader("(c) Find the expected value of the winning in the 8 spot game.")
Prob_1_8 = (math.comb(20, 8) * math.comb(60, 0)) / math.comb(80, 7)
Prob_2_8 = (math.comb(20, 7) * math.comb(60, 1)) / math.comb(80, 7)
Prob_3_8 = (math.comb(20, 6) * math.comb(60, 2)) / math.comb(80, 7)
Prob_4_8 = (math.comb(20, 5) * math.comb(60, 3)) / math.comb(80, 7)
Prob_5_8 = (math.comb(20, 4) * math.comb(60, 4)) / math.comb(80, 7)
Prob_6_8 = 1 - (Prob_5_7 + Prob_4_7 + Prob_3_7 + Prob_2_7 + Prob_1_7)
Exp_8 = (Prob_6_8 * 0) + (Prob_5_8 * 2) + (Prob_4_8 * 10) + (Prob_3_8 * 50) + (Prob_2_8 * 1000) + (Prob_1_8 * 15000)
df_8 = pd.DataFrame([('X', '15000', '1000', '50', '10', '2', '0'),
                   ('P(x)', "{:.7f}".format(Prob_1_8), "{:.4f}".format(Prob_2_8), "{:.4f}".format(Prob_3_8), "{:.4f}".format(Prob_4_8), "{:.4f}".format(Prob_5_8), "{:.4f}".format(Prob_6_8))],
                  columns=('', 'Match 8', 'Match 7', 'Match 6', 'Match 5', 'Match 4', 'Match <4'))
sl.dataframe(df_8)
sl.subheader("$$E(x) = $$ " + str(Exp_8))
sl.subheader("(d) Find the variance of the winning of the 7 spot game.")
Var_7 = ((Prob_1_7 * math.pow(5000, 2)) + (Prob_2_7 * math.pow(100, 2)) + (Prob_3_7 * math.pow(20, 2)) + (
        Prob_4_7 * math.pow(3, 2)) + (Prob_5_7 * math.pow(1, 2)) + (Prob_6_7 * math.pow(0, 2))) - math.pow(Exp_7, 2)
sl.subheader("$$Var(x) = $$ " + str(Var_7))
sl.subheader("(e) Find the variance of the winning of the 8 spot game.")
Var_7 = ((Prob_1_8 * math.pow(15000, 2)) + (Prob_2_8 * math.pow(1000, 2)) + (Prob_3_8 * math.pow(50, 2)) + (
        Prob_4_8 * math.pow(10, 2)) + (Prob_5_8 * math.pow(2, 2)) + (Prob_6_8 * math.pow(0, 2))) - math.pow(Exp_8, 2)
sl.subheader("$$Var(x) = $$ " + str(Var_7))

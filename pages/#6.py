import streamlit as sl

sl.subheader("6. P(A) = 0.8, P(B) = 0.5, and P(A ∪ B) = 0.9")

sl.subheader("$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$")
sl.subheader("(a) Are A and B mutually exclusive?")
sl.subheader("$$P(A \cup B) \\neq\ P(A) + P(B)$$")
sl.subheader("Answer: No")
sl.subheader("(b) Are A and B independent?")
sl.subheader("$$P(A \cap B) = P(A) * P(B) - (Independent)$$")
sl.subheader("0.4 = 0.8 * 0.5")
sl.subheader("Answer: Yes")
sl.subheader("(c) P(A′∪ B′)")
sl.subheader("$$P(A' \cup B') = 1 - P(A \cap B) = 1 -0.4 = 0.6$$")
sl.subheader("(d) P(A|B)")
sl.subheader("$$P(A|B) = P(A) = 0.8$$")
sl.subheader("(e) P(A ∩ B|B')")
sl.subheader("$$P(A \cap B \cap B') = \dfrac{P(A \cap B \cap B')}{P(B')} = \dfrac{0}{P(B')} = 0$$")

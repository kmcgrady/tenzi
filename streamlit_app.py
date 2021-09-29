import random
import streamlit as st

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.keep = False
        self.save_value()

    def save_value(self):
        self.value = self.roll()

    def roll(self):
        return random.randint(1, self.sides)

st.title("Tenzi")

if 'dice' not in st.session_state:
    st.session_state.dice = []

NUM_DICE = 10
NUM_SIDES = 6
if st.button("Roll"):
    if len(st.session_state.dice) == 0:
        for idx in range(NUM_DICE):
            st.session_state.dice.append(Die(NUM_SIDES))
    else:
        for idx, die in enumerate(st.session_state.dice):
            if not die.keep:
                st.session_state.dice[idx].save_value()

current_value = 0
has_won = False
if len(st.session_state.dice) > 0:
    current_value = st.session_state.dice[0].value
    has_won = True
for idx, die in enumerate(st.session_state.dice):
    die.keep = st.checkbox(str(die.value), key=str(idx))
    if die.value != current_value:
        has_won = False

if has_won:
    st.write("You win!")
    st.balloons()

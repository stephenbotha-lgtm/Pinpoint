import random

import streamlit as st

st.title("pinpoint")
st.subheader("to help you find your next play")
st.write("lets get started")

faror = st.slider(

    "how much do you like 67 out of 100",
min_value=1,
max_value=100,
value=1,
    step=1,
)
tipe = st.radio(
    "what tipe of game are you looking for?",
   ["sandbox","horror","board","driving","other"]
)

if st.button("find game"):

    if tipe== "sandbox":
        task = [
            "minecraft", "Terraria","no mans sky"
        ]
    elif tipe== "other":
        task = [
            "go touch grass (easter egg)","call a friend","unc unc unc unc unc"
        ]
    elif tipe== "board":

        task = [
            "magic (card game)", "catan","get off games and read a book you susy baka"
        ]

    elif tipe== "horror":
        task = [
            "darkwood", "poppy playtime 1-5","red fall"
        ]

    elif tipe== "driving":
        task = [
            "The Purist Racing & Physics Sims", "Forza Horizon 5","SnowRunner"
        ]


    if faror == 1:
        st.write("how dare you not like 67 (easter egg)")

    task = random.choice(task)
    st.info(task)
    st.write(tipe)

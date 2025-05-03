import streamlit as st
import base64

# Jungle background (a green pattern)
def set_background():
    jungle_url = "https://images.unsplash.com/photo-1615361205439-684e308ea3dc?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{jungle_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Session state
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "dragons_raised" not in st.session_state:
    st.session_state.dragons_raised = 0

# Dragon stage emoji
def get_dragon_stage(xp):
    if xp < 3:
        return "🥚"
    elif xp < 7:
        return "🐣"
    elif xp < 15:
        return "🐉"
    elif xp < 25:
        return "🔥"
    else:
        return "🌈"

# Header
st.markdown("<h1 style='text-align: center; color: white;'>🐲 Dragon Jungle</h1>", unsafe_allow_html=True)

st.markdown(
    f"<h2 style='text-align: center; color: white;'>Dragon: {get_dragon_stage(st.session_state.xp)}</h2>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<h3 style='text-align: center; color: white;'>XP: {st.session_state.xp} / 25</h3>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<h4 style='text-align: center; color: white;'>🌟 Dragons Raised: {st.session_state.dragons_raised}</h4>",
    unsafe_allow_html=True,
)

# Task buttons
st.markdown("<h2 style='color: white;'>👶 Tap When You Finish:</h2>", unsafe_allow_html=True)
cols = st.columns(3)
tasks = {
    "🛏 Make Bed": "bed",
    "🍽 Eat": "eat",
    "🧸 Clean Toys": "toys",
    "🪥 Brush Teeth": "teeth",
    "🚿 Shower": "shower",
    "🎒 Pack Bag": "bag",
}

for i, (label, key) in enumerate(tasks.items()):
    if cols[i % 3].button(label):
        st.session_state.xp += 1

        if st.session_state.xp >= 25:
            st.balloons()
            st.success("🎉 Your dragon grew up and went into the wild!")
            st.session_state.dragons_raised += 1
            st.session_state.xp = 0

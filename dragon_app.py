import streamlit as st

# Set jungle background
def set_jungle_background():
    jungle_url = "https://images.unsplash.com/photo-1615361205439-684e308ea3dc?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{jungle_url}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            color: white;
        }}
        .emoji-button > button {{
            font-size: 50px !important;
            height: 80px !important;
            width: 80px !important;
        }}
        .big-dragon {{
            font-size: 100px;
            text-align: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_jungle_background()

# --- Session state ---
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "dragons_raised" not in st.session_state:
    st.session_state.dragons_raised = 0

# --- Get current dragon stage ---
def get_dragon_emoji(xp):
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

# --- Show dragon ---
st.markdown("<div class='big-dragon'>" + get_dragon_emoji(st.session_state.xp) + "</div>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align:center;'>XP: {st.session_state.xp} / 25</h2>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align:center;'>Dragons Raised: {st.session_state.dragons_raised}</h4>", unsafe_allow_html=True)

# --- Emoji task buttons (big) ---
st.markdown("<h2>Tap a button:</h2>", unsafe_allow_html=True)
task_emojis = ["🛏", "🍽", "🧸", "🪥", "🚿", "🎒", "🎮", "🎤"]
cols = st.columns(4)

for i, emoji in enumerate(task_emojis):
    with cols[i % 4]:
        if st.button(emoji, key=f"task_{i}"):
            st.session_state.xp += 1

            if st.session_state.xp >= 25:
                st.balloons()
                st.success("🎉 Your dragon grew up and went into the wild!")
                st.session_state.dragons_raised += 1
                st.session_state.xp = 0

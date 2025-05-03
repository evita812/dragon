import streamlit as st
import random

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
if "tasks_completed" not in st.session_state:
    st.session_state.tasks_completed = 0

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

# --- Fun and interactive task buttons ---
st.markdown("<h2>Complete these tasks to grow your dragon!</h2>", unsafe_allow_html=True)

task_list = ["🛏 Make Bed", "🍽 Eat", "🧸 Clean Toys", "🪥 Brush Teeth", "🚿 Shower", "🎒 Pack Bag", "🎮 Play", "🎤 Sing"]

# Select random task from the list
selected_task = random.choice(task_list)

st.markdown(f"<h3>Today's Task: {selected_task}</h3>", unsafe_allow_html=True)

# --- Task completion ---
if st.button("Complete Task"):
    st.session_state.xp += 1
    st.session_state.tasks_completed += 1
    st.success(f"Great job! You completed the task: {selected_task}")

    # Show the dragon evolve at certain XP levels
    if st.session_state.xp == 5:
        st.balloons()
        st.markdown("<h3>Your dragon is growing! It's now a baby dragon 🐣!</h3>", unsafe_allow_html=True)
    elif st.session_state.xp == 10:
        st.balloons()
        st.markdown("<h3>Your dragon is now a kid dragon 🐉!</h3>", unsafe_allow_html=True)
    elif st.session_state.xp == 15:
        st.balloons()
        st.markdown("<h3>Your dragon is now a teen dragon 🔥!</h3>", unsafe_allow_html=True)
    elif st.session_state.xp == 25:
        st.balloons()
        st.markdown("<h3>Your dragon is now an adult! 🌈</h3>", unsafe_allow_html=True)
        st.session_state.dragons_raised += 1
        st.session_state.xp = 0  # Reset XP after evolving

# --- Task buttons (interactive) ---
if st.button("Show Dragon's Tasks"):
    st.write("🛏 Make Bed, 🍽 Eat, 🧸 Clean Toys, 🪥 Brush Teeth, 🚿 Shower, 🎒 Pack Bag, 🎮 Play, 🎤 Sing")



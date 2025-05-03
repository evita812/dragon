import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Dragon Schedule App", layout="centered")

# Session state to keep track of tasks, XP, dragon count
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "dragons_raised" not in st.session_state:
    st.session_state.dragons_raised = 0

# Load images
def load_dragon_image(xp):
    if xp < 3:
        return "images/egg.png"
    elif xp < 7:
        return "images/baby.png"
    elif xp < 15:
        return "images/kid.png"
    elif xp < 25:
        return "images/teen.png"
    else:
        return "images/adult.png"

# Title
st.title("🐉 Dragon Schedule Tracker")

# Show dragon
dragon_stage = load_dragon_image(st.session_state.xp)
img = Image.open(dragon_stage)
st.image(img, caption=f"XP: {st.session_state.xp} | Dragons Raised: {st.session_state.dragons_raised}", use_column_width=True)

# Add new task
task = st.text_input("New task:")
if st.button("Add Task"):
    if task.strip() != "":
        st.session_state.tasks.append({"text": task, "done": False})

# Show task list
st.subheader("📋 Your Tasks")
for i, t in enumerate(st.session_state.tasks):
    if not t["done"]:
        if st.button(f"✅ {t['text']}", key=f"task_{i}"):
            st.session_state.tasks[i]["done"] = True
            st.session_state.xp += 1

            # Check if dragon is adult
            if st.session_state.xp >= 25:
                st.success("🎉 Your dragon went into the wild! A new egg has appeared.")
                st.session_state.dragons_raised += 1
                st.session_state.xp = 0
                st.session_state.tasks = []

# Clear completed tasks
if st.button("Clear Completed Tasks"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]

import streamlit as st

# Set page config
st.set_page_config(page_title="Dragon Schedule App", layout="centered")

# Session state to keep track of tasks, XP, and dragons raised
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "dragons_raised" not in st.session_state:
    st.session_state.dragons_raised = 0

# Get dragon stage as emoji
def get_dragon_stage(xp):
    if xp < 3:
        return "🥚 Egg"
    elif xp < 7:
        return "🐣 Baby"
    elif xp < 15:
        return "🐉 Kid"
    elif xp < 25:
        return "🔥 Teen"
    else:
        return "🌈 Adult Dragon!"

# App title
st.title("🐲 Your Dragon Schedule")

# Show dragon status
st.subheader(f"Dragon Stage: {get_dragon_stage(st.session_state.xp)}")
st.text(f"XP: {st.session_state.xp} / 25")
st.text(f"Dragons Raised: {st.session_state.dragons_raised}")

# Add new task
task = st.text_input("➕ Add a new task")
if st.button("Add Task"):
    if task.strip():
        st.session_state.tasks.append({"text": task, "done": False})

# Task list
st.subheader("📋 Your Tasks")
for i, t in enumerate(st.session_state.tasks):
    if not t["done"]:
        if st.button(f"✅ {t['text']}", key=f"task_{i}"):
            st.session_state.tasks[i]["done"] = True
            st.session_state.xp += 1

            # Dragon completed!
            if st.session_state.xp >= 25:
                st.success("🎉 Your dragon has grown up and returned to the wild!")
                st.session_state.dragons_raised += 1
                st.session_state.xp = 0
                st.session_state.tasks = []

# Clear finished tasks
if st.button("🗑 Clear Completed Tasks"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]


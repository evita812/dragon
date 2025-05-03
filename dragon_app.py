import streamlit as st

st.set_page_config(page_title="Dragon Schedule App", layout="centered")

# --- Session state setup ---
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "dragons_raised" not in st.session_state:
    st.session_state.dragons_raised = 0

# --- Dragon Stage ---
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

# --- Header ---
st.title("🐲 Your Dragon Schedule")
st.subheader(f"Dragon Stage: {get_dragon_stage(st.session_state.xp)}")
st.write(f"XP: **{st.session_state.xp}** / 25")
st.write(f"Dragons Raised: **{st.session_state.dragons_raised}**")

# --- Add Task ---
new_task = st.text_input("➕ Add a new task")
if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"text": new_task, "done": False})

# --- Task List ---
st.subheader("📋 Your Tasks")

# Create a list to hold updates
task_to_mark_done = None

for i, task in enumerate(st.session_state.tasks):
    if not task["done"]:
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.write(task["text"])
        with col2:
            if st.button("✅ Done", key=f"done_{i}"):
                task_to_mark_done = i

# Apply updates after loop
if task_to_mark_done is not None:
    st.session_state.tasks[task_to_mark_done]["done"] = True
    st.session_state.xp += 1

    if st.session_state.xp >= 25:
        st.success("🎉 Your dragon has grown up and returned to the wild!")
        st.session_state.dragons_raised += 1
        st.session_state.xp = 0
        st.session_state.tasks = []

# --- Clear completed ---
if st.button("🗑 Clear Completed Tasks"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]

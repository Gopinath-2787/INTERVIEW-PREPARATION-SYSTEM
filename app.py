import streamlit as st
from planner import generate_plan
from interviewer import ask_question
from feedback import evaluate_answer
from memory import save_user, load_user

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🤖"
)

st.title("🤖 Personalized Interview Preparation System")
st.sidebar.title("🤖 AI Interview Coach")

st.sidebar.header("🤖 AI Agents")

st.sidebar.success("🧠 Planner Agent")
st.sidebar.success("🎤 Interview Agent")
st.sidebar.success("📊 Feedback Agent")
st.sidebar.success("💾 Memory Agent")

user = load_user()

if user:
    st.sidebar.divider()
    st.sidebar.subheader("Stored Memory")
    st.sidebar.write(f"👤 Name: {user['name']}")
    st.sidebar.write(f"💼 Role: {user['role']}")
    st.sidebar.write(f"🛠 Skills: {user['skills']}")
    st.sidebar.write(f"📚 Weak Topics: {user['weak_topics']}")
from memory import load_user

user = load_user()

if user:
    st.success(f"👋 Welcome back, {user['name']}!")
    st.info(f"🎯 Last Target Role: {user['role']}")

name = st.text_input("Your Name")

role = st.text_input("Target Role")

skills = st.text_area("Your Skills")

weak = st.text_area("Weak Topics")

if st.button("Generate Plan"):

    with st.spinner("Planner Agent is creating your roadmap..."):

        save_user(name, role, skills, weak)
        plan = generate_plan(
            name,
            role,
            skills,
            weak
        )

    st.success("Roadmap Generated!")

    st.markdown(plan)
    st.divider()

st.subheader("🎤 AI Mock Interview")

if st.button("Start Interview"):

    question = ask_question(role)

    st.session_state.question = question

    st.write(question)

if "question" in st.session_state:

    answer = st.text_area("Your Answer")

    if st.button("Submit Answer"):

        with st.spinner("Feedback Agent is evaluating..."):

            feedback = evaluate_answer(
                st.session_state.question,
                answer
            )

        st.success("Evaluation Complete!")

        st.markdown(feedback)
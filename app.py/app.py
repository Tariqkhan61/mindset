import streamlit as st

# Set page configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="★")

# Title and header
st.title("📀 Welcome To My Growth Mindset Challenge")
st.header("🚀 Growth Mindset Challenge: Web App with Streamlit")
st.write(
    "🙌 Face obstacles head-on, discover valuable lessons in your errors, and unlock your limitless potential. "
    "This AI-driven app is designed to nurture a growth mindset by offering thought-provoking reflections, "
    "captivating challenges, and significant accomplishments."
)

# Quote section
st.header("🤗 Today’s Growth Mindset Quote")
st.write(
    "**🧠 Do not let your difficulties fill you with anxiety, after all, it is only in the darkest nights that stars shine more brightly.** "
    "_Mola Ali_"
)

# Challenge section
st.header("🛠 What’s Your Challenge Today?")
user_input = st.text_input("Describe a challenge you are facing:")

if user_input:
    st.success(f"🆚 You are facing: {user_input}. Persistently advance towards your goals, no matter the obstacles.")
else:
    st.warning("Tell us about your challenge to get started.")

# Reflection section
st.header("Reflection on Your Learning")
reflection = st.text_area("Write your outcome here:")

if reflection:
    st.success(f"⛳️ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

# Achievements section
st.header("🎖 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🤽 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now! 😍")

# Footer
st.write("_ _ _")
st.write("Keep believing in yourself. Growth is a journey, not a destination.")
st.write("🔴 🎯 Created By Muhammad Tariq Mahboob ©️®️")
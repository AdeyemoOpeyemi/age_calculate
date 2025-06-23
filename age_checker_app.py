import streamlit as st

st.title("Age Category Checker 🎂")

st.write("👋 Welcome! Please enter your age below to check your age category.")

# Input from user
age_input = st.text_input("Please, enter your age:")

if age_input:
    try:
        Age = int(age_input)

        if 2 <= Age <= 10:
            st.success("You are a child 👶")
        elif 11 <= Age <= 20:
            st.success("You are a teen 🧒")
        elif 21 <= Age <= 30:
            st.success("You are youth 🧑‍🎓")
        elif 31 <= Age <= 40:
            st.success("You are late youth 🧑")
        elif 41 <= Age <= 50:
            st.success("You are a young adult 👨‍💼")
        elif 51 <= Age <= 60:
            st.success("You are an adult 👴")
        elif 61 <= Age <= 70:
            st.success("You are old 🧓")
        else:
            st.success("You are the best! 🏆")
    
    except ValueError:
        st.error("Please, enter a valid number!")

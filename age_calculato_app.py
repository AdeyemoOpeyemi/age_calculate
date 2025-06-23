import streamlit as st
import datetime

st.set_page_config(page_title="Age Calculator", page_icon="🎂")

st.title("🎂 Age Calculator")
st.write("Select your date of birth to find out your age.")

# Ask for date of birth
dob = st.date_input("Date of Birth", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())

# Get today's date
today = datetime.date.today()

if dob > today:
    st.error("Date of birth cannot be in the future.")
else:
    # Age in years
    age_years = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age_years -= 1

    # Age in months
    age_months = (today.year - dob.year) * 12 + (today.month - dob.month)
    if today.day < dob.day:
        age_months -= 1

    # Age in days
    age_days = (today - dob).days


    st.success("🎉 Here are your age details:")
    st.write(f"🗓️ **Years:** {age_years}")
    st.write(f"📆 **Months:** {age_months}")
    st.write(f"📅 **Days:** {age_days}")

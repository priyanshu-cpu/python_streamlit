import streamlit as st

st.title("programming language picker.")
st.subheader("running the first app")
st.text("please choose your language.")
user_choice = st.selectbox("your fav language: ", ["java", "python", "c++", "javascript"])
st.write(f"you choose {user_choice}. Excellent choice.")
st.success("your language has been picked.")
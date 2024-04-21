import streamlit as st

st.title("Find the Largest Number")

# Get input for the three numbers
num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")
num3 = st.number_input("Enter Third Number")

# Find the largest number
largest = max(num1, num2, num3)

# Display the result
if st.button("Find Largest"):
  st.write("The largest number is:", largest)

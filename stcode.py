import streamlit as st

st.title("Statistics Calculator")

st.subheader("Please input 10 numbers: ")
n1 = st.number_input("Please input 1st number: ")
n2 = st.number_input("Please input 2nd number: ")
n3 = st.number_input("Please input 3rd number: ")
n4 = st.number_input("Please input 4th number: ")
n5 = st.number_input("Please input 5th number: ")
n6 = st.number_input("Please input 6th number: ")
n7 = st.number_input("Please input 7th number: ")
n8 = st.number_input("Please input 8th number: ")
n9 = st.number_input("Please input 9th number: ")
n10 = st.number_input("Please input 10th number: ")
lyst = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

if st.button("Mean"):
    meanNum = sum(lyst) / len(lyst)
elif st.button("Median"):
    lyst.sort()
    m1 = lyst[len(lyst) // 2]
    m2 = lyst[len(lyst) // 2 - 1]
    medianNum = (m1 + m2) / 2
elif st.button("Mode")
    frequency = {}
    for i in lyst:
        frequency.setdefault(i, 0)
        frequency[i] += 1
    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            modeNum = i

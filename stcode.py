import streamlit as st

st.title("Statistics Calculator")

st.subheader("Please input 10 numbers: ")
n1 = st.number_input("0.0")
n2 = st.number_input("0.0")
n3 = st.number_input("0.0")
n4 = st.number_input("0.0")
n5 = st.number_input("0.0")
n6 = st.number_input("0.0")
n7 = st.number_input("0.0")
n8 = st.number_input("0.0")
n9 = st.number_input("0.0")
n10 = st.number_input("0.0")
lyst = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

if st.button("Mean"):
    meanNum = sum(lyst) / len(lyst)
elif st.button("Median"):
    lyst.sort()
    m1 = lyst[len(lyst) // 2]
    m2 = lyst[len(lyst) // 2 - 1]
    medianNum = (m1 + m2) / 2
else:
    frequency = {}
    for i in lyst:
        frequency.setdefault(i, 0)
        frequency[i] += 1
    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            modeNum = i

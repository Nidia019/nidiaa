st.title("Statistics Calculator")

st.subheader(text = "Please input 10 numbers: ", row = 0, column = 0)
n1 = st.number_input(value = 0.0, row = 1, column = 0)
n2 = st.number_input(value = 0.0, row = 1, column = 1)
n3 = st.number_input(value = 0.0, row = 1, column = 2)
n4 = st.number_input(value = 0.0, row = 1, column = 3)
n5 = st.number_input(value = 0.0, row = 1, column = 4)
n6 = st.number_input(value = 0.0, row = 1, column = 5)
n7 = st.number_input(value = 0.0, row = 1, column = 6)
n8 = st.number_input(value = 0.0, row = 1, column = 7)
n9 = st.number_input(value = 0.0, row = 1, column = 8)
n10 = st.number_input(value = 0.0, row = 1, column = 9)
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

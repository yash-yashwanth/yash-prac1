import streamlit as st

st.title("Python Mini Programs Showcase")

st.header("1. Area of a Circle")
radius = st.number_input("Enter radius:", min_value=0.0, value=5.0)
area = 3.14 * radius * radius
st.write("Area:", area)

st.header("2. Count Vowels in a String")
s = st.text_input("Enter a string to count vowels:")
if s:
    v = "aeiouAEIOU"
    count = sum(1 for char in s if char in v)
    st.write("Number of vowels:", count)

st.header("3. Count Vowels and Consonants")
text = st.text_input("Enter a string to count vowels and consonants:")
if text:
    v = "aeiouAEIOU"
    vowels = sum(1 for char in text if char in v)
    consonants = len([ch for ch in text if ch.isalpha()]) - vowels
    st.write("Vowels:", vowels)
    st.write("Consonants:", consonants)

st.header("4. Subtract 5 from numbers divisible by 5")
nums_input = st.text_input("Enter numbers separated by space:")
if nums_input:
    n = list(map(int, nums_input.split()))
    for i in range(len(n)):
        if n[i] % 5 == 0:
            n[i] -= 5
    st.write("Updated list:", n)

st.header("5. Split numbers into Even and Odd Indices")
nums_input2 = st.text_input("Enter numbers to split (space-separated):", key="split_input")
if nums_input2:
    n = list(map(int, nums_input2.split()))
    even_idx = [num for i, num in enumerate(n) if i % 2 == 0]
    odd_idx = [num for i, num in enumerate(n) if i % 2 != 0]
    st.write("Even indices:", even_idx)
    st.write("Odd indices:", odd_idx)

st.header("6. Sum of Even and Odd Indices")
nums_input3 = st.text_input("Enter numbers (space-separated):", key="sum_input")
if nums_input3:
    n = list(map(int, nums_input3.split()))
    se = sum(num for i, num in enumerate(n) if i % 2 == 0)
    so = sum(num for i, num in enumerate(n) if i % 2 != 0)
    st.write("Sum of Even indices:", se)
    st.write("Sum of Odd indices:", so)

st.header("7. Sum of Indices based on Even/Odd Values")
nums_input4 = st.text_input("Enter numbers (space-separated):", key="index_input")
if nums_input4:
    n = list(map(int, nums_input4.split()))
    e = sum(i for i, num in enumerate(n) if num % 2 == 0)
    o = sum(i for i, num in enumerate(n) if num % 2 != 0)
    st.write("Sum of indices of even numbers:", e)
    st.write("Sum of indices of odd numbers:", o)

st.header("8. Filter Cities Starting with D or d")
li = ["Mumbai", "Hyd", "delhi", "Dubai", "Jaipur", "Kolkata", "Dadar", "Danish"]
filtered = [city for city in li if city[0].lower() == "d"]
st.write("Cities starting with D/d:", filtered)

st.header("9. Cities with value < 100")
a = {
    'Mumbai': 50, 'Hyd': 40, 'delhi': 30, 'Dubai': 20,
    'Jaipur': 100, 'Kolkata': 250, 'Dadar': 200, 'chenn': 280
}
b = [city for city, value in a.items() if value < 100]
st.write("Cities with value < 100:", b)

st.success("All programs executed interactively with Streamlit.")

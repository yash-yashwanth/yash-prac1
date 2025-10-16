import streamlit as st
import numpy as np

st.title("NumPy Demonstration")

st.header("1. Creating a 1D NumPy Array")
arr1 = np.array([1, 2, 3, 4, 5])
st.write("Array:", arr1)
st.write("Type:", type(arr1))
st.write("Size:", arr1.size)
st.write("Dimensions:", arr1.ndim)
st.write("Shape:", arr1.shape)

st.header("2. Multi-dimensional Array Example")
my_matrix = [[2, 3, 4.5, 4], [3, 5, 43, 64], [5, 6.6, 45, 4]]
b = np.array(my_matrix)
st.write("Matrix:", b)
st.write("Dimensions:", b.ndim)
st.write("Size:", b.size)
st.write("Shape:", b.shape)

st.header("3. Integer Arrays with Different Data Types")
int8_arr = np.array([1, 2, 3], dtype=np.int8)
int16_arr = np.array([1003, -2000, 3000], dtype=np.int16)
int32_arr = np.array([1003000, -2000000, 300000], dtype=np.int32)
int64_arr = np.array([1003000000, -200000000, 30000000], dtype=np.int64)

st.write("int8 array:", int8_arr, "dtype:", int8_arr.dtype)
st.write("int16 array:", int16_arr, "dtype:", int16_arr.dtype)
st.write("int32 array:", int32_arr, "dtype:", int32_arr.dtype)
st.write("int64 array:", int64_arr, "dtype:", int64_arr.dtype)

st.header("4. Float Arrays with Different Data Types")
float16_arr = np.array([1.1, -2.2, 3.3], dtype=np.float16)
float32_arr = np.array([1.112345, -2.212345, 3.321123], dtype=np.float32)
float64_arr = np.array([1.5434534541, -2.2123456789, 0.31234234567], dtype=np.float64)

st.write("float16 array:", float16_arr, "dtype:", float16_arr.dtype)
st.write("float32 array:", float32_arr, "dtype:", float32_arr.dtype)
st.write("float64 array:", float64_arr, "dtype:", float64_arr.dtype)

st.header("5. Complex Arrays")
complex64_arr = np.array([1+2j, 3+4j], dtype=np.complex64)
complex128_arr = np.array([1+2j, 3+4j], dtype=np.complex128)

st.write("complex64 array:", complex64_arr, "dtype:", complex64_arr.dtype)
st.write("complex128 array:", complex128_arr, "dtype:", complex128_arr.dtype)

st.header("6. Boolean Array")
bool_arr = np.array([True, False, True], dtype=bool)
st.write("Boolean array:", bool_arr)
st.write("Data type:", bool_arr.dtype)

st.header("7. String Array")
string_arr = np.array(["apple", "banana", "cherry"], dtype='<U10')
st.write("String array:", string_arr)
st.write("Data type:", string_arr.dtype)

st.header("8. Object Array (Mixed Data Types)")
object_arr = np.array([1, "two", 3.0, True], dtype=object)
st.write("Object array:", object_arr)
st.write("Data type:", object_arr.dtype)

st.success("NumPy examples displayed successfully with Streamlit.")

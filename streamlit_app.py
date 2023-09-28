from collections import namedtuple
import altair as alt
import math
import pandas as pd
import numpy as np
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

def plot_normal_distribution(mean, variance):
    x = np.linspace(-10, 10, 500)
    y = (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-(x - mean)**2 / (2 * variance))

    df = pd.DataFrame({"x": x, "y": y})

    chart = alt.Chart(df).mark_line().encode(
        x='x',
        y='y'
    ).properties(
        width=300,
        height=300
    )

    return chart

def plot_hyperbolic_function(a, b):
    x = np.linspace(-10*a, 10*a, 500)
    y = b * np.sqrt(1 + (x**2 / a**2))

    df = pd.DataFrame({"x": x, "y": y})

    chart = alt.Chart(df).mark_line().encode(
        x='x',
        y='y'
    ).properties(
        width=300,
        height=300
    )

    return chart

# Streamlit 应用程序
st.title("Distribution Visualization")

# 调节正态分布函数的均值和方差
mean = st.slider("Mean", -5.0, 5.0, 0.0, 0.1)
variance = st.slider("Variance", 0.1, 5.0, 1.0, 0.1)

# 绘制正态分布函数
st.subheader("Normal Distribution")
normal_chart = plot_normal_distribution(mean, variance)
st.altair_chart(normal_chart)

# 调节双曲线函数的参数
a = st.slider("Parameter a", 0.1, 5.0, 1.0, 0.1)
b = st.slider("Parameter b", 0.1, 5.0, 1.0, 0.1)

# 绘制双曲线函数
st.subheader("Hyperbolic Function")
hyperbolic_chart = plot_hyperbolic_function(a, b)
st.altair_chart(hyperbolic_chart)

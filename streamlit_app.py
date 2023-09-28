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
        width=500,
        height=300
    )

    st.altair_chart(chart)

# Streamlit 应用程序
st.title("Normal Distribution Visualization")

# 调节均值和方差
mean = st.slider("Mean", -5.0, 5.0, 0.0, 0.1)
variance = st.slider("Variance", 0.1, 5.0, 1.0, 0.1)

# 绘制正态分布函数
st.subheader("Normal Distribution")
plot_normal_distribution(mean, variance)

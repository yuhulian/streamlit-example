from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))

import numpy as np
import matplotlib.pyplot as plt

def plot_fourier_transform(signal):
    # 进行傅里叶变换
    fft_result = np.fft.fft(signal)
    freq = np.fft.fftfreq(len(signal))

    # 绘制频谱
    plt.figure(figsize=(8, 6))
    plt.stem(freq, np.abs(fft_result))
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("Fourier Transform - Frequency Spectrum")
    st.pyplot()

# Streamlit 应用程序
st.title("Fourier Transform Visualization")

# 生成正弦波信号
frequency = st.slider("Frequency", 1, 100, 5)  # 频率滑动条
time = np.linspace(0, 1, 1000)  # 时间范围为 0 到 1，总共 1000 个点
signal = np.sin(2 * np.pi * frequency * time)  # 正弦波信号

# 绘制时域信号
st.subheader("Time Domain Signal")
st.line_chart(signal)

# 绘制频谱
st.subheader("Frequency Spectrum")
plot_fourier_transform(signal)

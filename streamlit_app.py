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

def plot_fourier_transform(signal):
    # 进行傅里叶变换
    fft_result = np.fft.fft(signal)
    freq = np.fft.fftfreq(len(signal))

    # 创建频谱数据框
    df = pd.DataFrame({"Frequency": freq, "Magnitude": np.abs(fft_result)})

    # 绘制频谱图
    chart = alt.Chart(df).mark_circle(color='#0068c9', opacity=0.5).encode(
        x='Frequency:Q',
        y='Magnitude:Q'
    ).properties(
        width=500,
        height=500
    )

    st.altair_chart(chart)

# Streamlit 应用程序
st.title("Fourier Transform Visualization")

# 生成正弦波信号
frequency = st.slider("Frequency", 1, 100, 5)  # 频率滑动条
time = np.linspace(0, 1, 1000)  # 时间范围为 0 到 1，总共 1000 个点
signal = np.sin(2 * np.pi * frequency * time)  # 正弦波信号

# 绘制时域信号
st.subheader("Time Domain Signal")
st.line_chart(pd.DataFrame({"Time": time, "Amplitude": signal}))

# 绘制频谱
st.subheader("Frequency Spectrum")
plot_fourier_transform(signal)

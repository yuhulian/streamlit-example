from collections import namedtuple
import altair as alt
import math
import pandas as pd
import numpy as np
import streamlit as st
import cv2
import matplotlib.pyplot as plt

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def laplacian_transform(image, laplacian_ksize):
    laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=laplacian_ksize)
    return laplacian

# Streamlit 应用程序
st.title("Image Processing")

# 上传图像文件
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 读取上传的图像文件
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)

    # 灰度化
    gray_image = grayscale(image)

    # 调节拉普拉斯变换的参数
    laplacian_ksize = st.slider("Laplacian Kernel Size", 3, 15, 3)

    # 拉普拉斯变换
    laplacian_image = laplacian_transform(gray_image, laplacian_ksize)

    # 显示原始图像和处理后的图像
    st.subheader("Original Image")
    st.image(image, channels="BGR")

    st.subheader("Grayscale Image")
    st.image(gray_image, cmap="gray")

    st.subheader("Laplacian Transformed Image")
    st.image(laplacian_image, cmap="gray")

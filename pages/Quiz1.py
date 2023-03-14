import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt


def orig(picture):
    height, width = picture.shape[:2]

    plt.axis('off')
    plt.imshow(image)
    st.image(translated_img)


def translation_1(picture, bx, by, tx, ty):
    height, width = picture.shape[:2]
    
    bx = 0
    by = 0
    nx = bx + tx
    ny = by + ty

    m_translation_ = np.float32([[1,0,nx],
                                 [0,1,ny]])
    translated_img_ = cv2.warpAffine(picture, m_translation_, dsize=(width,height))

        plt.axis('off')
        plt.imshow(translated_img_)
        st.image(translated_img)

def main():
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image", use_column_width=True)

    # picture = ["pic1.jpg", "pic2.jpg", "pic3.jpg", "pic4.jpeg", "pic5.png"]
    bx = st.number_input("How much would you like x to move?:")
    by = st.number_input("How much would you like y to move?:")
    tx = st.number_input("How much would you like x to move?:")
    ty = st.number_input("How much would you like y to move?:")

    for p in image:
        img_ = cv2.imread(image)
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        orig(img_)
        translation_1(img_, bx, by, tx, ty)

main()

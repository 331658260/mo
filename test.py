import pandas as pd
import numpy as np
import pickle
import streamlit as st

from PIL import Image

  # loading in the model to predict on the data

model = open('model.pkl', 'rb')

classifier = pickle.load(model)

def welcome():

    return 'welcome all'

  # defining the function which will make the prediction using

# the data which the user inputs

def prediction(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,
               a11,a12,a13,a14,a15,a16,a17,a18,
               a19,a20,a21,a22,a23,a24,a25,a26,
               a27,a28,a29,a30,a31,a32,a33,a34,a35):

    prediction = classifier.predict(
    [[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,
    a11,a12,a13,a14,a15,a16,a17,a18,
    a19,a20,a21,a22,a23,a24,a25,a26,
    a27,a28,a29,a30,a31,a32,a33,a34,a35]])

    print(prediction)
    return prediction

        # this is the main function in which we define our webpage

def main():

      # giving the webpage a title

    st.title("土地价格预测")

          # here we define some of the front end elements of the web page like

    # the font and background color, the padding and the text to be displayed

    html_temp = """

    <div style ="background-color:yellow;padding:13px">

    <h1 style ="color:black;text-align:center;">样点地价预测部署平台</h1>

    </div>

    """

          # this line allows us to display the front end aspects we have

    # defined in the above code

    st.markdown(html_temp, unsafe_allow_html = True)

          # the following lines create text boxes in which the user can enter

    # the data required to make the prediction

    a1 = st.number_input("级别", 1)

    a2 = st.number_input("功能分", 100)

    a3 = st.number_input("等级", 2)

    a4 = st.number_input("面积_1", 112466.8)

    a5 = st.number_input("折现年份", 0)

    a6 = st.number_input("设定功能分", 80)

    a7 = st.number_input("贴现系数", 1)

    a8 = st.number_input("等级_1", 2)

    a9 = st.number_input("级别价", 2558)

    a10 = st.number_input("距车站距离", 550)

    a11 = st.number_input("级别价评估", 2460)

    a12 = st.number_input("区片价评估", 2558)

    a13 = st.number_input("测算容积率", 2.5)

    a14 = st.number_input("用途_E", 5)

    a15 = st.number_input("乡镇名称_E", 18)

    a16 = st.number_input("名称_E", 7)

    a17 = st.number_input("规划用途_E", 25)

    a18 = st.number_input("开发程度_E", 14)

    a34 = st.number_input("规划用途_1_E", 25)

    a35 = st.number_input("开发程度_1_E", 14)

    a19 = st.number_input("分类_E", 3)

    a20 = st.number_input("主要区域_E", 4)

    a21 = st.number_input("DLBM_E", 14)

    a33 = st.number_input("DLMC_E", 14)

    a22 = st.number_input("ZLDWMC_E", 65)

    a23 = st.number_input("BZ_E",4)

    a24 = st.number_input("用途_1_E",5)

    a25 = st.number_input("区片_E", 43)

    a26 = st.number_input("容积率_1_E", 31)

    a27 = st.number_input("商服评价_E", 7)

    a28 = st.number_input("市场评价_E", 7)

    a29 = st.number_input("车站评价_E", 6)

    a30 = st.number_input("银行评价_E", 9)

    a31 = st.number_input("文娱评价_E", 8)

    a32 = st.number_input("评估用途_E", 15)


    result =""

          # the below line ensures that when the button called 'Predict' is clicked,

    # the prediction function defined above is called to make the prediction

    # and store it in the variable result

    if st.button("预测结果"):

        result = prediction(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,
               a11,a12,a13,a14,a15,a16,a17,a18,
               a19,a20,a21,a22,a23,a24,a25,a26,
               a27,a28,a29,a30,a31,a32,a33,a34,a35)
    st.success('样点地价的预测值为 {}'.format(result))

if __name__=='__main__':

    main()

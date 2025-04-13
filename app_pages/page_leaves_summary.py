import streamlit as st
import matplotlib.pyplot as plt

# code for Data Visualization and its functions were adapted
# and taken from Walkthrough Project 01 Malaria Detector


def page_leaves_summary_body():
    """
    display the projects summary and additional
    information on the dashboard
    """

    st.header("Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew is among the most prevalent crop diseases "
        f"worldwide. Especially for the agricultural sector, eg. "
        f"for cherry trees, this infection can cause great harm to "
        f"crops and minimize the harvest. That is why it is "
        f"important to manage an easily applicable way of visually "
        f"identifying powderdy mildew, which so far takes too much "
        f"time to be done manually and is hence too costly.\n\n"
        f"\nFirst, what exactly is powdery mildew in sweet and sour "
        f"cherries:\n\n* a parasitic fungal disease that is caused "
        f"by Podosphaera clandestina\n* mid- and late-season cherries "
        f"are most commonly affected and become non-sellable\n"
        f"* primary infection is initiated by temperatures above 10°C "
        f"& high humidity and temperatures (21°C - 26°C) will favor the "
        f"disease\n* Infected plants display white powdery spots on the "
        f"leaves and stems \n\n\nOur client experienced a serious outbreak "
        f"and we hence developed a program to detect infected "
        f"leaves via visual distinction from healthy leaves.\n\n"
        f"These dashboards give our client the insight of powdery mildew "
        f"detection as well as the possibility to upload images and "
        f"predict whether they are infected or not, "
        f"which will save time and hence reduces the cost of quality "
        f"control of the crops.\n\n"
        )

    st.warning(
        f"**Project Dataset**\n\n"
        f"The dataset contains 2104 healthy leaves and 2104 powdery mildew "
        f"infected leaves , so 4208 in total It can be downloaded from "
        f"[Kaggle]"
        f"(https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)"
        )

    st.write(
        f"For more information on how the model was created and on the "
        f"general process of this project please read through the "
        f"documentation in this project's  [README file]"
        f"(https://github.com/Xakkusu/PP5-mildew-detection)"
        )

    st.success(
        f"The business requirements for this project are:\n\n"
        f"**1.** The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that "
        f"contains powdery mildew. \n\n**2.** The client is interested in "
        f"predicting a cherry tree is healthy or contains powdery mildew.\n\n"
        )

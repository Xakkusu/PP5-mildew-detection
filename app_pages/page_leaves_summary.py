import streamlit as st
import matplotlib.pyplot as plt

# code for Data Visualization and its functions were adapted and taken from Walkthrough Project 01 Malaria Detector 
def page_leaves_summary_body():

    st.header("Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew is among the most prealent crop diseases worldwide. Especially for the agricultural "
        f"sector, eg. for cherry trees, this infection can cause great harm to corps and minimize the harvest. "
        f"That is why it is important to manage an easy applicable way of visually identifying "
        f"powderdy mildew, which so far takes too much time to be done manually and is hence to costly.\n\n"
        f"\nFirst, what exactly is powdery mildew in sweet and sour cherries:\n\n"
        f"* a parasitic fungal disease that is caused by Podosphaera clandestina\n"
        f"* mid- and late-season cherries are most commonly affected and become non-sellable\n"
        f"* primary infection is initiated by temperatures above 10°C "
        f"& high humidity and temperatures (21°C - 26°C) will favor the disease\n"
        f"* Infected plants display white powdery spots on the leaves and stems \n\n"
        f"\nOur client experienced a serious outbreak and we hence developed a programm "
        f"to detect infected leaves via visual distinction from healthy leaves.\n\n"
        f"These dashboards give our client the insight of powdery mildew detection "
        f"as well as the possibility to upload images and predict whether they are infected or not, "
        f"which will save time and hence reduces the cost of quality control of the crops.\n\n")
    
    st.warning(
        f"**Project Dataset**\n\n"
        f"The dataset contains 2104 healthy leaves and 2104 powdery mildew infected leaves , so 4208 in total"
        f"It can be downloaded from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)")

    st.write(
        f"For more information on how the model was created and on the general process of this "
        f"project please read through the documentation in this project's "
        f"[README file](https://github.com/Xakkusu/PP5-mildew-detection)")
    

    st.success(
        f"The business requirements for this project are:\n\n"
        f"**1.** The client is interested in conducting a study to visually differentiate a cherry leaf "
        f"that is healthy from one that contains powdery mildew. \n\n"
        f"**2.** The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.  \n\n")
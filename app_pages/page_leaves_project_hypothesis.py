# code for Data Visualization and its functions were adapted and taken from Walkthrough Project 01 Malaria Detector 

import streamlit as st
import matplotlib.pyplot as plt


def page_leaves_project_hypothesis_body():
    """
    display the projects hypothgesis
    """
    st.header("Project Hypothesis and Validation")
    
    st.write("### Hypothesis")

    st.success(
        f"* We suspect that leaves that are infected by mildew have a visible differentiation from "
        f"non-infected leaves which commonly looks like a white powdery substance on the leaves. \n"
        f"This way we can differentiate healthy from infected leaves through an ML model with an "
        f"average image study using image classification, a binary classifier with an 97 % accuracy.*\n"
    )

    st.write("---")

    st.write("### Validation")

    st.info(
        f" We were able to create a model with an **99,66%** accuray to predict whether "
        f"an image of a leaf has powdery mildew on the leaf or not.\n\n"
        f"**With this accuracy we were able to prove our hypothesis that there is a visible differentiation "
        f"from non-infected leaves and powdery mildew infected leaves on which our ML model was build on.**"
    )
    
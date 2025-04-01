# code for Data Visualization and its functions were adapted and taken from Walkthrough Project 01 Malaria Detector 

import streamlit as st
import matplotlib.pyplot as plt


def page_leaves_project_hypothesis_body():
    """
    display the projects hypothgesis
    """
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect that leaves that are infected by mildew have a visible differentiation from "
        f"non-infected leaves which commonly looks like a white powdery substance on the leaves. \n"
        f"This way we can differentiate healthy from infected leaves with an "
        f"with an average image study using image classification, a binary classifier with an 97 % accuracy.\n"
        f"fill this in later"
    )

    
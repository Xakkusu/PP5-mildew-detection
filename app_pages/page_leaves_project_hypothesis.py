#code for Data Visualization and its functions were adapted and taken from Walkthrough Project 01 Malaria Detector 

import streamlit as st
import matplotlib.pyplot as plt


def page_leaves_project_hypothesis_body():
    """
    display the projects hypothgesis
    """
    st.header("Project Hypotheses and Validation")

    st.write("#### Hypothesis 1")

    st.success(
        f"* We suspect that there is a visual difference between healthy "
        f"and mildew-infected leaves."
    )


    st.write("#### Validation 1")

    st.info(
        f"Even though it was not a significant difference to the human eye "
        f"there was a slight visual difference as can be seen on the average "
        f"and variability images."
    )
    
    st.write("---")
    
    st.write("#### Hypothesis 2")

    st.success(
        f"* We suspect that the visual differentiation manifests in that leaves "
        f"that are infected by mildew have a visible differentiation from non-infected "
        f"leaves which commonly looks like a white powdery substance on the leaves "
        f"compared to healthy green leaves."
    )


    st.write("#### Validation 2")

    st.info(
        f"As can be seen on the leaves visualizer dashboard the mildew infected "
        f"leaves have white powdery spots on its topcoat and they are less "
        f"vibrant/saturated greenish than the healthy leaves images."
    )
    
    st.write("---")

    st.write("#### Hypothesis 2")

    st.success(
        f"We suspect that we can differentiate healthy from infected leaves through an ML model with an "
        f"average image study using image classification, a binary classifier with an 97 % accuracy.*\n"
    )

    st.write("#### Validation 2")

    st.info(
        f"We were able to create a model with an **98,93%** accuray to predict whether "
        f"an image of a leaf has powdery mildew on the leaf or not.\n\n"
        f"**With this accuracy we were able to prove our hypothesis that there is a visible differentiation "
        f"from non-infected leaves and powdery mildew infected leaves on which our ML model was built on. "
        f"Even though to the human eyes the pattern of the average/variability images was not that significant "
        f"Using the ML-model will minimize human error during harvest.**"
    )
    
    st.write("---")
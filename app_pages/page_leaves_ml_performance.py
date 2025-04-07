# code for Data Visualization and its functions were adapted and taken from Walkthrough Project 01 Malaria Detector 

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_leaves_ml_performance_body():
    version = 'v2'

    st.header("Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    pie_chart_distr = plt.imread(f"outputs/{version}/image_distribution_piechart.png")
    st.image(pie_chart_distr, caption='Dataets Distribution into Train-, Validation- and Test-Set')

    st.info(
        f"Our dataset was split into 70% train- 20% validation- & 10% test-set. In each set the "
        f"images are evenly distributed between both labels."
    )

    st.write("---")

    #add more content and explain model performance
    st.write("### Model History")
    col1, col2 = st.columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.info(
        f"The model was able to achieve a high accuracy and low losses. To "
        f"not overfit the model, the fitting process was stopped at 6 epochs."
    )
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

    st.info(
        f"Our model achieved an accuracy rate of **98,93%** which fulfills the "
        f"second business requirement of 97%."
    )
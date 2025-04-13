# code for Data Visualization and its functions were adapted
# and taken from Walkthrough Project 01 Malaria Detector

import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
    )


def page_leaves_detector_body():
    """"
    This function creates the ability for the user to upload their own PNG
    image and detect through the model if there is powdery mildew
    present on  the image or not
    """
    st.header("Powdery Mildew Detection Tool")

    st.info(
        f"Our client is interested in detecting whether a leaf in an "
        f"image is powdery-mildew infected or not."
        )

    st.warning(
        f"If you do not have your own cherry leaf image to run the d"
        f"etection on, please download an image from the [Kaggle]"
        f"(https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) "
        f"dataset and use it below.\n\n"
        f"*As our model was built on this dataset so we know the format of "
        f"them works and this format can be applied on the client images.*"
        )

    st.write("---")

    images_buffer = st.file_uploader('Upload a leaf sample image (.png). ' +
                                     'You may select more than one.',
                                     type='png',  accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Leaf image: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil,
                     caption=f"Image Size: {img_array.shape[1]}px " +
                     "width x {img_array.shape[0]}px height")

            version = 'v2'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report._append({"Name": image.name,
                                          'Result': pred_class},
                                          ignore_index=True)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report),
                        unsafe_allow_html=True)

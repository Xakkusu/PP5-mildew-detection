import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

# code for Data Visualization and its functions were adapted
# and taken from Walkthrough Project 01 Malaria Detector


def page_leaves_visualizer_body():
    """
    This function displays the difference between average and variability
    of healthy and mildew infected images, as well as calling the
    image_montage function
    """
    st.header("Mildew Leaves Visualizer")

    st.write(
        f"For more information on how the model was created and on the "
        f"general process of this project please read through the "
        f"documentation in this project's [README file]"
        f"(https://github.com/Xakkusu/PP5-mildew-detection)"
        )

    st.info(
        f"As mentioned in the business requirements our client, Farmy "
        f"& Foods, is interested in a model which can differentiate "
        f"visually between a powdery mildew infected leaf image "
        f"and a healthy one.\n\n Different analyses were conducted "
        f"to analyze possible factors that differ between the two types."
        )

    st.success(
        f"This dashboards focuses on answering the first business "
        f"requirement:\n\n **The client is interested in conducting "
        f"a study to visually differentiate a cherry leaf that is "
        f"healthy from one that contains powdery mildew**"
    )

    st.write("---")

    version = 'v2'
    if st.checkbox("**Difference between average and variability image**"):
        avg_mildew = plt.imread(
           f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_healthy = plt.imread(
           f"outputs/{version}/avg_var_healthy.png")

        st.warning(
          f"We notice the average and variability images did not show "
          f"strong significant patterns where we could intuitively "
          f"differentiate one from another.\n\n *Yet, the mildew "
          f"infected one has a whitish looking top-powder instead of being "
          f"vibrant green like the healthy one which can be used for "
          f"the model.*"
          )

        st.image(avg_mildew,
                 caption='Mildew Infected Leaf - Average and Variability')
        st.image(avg_healthy,
                 caption='Healthy Leaf - Average and Variability')
        st.write("---")

    if st.checkbox("**Differences between average mildew " +
                   "infected and average healthy leaves**"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
          f"We notice that this analysis didn't show a strong significant "
          f"pattern to differentiate healthy- and infected leaves from one "
          f"another.\n\n *Yet again, there is a slight difference, "
          f"where the mildew infected average image displays a pattern "
          f"where we can somehow differentiate it from the healthy one "
          f"due to the slightly white top coat spots*.")
        st.image(diff_between_avgs,
                 caption='Difference between average images')

    # created our image montage
    if st.checkbox("**Show Image Montage of mildew infected or " +
                   "average healthy leaves**"):
        st.write("* To refresh the montage, click on the " +
                 "'Create Montage' button")
        my_data_dir = 'inputs/dataset/cherry_leaves_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label",
                                        options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows,
                  ncols, figsize=(15, 10)):
    """
    Create image montage to visualize used data
    """
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:
        # checks if your montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path + '/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0],
                 plot_idx[x][1]].set_title(
                     f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
        # plt.show()

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")

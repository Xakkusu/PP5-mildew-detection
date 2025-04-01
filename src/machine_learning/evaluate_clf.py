# code for Data Visualization and its functions were adapted and taken from Walkthrough Project 01 Malaria Detector 

import streamlit as st
from src.data_management import load_pkl_file


def load_test_evaluation(version):
    return load_pkl_file(f'outputs/{version}/evaluation.pkl')
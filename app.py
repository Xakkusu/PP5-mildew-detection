# import streamlit and Multioage
import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_leaves_summary import page_leaves_summary_body
from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
from app_pages.page_leaves_detector import page_leaves_detector_body
from app_pages.page_leaves_project_hypothesis import page_leaves_project_hypothesis_body
from app_pages.page_leaves_ml_performance import page_leaves_ml_performance_body

app = MultiPage(app_name="Mildew Detetor")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Mildew Project Summary", page_leaves_summary_body)
app.add_page("Leaves Visualizer", page_leaves_visualizer_body)
app.add_page("Mildew Detection", page_leaves_detector_body)
app.add_page("Project Hypothesis", page_leaves_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_leaves_ml_performance_body)

app.run()  # Run the app
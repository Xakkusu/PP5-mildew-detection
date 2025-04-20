
# Mildew Detection in Cherry Tree Leaves

[Mildew Detector - Deployed Website](https://pp5-mildew-detection.onrender.com/)

This "Mildew Detector" project used machine learning to predict whether cherry leaves on uploaded images are mildew-infected or not.
Powdery mildew is among the most prevalent crop diseases worldwide. Especially for the agricultural sector, eg. for cherry trees, this infection can cause great harm to crops and minimize the harvest. 
While farmers face an increasing number of hurdles during their work, especially with accelerating climate factors, there are some topics where machine learning models can take pressure from other time consuming daily tasks.
That is why it is important to manage an easily applicable way of visually identifying powdery mildew, which so far takes too much time to be done manually and is hence too costly.

Our dashboards serve our client, Farmy & Foods (a fictitious company), in giving a short overview of the models performance, as well as the ability to upload images and download a report with the prediction on which their employees can then decide which trees need treatment and which do not. Maximizing time efficiency and reducing costs.

![Mildew Detector Am I Responsive screenshot](docs/am-i-responsive-mildew-detector.png)

## Contents
- [Mildew Detection in Cherry Tree Leaves](#mildew-detection-in-cherry-tree-leaves)
  - [Contents](#contents)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Project Hypotheses and Validation](#project-hypotheses-and-validation)
    - [Hypothesis \& Validation 1](#hypothesis--validation-1)
    - [Hypothesis \& Validation 2](#hypothesis--validation-2)
    - [Hypothesis \& Validation 3](#hypothesis--validation-3)
  - [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
  - [User Experience](#user-experience)
  - [ML Business Case](#ml-business-case)
  - [Dashboard Design](#dashboard-design)
    - [Summary Page](#summary-page)
    - [Leaves Visualizer Page](#leaves-visualizer-page)
    - [Mildew Detection Page](#mildew-detection-page)
    - [Project Hypothesis Page](#project-hypothesis-page)
    - [ML Performance Metrics Page](#ml-performance-metrics-page)
  - [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Preparations](#preparations)
    - [Render](#render)
    - [How to fork/clone the project locally on Github:](#how-to-forkclone-the-project-locally-on-github)
  - [Testing](#testing)
  - [Frameworks, Libraries and Programs used](#frameworks-libraries-and-programs-used)
  - [Credits \& Resources](#credits--resources)
    - [Content](#content)
    - [Other student's repositories](#other-students-repositories)
    - [Resources](#resources)
  - [Acknowledgements](#acknowledgements)


## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains more than 4,000 images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.
- The dataset was provided by Code Institute, so further research if the data is credible and if we are allowed to use it was not conducted. Ideally our client could provide us in the future with updated image data, so we can train our model with even more accuracy created from and for their products.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Project Hypotheses and Validation

### Hypothesis & Validation 1

> 1. Hypothesis: We suspect that there is a visual difference between healthy and mildew-infected leaves.

We built an average image study with images of healthy and powdery mildew infected leaves.

**Outcome**: Even though it was not a significant difference to the human eye there was a slight visual difference as can be seen on the average and variability images

.


### Hypothesis & Validation 2

> 2. Hypothesis: We suspect that the visual differentiation manifests in that leaves that are infected by mildew have a visible differentiation from non-infected leaves which commonly looks like a white powdery substance on the leaves compared to healthy green leaves.

In an image study we plot the average images next to one another to compare how they look like and we create an image montage for each label to see similiarities between singular images of the same label.

**Outcome**: As can be seen on the leaves visualizer dashboard the mildew infected leaves have white powdery spots on its topcoat and they are less vibrant/saturated greenish than the healthy leaves images.


### Hypothesis & Validation 3

> 3. Hypothesis: We suspect that we can differentiate healthy from infected leaves through an ML model with an 97 % accuracy.

We create a machine learning model with an average image study using image classification, a binary classifier, the sigmoid activation function  

**Outcome**: We were able to create a model with an 98,93% accuray to predict whether an image of a leaf has powdery mildew on the leaf or not.
With this accuracy we were able to prove our hypothesis that there is a visible differentiation from mildew infected leaves on which our ML model was built on. Even non-infected leaves and powdery to the human eyes the pattern of the though average/variability images was not that significant using the ML-model will minimize human error during harvest.


## The rationale to map the business requirements to the Data Visualisations and ML tasks

**Business requirement 1 - Data Visualization**

The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

* First we clean and prepare the data to be used in Data Visualization.
* The visualization made it possible to see and understand patterns in the data, even if they were not significant beforehand. The data quality was enhanced and ensured.
* The outputs from this step were used in the accordingly named dashboard where the user can see the average and difference within the dataset/within the labels. Hence they were visually differentiated between a healthy cherry leaf image and between an image with powdery mildew.


**Business requirement 2 - Machine Learning**

The client is interested in predicting if a cherry tree is healthy or contains powdery mildew. 

* First we focused on what functions etc. to use for our model according to our business case.
* We used our before splitted dataset (split into test- train & validation set) which were labeled into healthy and powdery_mildew images.
* We trained and optimized the model through these datasets.
* We validated our model to see if it is accurate for real time prediction.
* We created a dashboard to display our model's performance for the client to see how effective the model is.
* We created a dashboard to conduct the prediction on uploaded images and for the user to download a report about this prediction.

## User Experience

## ML Business Case

- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.


## Dashboard Design

### Summary Page

![Summary Page Screenshot](docs/dashboard-design/summary-page-dd.png)

- We provide a quick summary of the project, what business case our models works towards, give information about the dataset and go over the business requirements.
- The user should know all important points about the project and what problem the model will help solve.
- A link to the database as well as to the README of this project is provided as well.

### Leaves Visualizer Page

![Data Visualizer Page Screenshot](docs/dashboard-design/visualizer-page-dd.png)

- This page handels the first business requirement: **The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.** The client can hence further use this page for their requirement.

![Data Visualizer Checkbox Selection Page Gif](docs/dashboard-design/visualizer-checkboxDD.gif)

- By checking off the checkboxes the user can go through various images:
  - Difference between average and variability image - images are displayed side by side and on top of one another to compare them
  - Differences between average mildew infected and average healthy leaves - images are displayed side by side to compare them
  - Image Montage -choose label from dropdown menu and the montage will appear
- The machine learning model is built on these findings.

### Mildew Detection Page

![Mildew Detection Page Screenshot](docs/dashboard-design/detector-page-dd.png)

- This page handels the second business requirement: **The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.** The client can hence further use this page for future images to run detection on.
- The user can upload PNG images to detect whether powdery mildew is present or not.
- A link to the dataset it provided in case the user does not have their own image to draw a report from.

![Mildew Detection Page Screenshot](docs/dashboard-design/detector1-page-dd.png)
![Mildew Detection Page Screenshot](docs/dashboard-design/detector2-page-dd.png)

- The user can upload as many PNG-images as they like.
- For every singular image there is a message about the powdery-mildew status and a diagram.
- At the bottom of the page the user can download their report.

### Project Hypothesis Page

![Hypothesis Page Screenshot](docs/dashboard-design/hypotheses-page-dd.png)

- This page provides an explanation of our assumptions before starting our project, as shown in our three hypotheses.
- After finishing our Model we drew our conclusions in the validation sections on how and why they were validated.
- You can read more on our hypothesis [here](#project-hypotheses-and-validation).

### ML Performance Metrics Page

![ML Performance Metrics Page Screenshot](docs/dashboard-design/performance1-page-dd.png)
![ML Performance Metrics Page Screenshot](docs/dashboard-design/performance2-page-dd.png)

- This page provides more insights into our model and the data that was used.
- We display the label frequencies and how our datasets are divided.
- We display our accuracy and models over epochs shown in the diagrams.
- We display our accuracy which is vital for answering the second business requirement as well as our third hypothesis.


## Bugs

### Fixed Bugs

### Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Preparations

- Store all dependencies in ``requirements.txt`` file.

### Render

> OPTIONAL

- Delete Procfile
- Delete runtime.txt
- Add, commit, and push your changes to GitHub

> MANDATORY

1. Log in to Render (your github account needs to be connected to your render account) and click on new.
2. Select Web Service
3. Search the name of the desired repository and connect it.
4. Check for the settings to match:
   - Set the Name
   - Leave root directory blank
   - Define Python 3 as the environment
   - Set the region to your region
   - Set Branch to main
5. Set the build command ``pip install -r requirements.txt && ./setup.sh``.
6. Set the start command ``streamlit run app.py``.
7. Set the plan (I used the standard plan because of the size of my project and due the free version not being able to process the code properly).
8. Set the environment variables:
     - ``PORT``  ``8501``
     - ``PYTHON_VERSION``  ``3.12.1``
9.  Select the advanced setting.
10. Set Auto-Deploy to your preference.
11. Select **Create Web Service**.
12. Deploy

The live link can be found here - [Mildew Detector - Deployed website](https://pp5-mildew-detection.onrender.com/)

### How to fork/clone the project locally on Github:

> Need to install dependencies from requirements.txt

Fork the repository:

- Log in (or sign up) to Github.
- Go to the repository for: Xakkusu/PP5-mildew-detection.
- Click the Fork button in the top right corner.

Clone repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for: Xakkusu/PP5-mildew-detection.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
6. A clone of the repository will now be created on your machine.


## Testing

## Frameworks, Libraries and Programs used

- [Am I Responsive](https://ui.dev/amiresponsive) Used for the mockup image.
- [GitHub](https://GitHub.com/) - Used for version control.
- [Github's Codespacs](https://github.com/features/codespaces) - IDE to develop the website.
- [Google Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)- Used for troubleshooting, debugging, inspecting page's elements & testing responsiveness.
- [Render](https://render.com/) - Used to deploy the project.
- [Code Institute's milestone-project-mildew-detection-in-cherry-leaves repository](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves) - Forked for base structure of files and README.
- [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves) - Used as the source for the dataset.
- [Jupyter Notebook]() - Used for the notebook's coding environment.
- [Joblib](https://joblib.readthedocs.io/en/stable/) - Used to load and use images.
- [NumPy](https://numpy.org/) - Used for arrays.
- [Pandas](https://pandas.pydata.org/) - Used to create dataframes.
- [Matplotlib](https://matplotlib.org/) - Used to plot distribution and visualizing data.
- [Seaborn](https://seaborn.pydata.org/) - Used for graphs, figures and visualizing data.
- [Plotly](https://plotly.com/) - Used to plot learning curve and visualizing data
- [Streamlit](https://streamlit.io/) - Used to create dashboards.
- [Scikit-Learn](https://scikit-learn.org/stable/) - Used for model evaluation.
- [Tensorflow](https://www.tensorflow.org/) - Used for creating and fitting the model.
- [Pillow](https://python-pillow.github.io/) - Used for image manipulation.
- [Keras](Keras) - Used for creating and fitting the model.
- [Python](https://www.python.org/) - Used as one of the coding languages.


## Credits & Resources

### Content

- The text in for the summary dashboard was compiled from [this article from EOS Data Analytics](https://eos.com/blog/powdery-mildew/) about Powdery Mildew,  [Wikipedia's Powdery mildew](https://en.wikipedia.org/wiki/Powdery_mildew) article & from [this publication from Washington State University](https://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/)  about Cherry Powdery Mildew.

### Other student's repositories

- [Cla-cif's cherry powdery mildew detector repository](https://github.com/cla-cif/Cherry-Powdery-Mildew-Detector) as recommended by my mentor for structure and what is needed in this project. When I got stuck their code was used to see where I made mistakes.
- [HughKeenan's Detection of mildew on cherry leaves repository](https://github.com/HughKeenan/CherryPicker) as recommended by my mentor for structure and what is needed in this project. When I got stuck their code was used to see where I made mistakes.

### Resources

- Tutorials from Code Institute's lessons that we learned in the course of our diploma-education used to understand the basic concepts of Python. Especially topics from the Malaria Detector project were helpful.
- [Stack Overflow](https://stackoverflow.co/)
- [W3Schools](https://www.w3schools.com/)


## Acknowledgements

- My mentor Mo Shami for their guidance and support.
- Code Institute for course material.
- The Code Institute's Slack community for support.
- All students with whom I was able to exchange ideas for our projects.
- My cats

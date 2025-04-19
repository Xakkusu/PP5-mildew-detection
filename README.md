
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
    - [Render](#render)
  - [Testing](#testing)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
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

- List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

## User Experience

## ML Business Case

- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

### Summary Page

### Leaves Visualizer Page

### Mildew Detection Page

### Project Hypothesis Page

### ML Performance Metrics Page


## Bugs

### Fixed Bugs

### Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Render

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Testing

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements

- Thank the people who provided support throughout this project.

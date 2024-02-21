# Team-id : HM0034 
# Team Name : 404 NOT FOUND
# Problem Statement : Develop a solution that helps individuals track their daily nutritional intake and provides personalized recommendations for a healthier lifestyle.



## :bookmark_tabs:Table of contents
* [General info](#general-info)
* [Development](#development)
* [Technologies](#technologies)
* [Setup](#setup)

## :scroll: General info

### Motivation
People from all around the world are getting more concerned in their health and way of life in today's modern environment. However, avoiding junk food and exercising alone are insufficient; we also need to eat a balanced diet. We can live a healthy life with a balanced diet based on our height, weight, and age. Your diet can help you achieve and maintain a healthy weight, lower your chance of developing chronic diseases (including cancer and heart disease), and improve your general health when combined with physical activity. Nevertheless, there is a little SOTA project on food/diet recommendation system. Therefore I got the idea to build a content-based recommendation system for this purpose using machine learning. 


### Backend Developement
The application is built using the FastAPI framework, which allows for the creation of fast and efficient web APIs. When a user makes a request to the API (user data,nutrition data...) the model is used to generate a list of recommended food similar/suitable to his request (data) which are then returned to the user via the API.

### Frontend Developement

The application's front-end is made with Streamlit. Streamlit is an open source app framework in Python language. It helps to create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc. For our case the front-end is composed of three web pages. The main page is Hello.py which is a welcoming page used to introduce you to my project. The side bar on the left allows the user to navigate too the automatic diet recommendation page and the custom food recommendation page. In the diet recommendation page the user can fill information about his age,weight,height.. and gets a diet recommendation based on his information. Besides, the custom food recommendation allows the user to specify more his food preferency using nutritional values.


## :rocket: Technologies
The project is created with:
* Python: 3.10.8
* fastapi 0.88.0
* uvicorn 0.20.0
* scikit-learn 1.1.3
* Pandas: 1.5.1
* Streamlit: 1.16.0
* streamlit-echarts 1.24.1
* Numpy: 1.21.5
* beautifulsoup4 4.11.1

![](https://img.icons8.com/color/48/null/python--v1.png)![](https://img.icons8.com/color/48/null/numpy.png)![](Assets/streamlit-icon-48x48.png)![](Assets/fastapi.ico)![](Assets/scikit-learn.ico) ![](https://img.icons8.com/color/48/null/pandas.png)

## :whale: Setup
Pre-requisites: You should have docker and docker-compose already installed

### Run it locally
#### Clone the repo
```
$ git clone https://github.com/samarthhapse/HM0034_404NOTFOUND
```
### docker-compose
In the project root run:
```
$ docker-compose up -d --build
```
Then open http://localhost:8501 and enjoy :smiley:.


### Deployed Url
[Link to Deployed Solution](gfgpccoe.in)

### Video Url
[Link to Demo Video](video_url)

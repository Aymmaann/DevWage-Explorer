# DevWage Explorer
DevWage Explorer is a web application designed to provide predictive insights into estimating future Software Engineering salaries. This application utilizes machine learning models trained on survey data, offering users the ability to explore salary trends and predict their potential earnings based on various factors.


## Application Preview
<img width="1440" alt="Screenshot 2024-02-03 at 9 22 15 PM" src="https://github.com/Aymmaann/DevWage-Explorer/assets/114000374/ea64227f-e92a-483e-bbe4-ee33dc4dbc6a">
<img width="1440" alt="Screenshot 2024-02-03 at 9 22 27 PM" src="https://github.com/Aymmaann/DevWage-Explorer/assets/114000374/25d90f28-758e-4c76-881f-126504ca7d8f">


## Table of Contents
- Getting Started
- Features
- Usage
- File Overview in DevWage Explorer
- Model Training
- Model Usage in the Application
- Contributing


## Getting Started
Ensure you have the following packages installed:
- Python (3.7 or later)
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- Matplotlib


## Installation
1. Clone the repository:
```bash
git clone https://github.com/Aymmaann/DevWage-Explorer.git
```
2. Install dependencies:


## Features
- Predictive Insights: Estimate your future Software Engineering salary based on your country, education level, age, and years of experience.
- Explore Salary Trends: Visualize and explore current trends in Software Engineering salaries by country, education level, and experience.
- User-Friendly Interface: An easy-to-use web interface built with Streamlit for a seamless user experience.


## Usage
1. Run the application:
```bash
streamlit run application.py
```
2. Choose between "Predict" and "Explore" options from the sidebar.
3. Fill in the required information in the Predict page to calculate your predicted salary.
4. Explore current trends by selecting different visualization options on the Explore page.


## File Overview in DevWage Explorer
- #### predict.py:
Imports necessary libraries and modules, including Streamlit, NumPy, and the saved machine learning model.
Defines categorical variables such as countries, education levels, and age groups.
Provides functions for loading the saved machine learning model and preprocessing user input for salary prediction.
Implements the Streamlit user interface for the salary prediction page.

- #### application.py:
Imports Streamlit and the functions defined in predict.py and data.py.
Implements the main Streamlit web application.
Provides a sidebar for users to choose between the "Predict" and "Explore" options.
Calls the respective functions based on the user's choice.

- #### data.py:
Imports necessary libraries, including Streamlit, Pandas, and Matplotlib.
Defines functions for data loading, cleaning, and exploration.
Implements Streamlit visualizations to explore trends in Software Engineering salaries, such as pie charts, bar charts, and line charts.
Utilizes caching to optimize data loading for improved performance.

- #### Notebook for Model Training:
Contains the code used in a Jupyter notebook for training the machine learning model.
Involves data loading, preprocessing, feature engineering, model selection, training, and evaluation.
Chooses the Decision Tree Regressor as the final model and saves it along with Label Encoders using the pickle library.

Note that the 2023 Stack Overflow Developer Survey dataset, essential for the application, can be downloaded from https://insights.stackoverflow.com/survey.

## Model Training
1. #### Data Collection:
The training data was sourced from the Stack Overflow Developer Survey 2023.
Relevant features, including 'Country,' 'Education Level,' 'Age,' and 'Years of Professional Coding Experience,' were selected.

2. #### Data Preprocessing:
The 'Salary' column was chosen as the target variable for prediction.
Data preprocessing steps included handling missing values, cleaning categorical variables, and transforming categorical data into a suitable format.

3. #### Feature Engineering:
Certain categorical variables, such as 'Country' and 'Education Level,' were encoded using Label Encoding to convert them into numerical representations.
The 'Age' column was organized into meaningful categories to improve model performance.

4. #### Model Selection:
Decision Tree Regressor was chosen due to its ability to capture non-linear relationships and handle both numerical and categorical features effectively.

5. #### Model Training:
The model was trained using the processed data, with 'Country,' 'Education Level,' 'Age,' and 'Years of Experience' as input features and 'Salary' as the target variable.

6. #### Model Evaluation:
Various machine learning models, including Linear Regression and Random Forest, were evaluated for predictive performance.
Decision Tree Regressor was selected based on its accuracy in predicting software engineer salaries.


## Model Usage in the Application
1. #### Loading the Model:
The trained Decision Tree Regressor model, along with Label Encoders for categorical features, is saved using the pickle library.
```python
with open('saved_data.pkl', 'rb') as file:
    data = pickle.load(file)

regressor_model = data['model']
le_country = data['le_country']
le_edlevel = data['le_edlevel']
le_age = data['le_age']
```

2. #### Prediction:
When a user inputs their information in the web application, the model transforms and predicts their salary based on the provided features.

```python
X = np.array([[country, education, age, experience]])
X[:, 0] = le_country.transform(X[:, 0])
X[:, 1] = le_edlevel.transform(X[:, 1])
X[:, 2] = le_age.transform(X[:, 2])
X = X.astype(float)

salary = regressor_model.predict(X)
```

3. #### Displaying the Prediction:
The predicted salary is then displayed to the user on the web application..

```python
st.subheader(f"The predicted salary is ${round(salary[0], 2)}")
```

This Decision Tree Regressor model, trained on survey data, allows users to get personalized insights into their potential software engineering salary based on key factors. The model's ability to handle categorical features and capture non-linear relationships makes it suitable for this predictive application.

## Contributing
Contributions are welcome! Feel free to open issues and pull requests to improve the application.


*Thank you for exploring DevWage Explorer! We hope you find valuable insights into your future Software Engineering salary. Feel free to predict your earnings and explore current salary trends. Happy coding!*

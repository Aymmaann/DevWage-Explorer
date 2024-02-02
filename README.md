# DevWage Explorer
DevWage Explorer is a web application designed to provide predictive insights into estimating future Software Engineering salaries. This application utilizes machine learning models trained on survey data, offering users the ability to explore salary trends and predict their potential earnings based on various factors.


## Table of Contents
- Getting Started
- Features
- Usage
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
git clone <repository-url>
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
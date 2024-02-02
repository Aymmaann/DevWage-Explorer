import streamlit as st
import pickle
import numpy as np

countries = (
    'Argentina', 'Australia', 'Austria', 'Bangladesh', 'Belgium', 'Brazil', 'Bulgaria',
    'Canada', 'Chile', 'China', 'Colombia', 'Costa Rica', 'Croatia', 'Czech Republic',
    'Denmark', 'Egypt', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany',
    'Greece', 'Hong Kong (S.A.R.)', 'Hungary', 'India', 'Indonesia', 'Iran, Islamic Republic of...',
    'Ireland', 'Israel', 'Italy', 'Japan', 'Kenya', 'Latvia', 'Lithuania',
    'Malaysia', 'Mexico', 'Nepal', 'Netherlands', 'New Zealand', 'Nigeria', 'Norway',
    'Russian Federation', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea',
    'Spain', 'Sri Lanka', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Turkey',
    'Ukraine', 'United Arab Emirates', 'United Kingdom of Great Britain and Northern Ireland',
    'United States of America', 'Uruguay', 'Viet Nam', 'Other'
)

education_level = ('Post grad', 'Master’s degree', 'Bachelor’s degree', 'Associate degree', 'No Formal Education Beyond High School')

age_groups = ('25-34 years old', '35-44 years old', '45-54 years old',
       '55-64 years old', '18-24 years old', 'Others')

def load_model():
    with open('saved_data.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor_model = data["model"]
le_country = data["le_country"]
le_edlevel = data["le_edlevel"]
le_age = data["le_age"]


def line_break():
    st.markdown("<br>", unsafe_allow_html=True)


def predict_page():
    st.title("DevWage Explorer")
    line_break()
    st.write("""##### DevWage Explorer empowers you with predictive insights for estimating your future Software Engineering salary.""")

    line_break()
    st.write("""###### Enter your information down below""")
    country = st.selectbox("Country of employment", countries)

    line_break()
    education = st.selectbox("Education Level", education_level)

    line_break()
    age = st.selectbox("Age", age_groups)

    line_break()
    experience = st.slider("Years of Experience", 0, 50, 3)

    predict = st.button("Calculate Salary")
    if predict:
        X = np.array([[country, education, age, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_edlevel.transform(X[:, 1])
        X[:, 2] = le_age.transform(X[:, 2])
        X = X.astype(float)

        salary = regressor_model.predict(X)
        st.subheader(f"The predicted salary is ${round(salary[0],2)}")
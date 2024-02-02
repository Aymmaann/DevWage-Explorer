import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def shorten_categories(category, cutoff):
    categorical_map = {}
    for i in range(len(category)):
        if category.values[i] >= cutoff:
            categorical_map[category.index[i]] = category.index[i]
        else:
            categorical_map[category.index[i]] = 'Other'
    return categorical_map


def polished_experience(years):
    if years == 'More than 50 years':
        return 50
    elif years == 'Less than 1 year':
        return 0.5
    else:
        return float(years)


def polish_education(x):
    if x == "Bachelor’s degree (B.A., B.S., B.Eng., etc.)":
        return "Bachelor’s degree"
    if x == "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)":
        return "Master’s degree"
    if x == "Professional degree (JD, MD, Ph.D, Ed.D, etc.)":
        return "Post grad"
    if x == "Associate degree (A.A., A.S., etc.)":
        return "Associate degree"
    return "No Formal Education Beyond High School"


def organize_age(age):
    if age in ['Prefer not to say', 'Under 18 years old', '65 years or older']:
        return 'Others'
    return age


@st.cache_data
def load_data():
    data = pd.read_csv('survey_results_public.csv')
    data = data[['Country', 'EdLevel', 'Age', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]
    data = data.rename({'ConvertedCompYearly': 'Salary'}, axis=1)
    data = data[data['Salary'].notnull()]
    data.dropna(inplace=True)
    data = data[data['Employment'] == 'Employed, full-time']

    countries = shorten_categories(data['Country'].value_counts(), 40)
    data['Country'] = data['Country'].map(countries)
    data = data[data['Salary'] <= 240000]
    data = data[data['Salary'] >= 12000]
    data = data[data['Country'] != 'Other']

    data['YearsCodePro'] = data['YearsCodePro'].apply(polished_experience)
    data['EdLevel'] = data['EdLevel'].apply(polish_education)
    data.drop('Employment', axis=1, inplace=True)
    data['Age'] = data['Age'].apply(organize_age)
    return data


data = load_data()


def line_break():
    st.markdown('<br><br>', unsafe_allow_html=True)


def explore_page():
    st.title("Explore the Current Trends of SWE Salaries")

    # Pie Chart
    line_break()
    st.write("""##### Percentage of Software Engineers by Country""")
    counts = data['Country'].value_counts()
    percentages = counts / counts.sum() * 100
    significant_components = percentages[percentages > 2.0].index
    data['Country'] = data['Country'].apply(lambda x: x if x in significant_components else 'Others')
    fig1, ax1 = plt.subplots()
    ax1.pie(data['Country'].value_counts(), labels=data['Country'].unique(), autopct="%1.1f%%", startangle=90,
            labeldistance=1.1, textprops={'fontsize': 6})
    st.pyplot(fig1)

    # Bar Chart
    line_break()
    st.write("##### Mean Salary Based on Country")
    sal = data.groupby(['Country'])['Salary'].mean()
    st.bar_chart(sal)

    # Line Chart
    line_break()
    st.write("""##### Mean Salary Based on Experience""")
    exp = data.groupby(['YearsCodePro'])['Salary'].mean()
    st.line_chart(exp)

    line_break()
    st.write("###### Reference: Stack Overflow Developer Survey 2023")
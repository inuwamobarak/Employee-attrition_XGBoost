#importing libraries
#import catboost
import xgboost as xgb
import pandas as pd
import streamlit as st
import base64
import numpy as np
 
#importing model
model = xgb.XGBRegressor()
model.load_model('xgboost_model.json')

#setting background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:images/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/bg3.jpg')

#main body
def main():
    st.title('Employee Attrition Prediction')
    st.image('images/rsz_bg4.png')
    st.write("Replacing a departing employee often costs an organization"\
    "$4,000 or rfsrfwrfwer more. The average cost to hire an employee, according to a"\
    "different research by the Society for Human Resource Management, is"\
    "$4,129, and it often takes 42 days to fill a post."\
    "The typical American company spends $4,000 to hire a new employee,"\
    "and it might take up to 52 days to fill a post, according to Glassdoor.")
    st.subheader('(Please fill in the Employee details accordingly)')
    import math

    Age = st.number_input('Age')
    BusinessTravel = st.number_input('BusinessTravel')
    DailyRate = st.number_input('DailyRate')
    Department = st.number_input('Department')     
    DistanceFromHome = st.number_input('DistanceFromHome')
    Education = st.number_input('Education')
    EducationField  = st.number_input('EducationField')
    EmployeeCount = st.number_input('EmployeeCount')
    EmployeeNumber = st.number_input('EmployeeNumber')
    EnvironmentSatisfaction = st.number_input('EnvironmentSatisfaction')
    Gender = st.number_input('Gender')
    HourlyRate = st.number_input('HourlyRate')
    JobInvolvement = st.number_input('JobInvolvement')
    JobLevel = st.number_input('JobLevel')
    JobRole = st.number_input('JobRole')
    JobSatisfaction   = st.number_input('JobSatisfaction')
    MaritalStatus = st.number_input('MaritalStatus')
    MonthlyIncome = st.number_input('MonthlyIncome')
    MonthlyRate = st.number_input('MonthlyRate')
    NumCompaniesWorked = st.number_input('NumCompaniesWorked')
    Over18 = st.number_input('Over18')
    OverTime = st.number_input('OverTime')
    PercentSalaryHike = st.number_input('PercentSalaryHike')
    PerformanceRating = st.number_input('PerformanceRating')
    RelationshipSatisfaction = st.number_input('RelationshipSatisfaction')
    StandardHours = st.number_input('StandardHours')
    StockOptionLevel = st.number_input('StockOptionLevel')
    TotalWorkingYears = st.number_input('TotalWorkingYears')
    TrainingTimesLastYear = st.number_input('TrainingTimesLastYear')
    WorkLifeBalance = st.number_input('WorkLifeBalance')
    YearsAtCompany = st.number_input('YearsAtCompany')
    YearsInCurrentRole = st.number_input('YearsInCurrentRole')
    YearsSinceLastPromotion  = st.number_input('YearsSinceLastPromotion')
    YearsWithCurrManager = st.number_input('YearsWithCurrManager')

    if st.button('Click to Predict'):
        result = model.predict([[Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, EmployeeCount, EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, Over18, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StandardHours, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager]])
        #st.text(result) #uncomment to view the exact prediction before it is rounded off
        result2 = (np.rint(result)).astype(int)
        if result2 > 0 :
            st.success(result2)
            st.success('Employee Does not seem to attrite')
        else:
            st.warning(result2)
            st.warning('Employee tends to attrite')
            

if __name__=='__main__':
    main()

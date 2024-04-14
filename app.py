import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import *
from prediction import prediction

col1, col2 = st.columns([2, 5])
with col1:
    st.image("https://raw.githubusercontent.com/royanfauzimaulana25/education_recomendation/main/asset/logo.jpg", width=200)
with col2:
    st.header('Dropout Student Prediction App (Prototype)')

data = pd.DataFrame()
 
col1, col2, col3 ,col4= st.columns(4)
 
with col1:
    Marital_status = st.selectbox(label='Marital Status', options=encoder_Marital_status.classes_, placeholder = 'Choose an option', index=None)
    data["Marital_status"] = [Marital_status]

with col2:
    Daytime_evening_attendance = st.selectbox(label='Daytime Attendance', options=encoder_Daytime_evening_attendance.classes_, placeholder = 'Choose an option', index=None)
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]
 
with col3:
    Previous_qualification_grade = float(st.number_input(label='Previous Qualification Grade'))
    data["Previous_qualification_grade"] = [Previous_qualification_grade]
 
with col4:
    Admission_grade = float(st.number_input(label='Admission Grade'))
    data["Admission_grade"] = Admission_grade

col1, col2, col3, col4 = st.columns(4)

with col1:
    Displaced = st.selectbox(label='Displaced', options=encoder_Displaced.classes_, placeholder = 'Choose an option', index=None)
    data["Displaced"] = [Displaced]
 
with col2:
    Debtor = st.selectbox(label='Debtor', options=encoder_Debtor.classes_, placeholder = 'Choose an option', index=None)
    data["Debtor"] = [Debtor]
 
with col3:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition Fees Up to date', options=encoder_Tuition_fees_up_to_date.classes_, placeholder = 'Choose an option', index=None)
    data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
 
with col4:
    Gender = st.selectbox(label='Gender', options=encoder_Gender.classes_, placeholder = 'Choose an option', index=None)
    data["Gender"] = [Gender]
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Scholarship_holder = st.selectbox(label='Scholarship Holder', options=encoder_Scholarship_holder.classes_, placeholder = 'Choose an option', index=None)
    data["Scholarship_holder"] = [Scholarship_holder]
 
with col2:
    Age_at_enrollment = int(st.number_input(label='Age at Enrollment'))
    data["Age_at_enrollment"] = [Age_at_enrollment]
 
with col3:
    International = st.selectbox(label='International', options=encoder_International.classes_, placeholder = 'Choose an option', index=None)
    data["International"] = [International]

with col4:
    Educational_special_needs = st.selectbox(label='Educational Special Needs', options=encoder_Educational_special_needs.classes_, placeholder = 'Choose an option', index=None)
    data["Educational_special_needs"] = [Educational_special_needs]



col1, col2 = st.columns(2)
with col1:       
    Curricular_units_1st_sem_credited = int(st.number_input(label='Curricular_units_1st_sem_credited', placeholder = 'Input Number'))
    data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited
    
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular_units_1st_sem_enrolled'))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled
    
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Curricular_units_1st_sem_evaluations'))
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations
    
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular_units_1st_sem_approved'))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved
    
    Curricular_units_1st_sem_grade = int(st.number_input(label='Curricular_units_1st_sem_grade'))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade
    
    Curricular_units_1st_sem_without_evaluations = int(st.number_input(label='Curricular_units_1st_sem_without_evaluations'))
    data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations
 
with col2:       
    Curricular_units_2nd_sem_credited = int(st.number_input(label='Curricular_units_2nd_sem_credited'))
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited
    
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular_units_2nd_sem_enrolled'))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled
    
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_evaluations'))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations
    
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular_units_2nd_sem_approved'))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved
    
    Curricular_units_2nd_sem_grade = int(st.number_input(label='Curricular_units_2nd_sem_grade'))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade
    
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_without_evaluations'))
    data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations
 
GDP = int(st.number_input(label='GDP'))
data["GDP"] = GDP

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=None, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Student Status: {}".format(prediction(new_data)))
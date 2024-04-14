import streamlit as st
import pandas as pd
import joblib
# from data_preprocessing import data_preprocessing, encoder_Credit_Mix, encoder_Payment_Behaviour, encoder_Payment_of_Min_Amount
# from prediction import prediction

col1, col2 = st.columns([2, 5])
with col1:
    st.image("https://raw.githubusercontent.com/royanfauzimaulana25/education_recomendation/main/asset/logo.jpg", width=200)
with col2:
    st.header('Dropout Student Prediction App (Prototype)')

data = pd.DataFrame()
 
col1, col2, col3 ,col4= st.columns(4)
 
with col1:
    # Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.joblib.classes_, index=1)
    Marital_status = st.selectbox(label='Marital_status', options=['single', 'married','widower', 'divorced', 'facto union', 'legally separated'], placeholder = 'Choose an option', index=None)
    data["Marital_status"] = [Marital_status]

with col2:
    # Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.joblib.classes_, index=1)
    Daytime_evening_attendance = st.selectbox(label='Daytime Attendance', options=['Yes', 'No'], placeholder = 'Choose an option', index=None)
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]
 
with col3:
    Previous_qualification_grade = float(st.number_input(label='Previous Qualification Grade'))
    data["Previous_qualification_grade"] = [Previous_qualification_grade]
 
with col4:
    Admission_grade = float(st.number_input(label='Admission Grade'))
    data["Admission_grade"] = Admission_grade

col1, col2, col3, col4 = st.columns(4)

with col1:
    # Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.joblib.classes_, index=1)
    Displaced = st.selectbox(label='Displaced', options=['Yes', 'No'], placeholder = 'Choose an option', index=None)
    data["Displaced"] = [Displaced]
 
with col2:
    # Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.joblib.classes_, index=1)
    Debtor = st.selectbox(label='Debtor', options=['Yes', 'No'], placeholder = 'Choose an option', index=None)
    data["Debtor"] = [Debtor]
 
with col3:
    # Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.joblib.classes_, index=1)
    Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=['Yes', 'No'], placeholder = 'Choose an option', index=None)
    data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
 
with col4:
    # Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.joblib.classes_, index=1)
    Gender = st.selectbox(label='Gender', options=['Yes', 'No'], placeholder = 'Choose an option', index=None)
    data["Gender"] = [Gender]
 
col1, col2, col3 = st.columns(3)
 
with col1:
    # Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.joblib.classes_, index=1)
    Scholarship_holder = st.selectbox(label='Scholarship_holder', options=['Yes', 'No'], placeholder = 'Choose an option', index=None)
    data["Scholarship_holder"] = [Scholarship_holder]
 
with col2:
    # Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.joblib.classes_, index=1)
    Age_at_enrollment = st.selectbox(label='Age_at_enrollment', options=['Yes', 'No'], placeholder = 'Choose an option', index=None)
    data["Age_at_enrollment"] = [Age_at_enrollment]
 
with col3:
    # Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.joblib.classes_, index=1)
    International = st.selectbox(label='International', options=['Yes', 'No'], placeholder = 'Choose an option', index=None)
    data["International"] = [International]



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
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Credit Scoring: {}".format(prediction(new_data)))
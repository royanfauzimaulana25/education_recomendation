import joblib
import numpy as np
import pandas as pd

encoder_Marital_status = joblib.load("model/encoder_Marital_status.joblib")
encoder_Daytime_evening_attendance = joblib.load("model/encoder_Daytime_evening_attendance.joblib")
encoder_Displaced = joblib.load("model/encoder_Displaced.joblib")
encoder_Educational_special_needs = joblib.load("model/encoder_Educational_special_needs.joblib")
encoder_Debtor = joblib.load("model/encoder_Debtor.joblib")
encoder_Tuition_fees_up_to_date = joblib.load("model/encoder_Tuition_fees_up_to_date.joblib")
encoder_Gender = joblib.load("model/encoder_Gender.joblib")
encoder_Scholarship_holder = joblib.load("model/encoder_Scholarship_holder.joblib")
encoder_International = joblib.load("model/encoder_International.joblib")

encoder_target = joblib.load("model/encoder_target.joblib")

pca_1 = joblib.load("model/pca_1.joblib")
pca_2 = joblib.load("model/pca_2.joblib")

scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")
scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Age_at_enrollment = joblib.load("model/scaler_Age_at_enrollment.joblib")

scaler_Curricular_units_1st_sem_credited = joblib.load("model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_evaluations.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_grade =joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")

scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")
scaler_Curricular_units_2nd_sem_credited = joblib.load("model/scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_evaluations.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_grade =joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")

scaler_GDP = joblib.load("model/scaler_GDP.joblib")

pca_numerical_columns_1 = [
    'Age_at_enrollment',
    'Curricular_units_1st_sem_credited',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',	
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',	
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_2nd_sem_without_evaluations'
]
 
pca_numerical_columns_2 = [
    'Previous_qualification_grade',    
    'Admission_grade'
]
 
def data_preprocessing(data):
    """Preprocessing data
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()
    
    df["Age"] = scaler_Age.transform(np.asarray(data["Age"]).reshape(-1,1))[0]
    
    df["Credit_Mix"] = encoder_Credit_Mix.transform(data["Credit_Mix"])[0]
    df["Payment_of_Min_Amount"] = encoder_Payment_of_Min_Amount.transform(data["Payment_of_Min_Amount"])
    df["Payment_Behaviour"] = encoder_Payment_Behaviour.transform(data["Payment_Behaviour"])
    
    # PCA 1
    data["Num_Bank_Accounts"] = scaler_Num_Bank_Accounts.transform(np.asarray(data["Num_Bank_Accounts"]).reshape(-1,1))[0]
    data["Num_Credit_Card"] = scaler_Num_Credit_Card.transform(np.asarray(data["Num_Credit_Card"]).reshape(-1,1))[0]
    data["Interest_Rate"] = scaler_Interest_Rate.transform(np.asarray(data["Interest_Rate"]).reshape(-1,1))[0]
    data["Num_of_Loan"] = scaler_Num_of_Loan.transform(np.asarray(data["Num_of_Loan"]).reshape(-1,1))[0]
    data["Delay_from_due_date"] = scaler_Delay_from_due_date.transform(np.asarray(data["Delay_from_due_date"]).reshape(-1,1))[0]
    data["Num_of_Delayed_Payment"] = scaler_Num_of_Delayed_Payment.transform(np.asarray(data["Num_of_Delayed_Payment"]).reshape(-1,1))[0]
    data["Changed_Credit_Limit"] = scaler_Changed_Credit_Limit.transform(np.asarray(data["Changed_Credit_Limit"]).reshape(-1,1))[0]
    data["Num_Credit_Inquiries"] = scaler_Num_Credit_Inquiries.transform(np.asarray(data["Num_Credit_Inquiries"]).reshape(-1,1))[0]
    data["Outstanding_Debt"] = scaler_Outstanding_Debt.transform(np.asarray(data["Outstanding_Debt"]).reshape(-1,1))[0]
    data["Credit_History_Age"] = scaler_Credit_History_Age.transform(np.asarray(data["Credit_History_Age"]).reshape(-1,1))[0]
    
    df[["pc1_1", "pc1_2", "pc1_3", "pc1_4", "pc1_5"]] = pca_1.transform(data[pca_numerical_columns_1])
    
    # PCA 2
    data["Monthly_Inhand_Salary"] = scaler_Monthly_Inhand_Salary.transform(np.asarray(data["Monthly_Inhand_Salary"]).reshape(-1,1))[0]
    data["Monthly_Balance"] = scaler_Monthly_Balance.transform(np.asarray(data["Monthly_Balance"]).reshape(-1,1))[0]
    data["Amount_invested_monthly"] = scaler_Amount_invested_monthly.transform(np.asarray(data["Amount_invested_monthly"]).reshape(-1,1))[0]
    data["Total_EMI_per_month"] = scaler_Total_EMI_per_month.transform(np.asarray(data["Total_EMI_per_month"]).reshape(-1,1))[0]
    
    df[["pc2_1", "pc2_2"]] = pca_2.transform(data[pca_numerical_columns_2])
    
    return df
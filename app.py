import streamlit as st
import streamlit.components.v1 as stc
import pickle

with open('logistic_regression_model.pkl', 'rb') as file:
    Logistic_Regression_Model = pickle.load(file)

html_temp = """<div style="background-color:#000;padding:10px;border-radius:10px">
                <h1 style="color:#fff;text-align:center">Loan Eligibility Prediction App</h1> 
                <h4 style="color:#fff;text-align:center">Made for: Credit Team</h4> 
                """

desc_temp = """ ### Loan Prediction App 
                This app is used by Credit team for deciding Loan Application
                
                #### Data Source
                Kaggle: Link <Masukkan Link>
                """

def main():
    stc.html(html_temp)
    menu = ["Home", "Machine Learning App"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "Machine Learning App":
        run_ml_app()

def run_ml_app():
    design = """<div style="padding:15px;">
                    <h1 style="color:#fff">Loan Eligibility Prediction</h1>
                </div
             """
    st.markdown(design, unsafe_allow_html=True)
    
     #membuat struktur form
    left, right = st.columns((2,2))
    gender = left.selectbox('Gender', ('Male', 'Female'))
    married = right.selectbox('Married', ('Yes', 'No'))
    dependent = left.selectbox('Dependent', (0, 1, 2, 3))
    education = right.selectbox('Education', ('Graduate', 'Not Graduate'))
    self_employed = left.selectbox('Self Employed', ('Yes', 'No'))
    applicant_income = right.number_input('Applicant Income')
    coapplicant_income = left.number_input('Co-Applicant Income')
    loan_amount = right.number_input('Loan Amount')
    loan_amount_term = left.number_input(Label = 'Loan Amount Term',
                                        min_value = 10, max_value = 360)
    credit_history = right.selectbox('Credit History', (0.0, 1.0))
    property_area = st.selectbox('Property Area', ('Rural', 'Semiurban', 'Urban'))

    button = st.button("Predict")



    #If button is clilcked
    pass

def predict(gender, married, dependent, education, self_employed, applicant_income, coApplicant_income
                         ,loan_amount, loan_amount_term, credit_history, property_area):
    
   

    #Making prediction
    pass

if __name__ == "__main__":
    main()

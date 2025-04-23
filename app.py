import streamlit as st 
import joblib
import numpy as np

st.title('Salary Prediction App')

st.divider()

st.write('With this app , you can get estimations for the salaries of the Manufacturing company employees')

years = st.number_input('Enter the years of experience they have at company',value = 1, step=1,min_value=0)
jobrate = st.number_input('Enter the job rate(employee rating)',value=3.5,step=0.5,min_value=0.0)
overtime = st.number_input('Enter Overtime Hours they take',value=1.0,step=1.0,min_value=0.0)

X = [years , jobrate , overtime]

model = joblib.load('linearmodel.pkl')

st.divider()

predict = st.button('Press the button for Salary Prediction')

st.divider()

if predict:
    
    # to display balloons
    st.success("Yay!")
    
    # since need to add 2d array for prediction
    X1 = np.array([X])
    
    prediction = model.predict(X1)[0]
    
    st.write(f'Salary Predicted is {prediction:,.2f}')
    
else:
    'Press button for app to make prediction'
import numpy as np
import streamlit as st
import pickle

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

#creating a function for prediction

def diabetes_prediction(input_data):

    # convert input data into numpy array
    input_data_as_numpy = np.asarray(input_data)

    #reshape the array since we are predicting for one instance
    input_data_reshape = input_data_as_numpy.reshape(1,-1)

    #making prediction
    prediction = loaded_model.predict(input_data_reshape)
    print (prediction)

    if (prediction[0]==0):
        return 'This patient is not Diabetic'
    else:
        return 'This patient is Diabetic '

def main():

    #giving title for the interface
    st.title('Diabetes Prediction Web App')

    #getting the input from user

    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age of the Patient')

    #code for Prediction

    diagnosis = ''

    #creating a button for prediction

    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)


if __name__ == '__main__':
    main()





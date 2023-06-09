import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("C:/Users/91845/Desktop/Python/deploying machine learning model using streamlit/trained_model.sav", 'rb'))

#creating a function for prediction

def diabetes_prediction(input_data): 

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return'The person is not diabetic'

    else:
        return'The person is diabetic'
    
def main():
    st.title('Diabetes Prediction Web app')
     
     #getting the input data from the user
     
    Pregnancies = st.text('Number of Pregnancies')
    Glucose= st.text('Glucose')
    BloodPressure= st.text('Blood Pressure value')
    SkinThickness= st.text('Skin Thickness value')
    Insulin= st.text('Insulin level')
    BMI= st.text('BMI value')
    DiabetesPedigreeFunction= st.text('Diabetes Pedigree Function value')
    Age= st.text('Age')

    #code for prediction
    dignosis = ''

    #creating a button for prediction

    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()

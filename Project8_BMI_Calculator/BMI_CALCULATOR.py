# prompt: def bmi_calculator():
# """
# Please create a "BMI calculator Web App" by using "Streamlit" and "Pandas". The app will obtain an input from the user as follows:
# 1. Height in cm
# 2. Weight in kgs.
# After obtaining the inputs the program will calculate the associated BMI by dividing the "weight" from "Height" and the result will be "square by 2". The program should also display the BMI international averages as well with clear description of each BMI.

import streamlit as st
import pandas as pd

def bmi_calculator():
    st.title("BMI Calculator")

    # Input fields
    height_cm = st.number_input("Enter your height (cm)", min_value=0.0, step=0.1)
    weight_kg = st.number_input("Enter your weight (kg)", min_value=0.0, step=0.1)

    # BMI Calculation
    if height_cm > 0 and weight_kg > 0:
      height_m = height_cm / 100
      bmi = weight_kg / (height_m ** 2)

      # Display BMI
      st.write(f"Your BMI is: {bmi:.2f}")

      # BMI Categories
      bmi_categories = pd.DataFrame({
          'Category': ['Underweight', 'Normal weight', 'Overweight', 'Obesity Class I', 'Obesity Class II', 'Obesity Class III'],
          'BMI Range (kg/m²)': ['< 18.5', '18.5 - 24.9', '25.0 - 29.9', '30.0 - 34.9', '35.0 - 39.9', '≥ 40'],
          'Description': [
              'Malnutrition risk',
              'Low risk',
              'Moderate risk',
              'High risk',
              'Very high risk',
              'Extremely high risk'
          ]
      })

      st.subheader("BMI Categories:")
      st.table(bmi_categories)

      # BMI interpretation based on calculated BMI
      if bmi < 18.5:
          st.write("You are underweight.")
      elif 18.5 <= bmi < 25:
          st.write("You are in a healthy weight range.")
      elif 25 <= bmi < 30:
          st.write("You are overweight.")
      elif 30 <= bmi < 35:
          st.write("You are in Obesity Class I.")
      elif 35 <= bmi < 40:
          st.write("You are in Obesity Class II.")
      else:
          st.write("You are in Obesity Class III.")
    else:
        st.write("Please enter valid height and weight values.")

if __name__ == "__main__":
    bmi_calculator()
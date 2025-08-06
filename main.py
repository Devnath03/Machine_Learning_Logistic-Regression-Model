#Import Libraries
import streamlit as st
import pickle 
import numpy as np

# Load the pre-trained model
model = pickle.load(open('model.pickle', 'rb'))

# Set up the Streamlit app
st.set_page_config(page_icon="🤖", page_title="Purchased Prediction",layout="centered")

# Title of the app
st.title("🤖 Purchased Prediction App")
st.markdown("""
        welcome to the Purchased Prediction App!
        This app predicts the likelihood of a customer making a purchase based on their details.
        Please fill in the customer information below to get started.
""")
st.markdown("""
        Enter customer details to predict purchase likelihood:
            
""")

# Input fields for customer details
with st.form("prediction_form"):
    age = st.number_input("Enter Age", min_value=18, max_value=100, value=30 , step=1 , help="Enter the age of the customer")
    sub = st.form_submit_button("Predict Purchase")

if sub:
    # Prepare the input data for prediction
    st.success("Processing your request...")
    # Convert the input data into a format suitable for the model
    input_data = np.array([[age]])
    # Make the prediction using the loaded model
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("The customer is likely to make a purchase! 🎉")
    else:
        st.warning("The customer is unlikely to make a purchase. 😞")
    st.markdown("Thank you for using the Purchased Prediction App! If you have any questions, feel free to reach out.")

    st.success(f"Prediction Result: {'Purchase' if prediction[0] == 1 else 'No Purchase'}   ")
    if prediction[0] == 1:
        st.balloons()
    else:
        st.snow()
    
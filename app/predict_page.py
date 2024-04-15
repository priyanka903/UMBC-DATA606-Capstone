import streamlit as st
import pickle
import numpy as np

def load_model():
    try:
        with open('https://github.com/priyanka903/UMBC-DATA606-Capstone/raw/main/app/saved_steps.pkl', 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        print("The file 'saved_steps.pkl' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

data = load_model()
regressor = data["model"]

def show_predict_page():
    
    st.title("Fraud Transaction Prediction")
    st.write("""### We need some information to predict the transaction""")

    # Collect inputs as strings
    user_input_step = st.text_input("Enter step number349, 28366.71, 31110.0, 2743.29, 359900.5, 388267.21, 0", key="input_step")
    user_input_amount = st.text_input("Enter amount", key="input_amount")
    user_input_oldbalanceOrig = st.text_input("Enter old balance origin", key="input_oldbalanceOrig")
    user_input_newbalanceOrig = st.text_input("Enter new balance origin", key="input_newbalanceOrig")
    user_input_oldbalanceDest = st.text_input("Enter old balance destination", key="input_oldbalanceDest")
    user_input_newbalanceDest = st.text_input("Enter new balance destination", key="input_newbalanceDest")
    user_input_isFlaggedFraud = st.text_input("Enter if transaction is flagged as fraud (0 or 1)", key="input_isFlaggedFraud")

    ok = st.button("Predict Transaction")
    if ok:
        try:
            # Convert inputs to float
            X = np.array([[float(user_input_step), float(user_input_amount), float(user_input_oldbalanceOrig),
                           float(user_input_newbalanceOrig), float(user_input_oldbalanceDest),
                           float(user_input_newbalanceDest), float(user_input_isFlaggedFraud)]])
            
            # Predict
            Identified = regressor.predict(X)
            st.subheader(f"Transaction is {'Fraud' if Identified[0] else 'Not Fraud'}")
        except ValueError as e:
            st.error("Please enter valid numeric inputs. Error: " + str(e))
            

show_predict_page()
# AI-powered health chatbot
import streamlit as st
from transformers import pipeline

# Initialize the chatbot model
chatbot = pipeline("text-generation", model="gpt2")

# Function to handle user input and generate responses
def healthcare_chatbot(user_input):
    user_input = user_input.lower()
    if "symptoms" in user_input and "flu" in user_input:
        return "Common symptoms of the flu include fever, cough, sore throat, runny or stuffy nose, body aches, headache, chills, and fatigue. Please consult a doctor for accurate advice."
    elif "symptoms" in user_input:
        return "Please specify the condition you are asking about, such as 'symptoms of flu'."
    elif "appointment" in user_input:
        return "Would you like to book an appointment? Please provide your preferred date and time."
    elif "medication" in user_input:
        return "It is important to take prescribed medicines regularly. If you have concerns, please consult a doctor."
    elif "emergency" in user_input:
        return "If this is an emergency, please call emergency services immediately."
    elif "advice" in user_input:
        return "For personalized medical advice, please consult a healthcare professional."
    else:
        response = chatbot(user_input, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']

# Main function to run the Streamlit app
def main():
    # Custom CSS for background and styling
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://www.example.com/background.jpg');
            background-size: cover;
            color: white;
        }
        .main {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 10px;
        }
        .stTextInput>div>div>input {
            border: 2px solid #4CAF50;
            border-radius: 10px;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Healthcare Assistant Chatbot")
    st.write("Welcome to the Healthcare Assistant Chatbot. How can I assist you today?")
    
    # Example prompts
    st.write("Try asking:")
    

    user_input = st.text_input("Enter your message here:")
    
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner('Processing your request...'):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a message to get a response.")

if __name__ == "__main__":
    main()
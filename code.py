import streamlit as st
from cryptography.fernet import Fernet
import os

# Encryption key generation
def generate_key():
    return Fernet.generate_key()

# Save the encryption key to a file
def save_key(key, filename):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Load the encryption key from a file
def load_key(filename):
    return open(filename, "rb").read()

# Encrypt data
def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

# Decrypt data
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()

# Save encrypted data to a file
def save_encrypted_data(encrypted_data, filename):
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Load encrypted data from a file
def load_encrypted_data(filename):
    with open(filename, "rb") as file:
        return file.read()

# Streamlit app
def main():
    st.title("Quiz Application")

    # Login details
    login_id = st.text_input("Login ID")
    password = st.text_input("Password", type="password")

    if login_id == "CS4EDLD" and password == "root123":
        st.sidebar.title("Welcome to the Quiz")

        roll_number = st.sidebar.text_input("Enter Roll Number (Format: 23F-XXXX)")
        student_name = st.sidebar.text_input("Enter Your Name")

        questions = [
            "What is the capital of France?",
            "Which planet is known as the Red Planet?",
            "What is 2 + 2?"
        ]
        correct_answers = ["Paris", "Mars", "4"]

        responses = []
        for i, question in enumerate(questions):
            response = st.sidebar.text_input(f"Q{i + 1}. {question}")
            responses.append(response)

        if st.sidebar.button("Finish"):
            # Encrypt student's responses
            key = generate_key()
            encrypted_responses = encrypt_data(str(responses), key)
            save_encrypted_data(encrypted_responses, "encrypted_responses.txt")

            # Provide encrypted file download link
            st.sidebar.markdown("### Download Encrypted Responses")
            st.sidebar.markdown(
                f'<a href="data:file/txt;base64,{encrypted_responses.decode()}" download="encrypted_responses.txt">Click here to download</a>',
                unsafe_allow_html=True
            )

            # Save encryption key
            save_key(key, "encryption_key.txt")

            st.sidebar.success("Quiz submitted successfully!")
    else:
        st.error("Invalid login credentials. Please try again.")


if __name__ == "__main__":
    main()

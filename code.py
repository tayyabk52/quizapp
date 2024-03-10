import streamlit as st

def main():
    st.title("Multiple Choice Quiz")

    # Login
    login_id = st.text_input("Login ID")
    password = st.text_input("Password", type="password")
    if login_id == "CS4EDLD" and password == "root123":
        st.success("Login successful!")
        # Quiz
        roll_number = st.text_input("Roll Number", "23F-XXXX")
        name = st.text_input("Name")
        questions = [
            "What is the capital of France?",
            "Which planet is known as the Red Planet?",
            "What is 2 + 2?"
        ]
        answers = ["Paris", "Mars", "4"]
        responses = []
        for i, question in enumerate(questions):
            response = st.text_input(f"Q{i+1}: {question}")
            responses.append(response)
        if st.button("Finish"):
            # Generate text file with responses
            filename = f"{roll_number}_{name}_quiz_responses.txt"
            content = "Quiz Responses:\n"
            for i, response in enumerate(responses):
                content += f"Q{i+1}: {questions[i]}\nAnswer: {response}\n\n"
            st.download_button(label="Download Responses", data=content, file_name=filename, mime="text/plain")
    else:
        st.error("Invalid login credentials.")

if __name__ == "__main__":
    main()

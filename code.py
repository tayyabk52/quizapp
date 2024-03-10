import streamlit as st

def main():
    st.title("MCQ Quiz")

    # Login
    login_id = st.text_input("Login ID", type="password")
    password = st.text_input("Password", type="password")
    if login_id == "CS4EDLD" and password == "root123":
        st.success("Login successful!")
        roll_number = st.text_input("Enter Roll Number (Format: 23F-XXXX)", key="roll_number")
        name = st.text_input("Enter Name")

        # Quiz questions and answers
        questions = [
            "What is the capital of France?",
            "Which planet is known as the Red Planet?",
            "What is 2 + 2?"
        ]
        correct_answers = ["Paris", "Mars", "4"]

        # Display quiz questions
        st.subheader("Quiz")
        responses = []
        for i, question in enumerate(questions):
            response = st.text_input(f"Q{i + 1}: {question}", key=f"response_{i}")
            responses.append(response)

        if st.button("Finish"):
            # Check answers
            score = 0
            for i, response in enumerate(responses):
                if response.lower() == correct_answers[i].lower():
                    score += 1

            # Generate file for download
            filename = f"{roll_number}_{name}_quiz_results.txt"
            with open(filename, "w") as file:
                file.write(f"Roll Number: {roll_number}\n")
                file.write(f"Name: {name}\n")
                file.write(f"Score: {score}/{len(questions)}\n")
                for i, response in enumerate(responses):
                    file.write(f"Q{i + 1}: {questions[i]}\n")
                    file.write(f"Response: {response}\n")
                    file.write(f"Correct Answer: {correct_answers[i]}\n\n")

            st.success(f"Quiz results saved to {filename}")

    else:
        st.error("Invalid login credentials")

if __name__ == "__main__":
    main()

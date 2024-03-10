import streamlit as st
import pandas as pd

# Sample quiz questions and answers
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is 2 + 2?"
]
answers = ["Paris", "Mars", "4"]

def login():
    st.title("Login")
    login_id = st.text_input("Login ID")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_id == "CS4EDLD" and password == "root123":
            st.success("Login successful")
            return True
        else:
            st.error("Invalid login credentials")
            return False

def quiz():
    st.title("Quiz")
    responses = []
    for i, question in enumerate(questions):
        response = st.radio(f"Q{i + 1}. {question}", ["A", "B", "C", "D"])
        responses.append(response)
    return responses

def grade_quiz(responses):
    score = 0
    for i, response in enumerate(responses):
        if response.strip().lower() == answers[i].strip().lower():
            score += 1
    return score

def download_quiz(roll_number, name, responses, score):
    df = pd.DataFrame({
        "Question": questions,
        "Response": responses
    })
    df["Answer"] = answers
    df["Result"] = ["Correct" if r.strip().lower() == a.strip().lower() else "Incorrect" for r, a in zip(responses, answers)]
    df.to_csv(f"{roll_number}_{name}_quiz_results.csv", index=False)

def main():
    if login():
        roll_number = st.text_input("Enter Roll Number (Format: 23F-XXXX)")
        name = st.text_input("Enter Name")
        responses = quiz()
        if st.button("Finish"):
            score = grade_quiz(responses)
            st.success(f"Your score: {score}/{len(questions)}")
            download_quiz(roll_number, name, responses, score)
            st.markdown(f"### [Download Quiz Results](/{roll_number}_{name}_quiz_results.csv)")

if __name__ == "__main__":
    main()

import json
import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import openai

# Initialize OpenAI with your API key
openai.api_key = 'your_openai_api_key'

def load_questions(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def enhance_question(question_data):
    # Use OpenAI to enhance the question
    question = question_data['question']
    answer = question_data['answer']

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Enhance the following Java interview question and provide a detailed answer:\n\nQuestion: {question}\n\nAnswer: {answer}",
        max_tokens=150
    )
    
    enhanced_answer = response.choices[0].text.strip()
    return {
        'question': question,
        'answer': enhanced_answer
    }

def ask_question(question_data):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    question = question_data['question']
    answer = question_data['answer']
    
    user_input = simpledialog.askstring("Flash Card Question", question)
    if user_input is not None:
        messagebox.showinfo("Answer", answer)
    root.destroy()

def main():
    questions = load_questions('questions.json')
    enhanced_questions = [enhance_question(q) for q in questions]
    random.shuffle(enhanced_questions)
    for question_data in enhanced_questions:
        ask_question(question_data)

if __name__ == "__main__":
    main()

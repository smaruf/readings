import json
import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import openai

# Documentation for obtaining OpenAI API key
"""
To use the OpenAI API, you need to obtain an API key. Follow these steps to get your key:

1. Sign up for an OpenAI account at https://beta.openai.com/signup/.
2. log in to the OpenAI platform once you have an account.
3. Navigate to the API section: https://beta.openai.com/account/api-keys.
4. Click "Create new secret key" to generate a new API key.
5. Copy the generated API key and replace 'your_openai_api_key' in the script with your actual API key.

Make sure to keep your API key secure and do not share it publicly.
"""

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

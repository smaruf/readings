# Interactive Flash Card Game for Interview Preparation

This repository contains an interactive flashcard game to help users prepare for Java and Spring Framework interviews. The game uses dialog boxes to present questions and answers, and leverages GitHub AI to enrich the content with each run.

## Features
- Fetches and randomizes interview questions from a markdown file.
- Uses a dialog box interface for an interactive experience.
- Enriches questions and answers using GitHub AI tools.
- Designed to help novices prepare effectively for technical interviews.

## Contents
- `interview/java_spring_preparation.md`: A guide with essential Java and Spring Framework interview topics.
- `questions.json`: A JSON file containing the extracted questions and answers from the guide.
- `java_spring_interview.py`: A Python script to run the interactive flashcard game.

## How to Use

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/smaruf/readings.git
   cd readings
   ```
2. **Extract Questions and Answers**: Ensure that the questions from `interview/java_spring_preparation.md` are extracted into `questions.json`.

3. **Run the Flash Card Game**: Execute the Python script to start the game:

   ```sh 
   python java_spring_interview.py
   ```

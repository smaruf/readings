import random
import time
import requests

# URL of the markdown file in the GitHub repository
url = "https://raw.githubusercontent.com/smaruf/readings/master/interview/java_interview_topics.md"

def fetch_topics(url):
    response = requests.get(url)
    content = response.text.splitlines()
    topics = []
    for line in content:
        if line.strip().startswith("1. "):  # Find the start of the topics list
            topics = content[content.index(line):]
            break
    return [line.split('. ', 1)[1] for line in topics if line.strip() and line[0].isdigit()]

def enhance_topic(topic):
    # Simulate AI enhancement (can be replaced with actual AI enhancement logic)
    return f"Enhanced details for: {topic}"

def display_topic(topic):
    print("\nTopic:", topic)
    # Simulating fetching and displaying enhanced information
    enhanced_topic = enhance_topic(topic)
    print("Fetching detailed information...")
    time.sleep(1)
    print(enhanced_topic)

def main():
    topics = fetch_topics(url)
    print("Java Interview Topics Interactive Display")
    while True:
        input("Press Enter to display a random topic...")
        topic = random.choice(topics)
        display_topic(topic)
        print("\n")

if __name__ == "__main__":
    main()

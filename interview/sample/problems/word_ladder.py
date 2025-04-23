from collections import deque

def wordLadderLength(beginWord, endWord, wordList):
    wordList = set(wordList)  # Convert to set for O(1) lookups
    if endWord not in wordList:
        return 0
    
    # Initialize BFS
    queue = deque([(beginWord, 1)])  # (current word, transformation steps)
    
    while queue:
        current_word, steps = queue.popleft()
        
        # Check all possible one-letter transformations
        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                # Generate the transformed word
                transformed_word = current_word[:i] + char + current_word[i+1:]
                
                # If the transformed word is the endWord, return the steps
                if transformed_word == endWord:
                    return steps + 1
                
                # If the transformed word is in the word list, add it to the queue
                if transformed_word in wordList:
                    wordList.remove(transformed_word)  # Mark as visited
                    queue.append((transformed_word, steps + 1))
    
    return 0  # No transformation sequence found

# Example Usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(wordLadderLength(beginWord, endWord, wordList))  # Output: 5

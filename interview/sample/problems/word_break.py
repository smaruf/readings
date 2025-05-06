def wordBreak(s, wordDict):
    wordSet = set(wordDict)  # Convert wordDict to a set for O(1) lookup
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: empty string

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return dp[n]

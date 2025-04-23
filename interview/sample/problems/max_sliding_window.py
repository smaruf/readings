from collections import deque

def maxSlidingWindow(nums, k):
    # Deque to store indices of array elements
    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove indices that are out of the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements from the deque that are smaller than the current element
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add the current element's index to the deque
        dq.append(i)

        # Append the maximum of the current window to the result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))  # Output: [3, 3, 5, 5, 6, 7]

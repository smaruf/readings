def maxArea(height):
    # Initialize two pointers and the maximum area
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area between the two pointers
        width = right - left
        area = min(height[left], height[right]) * width
        max_area = max(max_area, area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # Output: 49 (between the lines at index 1 and 8)

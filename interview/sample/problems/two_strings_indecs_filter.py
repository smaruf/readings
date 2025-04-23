def find_removable_indices(str1, str2):
    if len(str1) != len(str2) + 1:
        return [-1]

    result = []

    def matches_after_removal(skip_index):
        for i in range(len(str2)):
            if str1[i if i < skip_index else i + 1] != str2[i]:
                return False
        return True

    for i in range(len(str1)):
        if matches_after_removal(i):
            result.append(i)

    return result if result else [-1]

# Test case
str1 = "abdgggda"
str2 = "abdggda"
print(find_removable_indices(str1, str2))  # Output: [3, 4, 5]

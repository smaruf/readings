def find_removable_indices(str1, str2):
    if len(str1) != len(str2) + 1:
        return [-1]

    result = []

    for skip_index in range(len(str1)):
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            if i == skip_index:
                i += 1  # skip this character
                continue
            if str1[i] != str2[j]:
                break
            i += 1
            j += 1
        if j == len(str2):  # matched all of str2
            result.append(skip_index)

    return result if result else [-1]


# Test case
str1 = "abdgggda"
str2 = "abdggda"
print(find_removable_indices(str1, str2))  # Output: [3, 4, 5]

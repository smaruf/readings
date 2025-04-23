#include <stdio.h>
#include <string.h>

#define MAX_LEN 200005

void findRemovableIndices(const char *str1, const char *str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    int found = 0;

    if (len1 != len2 + 1) {
        printf("-1\n");
        return;
    }

    for (int skip = 0; skip < len1; skip++) {
        int i = 0, j = 0;
        while (i < len1 && j < len2) {
            if (i == skip) {
                i++;  // skip this character
                continue;
            }
            if (str1[i] != str2[j])
                break;
            i++;
            j++;
        }
        if (j == len2) {
            printf("%d ", skip);
            found = 1;
        }
    }

    if (!found) {
        printf("-1");
    }
    printf("\n");
}

int main() {
    const char *str1 = "abdgggda";
    const char *str2 = "abdggda";

    findRemovableIndices(str1, str2);  // Output: 3 4 5

    return 0;
}

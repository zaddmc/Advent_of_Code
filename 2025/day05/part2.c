#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int comp(const void *a, const void *b) { return strcmp(a, b); }

int main(void) {
    FILE *fptr = fopen("./input.txt", "r");
    char ranges[256][33];
    int range_idx = 0;

    while (fgets(ranges[range_idx], 33, fptr)) {
        if (strcmp(ranges[range_idx++], "\n") == 0)
            break;
    }
    range_idx--;
    fclose(fptr);
    printf("%d", range_idx);

    qsort(ranges, range_idx, sizeof(char) * 33, comp);
    for (int i = 0; i < range_idx; i++) {
        printf("%s", ranges[i]);
    }

    return EXIT_SUCCESS;
}

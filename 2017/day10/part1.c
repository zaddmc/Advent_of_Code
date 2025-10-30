#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
int main(void) {
    FILE *fptr = fopen("input.txt", "r");

    int values[256];
    for (int i = 0; i < 256; i++) {
        values[i] = i;
    }
    char ch;
    int change = 0;
    int skip = 0;
    int j = 0;

    while ((ch = getc(fptr)) != EOF) {
        if (ch == ',' || ch == 10) {
            printf("%i\n", change);
            change = 0;
        } else {
            change *= 10;
            change += ch - '0';
        }
    }

    fclose(fptr);
    return EXIT_SUCCESS;
}

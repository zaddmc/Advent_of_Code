#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *fptr = fopen("input.txt", "r");
    char lch = '\0';
    char fch = '\0';
    char ch;
    int sum = 0;

    while ((ch = fgetc(fptr)) != EOF) {
        if (lch == '\0') {
            lch = ch;
            fch = ch;
            continue;
        }
        if (lch == ch) {
            sum += ch - '0';
        }
        if (ch == 10) { // Weird end of file chars, it might be LF (10)
            sum += lch - '0';
            break;
        }
        lch = ch;
    }
    fclose(fptr);
    printf("%i\n", sum);
    return EXIT_SUCCESS;
}

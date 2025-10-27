#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 1024

int val = 5;
int handler(char line[BUFFER_SIZE]) {
    int i = 0;
    char ch;
    while ((ch = line[i]) != '\n') {
        int temp = val;
        switch (ch) {
        case 'U':
            temp += -3;
            break;
        case 'L':
            temp += -1;
            break;
        case 'D':
            temp += 3;
            break;
        case 'R':
            temp += 1;
            break;
        default:
            break;
        }
        if (0 < temp && temp <= 9)
            val = temp;

        i++;
    }
    return val;
}

int main(int argc, char *argv[]) {
    char fullline[BUFFER_SIZE];
    FILE *ftpr;
    ftpr = fopen("./input.txt", "r");
    while (fgets(fullline, BUFFER_SIZE, ftpr) != NULL) {
        printf("%i", handler(fullline));
    }
    printf("\n");

    fclose(ftpr);
    return EXIT_SUCCESS;
}

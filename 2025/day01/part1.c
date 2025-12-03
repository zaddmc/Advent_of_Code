#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
    FILE *fptr = fopen("./input.txt", "r");

    char dir = 'R';
    char line[10] = {'\0'};
    int pointing = 50;
    int zeros = 0;

    while ((dir = fgetc(fptr)) != EOF && (fgets(line, 10, fptr))) {
        pointing += (dir == 'R') ? atoi(line) : -atoi(line);
        pointing %= 100;
        zeros += pointing == 0;
    }

    printf("%i\n", zeros);
    fclose(fptr);
    return EXIT_SUCCESS;
}

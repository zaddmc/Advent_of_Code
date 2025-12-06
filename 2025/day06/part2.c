#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    FILE *fptr = fopen("./input.txt", "r");
    char data[5][4000];

    uint64_t total = 0;

    for (int i = 0; i < 5; i++) {
        fgets(data[i], 4000, fptr);
    }

    for (int i = 0; i < strlen(data[0]); i++) {
        // Do something with this data
    }

    fclose(fptr);
    return EXIT_SUCCESS;
}

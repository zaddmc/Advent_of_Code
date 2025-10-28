#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
int main(void) {
    FILE *fptr = fopen("./input.txt", "r");
    fseek(fptr, 0, SEEK_END);
    size_t fsize = ftell(fptr);
    fseek(fptr, 0, SEEK_SET);
    int *memory = calloc(fsize, sizeof(int));
    if (!memory) {
        perror("Failed to init memory");
        exit(EXIT_FAILURE);
    }

    char line[16] = {'\0'};
    int i = 0;
    while (fgets(line, sizeof(line), fptr)) {
        memory[i++] = atoi(line);
    }
    fclose(fptr);

    int ip = 0;
    int val = memory[ip];
    int steps = 0;
    while (ip < i && ip >= 0) {
        if (val >= 3) {
            memory[ip]--;
        } else {

            memory[ip]++;
        }
        ip += val;
        val = memory[ip];
        steps++;
    }

    printf("%i\n", steps);
    free(memory);
    return EXIT_SUCCESS;
}

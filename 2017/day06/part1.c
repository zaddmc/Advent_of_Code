#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *fptr = fopen("./input.txt", "r");
    fseek(fptr, 0, SEEK_END);
    size_t fsize = ftell(fptr);
    fseek(fptr, 0, SEEK_SET);

    char ch;
    int nums = 0;
    while ((ch = fgetc(fptr)) != EOF) {
        if (ch == 9 || ch == 10) {
            nums++;
        }
    }
    fseek(fptr, 0, SEEK_SET);

    int *numbers = calloc(nums, sizeof(int));
    nums = 0;
    char flag = 0;
    while ((ch = fgetc(fptr)) != EOF) {
        if (ch == 9 || ch == 10) {
            flag = 0;
            nums++;
        } else {
            if (flag) {
                numbers[nums] *= 10;
            }
            numbers[nums] += ch - '0';
            flag = 1;
        }
    }
    fclose(fptr);

    printf("I can get the memory, but have a hard time thinking how i will "
           "store the attempts\n");

    return EXIT_SUCCESS;
}

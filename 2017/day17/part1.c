#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {

    char buf[10];
    FILE *fptr = fopen("input.txt", "r");
    fgets(buf, sizeof(buf), fptr);
    fclose(fptr);
    int cur_pos = atoi(buf);

    printf("input is %i\n", cur_pos);

    for (int i = 0; i < 2017; i++) {
    }

    return EXIT_SUCCESS;
}

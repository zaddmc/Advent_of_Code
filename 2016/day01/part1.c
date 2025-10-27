#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

int myDirection = 0;
int northsouth = 0;
int eastwest = 0;

void interpret(char dir, int dist) {
    if (dir == 'R') {
        myDirection += 1;
    } else {
        myDirection += -1;
    }
    if (myDirection >= 4) {
        myDirection -= 4;
    } else if (myDirection < 0) {
        myDirection += 4;
    }

    switch (myDirection) {
    case 0: // North
        northsouth += dist;
        break;
    case 1: // East
        eastwest += dist;
        break;
    case 2: // South
        northsouth -= dist;
        break;
    case 3: // West
        eastwest -= dist;
        break;
    }
}
int main(int argc, char *argv[]) {
    char ch;
    char dir = 'n';
    char number[10] = "        ";
    int numberPtr = 0;

    FILE *fptr;
    fptr = fopen("input.txt", "r");
    while ((ch = fgetc(fptr)) != EOF) {
        if (ch == 'R' | ch == 'L') {
            dir = ch;
            continue;
        }
        if (isdigit(ch)) {
            number[numberPtr] = ch;
            numberPtr += 1;
            continue;
        }
        if (ch == ' ') {
            continue;
        }
        interpret(dir, atoi(number));
        dir = 'n';
        for (int i = 0; i < 10; i++) {
            number[i] = ' ';
        }
        numberPtr = 0;
    }
    fclose(fptr);

    int result = abs(northsouth) + abs(eastwest);
    printf("%i\n", result);

    return EXIT_SUCCESS;
}

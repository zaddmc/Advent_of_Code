#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

int myDirection = 0;
int northsouth = 0;
int eastwest = 0;

void interpret() {
    switch (myDirection) {
    case 0: // North
        northsouth += 1;
        break;
    case 1: // East
        eastwest += 1;
        break;
    case 2: // South
        northsouth -= 1;
        break;
    case 3: // West
        eastwest -= 1;
        break;
    default:
        printf("The world is gonna burn  %i\n", myDirection);
        break;
    }
}
int known[2000] = {0};
int knownPtr = 0;

int cmpDub(int ns, int ew) {
    for (int i = 0; i < knownPtr - 2; i += 2) {
        int cmp_ns = known[i];
        int cmp_ew = known[i + 1];
        if (cmp_ns == 0 && cmp_ew == 0)
            continue;
        if (ns == cmp_ns && ew == cmp_ew) {
            printf("Found %i   %i", cmp_ns, cmp_ew);
            return 1;
        }
    }
    // printf("No\n");
    return 0;
}

int walk(int dist) {
    int return_value = 0;
    for (int i = 0; i < dist; i++) {
        interpret();
        known[knownPtr++] = northsouth;
        known[knownPtr++] = eastwest;
        if (cmpDub(northsouth, eastwest)) {
            printf("  Est %i,   %i\n", northsouth, eastwest);
            return_value = 1;
        }
        if (knownPtr >= sizeof(known)) {
            printf("knownPtr is nearly the same size of known");
            exit(EXIT_FAILURE);
        }
    }
    return return_value;
}

int main(int argc, char *argv[]) {
    char ch;
    char dir = 'n';
    char number[10] = "        ";
    int numberPtr = 0;

    FILE *ftpr;
    ftpr = fopen("input.txt", "r");
    while ((ch = fgetc(ftpr)) != EOF) {
        if (ch == 'R') {
            myDirection += 1;
            myDirection = abs(myDirection) % 4;
            continue;
        }
        if (ch == 'L') {
            myDirection += -1;
            myDirection = abs(myDirection) % 4;
            continue;
        }

        // Generate number
        if (isdigit(ch)) {
            number[numberPtr] = ch;
            numberPtr += 1;
            continue;
        }
        if (ch == ' ') {
            continue;
        }

        if (walk(atoi(number))) {
        }

        // Reset number
        for (int i = 0; i < 10; i++) {
            number[i] = ' ';
        }
        numberPtr = 0;
    }

    int result = abs(northsouth) + abs(eastwest);
    printf("Result  %i\n", result);

    printf("Memory Dump:\n");
    for (int i = 0; i < knownPtr; i += 2) {
        printf("%i  %i\n", known[i], known[i + 1]);
    }

    return EXIT_SUCCESS;
}

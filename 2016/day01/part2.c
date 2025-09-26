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
int known[200] = {0};
int knownPtr = 0;

int cmpDub(int ns, int ew) {
    printf("%i,    %i\n", ns, ew);
    for (int i = 0; i < knownPtr; i += 2) {
        if (ns == known[i] && (ew >= ns && ns >= known[i + 1])) {
            printf("Found Candidat\n");
        }
        if (ew == known[i + 1] && (ns >= ew && ew >= known[i])) {
            printf("Found Candidat: ns:%i, ew:%i, ki:%i, ki+:%i\n", ns, ew,
                   known[i], known[i + 1]);
        }
    }
    return 0;
}
int main(int argc, char *argv[]) {
    char ch;
    char dir = 'n';
    char number[10] = "        ";
    int numberPtr = 0;

    FILE *ftpr;
    ftpr = fopen("input.txt", "r");
    while ((ch = fgetc(ftpr)) != EOF) {
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

        if (cmpDub(northsouth, eastwest)) {
            printf("Est %i,   %i\n", northsouth, eastwest);
            break;
        }
        known[knownPtr++] = northsouth;
        known[knownPtr++] = eastwest;
    }

    int result = abs(northsouth) + abs(eastwest);
    printf("Result  %i\n", result);

    return EXIT_SUCCESS;
}

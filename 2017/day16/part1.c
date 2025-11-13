#include "string.h"
#include <stdio.h>
#include <stdlib.h>

int find_char(const char arr[], const char target) {
    for (int i = 0; i < strlen(arr); i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

int main(void) {
    char programs[] = "abcdefghijklmnop";

    FILE *fptr = fopen("input.txt", "r");
    char ch;
    char taskFlag = '\0';
    int paramNum = 0;
    char param1[5];
    char param2[5];

    char store;
    int tar1, tar2;
    char mycopy[16];

    while ((ch = fgetc(fptr)) != EOF) {
        if (ch == ',' || ch == 10) {
            switch (taskFlag) {
            case 's':
                strcpy(mycopy, programs);
                tar1 = atoi(param1);
                for (int i = 0; i < 16; i++) {
                    programs[(i + tar1) % 16] = mycopy[i];
                }
                break;
            case 'x':
                store = programs[atoi(param1)];
                programs[atoi(param1)] = programs[atoi(param2)];
                programs[atoi(param2)] = store;
                break;
            case 'p':
                tar1 = find_char(programs, param1[0]);
                tar2 = find_char(programs, param2[0]);

                store = programs[tar1];
                programs[tar1] = programs[tar2];
                programs[tar2] = store;
                break;
            default:
                break;
            }

            taskFlag = '\0';
            paramNum = 0;
            memset(param1, 0, 5);
            memset(param2, 0, 5);

        } else if (taskFlag == '\0') {
            taskFlag = ch;
        } else if (ch == '/') {
            paramNum = 1;
        } else {
            if (paramNum == 0) {
                param1[strlen(param1)] = ch;
            } else {
                param2[strlen(param2)] = ch;
            }
        }
    }

    printf("%s\n", programs);
    return EXIT_SUCCESS;
}

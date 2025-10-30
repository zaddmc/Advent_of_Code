#include <stdio.h>
#include <stdlib.h>
struct BinaryTreeNode {
    int weight;
    struct BinaryTreeNode *nodes;
};

struct BinaryTreeNode *newNodeCreate(int value) {
    struct BinaryTreeNode *temp =
        (struct BinaryTreeNode *)malloc(sizeof(struct BinaryTreeNode));
    temp->weight = value;
    temp->nodes = NULL;
    return temp;
}

int main(void) {
    FILE *fptr = fopen("exp.txt", "r");

    fclose(fptr);
    return EXIT_SUCCESS;
}

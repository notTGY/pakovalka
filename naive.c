#include <stdio.h>
#include <stdlib.h>

int main() {
    int num, idx;

    FILE *fp = freopen("output.txt", "w", stdout);
    if (fp == NULL) {
        perror("Failed to redirect stdout");
        return 1;
    }
    if (freopen("data/lengths.csv", "r", stdin) == NULL) {
        perror("Failed to redirect stdin");
        return 1;
    }
    scanf("Id, Length\n");
    while (scanf("%d, %d", &idx, &num) == 2) {
        printf("%d\n", idx);
    }

    fclose(fp);
    return 0;
}

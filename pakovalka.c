#include <stdio.h>
#include <stdlib.h>

#define N 1058740
#define seqlen 4096
int lengths[N];

int main() {
    int *lengths;
    int num, idx;

    lengths = malloc(sizeof(int) * N);

    FILE *fp = freopen("output.txt", "w", stdout);
    if (fp == NULL) {
        perror("Failed to redirect stdout");
        return 1;
    }
    if (freopen("data/babylm-10M.csv", "r", stdin) == NULL) {
        perror("Failed to redirect stdin");
        return 1;
    }
    scanf("Id, Length\n");
    while (scanf("%d, %d", &idx, &num) == 2) {
        lengths[idx] = num;
    }

    for (int i = 0; i < N; i++) {
        printf("%d\n", i);
    }

    fclose(fp);
    free(lengths);
    return 0;
}

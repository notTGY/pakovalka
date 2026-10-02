#include <stdio.h>
#include <stdlib.h>

#define SEQLEN 4096

int main() {
    int num, idx;
    int heads[SEQLEN + 1];
    size_t capacity = 1024;
    int *next = malloc(capacity * sizeof(*next));
    if (!next) return 1;
    for (int i = 0; i <= SEQLEN; ++i) heads[i] = -1;

    FILE *fp = freopen("output.txt", "w", stdout);
    if (fp == NULL) {
        perror("Failed to redirect stdout");
        return 1;
    }
    if (freopen("data/lengths.csv", "r", stdin) == NULL) {
        perror("Failed to redirect stdin");
        return 1;
    }
    scanf("Length\n");
    idx = 0;
    while (scanf("%d", &num) == 1) {
        if (idx < 0 || num < 0 || num > SEQLEN) return 1;
        if ((size_t)idx >= capacity) {
            while ((size_t)idx >= capacity) capacity *= 2;
            int *grown = realloc(next, capacity * sizeof(*next));
            if (!grown) return 1;
            next = grown;
        }
        next[idx] = heads[num];
        heads[num] = idx;
        idx++;
    }

    /* Fill each batch with the largest remaining sequence that fits.
       Length buckets avoid sorting the million input records. */
    int largest = SEQLEN;
    while (largest >= 0) {
        while (largest >= 0 && heads[largest] == -1) --largest;
        if (largest < 0) break;
        int remaining = SEQLEN;
        int first = 1;
        for (int length = largest; length >= 0; --length) {
            while (length <= remaining && heads[length] != -1) {
                int id = heads[length];
                heads[length] = next[id];
                printf(first ? "%d" : " %d", id);
                first = 0;
                remaining -= length;
            }
        }
        putchar('\n');
    }

    fclose(fp);
    free(next);
    return 0;
}

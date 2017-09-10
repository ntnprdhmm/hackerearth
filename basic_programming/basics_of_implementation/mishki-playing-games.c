#include <stdio.h>

int count_divisible_by_2(int n)
{
    if (n == 1 || n == 0)
        return n;

    int power = 0;
    int value = 1;
    while (value * 2 <= n) {
        value *= 2;
        power++;
    }
    return power + 1;
}

int main()
{
    int n, q, v, i, l, r, nb_turns = 0;

    scanf("%d %d", &n, &q);

    int arr[n+1];
    arr[0] = 0;

    for (i = 0; i < n; i++) {
        scanf("%d", &v);
        arr[i+1] = count_divisible_by_2(v) + arr[i];
    }

    while (q--) {
        scanf("%d %d", &l, &r);

        nb_turns = l == 1 ? arr[r] : arr[r] - arr[l-1];

        printf(nb_turns % 2 == 1 ? "Mishki" : "Hacker");
        printf("\n");
    }

    return 0;
}

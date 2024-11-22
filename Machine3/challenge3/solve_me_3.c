#include <stdio.h>

int main() {
    int x = 0;
    printf("Enter a number: ");
    scanf("%d", &x);

    // Corrected condition: x^2 - x + 1 == 1333
    if ((x * x - x + 1) == 1333) {
        printf("Flag: ctf_{custom_alg_solution}\n");
    } else {
        printf("Incorrect input.\n");
    }
    return 0;
}


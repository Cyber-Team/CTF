#include <stdio.h>
#include <string.h>

int main() {
    char input[20];
    printf("Enter password: ");
    scanf("%19s", input);
    if (strcmp(input, "Security-is-myth") == 0) {
        printf("Flag: ctf_{simple_password_found}\n");
    } else {
        printf("Incorrect password.\n");
    }
    return 0;
}

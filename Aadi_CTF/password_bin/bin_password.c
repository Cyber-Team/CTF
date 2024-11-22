#include <stdio.h>
#include <string.h>

void hint() {
    printf("Hint: The password is the name of a cybersecurity team founded by the author, who is involved in Linux Foundation Networking.\n");
}

int main() {
    char input[50];
    hint();
    printf("Enter the password: ");
    scanf("%s", input);

    if (strcmp(input, "CyberTeam") == 0) {
        printf("Congratulations! Here is your flag: ctf_{cYBer_tEAm_AdiTi_47}\n");
    } else {
        printf("Wrong password. Try again!\n");
    }

    return 0;
}


#include <stdio.h>
#include <string.h>

void decrypt(char *input) {
    char key = 0x5A;
    for (int i = 0; i < strlen(input); i++) {
        input[i] ^= key;
    }
}

int main() {
    char encrypted_flag[] = {0x1F, 0x39, 0x28, 0x28, 0x0E, 0x33, 0x36, 0x35, 0x00};  // "ctf_{xor_flag}"
    decrypt(encrypted_flag);
    printf("Flag: %s\n", encrypted_flag);
    return 0;
}

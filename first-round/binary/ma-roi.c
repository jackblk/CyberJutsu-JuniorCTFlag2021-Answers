#include <stdio.h>
#include <string.h>

int checkPassword(char * pwd) {
    int length = strlen(pwd);
    printf("%d", length);
    // password length is 15 char
    if ((length ^ 0x000000000000000F))
        return 0;;

    // pwd: CTF{...
    if ((strncmp(pwd, "\x43" "T\106{", 0x4) ^ 0))
            return 0;;

    printf("\n%s", pwd);
    // CTF{...}
    if (pwd[14] != '}')
        return 0;;

    // slice first 4 chars
    // temp is now: xxxxxxxxxx}
    const char * temp = pwd + 0x4;

    printf("\n\n%s\n", temp);
    printf("\n\nDEBUG: %d, %d\n", (temp[0x4] - temp[0x3]), (char)(-0x12) );

    // t[0]: 0
    if (temp[0] != '0') return 0;;

    // t[1]: b
    if (((int) temp[1] + 0x1b39 ^ 0x1B9B)) return 0;;

    // t[2] + t[3] = 219
    // t[3] - t[2] = 15
    if (((int) temp[2] + (int) temp[3] ^ 0x00000000000000DB)) return 0;;
    if (((int) temp[3] - (int) temp[2] ^ 0x000000000000000F)) return 0;;
    // => CTF{0bfu...} 89: fu

    // t[5]: '4'
    if (((temp[5] ^ '0') ^ 0x0000000000000004)) return 0;;

    // t[4]: c
    if (temp[0x4] - temp[0x3] != (char)(-0x12)) return 0;;


    // not used?
    // char o_f5c873c850d6c0a448164d6be733d86f = (char) temp[0x6] * (char) temp[0x5];

    // guessed: t[6]: t
    if ((char)(temp[0x6] * temp[0x5]) != -0x70) return 0;;

    // guessed: t[7]
    // 10*a - 12*b + 19*c = 2004
    if ((0xA * (int) temp[0x7] - 0xc * (int) temp[0x8] + 0x13 * (int) temp[0x9] ^ 0x00000000000007D4)) return 0;;
    printf("\n\nOK\n\n");
    // 28*a - b + 69*c = 8914
    if ((0x1c * (int) temp[0x7] - (int) temp[0x8] + 0x45 * (int) temp[0x9] ^ 0x00000000000022D2)) return 0;;
    // 113*a - 126*b + 999 *c = 109379
    if ((0x71 * (int) temp[0x7] - 0x7e * (int) temp[0x8] + 0x3e7 * (int) temp[0x9] ^ 0x000000000001AB43)) return 0;;
    // -> 49 48 110 -> '10n'
    return 1;
};

int main()
{
    // obfucation, can guess without solving last 4 - CTF{0bfuc4xxxx}
	char password[128] = "CTF{0bfuc4t10n}";
	printf("[+] Hay~ nhap password: ");
	// gets(password);
	if (0 != checkPassword(password))
		printf("[+] Password dung, flag la %s\n", password);
	else
		printf("[+] Ban da nhap sai password\n");
	return 0;
}

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool only_digits(string arg);
char rotate(char chr, int key);

int main(int argc, string argv[])
{
    if (!(argc == 2))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    if (!(only_digits(argv[1])))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        printf("%c", rotate(plaintext[i], atoi(argv[1])));
    }
    printf("\n");
}

bool only_digits(string arg)
{
    if (isdigit(arg[0]))
    {
        return true;
    }
    else
    {
        return false;
    }
}

char rotate(char chr, int key)
{
    if (isalpha(chr))
    {
        if (isupper(chr))
        {
            return (chr - 'A' + key) % 26 + 'A';
        }
        if (islower(chr))
        {
            return (chr - 'a' + key) % 26 + 'a';
        }

        return 0;
    }
    else
    {
        return chr;
    }
}

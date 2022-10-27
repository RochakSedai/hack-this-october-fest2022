#include <stdio.h>
#include <string.h>
 
int main()
{
    char str[] = { "aabba" };

    int l = 0;
    int h = strlen(str) - 1;
 
    while (h > l) {
        if (str[l++] != str[h--]) {
            printf("%s is not a palindrome\n", str);
            return 0;
            // will return from here
        }
    }
 
    printf("%s is a palindrome\n", str);
 
    return 0;
}
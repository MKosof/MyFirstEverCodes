#include <stdio.h>

int main(void)
{

    int n;
    int *p = &n;
    printf("%p\n", &n);
    printf("%p\n", p);
    printf("%p\n", &p);

}
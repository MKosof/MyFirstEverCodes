#include <stdio.h>
#include <stdlib.h>

int main()
{
  // If you use the format char *pointers = "Something" to define them, the "something", becomes a permanant part of code, and is not freeable after.
  // I don't know if "Something" is stored in the RAM however or in the hard drive, but assuming ram by the nature of pointers?
  char *a="Hello\n";
  char *b=a;
  printf("%p\n",a);
  a="hey\n";
  printf("%p\n",a);
  printf("%p\n",b);
}

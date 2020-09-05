// single line comment

/*
 multiline comment
*/

#include <stdio.h>
#include <string.h>

#define NAME "GWAR"

//global vars can be used outside of main
int globalVar = 991;

int main () {

  char aLetter = 'G';

  // max vaule for int is 32,768
  int var1 = 23;
  long int var2 = -327670000;
  float pie = 3.14159;
  double bigvar1 = 3.14159141591415914159;

  /*
   *  \n for new line, \t is tab, to use backslash
      do \\, for quotes: \"
  */

  printf("<==========================>\n");
  printf("this is print\n\n");
  printf("I am %d years old\n\n",var1);
  printf("long int = %ld\n\n",var2);
  printf("pie float = %.5f\n\n",pie);
  printf("long pie = %.15f\n\n",bigvar1);
  printf("The char = %c\n\n",aLetter);
  printf("%s\n\n","Printing strings" );

  char ch1 [12] = "GWAR";
  strcpy(ch1, "Bob Smack");
  printf("rock = %s\n\n",ch1);
}


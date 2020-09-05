#include <stdio.h>
#include <string.h>

#define NAME "GWAR"

int globalVar = 991;

int main() {
  char mI1;
  printf("\n");
  printf("Give me a letter: ");  //question for scanf
  scanf(" %c", &mI1);  //input from keyboard goes into var
  char nM1 [30], lM1[30];
  printf("What is your name? ");
  scanf(" %s %s", nM1,lM1);
  printf("Name = %s %c %s\n\n",nM1,mI1,lM1);
  int month, day, year;
  printf("What is your B-day? ");
  scanf(" %d%d%d",&month,&day,&year);
  printf("\nBirth Date %d/%d/%d\n\n ", month,day,year);

}

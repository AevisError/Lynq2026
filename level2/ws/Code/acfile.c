#include <stdio.h>
#include <ctype.h>

/*
program for caluclation of bonus, given basic pay and age



*/
int main(void){

    int n1=1, n2=0, iteration=0;
    long int csum= 0, tsum = 0, esum = 0, limit=4000000;


    while(csum <= limit ){
       csum = n1+n2;
       tsum+=csum;
       printf("[%i]: n1=%i, n2=%i |csum= %li| tsum = %li\n", iteration, n1, n2, csum, tsum);
       n2=n1;
       n1=csum;
       
       if(csum %2 == 0){
            printf("enetered -->");
            esum +=csum;
            printf("esum = %li\n \n",esum);
       }


       iteration++;




    }       


    return 1;

}
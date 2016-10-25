#include <stdio.h>
#include <stdlib.h>
 
long int catalan(int n){
    int i;
    long int res = 0;
    if (n <= 1) return 1;
 
    for (i=0; i<n; i++)
        res += catalan(i)*catalan(n-i-1);
 
    return res;
}
 
int main(int argc, char **argv){
    int i;
    int count = atoi(argv[1]);

    for (i=0; i<=count; i++)
        printf("%ld ",catalan(i) );
    return 0;
}

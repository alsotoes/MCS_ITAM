#include<stdio.h>
 
int max(int a, int b){
    return (a > b)? a : b;
}
 
int knapSack(int W, int wt[], int v[], int n){
    int i, j;
    int T[n+1][W+1];

    /* starting max value for first iteration */
    for ( j = 0; j <= W; j++) T[0][j] = 0;
 
    for (i = 1; i <= n; i++){
        for (j = 0; j <= W; j++){
            if (j >= wt[i-1]){
                T[i][j] = max(T[i-1][j], T[i-1][j-wt[i-1]] + v[i-1]);
            }else{
                T[i][j] = T[i-1][j];
            }
        }
    }
 
    return T[n][W];
}
 
int main(){
    int wt[] = {11, 7, 5, 4, 3, 3, 2, 2, 2, 2, 1};
    int v[] = {20, 10, 11, 5, 25, 50, 12, 6, 4, 5, 30};
    int W = 20;
    int n = 11;
    printf("Optimal value => %d\n", knapSack(W, wt, v, n));
    return 0;
}

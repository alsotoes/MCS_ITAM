#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MAX 10

long minimunProduct(long matrixSol[][10], long matrixRanges[], int i, int j){
    long temp, minProduct = LONG_MAX;
    int k;

    for(k = i; k <= j-1; k++){
        temp = matrixSol[i][k] + matrixSol[k+1][j] + ( matrixRanges[i-1]*matrixRanges[k]*matrixRanges[j]);
        if(temp < minProduct)
            minProduct = temp;
    }

    printf("min: %ld\n",minProduct);
    return minProduct;
}

long matrix_mult(long size, long matrixRanges[]){
    long matrixSol[size][size];
    int diagonal, i, j;
    
    memset(matrixSol, 0, sizeof(matrixSol));

    for(diagonal = 1; diagonal <= size-1; diagonal++){
        for(i = 0; i <= size-diagonal; i++){
            matrixSol[i][i+diagonal] = minimunProduct(matrixSol, matrixRanges, i, i+diagonal);
        }
    }

    for(i = 0; i < size; i++){
        for(j = 0; j < size; j++)
            printf("%ld ",matrixSol[i][j]);
        printf("\n");
    }


    printf("mul: %ld",matrixSol[0][size]);
    return matrixSol[0][size];
}

/*
    for(iLength=2; iLength<= size; iLength++)
        for(iStart=0; iStart+iLength-1 < size; iStart++){
            iEnd = iLength + size - 1;
            matrixSol[size][iEnd] = LONG_MAX;
            for(iCut=iStart; iCut<iEnd; iCut++){
                iTemp = matrixSol[iStart][iCut] + matrixSol[iCut+1][iEnd] + matrixRanges[iStart]*matrixRanges[iCut+1] * matrixRanges[iEnd+1];
                if( iTemp < matrixSol[iStart][iEnd]){
                    matrixSol[iStart][iEnd] = iTemp;
                    aiPartition[iStart][iEnd] = iCut;
                }
            }
        }
    return matrixSol[0][size-1];
}
*/
int main(int argc, char **argv){
    int i;
    int size = atoi(argv[1]);
    long *matrixRanges;
    long matrixSol[size][size];
    
    matrixRanges = (long *)malloc(size*(sizeof(long)));

    if(size > 0){
        for(i=0; i< size; i++)
            scanf("%ld %ld", &matrixRanges[i], &matrixRanges[i+1]);
        matrix_mult(size+1, matrixRanges);
    }

    /*
    for(i = 0; i < size +1; i++){
        printf("%ld ",matrixRanges[i]);
    }
    */

    return 0;
}

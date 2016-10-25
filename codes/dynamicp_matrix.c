#include <stdio.h>
#include <string.h>
#include <limits.h>

#define MAX 10

long i, iN, iCase;
long aiMatrixSize[MAX+1];
long aiPartition[MAX][MAX];

long matrix_mult(long iSize){
    long aiCost[MAX][MAX];
    long iStart, iEnd, iCut, iLength, iTemp;

    memset(aiCost, 0, sizeof(aiCost));
    for(iLength=2; iLength<= iSize; iLength++)
        for(iStart=0; iStart+iLength-1 < iSize; iStart++){
            iEnd = iLength + iSize - 1;
            aiCost[iSize][iEnd] = LONG_MAX;
            for(iCut=iStart; iCut<iEnd; iCut++){
                iTemp = aiCost[iStart][iCut] + aiCost[iCut+1][iEnd] + aiMatrixSize[iStart]*aiMatrixSize[iCut+1] * aiMatrixSize[iEnd+1];
                if( iTemp < aiCost[iStart][iEnd]){
                    aiCost[iStart][iEnd] = iTemp;
                    aiPartition[iStart][iEnd] = iCut;
                }
            }
        }
    return aiCost[0][iSize-1];
}

void print_solution(long iStart, long iEnd){
    if(iStart == iEnd)
        printf("A%ld",iStart+1);
    else{
        printf("(");
        print_solution(iStart, aiPartition[iStart][iEnd]);
        printf(" x ");
        print_solution(aiPartition[iStart][iEnd]+1, iEnd);
        printf(" ) ");
    }
}

int main(void){
    iCase = 0;
    scanf("%ld",&iN);
    while(iN != 0){
        for(i=0; i< iN; i++)
            scanf("%ld %ld", &aiMatrixSize[i], &aiMatrixSize[i+1]);
        matrix_mult(iN);
        //printf("Case %ld : ", ++iCase);
        //print_solution(0, iN-1);
        //printf("\n");
        scanf("%ld",&iN);
    }
    int i,j;

    printf("solution : \n");
    for(i=0;i<6;i++){
        for(j=0;j<6;j++)
            printf("%ld ",aiPartition[i][j]);
        printf("\n");
    }

    return 0;
}

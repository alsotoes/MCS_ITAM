#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int partition(int sum, int largestNumber){
    
    if(sum < 0 || largestNumber == 0)
        return 0;

    if(0 == sum)
        return 1;
    else
        if(sum < largestNumber)
            return partition(sum, sum);
        else
            if(sum == largestNumber)
                return 1+partition(sum, sum-1);
            else
                return partition(sum,largestNumber-1)
                + partition(sum-largestNumber,
                largestNumber);
}

int main(int argc, char **argv){
    int sum = atoi(argv[1]);
    int largestNumber = 1000000;

    printf("%d\n",partition(sum,largestNumber));

return 0;
}

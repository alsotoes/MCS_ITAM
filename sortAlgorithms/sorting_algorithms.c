#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <fcntl.h>
#include <time.h>
 
struct node{
    unsigned int data;
    struct node *next;
};

bool isEmpty(struct node *node)
{
    return (node == NULL);
}
 
void push(struct node** head_ref, int new_data)
{
    struct node* new_node = (struct node*)malloc(sizeof(struct node));
    struct node* searcher = NULL;
 
    new_node->data = new_data;
    new_node->next = NULL;
    
    if( isEmpty(*head_ref) ){
        (*head_ref) = new_node;
    }else{
        searcher = (*head_ref);
        while( searcher->next ){
            searcher = searcher->next;
        }
        searcher->next = new_node;
    }
}

void printValue(unsigned int n)
{
    printf("%u ", n);
} 
 
void printList(struct node *node, void (*fptr)(unsigned int)){
    while(node != NULL){
        (*fptr)(node->data);
        node = node->next;
    }
}

void printArr(unsigned int arr[], int length, void (*fptr)(unsigned int))
{
    int i;
    for(i = 0; i < length; i++){
        (*fptr)(arr[i]);
    }
}

void countList(struct node *node, int *count)
{
    while( !isEmpty(node) ){
        (*count)++;
        node = node->next;
    }
}

unsigned int getRand(void)
{
    unsigned int randVal;
    int urandom_fd;
    
    urandom_fd = open("/dev/random", O_RDONLY);
    if( -1 == urandom_fd ){
        int errsv = urandom_fd;
        printf("Error opening [/dev/urandom]: %i\n", errsv);
        exit(1);
    }

    read(urandom_fd, &randVal, sizeof(randVal));
    close(urandom_fd);

    return randVal;
}

// https://en.wikipedia.org/wiki/Insertion_sort
struct node *insertionSort(struct node *pList)
{
    // zero or one element in list
    if(pList == NULL || pList->next == NULL)
        return pList;
    // head is the first element of resulting sorted list
    struct node * head = NULL;
    while(pList != NULL) {
        struct node * current = pList;
        pList = pList->next;
        if(head == NULL || current->data < head->data) {
            // insert into the head of the sorted list
            // or as the first element into an empty sorted list
            current->next = head;
            head = current;
        } else {
            // insert current element into proper position in non-empty sorted list
            struct node * p = head;
            while(p != NULL) {
                if(p->next == NULL || // last element of the sorted list
                   current->data < p->next->data) // middle of the list
                {
                    // insert into middle of the sorted list or as the last element
                    current->next = p->next;
                    p->next = current;
                    break; // done
                }
                p = p->next;
            }
        }
    }
    return head;
}

unsigned int *insertionSortArr(unsigned int arr[], int length)
{
    unsigned int x;
    int i, j;

    for(i = 1; i < length; i++){
        x = arr[i];
        j = i - 1;
        while((j >= 0) && (arr[j] > x)){
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j+1] = x;
    }

    return arr;
}

void CopyArray(unsigned int B[], int iBegin, int iEnd, unsigned int A[])
{
    int k;
    for(k = iBegin; k < iEnd; k++)
        A[k] = B[k];
}

void TopDownMerge(unsigned int A[], int iBegin, int iMiddle, int iEnd, unsigned int B[])
{
    int i, j, k;
    i = iBegin, j = iMiddle;

    for (k = iBegin; k < iEnd; k++) {
        if (i < iMiddle && (j >= iEnd || A[i] <= A[j])) {
            B[k] = A[i];
            i = i + 1;
        } else {
            B[k] = A[j];
            j = j + 1;
        }
    }
}

void TopDownSplitMerge(unsigned int A[], int iBegin, int iEnd, unsigned int B[])
{
    int iMiddle;

    if(iEnd - iBegin < 2)                       // if run size == 1
        return;                                 //   consider it sorted

    iMiddle = (iEnd + iBegin) / 2;              // iMiddle = mid point
    TopDownSplitMerge(A, iBegin,  iMiddle, B);  // split / merge left  half
    TopDownSplitMerge(A, iMiddle,    iEnd, B);  // split / merge right half
    TopDownMerge(A, iBegin, iMiddle, iEnd, B);  // merge the two half runs
    CopyArray(B, iBegin, iEnd, A);              // copy the merged runs back to A
}

void TopDownMergeSort(unsigned int A[], unsigned int B[], int n)
{
    TopDownSplitMerge(A, 0, n, B);
}

/////////
/* function prototypes */
struct node* SortedMerge(struct node* a, struct node* b);
void FrontBackSplit(struct node* source, struct node** frontRef, struct node** backRef);
 
void MergeSort(struct node** headRef)
{
    struct node* head = *headRef;
    struct node* a;
    struct node* b;
 
    if((head == NULL) || (head->next == NULL)){
        return;
    }
 
    FrontBackSplit(head, &a, &b); 
 
    MergeSort(&a);
    MergeSort(&b);
 
    *headRef = SortedMerge(a, b);
}
 
struct node* SortedMerge(struct node* a, struct node* b)
{
    struct node* result = NULL;
 
    if (a == NULL)
        return(b);
    else if (b==NULL)
        return(a);
 
    if(a->data <= b->data){
        result = a;
        result->next = SortedMerge(a->next, b);
    }else{
        result = b;
        result->next = SortedMerge(a, b->next);
    }
  
    return(result);
}
 
void FrontBackSplit(struct node* source, struct node** frontRef, struct node** backRef)
{
    struct node* fast;
    struct node* slow;
  
    if(source==NULL || source->next==NULL){
        *frontRef = source;
        *backRef = NULL;
    }else{
        slow = source;
        fast = source->next;
 
        while(fast != NULL){
            fast = fast->next;
            
            if(fast != NULL){
                slow = slow->next;
                fast = fast->next;
            }
        }
 
        *frontRef = source;
        *backRef = slow->next;
        slow->next = NULL;
    }
}

int main(int argc, char **argv){
    struct node *head = NULL;
    struct node *sorted = NULL;
    int count = 0, length, i;
    unsigned int randVal, *arr = NULL, *sortedArr = NULL;
    clock_t start, end;

    length = atoi(argv[1]);
    arr = (unsigned int*)malloc(length*sizeof(unsigned int));
    sortedArr = (unsigned int*)malloc(length*sizeof(unsigned int));

    srand(time(NULL));
    start = clock();
    for(i = 0; i < length; i++){
        randVal = rand();

        push(&head, randVal); // LinkedList
        arr[i] = randVal; // Array
    }
    end = clock();
    printf("fill structures: %7.5f secs\n", ((double) (end - start)) / CLOCKS_PER_SEC);

    start = clock();
    sorted = insertionSort(head);
    end = clock();
    printf("insertionSort in linked list: %7.5f secs\n", ((double) (end - start)) / CLOCKS_PER_SEC);

    start = clock();
    sortedArr = insertionSortArr(arr, length);
    end = clock();
    printf("insertionSort in array: %7.5f secs\n", ((double) (end - start)) / CLOCKS_PER_SEC);

    start = clock();
    MergeSort(&head);;
    end = clock();
    printf("mergeSort in linked list: %7.5f secs\n", ((double) (end - start)) / CLOCKS_PER_SEC);

    start = clock();
    TopDownMergeSort(arr, sortedArr, length);
    end = clock();
    printf("mergeSort in array: %7.5f secs\n", ((double) (end - start)) / CLOCKS_PER_SEC);

    return 0;
}

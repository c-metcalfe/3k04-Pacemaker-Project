#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"

int main(){
    //PACKING - DCM SIDE
    int n = 16;
    uint8_t data[] = {4,100,130,25,34,29,29,40,24,3,14,4,7,0,0,0};
    uint8_t sum = 0;
    for (int i = 0; i < n-1; i++){
        sum += data[i];
    }
    uint8_t checksum = (~sum)+1;
    data[n-1] = checksum;

    //UNPACKING - SIMULINK SIDE
    sum = 0;
    for (int i = 0; i < n - 1; i++){
        sum += data[i];
    }
    printf("%d\n", checksum);
}
#include <stdio.h>
#include <stdlib.h>

int main(){
    void **ppvVar1;
    int prot;
    int flags;
    void *var_ch;
    int32_t var_8h;
    
    ppvVar1 = (void **)mmap(0, 4, 3, 0x21, 0xffffffff, 0);
    *ppvVar1 = (void *)0x3b9aca00;
    fork();
    fork();
    fork();
    fork();
    *ppvVar1 = (void *)((int32_t)*ppvVar1 + 0x499602d2);
    doNothing(*ppvVar1);
    return 0;
}

void doNothing(void *my_arg){
    FILE *target_file;

    target_file = fopen("/home/dahir/workspace/wargames/picoctf/reverse_engineering/forky/answers", "a");
    if (target_file == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }
    fprintf(target_file, "picoCTF{%d}\n", (u_int32_t)my_arg);
    fclose(target_file);
}
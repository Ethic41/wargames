#include <stdio.h>
#include <string.h>


int main(void){
    char str[] = "picoCTF_a3112";
    
    fun(str);
}

void fun(char *str){
    printf("%s\n", str);
}
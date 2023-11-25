#include<stdio.h>
#include<unistd.h>
#include<iostream>
#include <string>
#include <class.h>


int ref(Animal & a)
{
    a.show_age();
}

int main()
{
/* 

std::cout<<"***************************************************"<<std::endl;

const int NUM=3;
Animal xiaodongwu[NUM]={
    Animal("aaa",4),
    Animal("bbb",5),
    Animal("cccc")
};

int i;
const Animal * older=&xiaodongwu[0];
for(i=1;i<NUM;i++)
{
        older=& older->compare_age(xiaodongwu[i]);
}

older->show_age(); */
Animal jinchao("jinchao");
ref(jinchao);



}


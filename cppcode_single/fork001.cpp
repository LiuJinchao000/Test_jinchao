#include<stdio.h>
#include<unistd.h>
#include<iostream>
#include <string>
#include <class.h>



int a=10;

Animal xiaoliu {"xiaoliu",78};

int main()
{


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

older->show_age();

}


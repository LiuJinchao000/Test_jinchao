#include <stdio.h>
#include <iostream>
#include <unistd.h>
int main()
{
    using namespace std;
    std::cout<<"I am running"<<endl;
    pid_t id=fork();        
    if(id==0)
    {
        cout<<"0000000000000"<<endl;
    }
    else if(id>0)
    {
        cout<<1111111111111111<<endl;

    }
    else
    {
        cout<<"----------"<<endl;

    }

}
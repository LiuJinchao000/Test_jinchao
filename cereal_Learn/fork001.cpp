#include <iostream>
using namespace std;
 
int main()
{
       for (int i = 0; i < 5; i++)
              cout << (rand()%2)<<" ";         //生成[0,1]范围内的随机数
       cout << endl;
       for (int i = 0; i < 20; i++)
              cout << (rand() % 5 + 3) << " "; //生成[3,7]范围内的随机数
       cout << endl;
}
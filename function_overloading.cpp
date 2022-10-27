#include <iostream>

using namespace std;
 inline void swap(int &, int &);
int main()
{
    int a=5,b=6;
    cout<< "Before swapping: a="<<a<<" and b="<<b<< endl;
    swap(a,b);
    cout<< "After swapping: a="<<a<<" and b="<<b<<endl;
    return 0;
}
void swap(int &x, int &y){
    int temp;
    temp=x;
    x=y;
    y=temp;


}

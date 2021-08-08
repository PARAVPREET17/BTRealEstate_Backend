#include <iostream>
using namespace std;
struct pair
{
    int min;
    int max;
};
struct getminmax(int arr[],int n)
{
   struct pair number;
   if(n==1)
   {
       number.max=arr[0];
       number.min=arr[0];
   }
   if(n==2)
   {
       if(arr[0]>arr[1])
       {
           number.max=arr[0];
           number.min=arr[1];
       }
       else
       {
           number.max=arr[1];
           number.min=arr[0];
       }
       for(i=2;i<n;i++)
       {
           if(arr[i]>number.max)
           {
               number.max=arr[i];
           }
           else if(arr[i]<number.min)
           {
               number.min=arr[i];
           }
       }
   }
   return 1;
};
int main()
{   
    int size=6;
    int arr[100]={1,3,4,6,8,9};
    struct pair number=getminmax(arr,size);
    cout<<"Maximum is "<<number.max<<endl;
    cout<<"Minimum is "<<number.min<<endl;
    return 0;
}
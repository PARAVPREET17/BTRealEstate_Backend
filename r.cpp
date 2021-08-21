#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    int i, j, k, l, flag;
    char A[100], B[100];
    cout << "Enter string 1\n"; //k
    cin >> A;
    cout << "Enter string 2\n";
    cin >> B;
    for (i = 0; A[i] != ('\0'); i++)
    {
    }
    for (j = 0; B[j] != ('\0'); j++)
    {
    }
    for (k = 0, l = '\0';  l >= 0; k++, l--)
    {
        if (i == j)
        {
            if (A[k] == B[l - k])
            {
                flag == 1;
            }
            else if(A[k] != B[l - k])
                {
                    flag == 3;
                    break;
                }
        }
        else
        {
            flag == 2;
            break;
        }
    }
    if (flag == 1)
    {
        cout << "rotation";
    }
    else if (flag == 2 || flag == 3)
    {
        cout << "not a rotation";
    }
    return 0;
}
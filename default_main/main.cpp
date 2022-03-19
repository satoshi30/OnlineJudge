#include <iostream>
using namespace std;

int main()
{
    int v, a, b, c;
    cin >> v >> a >> b >> c;
    int total;
    total = a + b + c;
    v = v % total;;
    if (v < a)
    {
        cout << "F" << endl;
    }
    else if (v < (a+b))
    {
        cout << "M" << endl;
    }
    else
    {
        cout << "T" << endl;
    }
}
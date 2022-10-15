#include <iostream>
#include <bits/stdc++.h>
using namespace std;


bool isValid(string x) 
{
    stack <char> st;
    for(int i=0;i<x.length();i++)
    {
        if(st.empty()) st.push(x[i]);
        else
        {
            if(x[i]=='(' || x[i]=='{' || x[i]=='[') st.push(x[i]);
            else if(x[i]==']' && st.top()=='[') st.pop();
            else if(x[i]=='}' && st.top()=='{') st.pop();
            else if(x[i]==')' && st.top()=='(') st.pop();
            else return false;
        }
    }
    if(st.empty()) return true;
    return false;
}


int main()
{
    string s="{()}[]";
    if(isValid(s)) cout<<"Valid";
    else cout<<"Invalid";
}
#include <iostream>
#include <string>
#include <vector>

int main()
{

string data="";
cin >> data;
vector<char> list;
//char[] list = char[data.length()];
for( int i=0; i < data.length(); i++)
  {
    if(isalpha(data[i]))
      {
          list.push_back(data[i]);
      }
  }


  return 0;
}

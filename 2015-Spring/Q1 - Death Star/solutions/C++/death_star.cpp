// C++ solution for S2015 Q1
// By Preston Hamlin

#include <iostream>

using std::cin;
using std::cout;
using std::endl;


int main() {
  char  op  =0;
  int   num =0;
  long  val =0;
  
  // get first value
  cin >>val;
  
  // operators and numbers come in pairs
  while(cin >> op >> num) {
    //cout << val << " " << op << " " << num;
    switch(op) {
      case '+': {
        val += num;
        break; 
      }
      case '-': {
        val -= num;
        break; 
      }
      case '*': {
        val *= num;
        break; 
      }
      case '/': {
        val /= num;
        break; 
      }
    }
    //cout << "  = " << val << endl;
  }
  
  cout << val << endl;
  return 0;
}
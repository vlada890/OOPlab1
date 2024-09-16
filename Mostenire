#include <iostream>
#include <string>
using namespace std;

// Base class
class Persoana {
  public: 
    string name = "Ion";
    void greet() {
      cout << "Salut \n" ;
    }
};

// Derived class
class Student: public Persoana {
  public: 
    string facultate = "programare";
};

int main() {
  Student obj1;
  obj1.greet();
  cout << obj1.name + " este de la " + obj1.facultate;
  return 0;
}


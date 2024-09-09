#include <iostream>
#include <string>

class Person {
private:
    std::string name;
    int age;

public:
    void setName(std::string newName) {
        name = newName;
    }
//str is from std -standard library type
    void setAge(int newAge) {
        age = newAge; //age- valoarea actualizata ,newAge- parametrul atribuit variabilei
    }
//int is a fundamental type
    void displayInfo() {
        std::cout << "Name: " << name << std::endl;
        std::cout << "Age: " << age << std::endl;
    }
};

int main() {
    Person person;

    // Setting the name and age using public methods
    person.setName("Ana");
    person.setAge(10);

    // Displaying the information
    person.displayInfo();

    return 0;
}

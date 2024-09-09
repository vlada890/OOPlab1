class Animal(object):
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return str(self.name)+" are "+str(self.age)+" ani"

class Student(Animal):
    def __init__(self,age,name,licenta):
        Animal.__init__(self,age,name)
#instanta obiectului de clasa Student se initializeaza cu ajutorul atributelor clasei Animal prin mostenire
        self.licenta=licenta
    def speak(self):
        print ("Salut!Invat la "+str(self.licenta))
    def __del__(self):
        print(str(self.name)+' a fost sters')
#metoda str e mostenita de la superclasa Animal
#exemplu:pers1=Student(21,'igor','programare') 
#        print(persoana1) --> 'igor are 21 ani'
#destructorul instantei clasei Student
#exemplu: del pers1 --> 'igor a fost sters'

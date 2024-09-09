class carte(object):
    def __init__(self,titlu,autor,ISBN):
        self.titlu=titlu
        self.autor=autor
        self.ISBN=ISBN

    def __str__(self):
        return "cartea "+str(self.titlu)+" scrisa de "+str(self.autor)+" are codul "+str(self.ISBN)
#C1=carte('Cireasa','Ion On','231231')
#print(C1)
class biblioteca(object):
    def __init__(self):
        self.carti=[]
    def insert(self,s):
        if s not in self.carti:
            self.carti.append(s)
    def remove(self,s):
        if s in self.carti:
            self.carti.remove(s)
    def __str__(self):
        return "lista de carti: "+" ".join([str(a) for a in self.carti]) 

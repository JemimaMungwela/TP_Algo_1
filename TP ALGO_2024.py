# MUNGWELA KITOKO JEMIMA 2LEI
# Définir une classe Fonction ayant les attributs num pour numérateur et den pour dénominateur.

class Fraction:
    def __init__(self, num, den):
        assert den > 0 # Le dénominateur doit etre strictement positif.
        self.__num = num
        self.__den = den
    
    def __str__(self):
        if self.__den == 1:
            return str(self.__num)
        else:
            return f"{self.__num}/{self.__den}"
        
    def __eq__(self,other):
        return self.__num*other.__den == self.__den*other.__num
    
# Création des instances:
F1 = Fraction(3,4)
F2 = Fraction(-8,1)
F3 = Fraction(2,3)
F4 = Fraction(21,28)

# Affichage des isntances:
print(F1)     
print(F2)     
print(F3)     
print(F4)     

# Test d'égalité:
print(F1.__eq__(F2))     
print(F1.__eq__(F3))
print(F1.__eq__(F4))
print(F2.__eq__(F3))
print(F2.__eq__(F4))
print(F3.__eq__(F4))
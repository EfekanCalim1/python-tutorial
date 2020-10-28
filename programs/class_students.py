 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    class_ = "student"

    def test_score(self, score_1, score_2, score_3):
        total = score_1 + score_2 + score_3
        avg = total / 3
        return avg


efekan = Student("Efekan", 25)
print(efekan.class_)
print(efekan.test_score(30, 40,50))
      


    
    

  
        


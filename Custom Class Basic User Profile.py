#  Creating my own class for a basic user profile 

class User:
  existing_account = True
  def __init__(self,name='anonymous',years_experience=0):
    self.name = name
    self.y_e = years_experience
  def bio(self):
    print(f'My name is {self.name} and I have {self.y_e} years experience')

User1 = User('Lucy',100)
print(User1.bio())
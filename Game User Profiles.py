class User():
  def logged_in(self):
    print("User is logged in.")

class Wizard(User): 
  def __init__(self, name, power):
    self.name = name
    self.power = power
     
  def attack(self):
    print(f"{self.name} is attacking with {self.power} power.")
        
class Archer(User):
  def __init__(self, name, initial_arrows, num_arrows):
    self.name = name
    self.i_a = initial_arrows
    self.n_a = num_arrows
  def attack(self):
    r_a = self.i_a - self.n_a
    print(f"{self.name} is attacking with {self.n_a} arrows, and has {r_a} arrows left.")

wizard1 = Wizard("Gandalf",50)
archer1 = Archer('Legolas',50,3)

wizard1.logged_in()
wizard1.attack()
archer1.logged_in()
archer1.attack()
#2.challenge- implement a calculator 
class calculator:
    def __init__(self,input_1,input_2):
        self.input_1 = input_1
        self.input_2 = input_2
    def addition(self):
        add = self.input_1 + self.input_2
        print(f"the addition of two numbers is {add}")
    def subtraction(self):
        sub = self.input_1 - self.input_2
        print(f"the subtraction of two numbers is {sub}")
    def division(self):
        divide = self.input_1 / self.input_2
        print(f"the division of two numbers is {divide}")
    def multiplication(self):
        multiply = self.input_1 * self.input_2
        print(f"the multiplication of two numbers is {multiply}")
calci = calculator(12,4)
calci.addition()
calci.subtraction()
calci.division()
calci.multiplication()
    




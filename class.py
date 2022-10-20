class numbers:
    num1 = 0.0
    num2 = 0.0
    def Set(self, num1, num2):
	self.num1 = num1
	self.num2 = num2
        

def Main():
	num = numbers()
	num.Set(7, 8)	
	print("X= " + str(num.num1) + ", Y= " + str(num.num2))

if __name__=='__main__':
	Main()

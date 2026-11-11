# calc.py - a tiny calculator module 
VERSION = "1.1-stable" 
def add(a, b): 
	return a + b 
def subtract(a, b): 
	return a - b 

if __name__ == "__main__": 
	print("Calculator v" + VERSION) 
	print("2 + 3 =", add(2, 3))

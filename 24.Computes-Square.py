# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25, 2019

File: Computes-Square.py
Illustrates the definition of a main function

@author: Byen23
"""

def main():
	"""The main function for this script."""
	number = float(input("Enter a number: "))
	result = square(number)
	print("The square of", number, "is", result)
	
def square(x):
	"""Returns the square of x."""
	return x * x

# The entry point for program executive
if __name__ == "__main__":
	main()
	
	


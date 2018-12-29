# --------------
import pandas as pd
import numpy as np
import math


#Code starts here
class complex_numbers:
    def __init__(self,real,imag):
        self.real = float(real)
        self.imag = float(imag)

    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    def __add__(self,other):
        return complex_numbers(self.real + other.real, self.imag + other.imag)

    def __sub__(self,other):
        return complex_numbers(self.real - other.real, self.imag - other.imag)

    def __mul__(self,other):
        return complex_numbers(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)

    def __truediv__(self,other):
        c = pow(other.real,2) + pow(other.imag,2)
        a = self.real * other.real + self.imag * other.imag
        b = self.imag * other.real - self.real * other.imag
        return complex_numbers(a/c,b/c)

    def absolute(self):
        return math.sqrt(pow(self.real,2) + pow(self.imag,2))
    
    def argument(self):
        ans = np.arctan(self.imag/self.real)
        return math.degrees(ans)
    
    def conjugate(self):
        return complex_numbers(self.real,self.imag*(-1))

    
comp_1 = complex_numbers(3,5)
comp_2 = complex_numbers(4,4)

comp_sum = comp_1 + comp_2
comp_diff = comp_1 - comp_2
comp_prod = comp_1 * comp_2
comp_quot = comp_1 / comp_2
comp_abs = comp_1.absolute()
comp_conj = comp_1.conjugate()
comp_arg = comp_1.argument()



class Fraction:

    def __init__(self, x, y):
        self.numerator = x
        self.denominator = y

    # automatically string mn dikhayega
    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return '{}/{}'.format(new_num, new_den)
    
    def __sub__(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return '{}/{}'.format(new_num, new_den)
    
    def __mul__(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return '{}/{}'.format(new_num, new_den)
    
    def __truediv__(self, other):
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return '{}/{}'.format(new_num, new_den)


a = Fraction(3,4)
b = Fraction(2,5)
print(a / b)

class Math:

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def diff(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    @staticmethod
    def div_int(a, b):
        return a / b 

    @staticmethod
    def mod(a, b):
        return a % b

    @staticmethod
    def pow(a, b):
        return a ** b

    @staticmethod
    def root(a, b):
        return a * (1 / b)

print(Math.sum(5,3))
print(Math.diff(5,3))
print(Math.mul(5,3))
print(Math.div(5,3))
print(Math.div_int(5,3))
print(Math.mod(5,3))
print(Math.pow(5,3))
print(Math.root(8,3))

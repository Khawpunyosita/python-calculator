class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b < 0 and a < 0 or a > 0:
            b = -b
            a = -a
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        status = 0
        result = 0
        if a < 0 and b < 0:
            status = 0
            a = -a
            b = -b
        elif a < 0 and b > 0:
            status = 1
            a = -a
        elif a > 0 and b < 0:
            status = 1
            b = -b
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if status:
            return -result
        else:
            return result
        
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        status = 0
        if a > 0 and b > 0 and a < b:
            return a
        elif a < 0 and b < 0 and a > b:
            return a
        else:
            if a < 0 and b < 0:
                a = -a
                b = -b
                status = 1
            if a > 0 and b > 0:
                while a >= b:
                    a = a-b
                if status:
                    return -a
                else:
                    return a
            elif a < 0 and b > 0:
                while a < 0:
                    a = a+b
                return a
            elif a > 0 and b < 0:
                while a > 0:
                    a = a+b
                return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
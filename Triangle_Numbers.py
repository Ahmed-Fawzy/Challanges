#Triangle_ Numbers

class Triangle_Numbers:
    def __init__(self):
        self.triangle_number = 0
        self.index = 0
        self.num_divisors = 5

    def get_divisors(self, number):        
        result = 2
        start = 2
        end = number
        i = start
        while i < end:
            if (number % i == 0):
                start = i
                end = number / i
                if(start == end):
                    result += 1
                else:
                    result += 2                
            i += 1
            
        return result

    def calculate_next_triangle_number(self):
        self.index += 1
        self.triangle_number += self.index 
        return self.triangle_number 

if __name__ == '__main__':
    divisors = 0
    triangle = Triangle_Numbers()
    found = False
    while found == False:
        triangle.calculate_next_triangle_number()
        if (triangle.triangle_number > 500):
            divisors = triangle.get_divisors(triangle.triangle_number)
            if(divisors > 500):
                found = True
                print("{0} : {1}".format(triangle.triangle_number, divisors))

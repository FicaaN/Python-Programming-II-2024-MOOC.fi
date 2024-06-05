class  NumberStats:
    
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number:int):
        self.sum += number
        self.numbers += 1

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        if self.numbers == 0:
            return 0
        else: return self.sum
    
    def average(self):
        if self.numbers == 0:
            return 0
        else: return self.sum / self.numbers

user_sum = NumberStats()
user_even_sum = NumberStats()
user_odd_sum = NumberStats()

print("Please type in integer numbers:")
while True:
    number = int(input(''))
    if number == -1:
        break
    elif number % 2 == 0:
        user_sum.add_number(number)
        user_even_sum.add_number(number)
    else:
        user_sum.add_number(number)
        user_odd_sum.add_number(number)

print(f"Sum of numbers: {user_sum.get_sum()}")
print(f"Mean of numbers: {user_sum.average()}")
print(f"Sum of even numbers: {user_even_sum.get_sum()}")
print(f"Sum of odd numbers: {user_odd_sum.get_sum()}")

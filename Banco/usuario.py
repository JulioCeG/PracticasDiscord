import random
import time

class User():
    existing_codes = set()

    def __init__(self, name, password, initial_balance=2000):
        self.name = name
        self.password = password
        self.user_code = self.generate_unique_code()
        self.money = initial_balance

    def generate_unique_code(self):
        while True:
            code = User.gen_random_code(4)
            if code not in User.existing_codes:
                User.existing_codes.add(code)
                return code

    def gen_random_code(length):
        random.seed(time.time())
        digits = [random.randint(0, 9) for _ in range(length)]
        return int(''.join(map(str, digits)))

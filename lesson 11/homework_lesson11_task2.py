class Soda():
    def __init__(self, taste: str = None):
        self.taste = taste
    def print_taste(self):
        if taste is None:
            print("У вас обычная газировка")
        else:
            print(f"У вас газировка с {self.taste} вкусом")
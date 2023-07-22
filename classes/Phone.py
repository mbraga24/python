class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        return f"{self.brand} calling {phone_number}..."

    def __str__(self) -> str:
        return f"brand = {self.brand}, price = {self.price}"


iphone = Phone("Iphone", 400)
samsung = Phone("Samsung", 350)

print(iphone.brand)
print(iphone.price)
print(iphone.call(23423424))
print()
print(samsung.brand)
print(samsung.price)
print(samsung.call(79797765))
print()
print("Overriding the str method")
print(iphone)
print(samsung)

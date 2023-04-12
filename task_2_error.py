class MyCustomException(Exception):
    def __init__(self):
        self.message = "Custom exception is occurred"
        super().__init__(self.message)

try:
    # Виклик функції або виконання коду, який може викликати помилку
    raise MyCustomException()
except MyCustomException as e:
    print(e.message)
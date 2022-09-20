def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Wybierz operację.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

while True:
    choice = input("Wybierz operację(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        if choice == '1':
            print(int(add(num1, num2)))
        if choice == '2':
            print(int(subtract(num1, num2)))
        if choice == '3':
            print(int(multiply(num1, num2)))
        if choice == '4' and num2 != 0:
            print("{:.2f}".format(divide(num1, num2))) #Brak int() ponieważ dzielenie może mieć miejsce po przecinku, użytya została również formuła formato by zmniejszyć miejsce po przecinku do 2
        if choice == '4' and num2 == 0: 
            print('Nie można dzielić przez 0')
    else:
        print("Błędna wartość, podaj poprawną")
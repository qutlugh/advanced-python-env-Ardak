import math

def get_gcd_euclid(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def solve_fraction_subtraction():
    print("=== Часть 1: Вычитание дробей (A/B - C/D) ===")
    try:
        print("Дробь 1 (A/B):")
        a = int(input("  Введите числитель A: "))
        b = int(input("  Введите знаменатель B: "))
        
        print("Дробь 2 (C/D):")
        c = int(input("  Введите числитель C: "))
        d = int(input("  Введите знаменатель D: "))

        if b == 0 or d == 0:
            print("Ошибка: Знаменатель не может быть равен нулю.")
            return

        res_numerator = (a * d) - (c * b)
        res_denominator = b * d

        common_divisor = get_gcd_euclid(res_numerator, res_denominator)
        
        final_num = res_numerator // common_divisor
        final_den = res_denominator // common_divisor

        print(f"\nРезультат: {final_num}/{final_den}")
        
    except ValueError:
        print("Пожалуйста, вводите только целые числа.")

def solve_divisors_task():
    print("\n=== Часть 2: Делители числа ===")
    try:
        num = int(input("Введите натуральное число: "))
        
        if num <= 0:
            print("Пожалуйста, введите положительное число.")
            return

        print(f"Делители числа {num}: ", end="")
        
        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end=" ")
        print() 
    except ValueError:
        print("Некорректный ввод. Введите целое число.")
if __name__ == "__main__":
    solve_fraction_subtraction()
    solve_divisors_task()
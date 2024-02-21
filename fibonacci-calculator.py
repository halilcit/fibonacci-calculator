# Fibonacci Serisi Hesaplama

def fibonacci(n):
    """
    Fibonacci serisinin ilk 'n' terimini hesaplar.
    """
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def main():
    """
    Kullanıcıdan bir sayı alarak Fibonacci serisinin o sayıya kadar olan terimlerini hesaplar ve ekrana basar.
    """
    try:
        n = int(input("Kaç terimlik Fibonacci serisi hesaplanacak? "))
        if n <= 0:
            print("Lütfen pozitif bir tam sayı giriniz.")
            return
        result = fibonacci(n)
        print(f"Fibonacci serisinin ilk {n} terimi: {result}")
    except ValueError:
        print("Geçersiz giriş! Lütfen bir tam sayı giriniz.")

if __name__ == "__main__":
    main()

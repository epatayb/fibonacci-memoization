def fibonacci_memoization(n, memo=None):
    if n < 0:
        raise ValueError("Hata: Fibonacci serisi için negatif bir sayı girilemez!")
    
    if memo is None:
        memo = {}   # Sözlük daha önce oluşmamışsa yeni bir sözlük oluşturur.

    if n in memo:
        return memo[n]  # Eğer değer daha önce hesaplandıysa, doğrudan değeri döndürür.
     
    if n <= 1:
        return n    # Temel durum
    
    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]

try:
    number = int(input("Kaçıncı Fibonacci sayısını görmek istiyorsunuz? "))
    print(f"Sonuç: {fibonacci_memoization(number)}")
except ValueError as e:
    print(e)
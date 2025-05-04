from math import log2

def prime_logs(n):
    for i in range(2, n+1):
        if prime(i):
            with open("primes.txt", "a") as f:
                f.write(f"log2({i}) = {log2(i):.3f}\n")

def prime(n) -> bool:
    # Function to check if a number is prime
    if n <= 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter a number: "))
    prime_logs(n)
    print("Logs of primes written successfully")

if __name__ == "__main__":
    main()
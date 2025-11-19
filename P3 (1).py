import math
def main():
    try:
        a1 = float(input("Enter the a1   : ").strip())
        d = float(input("Enter the d: ").strip())
        n = int(input("Enter n : ").strip())
        if n <= 0:
            raise ValueError("n must be positive")
    except Exception as e:
        print("Invalid input:", e)
        return

    nth = a1 + (n - 1) * d
    s_n = n * (2 * a1 + (n - 1) * d) / 2

    print(f"{n}th term = {nth}")
    print(f"Sum of first {n} terms = {s_n}")

if __name__ == "__main__":
    main()
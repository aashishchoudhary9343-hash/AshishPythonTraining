import math
def main():
    try:
        inches = float(input("Enter measurement: ").strip())
    except Exception as e:
        print("Invalid input:", e)
        return

    feet = inches / 12.0
    yards = inches / 36.0
    centimetres = inches * 2.54
    meters = inches / 39.37

    print(f"Inches : {inches}")
    print(f"Feet : {feet:.4f}")
    print(f"Yards : {yards:.4f}")
    print(f"Centimetres : {centimetres:.4f}")
    print(f"Meters: {meters:.4f}")

if __name__ == "__main__":
    main()
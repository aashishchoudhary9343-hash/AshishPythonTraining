import math
val = 0xCAFE
three_of_four = ((val & 0xF).bit_count() >= 3)
reversed_bytes = ((val & 0xFF) << 8) | ((val >> 8) & 0xFFFF)

rot4 = ((val >> 4) | ((val & 0xF) << 12)) & 0xFFFF

print(f"val = 0x{val:04X}")
print("At least 3 of last 4 bits on:", three_of_four)
print(f"Reversed bytes = 0x{reversed_bytes:04X}")
print(f"Rotate 4 bits = 0x{rot4:04X}")
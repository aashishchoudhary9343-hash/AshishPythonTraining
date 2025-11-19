def print_pascals_triangle(n):
    triangle = []

    for row_num in range(n):
        # Start each row with 1
        row = [1]
        if triangle:
            last_row = triangle[-1]
            # Compute inner elements
            row.extend([last_row[i] + last_row[i+1] for i in range(len(last_row)-1)])
            # End each row with 1
            row.append(1)
        triangle.append(row)

    # Print the triangle
    for row in triangle:
        print(' '.join(map(str, row)))


# Input number of rows
num_rows = int(input("Enter number of rows: "))
print_pascals_triangle(num_rows)

def print_multiplication_tables():
    for i in range(1, 11):  # Outer loop for the tables from 1 to 10
        for j in range(1, 11):  # Inner loop for each multiplication
            print(f"{i} x {j} = {i*j}")
        print("-" * 20)  # Separator after each table

print_multiplication_tables()

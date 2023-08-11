def print_operation_table(operation, num_rows=6, num_colums=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_colums + 1):
            table_unit = operation(i, j)
            print(table_unit, end=' ')
        print()



print_operation_table(lambda x, y: x*y)
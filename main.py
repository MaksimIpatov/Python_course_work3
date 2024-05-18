from src.utils import get_data, filter_data, last_five_operations, format_operation

operations = get_data()
operations = filter_data(operations)
operations = last_five_operations(operations)

for operation in operations:
    formatted_operation = format_operation(operation)
    print(formatted_operation)

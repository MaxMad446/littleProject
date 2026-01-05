import random
data = [random.randint(1, 100) for _ in range(10)]
print(f'Data: {data}')
print(f'Sum: {sum(data)}')
print(f'Average: {sum(data) / len(data):.2f}')

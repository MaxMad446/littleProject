# Daily script: data_processor
# Generated: 2026-09-11T13:07:06.274107

import random
data=[random.randint(1,100) for _ in range(10)]
print(f"Data: {data}")
print(f"Sum: {sum(data)}, Avg: {sum(data)/len(data):.2f}")

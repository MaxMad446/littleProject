# Daily script: data_processor
# Generated: 2026-10-07T15:55:10.582221

import random
data=[random.randint(1,100) for _ in range(10)]
print(f"Data: {data}")
print(f"Sum: {sum(data)}, Avg: {sum(data)/len(data):.2f}")

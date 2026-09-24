# Daily script: data_processor
# Generated: 2026-09-24T13:54:58.458729

import random
data=[random.randint(1,100) for _ in range(10)]
print(f"Data: {data}")
print(f"Sum: {sum(data)}, Avg: {sum(data)/len(data):.2f}")

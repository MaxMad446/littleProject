import os
print(f'Files in current directory:')
for file in os.listdir('.'):
    print(f'  {{file}}')
print(f'Current directory: {os.getcwd()}')

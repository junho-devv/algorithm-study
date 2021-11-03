import sys

in_n = int(sys.stdin.readline())
block_n = [''] + list(sys.stdin.readline().rstrip())

min_energy = [int(1e7)] * (int(1e3) + 1)
min_energy[1] = 0

for n in range(2, in_n + 1):
    temp_char = ''
    if block_n[n] == 'B':
        temp_char = 'J'
    elif block_n[n] == 'O':
        temp_char = 'B'
    else:
        temp_char = 'O'

    for m in reversed(range(n)):
        if block_n[m] == temp_char:
            min_energy[n] = min(min_energy[n], min_energy[m] + (n - m) ** 2)

if min_energy[in_n] == int(1e7):
    print(-1)
else:
    print(min_energy[in_n])

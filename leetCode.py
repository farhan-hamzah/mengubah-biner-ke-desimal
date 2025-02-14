# biner ke desimal
biner = int(input())
hasil = biner
i = 0
output = 0
while hasil > 0:
    akhir = hasil % 10
    output += akhir * (2**i)
    hasil //= 10
    i += 1
print(output)

import random
szam = random.randrange(1, 1000001)
szamjegy = 0

if   szam < 10:      szamjegy = 1
elif szam < 100:     szamjegy = 2
elif szam < 1000:    szamjegy = 3
elif szam < 10000:   szamjegy = 4
elif szam < 100000:  szamjegy = 5
elif szam < 1000000: szamjegy = 6
else:                szamjegy = 7

print(f'{szam}-ban a számjegyek száma: {szamjegy}')

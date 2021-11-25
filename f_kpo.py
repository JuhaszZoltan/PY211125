import random
# szg "titokban" véletlenszerűen választ a [kő, papír, olló] közül
# felhasználótól bekérjük, hogy ő mit szeretne mutatni
# meghatározzuk, hogy ki nyert

szg = random.randrange(0, 3)
jt = input("ezt mutatom: ")

gep = ''
if szg == 0: gep = "kő"
elif szg == 1: gep = "papír"
else: gep = "olló"

print(f'az AI ezt mutatja: {gep}')

if gep == jt: print('döntetlen')
elif (szg == 0 and jt == 'papír') or (szg == 1 and jt == 'olló') or (szg == 2 and jt == 'kő'): print('nyertél!')
else: print('vesztettél! :(')
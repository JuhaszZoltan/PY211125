import random

# zárt-zárt intervallumon belül előállított véletlen szám:
vsz_1 = random.randint(10, 21)

# zárt-nyílt intervallumon belül előállított véletlen szám:
vsz_2 = random.randrange(10, 21)

# [0 és 1) közötti lebegőpontos véletlen szám:
vsz_3 = random.random()

print(vsz_3)
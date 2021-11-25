kg = float(input('testtömeged (kg): '))
m = float(input('magasság (cm): ')) / 100

tti = kg / pow(m, 2)
tso = ''

if   tti < 16:   tso = 'súlyos soványság'
elif tti < 17:   tso = 'mérsékelt soványság'
elif tti < 18.5: tso = 'enyhe soványság'
elif tti < 25:   tso = 'normális testsúly'
elif tti < 30:   tso = 'túlsúlyos'
elif tti < 35:   tso = 'I. fokú elhízás'
elif tti < 40:   tso = 'II. fokú elhízás'
else:            tso = 'III. fokú (súlyos) elhízás'

print(f'tti: {round(tti, 2)}, testsúlyosztály: {tso}')
helyseg_neve = input("Adja meg a helyseég nevét: ")
lelekszam = int(input("Adja meg a helység lélekszámát: "))

if lelekszam <= 0:
    print("Hibás adatbevitel")
if lelekszam < 5000:
    print("község")
# csak pythonban működik:
if 5000 <= lelekszam < 20000:
    print("kisváros")
# általános megoldás
if 20000 <= lelekszam and lelekszam < 100000:
    print("középváros")    
if 100000 <= lelekszam < 1000000:
    print("nagyváros")    
if 1000000 <= lelekszam:
    print("metropolisz")
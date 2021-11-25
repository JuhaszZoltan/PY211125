helyseg_neve = input("Adja meg a helyseég nevét: ")
lelekszam = int(input("Adja meg a helység lélekszámát: "))

if lelekszam <= 0: print("Hibás adatbevitel")
elif lelekszam < 5000: print("község")
elif lelekszam < 20000: print("kisváros")
elif lelekszam < 100000: print("középváros")  
elif lelekszam < 1000000: print("nagyváros")
else: print("metropolisz")
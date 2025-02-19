import math
import datetime 
import random

def pierwsza_niedziela_miesiaca(rok, miesiac):
    for dzien in range(1, 8):
        if datetime.datetime(rok, miesiac, dzien).weekday() == 6:
            return dzien
    return None


expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}

def solution1(expenses):
    wynik = 0
    wydatki = []
    for data in expenses:
        rok, miesiac = map(int, data.split('-'))
        pierwsza_niedziela = pierwsza_niedziela_miesiaca(rok, miesiac)
        if pierwsza_niedziela == None:
            continue

        for dzien in range(1, pierwsza_niedziela + 1):
            dzien_klucz = "0"+str(dzien)
            if dzien_klucz in expenses[data]:
                for kategoria in expenses[data][dzien_klucz]:
                    wydatki.extend(expenses[data][dzien_klucz][kategoria])

    ilosc_wydatkow = len(wydatki)
    if ilosc_wydatkow == 0:
        wynik = None
    else:
        wydatki = sorted(wydatki)
        x = ilosc_wydatkow // 2
        if ilosc_wydatkow % 2 == 1:
            wynik += wydatki[x]
        else:
            wynik += ((wydatki[x - 1] + wydatki[x]) / 2)
    return wynik






def quickselect(arr, k):
    if not arr:
        return None
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))
 
'''
    Zastosowałem w rozwiązaniu tego zadania quickselect ponieważ jest on szybszy od rozwiązania na nr1.
    Rozwiązanie nr 1 ma złożoność O(n log n) natomiast quickselect O(n).
    Quickselect ma również przewage względem zużycia pamięci.
    Minusem tego algorytmu jest to że w najgorszym przypadku jego złożonośc wynosi O(n^2) oraz to że dla mniejszych zbiorów danych jest nie zawsze szybszy względem innych algorytmów.
    Plusem jest również to że nie musimy sortować zbioru kiedy korzystamy z quickselect.
'''
def solution2(expenses):
    wynik = 0
    wydatki = []
    for data in expenses:
        rok, miesiac = map(int, data.split('-'))
        pierwsza_niedziela = pierwsza_niedziela_miesiaca(rok, miesiac)
        if pierwsza_niedziela == None:
            continue

        for dzien in range(1, pierwsza_niedziela + 1):
            dzien_klucz = "0"+str(dzien)
            if dzien_klucz in expenses[data]:
                for kategoria in expenses[data][dzien_klucz]:
                    wydatki.extend(expenses[data][dzien_klucz][kategoria])
        
    ilosc_wydatkow = len(wydatki)
    if ilosc_wydatkow == 0:
        wynik = None
    if ilosc_wydatkow % 2 == 1:
        wynik += quickselect(wydatki, ilosc_wydatkow // 2)
    else:
        wynik += ((quickselect(wydatki, (ilosc_wydatkow - 1 ) // 2) + quickselect(wydatki, ilosc_wydatkow // 2) )/ 2 )
    return wynik


print(solution1(expenses))
print(solution2(expenses))

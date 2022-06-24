class przedmiot:
        def __init__(self, nazwa, status):
            self.nazwa = nazwa
            self.ocena = 0
            self.obowiazkowy = status

class uczen:
        def __init__(self, imie, nazwisko, birthday):
            self.imie = imie
            self.nazwisko = nazwisko
            self.id = 0
            self.birthday = birthday
            self.przedmioty = list()

        def add_przedmiot(self, _przedmiot, ocena):

            nowyprzedmiot = przedmiot(_przedmiot.nazwa, _przedmiot.obowiazkowy)
            nowyprzedmiot.ocena = ocena
            self.przedmioty.append(nowyprzedmiot)

        def wypisz_dane(self):
            _srednia=self.srednia()
            print(f"[{self.id}] {self.imie} {self.nazwisko}, Ur. {self.birthday}, Srednia: {_srednia}")

        def srednia(self):
            suma=0
            ilosc=0
            for przedmiot in self.przedmioty:
                suma+=przedmiot.ocena
                ilosc+=1
            if ilosc!=0:
                return (suma/ilosc)
            else:
                return 0

        def wypisz_oceny(self):
            for przedmiot in self.przedmioty:
                print(f"{przedmiot.nazwa}: {przedmiot.ocena}")


class Dziennik:
        def __init__(self):
            self.uczniowie = list()
            self.przedmioty = list()

        def add_uczen(self, uczen):
            self.uczniowie.append(uczen)
            self.sortowanie()

        def remove_uczen(self, numer):
            print(f"Usunieto ucznia {self.uczniowie[numer-1].imie} {self.uczniowie[numer-1].nazwisko}")
            del self.uczniowie[numer-1]
            self.sortowanie()

        def remove_przedmiot(self, nazwa):
            flaga=False
            i=0
            for przedmiot in self.przedmioty:
                if przedmiot.nazwa==nazwa:
                    flaga=True
                    del self.przedmioty[i]
                    for uczen in self.uczniowie:
                        j=0
                        for przedmiot_U in uczen.przedmioty:
                            if przedmiot_U.nazwa==nazwa:
                                del uczen.przedmioty[j]
                                break
                            j=j+1
                    break
                i=i+1
            if flaga==False:
                print("Nie znaleziono podanego przedmiotu\n")
            else:
                print(f"Przedmiot {nazwa} pomyslnie usuniety")

        def zmien_ocene(self, numer, nazwa):
            flaga=False
            for przedmiot in self.uczniowie[numer-1].przedmioty:
                if przedmiot.nazwa==nazwa:
                    flaga=True
                    ocena = float (input(f"Podaj ocene ucznia {self.uczniowie[numer-1].imie} {self.uczniowie[numer-1].nazwisko} z przedmiotu {nazwa}:\n"))
                    przedmiot.ocena=ocena
                    break
            if flaga==False:
                print("Uczen nie uczeszcza na dany przedmiot, lub ten przedmiot nie istnieje")

        def zapisz_ucznia(self, numer, nazwa):
            flaga=False
            flaga2=False
            for przedmiot in self.przedmioty:
                if przedmiot.nazwa==nazwa:
                    flaga=True
                    if przedmiot.obowiazkowy==False:
                        for przedmiot_U in self.uczniowie[numer-1].przedmioty:
                            if przedmiot_U.nazwa==nazwa:
                                flaga2=True
                                break
                        if flaga2==True:
                            print("Uczen jest juz zapisany na ten przedmiot")
                        else:
                            ocena = float (input(f"Podaj ocene ucznia {self.uczniowie[numer-1].imie} {self.uczniowie[numer-1].nazwisko} z przedmiotu {nazwa}:\n"))
                            self.uczniowie[numer-1].add_przedmiot(przedmiot, ocena)
                    else:
                        print("Przedmiot na ktory probujesz zapisac ucznia jest juz obowiazkowy. Uczen jest na niego zapisany.")
                        flaga2=True
                    break
            if flaga==False:
                print("Nie znaleziono podanego przedmiotu.")
            elif flaga2==False:
                print(f"Uczen {self.uczniowie[numer-1].imie} {self.uczniowie[numer-1].nazwisko} pomyslnie zapisany na przedmiot {nazwa}")

        def wypisz_ucznia(self, numer, nazwa):
            flaga=False
            for przedmiot in self.uczniowie[numer-1].przedmioty:
                if przedmiot.nazwa==nazwa:
                    flaga=True
                    if przedmiot.obowiazkowy==False:
                        del przedmiot
                        print(f"Pomyslnie wypisano ucznia {self.uczniowie[numer-1].imie} {self.uczniowie[numer-1].nazwisko} z przedmiotu {nazwa}")
                    else:
                        print("Nie mozesz wypisac ucznia z obowiazkowego przedmiotu.")
            if flaga==False:
                print("Uczen nie uczeszcza na dany przedmiot, lub ten przedmiot nie istnieje")

        def srednia(self):
            suma=0
            i=0
            for uczen in self.uczniowie:
                for przedmiot in uczen.przedmioty:
                    suma=suma+przedmiot.ocena
                    i=i+1
            if i!=0:
                wynik=suma/i
            else:
                wynik=0
            print(wynik)

        def najlepsi(self):
            ranking=sorted(self.uczniowie, key=lambda x: x.srednia(), reverse=True)
            for i in range(3):
                if i<len(ranking):
                    print(f"{i+1}. {ranking[i].imie} {ranking[i].nazwisko}, Nr w dzienniku:[{ranking[i].id}],  Ur. {ranking[i].birthday}, Srednia: {ranking[i].srednia()}")

        def add_przedmiot(self, przedmiot):
            self.przedmioty.append(przedmiot)

        def wypisz_uczniow(self):
            for pozycja in self.uczniowie:
                pozycja.wypisz_dane()

        def sortowanie(self):
            self.uczniowie.sort(key=lambda a: (a.nazwisko, a.imie))
            numer=0
            for pozycja in self.uczniowie:
                numer+=1
                pozycja.id = numer
        def wypisz_przedmioty(self):
            for przedmiot in self.przedmioty:
                print(f"{przedmiot.nazwa} -", end=" ")
                if przedmiot.obowiazkowy==True:
                    print(" obowiazkowy", end="; ")
                else:
                    print(" nieobowiazkowy", end="; ")
            print()

        def oceny(self, numer):
            self.uczniowie[numer-1].wypisz_dane()
            self.uczniowie[numer-1].wypisz_oceny()




class UI:
    def __init__(self, Dziennik):
        self.Dziennik = Dziennik

    def start(self):
        while True:
            if (self._mainmenu()):
                break

    def _mainmenu(self):
            print("\n1.  Dodaj ucznia\n2.  Usun ucznia\n3.  Dodaj przedmiot\n4.  Usun przedmiot\n5.  Zmien uczniowi ocene\n6.  Zapisz ucznia na przedmiot nieobowiazkowy\n7.  Wypisz ucznia z przedmiotu nieobowiazkowego\n8.  Wypisz srednia klasy\n9.  Wypisz 3 najlepszych uczniow\n10. Wypisz uczniow\n11. Wypisz przedmioty\n12. Wypisz oceny konkretnego ucznia\n13. Wyjscie\n")
            switch = int (input())
            if (switch == 1):
                nowy = self.nowy_uczen()
                self.Dziennik.add_uczen(nowy)
            elif (switch == 2):
                y = int (input("Podaj numer ucznia do usuniecia:\n"))
                if y<=len(self.Dziennik.uczniowie):
                    self.Dziennik.remove_uczen(y)
                else:
                    print("Nie ma ucznia o podanym numerze")
            elif (switch == 3):
                nowy_przedmiot = self.nowy_przedmiot()
                self.Dziennik.add_przedmiot(nowy_przedmiot)
            elif (switch == 4):
                nazwa = input("Podaj nazwe przedmiotu do usuniecia:\n")
                self.Dziennik.remove_przedmiot(nazwa)
            elif (switch == 5):
                y = int (input("Podaj numer ucznia ktoremu chcesz zmienic ocene:\n"))
                if y<=len(self.Dziennik.uczniowie):
                    nazwa = input("Podaj nazwe przedmiotu:\n")
                    self.Dziennik.zmien_ocene(y, nazwa)
                else:
                    print("Nie ma ucznia o podanym numerze")
            elif (switch == 6):
                y = int (input("Podaj numer ucznia ktorego chcesz zapisac:\n"))
                if y<=len(self.Dziennik.uczniowie):
                    nazwa = input("Podaj nazwe przedmiotu:\n")
                    self.Dziennik.zapisz_ucznia(y, nazwa)
                else:
                    print("Nie ma ucznia o podanym numerze")
            elif (switch == 7):
                y = int (input("Podaj numer ucznia ktorego chcesz wypisac:\n"))
                if y<=len(self.Dziennik.uczniowie):
                    nazwa = input("Podaj nazwe przedmiotu:\n")
                    self.Dziennik.wypisz_ucznia(y, nazwa)
                else:
                    print("Nie ma ucznia o podanym numerze")
            elif (switch == 8):
                self.Dziennik.srednia()
            elif (switch == 9):
                self.Dziennik.najlepsi()
            elif (switch == 10):
                self.Dziennik.wypisz_uczniow()
            elif (switch == 11):
                self.Dziennik.wypisz_przedmioty()
            elif (switch == 12):
                y = int (input("Podaj numer ucznia ktorego oceny chcesz sprawdzic:\n"))
                if y<=len(self.Dziennik.uczniowie):
                    self.Dziennik.oceny(y)
                else:
                    print("Nie ma ucznia o podanym numerze")
            else:
                return True
            return False

    def nowy_uczen(self):
        name, sur, bday  = input("Podaj dane ucznia: Imie, Nazwisko, date urodzin (w formacie XX.XX.XXXX); oddzielajac je spacja:\n").split(" ")
        wynik = uczen(name, sur, bday)
        for przedmiot in self.Dziennik.przedmioty:
            if przedmiot.obowiazkowy == True:
                ocena = float (input(f"Podaj ocene ucznia z przedmiotu {przedmiot.nazwa}:\n"))
                wynik.add_przedmiot(przedmiot, ocena)
            else:
                a = input(f"Czy uczen uczeszcza na przedmiot {przedmiot.nazwa}?(T/N):\n")
                if a=="T" or a=="t":
                    ocena = float (input(f"Podaj ocene ucznia z przedmiotu {przedmiot.nazwa}:\n"))
                    wynik.add_przedmiot(przedmiot, ocena)
        return wynik

    def nowy_przedmiot(self):
        name = input("Podaj nazwe dodawanego przedmiotu:\n")
        a = input("Czy przedmiot jest obowiazkowy?(T/N)\nJesli tak, bedziesz musial uzupelnic oceny uczniow:")
        if a=="T" or a=="t":
            _nowy_przedmiot = przedmiot(name, True)
            for uczen in self.Dziennik.uczniowie:
                ocena = float (input(f"Podaj ocene ucznia {uczen.imie} {uczen.nazwisko} z przedmiotu {_nowy_przedmiot.nazwa}:\n"))
                uczen.add_przedmiot(_nowy_przedmiot, ocena)
        else:
            _nowy_przedmiot = przedmiot(name, False)
        return _nowy_przedmiot


def main():
    uczen1 = uczen("Jan", "Kowalski", "21.01.2001")
    uczen2 = uczen("Adam", "Nowak", "14.02.2001")
    uczen3 = uczen("Jerzy", "Ogumny", "24.12.2001")
    uczen4 = uczen("Adam", "Bielecki", "02.11.2001")

    przedmiot1 = przedmiot("Matematyka", True)
    przedmiot2 = przedmiot("Chemia", True)
    przedmiot3 = przedmiot("Biologia", True)
    przedmiot4 = przedmiot("Religia", False)

    uczen1.add_przedmiot(przedmiot1, 2.0)
    uczen1.add_przedmiot(przedmiot2, 4.0)
    uczen1.add_przedmiot(przedmiot3, 5.5)
    uczen1.add_przedmiot(przedmiot4, 6.0)

    uczen2.add_przedmiot(przedmiot1, 1.0)
    uczen2.add_przedmiot(przedmiot2, 3.0)
    uczen2.add_przedmiot(przedmiot3, 3.0)
    uczen2.add_przedmiot(przedmiot4, 5.0)

    uczen3.add_przedmiot(przedmiot1, 4.5)
    uczen3.add_przedmiot(przedmiot2, 4.5)
    uczen3.add_przedmiot(przedmiot3, 2.5)
    uczen3.add_przedmiot(przedmiot4, 4.0)

    uczen4.add_przedmiot(przedmiot1, 6.0)
    uczen4.add_przedmiot(przedmiot2, 5.5)
    uczen4.add_przedmiot(przedmiot3, 5.0)


    dzien = Dziennik()

    dzien.add_przedmiot(przedmiot1)
    dzien.add_przedmiot(przedmiot2)
    dzien.add_przedmiot(przedmiot3)
    dzien.add_przedmiot(przedmiot4)

    dzien.add_uczen(uczen1)
    dzien.add_uczen(uczen2)
    dzien.add_uczen(uczen3)
    dzien.add_uczen(uczen4)

    print("PROJEKT -- DZIENNIK")
    print("***MIKOLAJ MUMOT***")
    print("(kilka funkcji typu wypisanie przedmiotow jest dodanych dla czytelnosci)")
    Menu = UI(dzien)
    Menu.start()


main()

#include <iostream>
#include <string>
#include <iomanip> //dla fixed precision
#include <vector>
using namespace std;
struct book //indeksem ksiazki jest indeks w wektorze
{
    string tytul;
    int rok; //rok wydania
    string autor;
    float cena;
    int wypozyczenia;
};

void pisanie(vector<book> tab, int i) //dla przejrzystosci kodu
{
    cout << "(" << i << ".) " << tab[i].tytul << " || "
         << "Rok wydania: " << tab[i].rok << " || "
         << "Autor: " << tab[i].autor << " || "
         << "Cena: " << fixed << setprecision(2) << tab[i].cena << "PLN || "
         << "Ilosc wypozyczen: " << tab[i].wypozyczenia << endl;
}

void Dodanie(vector<book> &tab) //dodawanie ksiazki
{
    int rok, wypozyczenia;
    float cena;
    string tytul, autor;
    cout << "Wprowadz tytul:" << endl;
    cin.ignore();
    getline(cin, tytul, '\n');
    cout << "Wprowadz rok wydania:" << endl;
    cin >> rok;
    cin.ignore();
    cout << "Wprowadz autora:" << endl;
    getline(cin, autor, '\n');
    cout << "Wprowadz cene (w PLN):" << endl;
    cin >> cena;
    cout << "Wprowadz dotychczasowe wypozyczenia:" << endl;
    cin >> wypozyczenia;
    book nowa = {tytul, rok, autor, cena, wypozyczenia};
    tab.push_back(nowa);
    cout << "\n"
         << endl;
}

void wypisz(vector<book> tab) //wypisywanie zawartosci biblioteki
{
    int i;
    for (i = 0; i < tab.size(); i++)
    {
        {
            pisanie(tab, i);
        }
    }
    cout << "\n"
         << endl;
}

void Usuniecie(vector<book> &tab) //usuwanie pozycji z biblioteki
{
    int x;
    cout << "Podaj numer biblioteczny ksiazki do usuniecia: " << endl;
    cin >> x;
    if (x >= 0 && x < tab.size())
    {
        cout << "Usunieto ksiazke \"" << tab[x].tytul << "\" o indeksie " << x << endl;
        tab.erase(tab.begin() + x);
    }
    else
    {
        cout << "Podano wartosc spoza zakresu";
    }
    cout << "\n"
         << endl;
}

void Wypozyczenie(vector<book> &tab) //inkrementacja wypozyczenia
{
    int x;
    cout << "Podaj numer biblioteczny wypozyczonej ksiazki: " << endl;
    cin >> x;
    if (x >= 0 && x < tab.size())
    {
        tab[x].wypozyczenia += 1;
        cout << "Pomyslnie dodano wypozyczenie ksiazce \"" << tab[x].tytul << "\" o indeksie " << x << endl;
        cout << "Laczna ilosc wypozyczen wynosi teraz " << tab[x].wypozyczenia << endl;
    }
    else
    {
        cout << "Podano wartosc spoza zakresu";
    }
    cout << "\n"
         << endl;
}

void Srednia(vector<book> tab) //wyswietlanie sredniej ceny ksiazek
{
    int i, j;
    float x, wynik;
    x = 0;
    for (i = 0; i < tab.size(); i++)
    {
        x += tab[i].cena;
    }
    wynik = (x / tab.size());
    cout << "Srednia cena ksiazek wynosi " << fixed << setprecision(2) << wynik << "PLN\n"
         << endl;
}

void Szukanie(vector<book> tab) //funkcja z wyszukiwaniami
{
    char o;
    cout << "Wybierz rodzaj wyszukiwania:\n\n 1. Po tytule\n 2. Po autorze \n 3. Po roku wydania\n 4. Po liczbie wypozyczen\n"
         << endl;
    cin >> o;
    string x;
    int y;
    int i;
    bool flag = false;
    switch (o)
    {
    case '1': //po tytule
    {
        cout << "Podaj szukany tytul:" << endl;
        cin.ignore();
        getline(cin, x, '\n');
        cout << "Wyniki wyszukiwana:" << endl;
        for (i = 0; i < tab.size(); i++)
        {
            if (tab[i].tytul.find(x) != string::npos)
            {
                pisanie(tab, i);
                flag = true;
            }
        }
        break;
    }
    case '2': //po autorze
    {
        cout << "Podaj szukanego autora:" << endl;
        cin.ignore();
        getline(cin, x, '\n');
        cout << "Wyniki wyszukiwana:" << endl;
        for (i = 0; i < tab.size(); i++)
        {
            if (tab[i].autor.find(x) != string::npos)
            {
                pisanie(tab, i);
                flag = true;
            }
        }
        break;
    }
    case '3': //po roku wydania
    {
        cout << "Podaj rok wydania:" << endl;
        cin >> y;
        cout << "Wyniki wyszukiwana:" << endl;
        for (i = 0; i < tab.size(); i++)
        {
            if (tab[i].rok == y)
            {
                pisanie(tab, i);
                flag = true;
            }
        }
        break;
    }
    case '4': //po wypozyczeniach
    {
        cout << "Podaj ilosc wypozyczen:" << endl;
        cin >> y;
        cout << "Wyniki wyszukiwana:" << endl;
        for (i = 0; i < tab.size(); i++)
        {
            if (tab[i].wypozyczenia == y)
            {
                pisanie(tab, i);
                flag = true;
            }
        }
        break;
    }
    default:
    {
        flag = true;
        cout << "Nieprawidlowy rodzaj wyszukiwania\n\n";
        break;
    }
    }
    if (flag == false)
    {
        cout << "Nie znaleziono zadnych ksiazek" << endl;
    }
    cout << endl;
}

int main()
{
    char akcja;
    vector<book> biblioteka(4);
    biblioteka[0] = {"Harry Potter i Komnata Tajemnic", 1998, "J.K. Rowling", 35.50, 3};
    biblioteka[1] = {"Opowiesci z Narnii: Lew, Czarownica i Stara Szafa", 1950, "Clive Staples Lewis", 29.99, 7};
    biblioteka[2] = {"Pan Tadeusz", 1834, "Adam Mickiewicz", 45.00, 12};
    biblioteka[3] = {"Rok 1984", 1949, "George Orwell", 35.00, 2}; //4 ksiazki automatycznie w spisie
    cout << "Baza danych: Biblioteka\nMikolaj Mumot 2020\n\n"
         << endl;
    ;
    cout << "Wybierz akcje do wykonania (wpisz numer polecenia):\n\n 1. Dodaj ksiazke\n 2. Wyszukaj ksiazke\n 3. Usun ksiazke\n 4. Wypisz wszystkie ksiazki\n 5. Dodaj wypozyczenie\n 6. Wyswietl srednia cene\n 7. Wyjdz\n\n"
         << endl;
    ;
    cin >> akcja;
    while (akcja != '7')
    {
        switch (akcja)
        {

        case '1':
        {
            Dodanie(biblioteka);
            break;
        }
        case '2':
        {
            Szukanie(biblioteka);
            break;
        }
        case '3':
        {
            Usuniecie(biblioteka);
            break;
        }
        case '4':
        {
            wypisz(biblioteka);
            break;
        }
        case '5':
        {
            Wypozyczenie(biblioteka);
            break;
        }
        case '6':
        {
            Srednia(biblioteka);
            break;
        }
        default:
        {
            cout << "Nieprawidlowa akcja." << endl;
            break;
        }
        }
        cout << "Wybierz nastepna akcje:" << endl;
        cin >> akcja;
    }

    return 0;
}

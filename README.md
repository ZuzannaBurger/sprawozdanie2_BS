# Algorytm Needleman-Wunsch do globalnego dopasowania sekwencji <br>

## Algorytm <br>

Program został napisany w Pythonie, który implementuje algorytm Needleman-Wunsch do <br> znajdowania globalnego dopasowania między dwoma sekwencjami. Algorytm tworzy macierz  na <br> podstawie dopasowania odpowiadających sobie pozycji w dwóch sekwencjach. Działa on na <br> parametrach podanych przez użytkownika tj. dopasowanie, niedopasowanie oraz luki, aby <br> wyliczyć maksymalny wynik dopasowania. Następnie, za pomocą procedury backtrackingu, <br> możliwe jest odtworzenie wyrównanych sekwencji na podstawie uzyskanej macierzy. <br>

## Implementacja <br>

Program przeszukuje całe sekwencje w celu znalezienia najlepszego globalnego dopasowania. <br> Użytkownik podaje wartości dla punktacji dopasowania, niedopasowania oraz luki, które <br> są następnie używane do wypełnienia macierzy (wartości te są muszą być liczbami <br> całkowitymi). Po wypełnieniu macierzy algorytm przeprowadza backtracking, aby odtworzyć <br> dopasowanie między sekwencjami (preferując wracanie na „ukos”). Wynik końcowy <br> obejmuje wyrównane sekwencje oraz ich wynik dopasowania, który jest wypisywany na ekranie <br> oraz zapisywany do pliku tekstowego. <br>

## Formatowanie wejścia <br>

Program wymaga, aby dane wejściowe znajdowały się w plikach formatu FASTA. Każdy plik <br> powinien zawierać jedną sekwencję poprzedzoną linią nagłówkową rozpoczynającą się znakiem `>`. Program <br> prosi aby użytkownik podał ścieżki do plików w formacie FASTA. Upewnij się, że pliki są w <br> prawidłowym formacie FASTA. <br>

## Wyjście <br>

Plik wyjściowy alignment_results.txt zawiera wynik dopasowania dwóch sekwencji po <br> zastosowaniu algorytmu Needleman-Wunscha. Jest on zapisany w formacie tekstowym i <br> składa się z trzech części: <br>
1. Nagłówek – Zawiera tytuł Alignment Results. <br>
2. Dopasowane sekwencje – Wyświetlone są dwie sekwencje (Seq1 i Seq2), wyrównane <br> względem siebie za pomocą znaków luki (-), aby wizualizować, gdzie występują <br> dopasowania, niedopasowania oraz wstawki (luki). <br>
3. Wynik dopasowania – Podany jest końcowy wynik dopasowania, czyli punktacja uzyskana <br> na podstawie podanych wartości match, mismatch i gap. <br>

## Przed uruchomieniem <br>
Przed uruchomieniem programu należy się upewnić czy jest zainstalowana bibloteka <br>
Bipython gdyż jest ona niezbędna do urochomienia programu. <br>
Komenda w przypadku niezainstalowanej biblioteki: pip install biopython <br>

## Przykład uruchomienia <br>

Po uruchomieniu programu przykładowy przebieg interakcji z uzytkownikiem wygląda tak: <br> <br>
![image](https://github.com/user-attachments/assets/f271c743-a47b-4d91-8e83-4701fec0841b) <br> <br>

Oczekiwane wyjście (w konsoli): <br> <br>
![image](https://github.com/user-attachments/assets/7e236b61-8723-4ecd-ad07-7406423f2284) <br> <br>

Przykład pliku alignment_results.txt <br> <br>
![image](https://github.com/user-attachments/assets/6f033342-2dd7-4d2b-b7a5-66ac45c7b395)











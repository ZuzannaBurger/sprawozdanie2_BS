# Algorytm Needleman-Wunsch do globalnego dopasowania sekwencji <br>

## Algorytm <br>

Program został napisany w Pythonie, który implementuje algorytm Needleman-Wunsch do <br> znajdowania globalnego dopasowania między dwoma sekwencjami. Algorytm tworzy macierz  na <br> podstawie dopasowania odpowiadających sobie pozycji w dwóch sekwencjach. Działa on na <br> parametrach podanych przez użytkownika tj. dopasowanie, niedopasowanie oraz luki, aby <br> wyliczyć maksymalny wynik dopasowania. Następnie, za pomocą procedury backtrackingu, <br> możliwe jest odtworzenie wyrównanych sekwencji na podstawie uzyskanej macierzy. <br>

## Implementacja <br>

Program przeszukuje całe sekwencje w celu znalezienia najlepszego globalnego dopasowania. <br> Użytkownik podaje wartości dla punktacji dopasowania, niedopasowania oraz luki, które <br> są następnie używane do wypełnienia macierzy (wartości te są muszą być liczbami <br> całkowitymi). Po wypełnieniu macierzy algorytm przeprowadza backtracking, aby odtworzyć <br> dopasowanie między sekwencjami (preferując wracanie na „ukos”). Wynik końcowy <br> obejmuje wyrównane sekwencje oraz ich wynik dopasowania, który jest wypisywany na ekranie <br> oraz zapisywany do pliku tekstowego. <br>

## Formatowanie wejścia <br>

Program wymaga, aby dane wejściowe znajdowały się w plikach formatu FASTA. Każdy plik <br> (`seq1.fasta` oraz `seq2.fasta`) powinien zawierać jedną sekwencję poprzedzoną <br> linią nagłówkową rozpoczynającą się znakiem `>`. Dodatkowo pliki te muszą <br> znajdować się w tym samym katalogu, co skrypt (main.py). <br>
![image](https://github.com/user-attachments/assets/f1ad2642-3a52-4c5d-b2a7-f939ad3f5440)





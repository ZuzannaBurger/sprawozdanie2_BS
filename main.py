from Bio import SeqIO
def read_sequence(fasta_file):
    for record in SeqIO.parse(fasta_file, "fasta"):
        return str(record.seq)

def needleman_Wunsch(match, mismatch, gap, seq1, seq2):
    x = len(seq1) #liczba wierszy po lewej
    y = len(seq2) #liczba kolumn u góry
    matrix = [[0 for j in range(y+1)] for i in range(x + 1)]

    for i in range(1, x+1):
        matrix[i][0] = i * gap
    for j in range(1, y+1):
        matrix[0][j] = j * gap

    for i in range(1, x+1):
        for j in range(1, y+1):
            if seq1[i-1] == seq2[j-1]:
                score = match
            else:
                score = mismatch

            match_score = matrix[i-1][j-1] + score
            delete_score = matrix[i-1][j] + gap
            insert_score = matrix[i][j-1] + gap
            matrix[i][j] = max(match_score, delete_score, insert_score)

    align1 = ""
    align2 = ""
    i = x
    j = y
    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):
            align1 = seq1[i-1] + align1
            align2 = seq2[j-1] + align2
            i = i-1
            j = j-1
        elif i > 0 and matrix[i][j] == matrix[i-1][j] + gap:
            align1 = seq1[i-1] + align1
            align2 = "-" + align2
            i = i-1
        else:
            align1 = "-" + align1
            align2 = seq2[j-1] + align2
            j = j-1

    return align1, align2, matrix[x][y]


file1 = input("Enter the path to the first FASTA file: ")
file2 = input("Enter the path to the second FASTA file: ")

seq1 = read_sequence(file1)
seq2 = read_sequence(file2)


while 1==1:
    try:
        match = int(input("Enter the sequence matching value (match): "))
        if match < 1:
            print("Error: The value must be a positive integer.")
            continue
    except ValueError:
        print("Error: This is not an integer.")
        continue
    break

while 1==1:
    try:
        mismatch = int(input("Enter the sequence mismatching value (mismatch): "))
    except ValueError:
        print("Error: This is not an integer.")
        continue
    break

while 1==1:
    try:
        gap = int(input("Enter the gap value (gap): "))
    except ValueError:
        print("Error: This is not an integer.")
        continue
    break

alignment = needleman_Wunsch(match, mismatch, gap, seq1, seq2)
print("Seq1: ", alignment[0])
print("Seq2: ", alignment[1])
print("Alignment score: ", alignment[2])

output_file = "alignment_results.txt"
with open(output_file, "w") as f:
    f.write("Alignment Results\n")
    f.write("Seq1: " + alignment[0] + "\n")
    f.write("Seq2: " + alignment[1] + "\n")
    f.write("Alignment score: " + str(alignment[2]) + "\n")

# print(seq1, "\n")
# print("sekwencja 2: ", seq2)



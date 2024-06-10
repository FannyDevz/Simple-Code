from sys import maxsize 
from itertools import permutations

V = 4                                                       #Jumlah simpul dalam graf

def travellingSalesmanProblem(graph, s):                    #Deklarasi Fungsi Dengan argumen graf dan simpul awal

    
    print(graph)
    vertex = []                                             #Deklarasi Array Kosong untuk di isi
    for i in range(V):                                      #Looping untuk Mengisi vertex, dalam hal ini diulang sebanyak V ## range(V) = (0,1,2,3)
        if i != s:                                          #Jika i bukan s 
            vertex.append(i)                                #Menyimpan i kedalam vertex dalam hal ini yang tersimpan adalah 1,2,3

    min_path = maxsize                                      #Deklarasi min_path = Maxsize = 9223372036854775807 (2^63-1) berasal dari sys.maxsize
    
    next_permutation = permutations(vertex)                 #Deklarasi next_permutation = permutations(vertex) = (1,2,3) (2,1,3) (3,1,2) (1,3,2) (2,3,1) (3,2,1)
    
    print("\n=========== Mulai Perulangan Next Permutation ===========") 
    for i in next_permutation:                              #Looping next_permutation dalam hal ini diulang sebanyak 6 kali ## next_permutation = (1,2,3) (2,1,3) (3,1,2) (1,3,2) (2,3,1) (3,2,1)
        print("\n\n=========== Start ===========") 
        current_pathweight = 0                              #Deklarasi variabelcurrent_pathweight = 0    
        print ("Variabel i :",i,"\n") #untuk cek variabel i 
        k = s                                               #Deklarasi variabel k = s (variabel s = 0)
        for j in i:                                         #Looping i dalam hal ini diulang sebanyak 3 kali sesuai dengan isi variabel i
            current_pathweight += graph[k][j]               #Menambahkan bobot dari array dengan index k dan j           
            print ("k, j:",k, j, "= ",graph[k][j]) #untuk cek variabel k dan j  dan array graph[k][j]
            k = j                                           #Menimpa variabel j kedalam variabel k
            print("Path weight:",current_pathweight) #untuk cek variabel current_pathweight
            
            
        print ("k, s:",k, s, "= ",graph[k][s]) #untuk cek variabel k dan j  dan array graph[k][j]
        current_pathweight += graph[k][s]                   #Menambahkan bobot dari array dengan index k dan s    
        print("Hasil Akhir:",current_pathweight) #untuk cek variabel current_pathweight dalam hal ini adalah 85 + 10

        print("min_path:",min_path) #cek variabel minpatch
        min_path = min(min_path, current_pathweight)        #Mencari nilai minimum dari variabel min_path dan current_pathweight jadi setiap perulangan akan mencari minimum dari bobot jalur yang ada

    return min_path                                         #Mengembalikan variabel min_path

# Kode Utama Untuk Memangil Fungsi
if __name__ == "__main__": 
    graph = [
        [0, 10, 15, 20], 
        [10, 0, 35, 25], 
        [15, 35, 0, 30], 
        [20, 25, 30, 0]
    ]
    s = 0  # Simpul awal
    print(travellingSalesmanProblem(graph, s))

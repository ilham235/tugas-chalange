# Mendefinisikan list untuk menyimpan data orang dan nilai mereka
data = []

# Memasukkan data 5 orang
for i in range(5):
    nama = input(f"Masukkan nama orang ke-{i+1}: ")
    nilai = float(input(f"Masukkan nilai {nama}: "))
    data.append((nama, nilai))

# Mengurutkan data berdasarkan nilai (ascending order)
data.sort(key=lambda x: x[1])

# Mencetak 2 orang dengan nilai terkecil
print("\n2 orang dengan nilai terkecil:")
for i in range(2):
    print(f"{data[i][0]} dengan nilai {data[i][1]}")


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)

def beli_tiket_konser():
    global antrian_tiket
    print("Antrian pembelian tiket:")
    while True:
        nama_pembeli = input("\nMasukkan nama pembeli (atau ketik 'selesai' untuk mengakhiri): ")
        if nama_pembeli.lower() == 'selesai':
            break
        while True:
            print("\nDaftar Konser:")
            for i, konser in enumerate(daftar_konser, start=1):
                print(f"{i}. {konser}")
            konser_index = int(input("\nPilih konser yang ingin ditonton (masukkan nomor): "))
            if 1 <= konser_index <= len(daftar_konser):
                konser_dipilih = daftar_konser[konser_index - 1]
                break
            else:
                print("Pilihan tidak valid. Harap masukkan nomor yang benar.")
        while True:
            print("\nDaftar Jenis Tiket:")
            for i, jenis in enumerate(daftar_jenis_tiket, start=1):
                print(f"{i}. {jenis}")
            jenis_index = int(input("\nPilih jenis tiket (masukkan nomor): "))
            if 1 <= jenis_index <= len(daftar_jenis_tiket):
                jenis_tiket = daftar_jenis_tiket[jenis_index - 1]
                break
            else:
                print("Pilihan tidak valid. Harap masukkan nomor yang benar.")
        jumlah_tiket = int(input(f"Masukkan jumlah tiket {jenis_tiket} yang ingin dibeli untuk {nama_pembeli}: "))
        antrian_tiket.enqueue((nama_pembeli, konser_dipilih, jenis_tiket, jumlah_tiket))
        print(f"{jumlah_tiket} tiket {jenis_tiket} untuk konser {konser_dipilih} telah dimasukkan ke dalam antrian untuk {nama_pembeli}.")
    
    print("\nDaftar pembeli dalam antrian:")
    for pembeli in antrian_tiket.items:
        print("-", pembeli[0], "akan membeli", pembeli[3], "tiket", pembeli[2], "untuk konser", pembeli[1])

def proses_pembelian():
    global antrian_tiket
    while not antrian_tiket.is_empty():
        pembeli_berikutnya = antrian_tiket.dequeue()
        print(f"Memproses pembelian untuk {pembeli_berikutnya[0]} ({pembeli_berikutnya[1]})...")
        print(f"{pembeli_berikutnya[3]} tiket {pembeli_berikutnya[2]} untuk konser {pembeli_berikutnya[1]} telah dibeli.")
        print(f"Jumlah antrian: {antrian_tiket.size()}")
    print("Antrian kosong. Tidak ada yang perlu diproses.")

# Membuat objek queue
antrian_tiket = Queue()

# Daftar jenis tiket
daftar_jenis_tiket = ["VIP", "Platinum", "Festival", "Cat1", "Cat2", "Cat3", "Cat4", "Cat5"]

# Daftar konser
daftar_konser = ["Nct dream", "Seventeen", "Ive", "New Jeans"]

# Main program
beli_tiket_konser()

print("\nProses pembelian:")
proses_pembelian()

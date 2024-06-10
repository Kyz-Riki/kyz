class TicketType:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Concert:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.ticket_types = []

    def add_ticket_type(self, ticket_type):
        self.ticket_types.append(ticket_type)

    def __str__(self):
        return f"{self.name} ({self.date})"

class TicketQueue:
    MAX_QUEUE_SIZE = 20

    def __init__(self):
        self.queue = []

    def add_to_queue(self, name, concert, ticket_type):
        if len(self.queue) >= self.MAX_QUEUE_SIZE:
            print("Antrian penuh. Tidak bisa menambahkan lebih banyak orang.")
            return
        self.queue.append((name, concert, ticket_type))
        print(f"{name} telah ditambahkan ke dalam antrian untuk konser {concert.name} dengan tiket {ticket_type.name}.")

    def remove_from_queue(self):
        if self.queue:
            removed_person, concert, ticket_type = self.queue.pop(0)
            print(f"{removed_person} telah dihapus dari antrian untuk konser {concert.name} dengan tiket {ticket_type.name}.")
        else:
            print("Antrian kosong, tidak ada yang dapat dihapus.")

    def check_queue(self):
        if self.queue:
            print("\n================================================")
            print("Daftar antrian saat ini:")
            for i, (name, concert, ticket_type) in enumerate(self.queue, 1):
                print(f"{i}. {name} (Konser: {concert.name}, Tiket: {ticket_type.name})")
        else:
            print("Antrian kosong.")

    def available_slots(self):
        return self.MAX_QUEUE_SIZE - len(self.queue)

    def print_individual_receipt(self, name, concert, ticket_type, position):
        print("\nStruk Pembelian Tiket")
        print("=========================")
        print(f"Nama: {name}")
        print(f"Konser: {concert.name}")
        print(f"Tiket: {ticket_type.name}")
        print(f"Tanggal Konser: {concert.date}")
        print(f"Posisi dalam antrian: {position}")
        print("=========================\n")

    def print_final_receipt(self):
        print("\n======================================================================")
        print("Detail Catatan Antrian")
        print(f"Total antrian yang ditambahkan: {len(self.queue)}")
        print(f"Sisa slot antrian: {self.available_slots()}")
        print("Detail Pembeli dan Tiket:")
        if self.queue:
            for i, (name, concert, ticket_type) in enumerate(self.queue, 1):
                print(f"{i}. Nama: {name}, Konser: {concert.name}, Tiket: {ticket_type.name}, Tanggal: {concert.date}")
        else:
            print("Tidak ada antrian.")
        print("Terima kasih telah menggunakan sistem antrian.")

    def print_specific_receipt(self, index):
        if 0 <= index < len(self.queue):
            name, concert, ticket_type = self.queue[index]
            self.print_individual_receipt(name, concert, ticket_type, index + 1)
        else:
            print("Indeks tidak valid.")

class ConcertManager:
    def __init__(self):
        self.concerts = []

    def add_concert(self, concert):
        self.concerts.append(concert)

        print(f"\tKonser '{concert.name}' akan hadir pada tanggal {concert.date}")
        print("\t-------------------------------------------------------")

    def list_concerts(self):
        if self.concerts:
            print("\nDaftar konser yang tersedia:")
            for i, concert in enumerate(self.concerts, 1):
                print(f"{i}. {concert.name} ({concert.date})")
        else:
            print("Tidak ada konser yang tersedia.")

    def get_concert_by_index(self, index):
        if 0 <= index < len(self.concerts):
            return self.concerts[index]
        else:
            print("Indeks konser tidak valid.")
            return None

def main():
    ticket_queue = TicketQueue()
    concert_manager = ConcertManager()

    # Menambahkan konser dan jenis tiket
    concerts_data = [
        ("Nct Dream", "2024-07-20"),
        ("Seventeen", "2024-08-15"),
        ("Ive", "2024-09-10"),
        ("New Jeans", "2024-10-05")
    ]
    ticket_types = ["VIP", "Platinum", "Festival", "Cat1", "Cat2", "Cat3", "Cat4", "Cat5"]
    
    for concert_name, concert_date in concerts_data:
        concert = Concert(concert_name, concert_date)
        for ticket_type_name in ticket_types:
            ticket_type = TicketType(ticket_type_name)
            concert.add_ticket_type(ticket_type)
        concert_manager.add_concert(concert)

    while True:
        print("\n\t----------------------------------------")
        print("\t|Sistem Antrian Penjualan Tiket Konser |")
        print("\t|1. Tambah ke antrian                  |")
        print("\t|2. Hapus dari antrian                 |")
        print("\t|3. Cek antrian                        |")
        print("\t|4. Cetak struk individu               |")
        print("\t|5. Cek sisa antrian yang tersedia     |")
        print("\t|6. Keluar                             |")
        print("\t----------------------------------------")

        choice = input("\tPilih opsi (1/2/3/4/5/6): ")
        
        if choice == '1':
            name = input("\nMasukkan nama untuk ditambahkan ke dalam antrian: ")
            concert_manager.list_concerts()
            concert_index = int(input("Pilih nomor konser yang ingin ditonton: ")) - 1
            concert = concert_manager.get_concert_by_index(concert_index)
            if concert:
                print("\nJenis tiket yang tersedia:")
                for i, ticket_type in enumerate(concert.ticket_types, 1):
                    print(f"{i}. {ticket_type}")
                ticket_type_index = int(input("Pilih nomor jenis tiket: ")) - 1
                if 0 <= ticket_type_index < len(concert.ticket_types):
                    ticket_type = concert.ticket_types[ticket_type_index]
                    ticket_queue.add_to_queue(name, concert, ticket_type)
                else:
                    print("Indeks jenis tiket tidak valid.")
        elif choice == '2':
            ticket_queue.remove_from_queue()
        elif choice == '3':
            ticket_queue.check_queue()
        elif choice == '4':
            if ticket_queue.queue:
                ticket_queue.check_queue()
                index = int(input("Masukkan nomor antrian yang ingin dicetak struknya: ")) - 1
                ticket_queue.print_specific_receipt(index)
            else:
                print("Antrian kosong.")
        elif choice == '5':
            available_slots = ticket_queue.available_slots()
            print("\n====================================")
            print(f"Sisa antrian yang tersedia: {available_slots} slot.")
            print("====================================")
        elif choice == '6':
            ticket_queue.print_final_receipt()
            print("======================================================================")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

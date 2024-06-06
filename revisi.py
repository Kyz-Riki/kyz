class TicketType:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

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
    def __init__(self):
        self.queue = []

    def add_to_queue(self, name, concert, ticket_type):
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
            print("\nDaftar antrian saat ini:")
            for i, (name, concert, ticket_type) in enumerate(self.queue, 1):
                print(f"{i}. {name} (Konser: {concert.name}, Tiket: {ticket_type.name})")
        else:
            print("Antrian kosong.")

class ConcertManager:
    def __init__(self):
        self.concerts = []

    def add_concert(self, concert):
        self.concerts.append(concert)
        print(f"Konser '{concert.name}' akan hadir pada tanggal {concert.date}")
    def list_concerts(self):
        if self.concerts:
            print("\nDaftar konser yang tersedia:\n")
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
        print("\n=========================================")
        print("Sistem Antrian Penjualan Tiket Konser")
        print("1. Tambah ke antrian")
        print("2. Hapus dari antrian")
        print("3. Cek antrian")
        print("4. List konser")
        print("5. Keluar")
        print("=========================================")

        choice = input("Pilih opsi (1/2/3/4/5): ")
        
        if choice == '1':
            name = input("Masukkan nama untuk ditambahkan ke dalam antrian: ")
            concert_manager.list_concerts()
            concert_index = int(input("\nPilih nomor konser yang ingin ditonton: ")) - 1
            concert = concert_manager.get_concert_by_index(concert_index)
            if concert:
                print("Jenis tiket yang tersedia:\n")
                for i, ticket_type in enumerate(concert.ticket_types, 1):
                    print(f"{i}. {ticket_type}")
                ticket_type_index = int(input("\nPilih nomor jenis tiket: ")) - 1
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
            concert_manager.list_concerts()
        elif choice == '5':
            print("Terima kasih telah menggunakan sistem antrian.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

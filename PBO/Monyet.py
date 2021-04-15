class Monyet:

    jumlah_monyet = 0

    def __init__(self,warna,berat,umur):
        self.warna = warna
        self.berat = berat
        self.umur = umur
        Monyet.jumlah_monyet += 1

    def tampilkan_jumlah(self):
        print("Total Monyet :", Monyet.jumlah_monyet)

    def tampilkan_profil(self):
        print("Warna :", self.warna)
        print("Berat :", self.berat)
        print("Umur :", self.umur)

monyet1 = Monyet("Hitam", 1.2, 4)
monyet2 = Monyet("Putih", 1.5, 3)

monyet1.tampilkan_profil()
monyet2.tampilkan_profil()
monyet1.tampilkan_jumlah()
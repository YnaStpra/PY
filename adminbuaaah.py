# Proses Login
username = "admin"
password = "123456"

print("Selamat datang di Aplikasi Admin Penjualan Buah")
print("Silakan login terlebih dahulu")

input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

if input_username == username and input_password == password:
    print("Login berhasil. Selamat bekerja!")
else:
    print("Username atau password yang Anda masukkan salah. Silakan coba lagi.")

# Proses Utama
buah = ["Apel", "Mangga", "Anggur", "Pisang", "Jeruk"]
harga = [10000, 20000, 30000, 4000, 5000]

print("Selamat datang di Aplikasi Admin Penjualan Buah")
print("Berikut adalah daftar buah yang tersedia:")

for i in range(len(buah)):
    print(f"{i+1}. {buah[i]} (Rp {harga[i]})")

print("Silakan pilih buah yang ingin Anda beli: ")
pilihan_buah = int(input("Masukkan nomor buah: "))

if pilihan_buah > 0 and pilihan_buah <= len(buah):
    buah_terpilih = buah[pilihan_buah-1]
    harga_terpilih = harga[pilihan_buah-1]
    jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))
    total_harga = jumlah_beli * harga_terpilih
    print(f"Anda telah membeli {jumlah_beli} {buah_terpilih} dengan harga total Rp {total_harga}")
else:
    print("Nomor buah yang Anda masukkan salah. Silakan coba lagi.")

# Proses Hasil
struk = {
    "nama_pembeli": input("Masukkan nama pembeli: "),
    "tanggal_beli": input("Masukkan tanggal beli: "),
    "daftar_belanja": [
        {
            "nama_buah": buah_terpilih,
            "harga_satuan": harga_terpilih,
            "jumlah_beli": jumlah_beli,
            "total_harga": total_harga
        }
    ]
}

print("--- Struk Pembelian ---")
print(f"Nama Pembeli: {struk['nama_pembeli']}")
print(f"Tanggal Beli: {struk['tanggal_beli']}")
print("Daftar Belanja: ")
for belanja in struk["daftar_belanja"]:
    print(f"{belanja['nama_buah']} x {belanja['jumlah_beli']} @ Rp {belanja['harga_satuan']} = Rp {belanja['total_harga']}")
print(f"Total Harga: Rp {struk['daftar_belanja'][0]['total_harga']}")
    
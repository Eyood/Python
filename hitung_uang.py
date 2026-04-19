NAMA_FILE = "catatan_uang.txt"

def baca_data():
  try:
    with open(NAMA_FILE, "r") as f:
      baris = f.read().splitlines()
      saldo = int(baris[0])
      transaksi = [int(uang) for uang in baris[1:]]
  except FileNotFoundError:
    saldo = 0
    transaksi = []
  return saldo, transaksi
    
def simpan_data(saldo, transaksi):
  with open(NAMA_FILE, "w") as f:
    f.write(str(saldo) + "\n")
    for uang in transaksi:
      f.write(str(uang) + "\n")
      
def tampilkan_data(saldo, transaksi):
  print(f"\nSaldo anda sekarang adalah Rp. {saldo:,}")
  print(f"Anda telah melakukan transaksi sebanyak {len(transaksi)} kali")
  
def nambah_data(saldo, transaksi):
  tipe = input("1.Pemasukan\n2.Pengeluaran\nPilih (1/2)\n> ")
  if tipe not in ("1", "2"):
    print("Invalid input\nPilih Antara 1 atau 2")
    return saldo, transaksi
  if tipe == "1":
    jenis = "pemasukan"
  if tipe == "2":
    jenis = "pengeluaran"
  if tipe in ("1", "2"):
    try:
      nambah = int(input(f"Masukkan jumlah {jenis}: "))
    except ValueError:
      print("Invalid Input\nPastikan input adalah angka")
      return saldo, transaksi
    if tipe == "1":
      saldo += nambah
      transaksi.append(nambah)
    else:
      saldo += -1 * nambah
      transaksi.append(-1 * nambah)
    print("Done.\n")
  return saldo, transaksi
  
def riwayat_transaksi(transaksi):
  panjang = len(transaksi)
  status = ""
  print("Riwayat transaksi:\n\n")
  for riwayat in transaksi[-5:]:
    if riwayat >= 0:
      status = "[+]"
    elif riwayat <= -1:
      status = "[-]"
      riwayat = -1 * riwayat
    print(f"{status} Rp {riwayat}")
  print("\n")
  
if __name__ == "__main__":
  saldo, transaksi = baca_data()
  while True:
    tampilkan_data(saldo, transaksi)
    if len(transaksi) >= 1:
      riwayat_transaksi(transaksi)
    pilihan = input("1.Tambah transaksi\n2.Keluar\n(1/2)\n> ")
    if pilihan not in ("1", "2"):
      print("Invalid input\n\nPilih antara 1 atau 2\n")
    elif pilihan == "1":
      saldo, transaksi = nambah_data(saldo, transaksi)
      simpan_data(saldo, transaksi)
    else:
      print("Bye")
      break

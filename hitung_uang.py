try:
  NAMA_FILE = "catatan_uang.txt"
  Run = True

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
    print(f"Saldo anda sekarang adalah Rp. {saldo:,}")
    print(f"Anda telah melakukan transaksi sebanyak {len(transaksi)} kali")
  
  def nambah_data(saldo, transaksi):
    tipe = input("1.Pemasukan\n2.Pengeluaran\n3.Exit\nPilih (1/2/3)\n> ")
    if tipe not in ("1", "2", "3"):
      print("Invalid input\n\nPilih Antara 1, 2, atau 3\n")
      return saldo, transaksi
    if tipe == "1":
      jenis = "pemasukan"
    elif tipe == "2":
      jenis = "pengeluaran"
    elif tipe == "3":
      print("Bye.")
      Run = False
    try:
      nambah = int(input(f"Masukkan jumlah {jenis}: "))
    except ValueError:
      print("Invalid Input\n\nPastikan input adalah angka\n")
      return saldo, transaksi
    if tipe == "1":
      saldo += nambah
      transaksi.append(nambah)
    else:
      saldo += -1 * nambah
      transaksi.append(-1 * nambah)
    print("Done.\n")
    return saldo, transaksi
  
  if __name__ == "__main__":
    saldo, transaksi = baca_data()
    while Run == True:
      tampilkan_data(saldo, transaksi)
      saldo, transaksi = nambah_data(saldo, transaksi)
      simpan_data(saldo, transaksi)
except UnboundLocalError:
  hi = "Jawa"
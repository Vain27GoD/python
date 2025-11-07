import time 
import sys

merah = "\033[91m"
biru = "\033[94m"
hijau = "\033[92m"
reset = "\033[0m"

lirik = [
  "Sudah terbiasa terjadi, Tante",
  "Teman datang ketika lagi butuh saja",
  "Coba kalau lagi susah",
  "Mereka semua menghilang, Tante",
]

waktu_jeda = 2

print(f"{biru}memulai lagi kapan kapan....{reset}")

for i in  range(3, 0, -1):
  print(f"{hijau}{i}.....{reset}")
  time.sleep(1)
  print("lirik lagu bermula")
  
  for baris in lirik:
    for huruf in baris :
      sys.stdout.write(huruf)
      sys.stdout.flush()
      time.sleep(0.05)
    print()
    time.sleep(waktu_jeda)
    
  print("\n{merah} lagu habisss.....")
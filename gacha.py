import random

welcome_pesan = '<<<<<WELCOME TO GACHA GACOR>>>>>'
no_gacor = random.randint(1, 10)
print('----------------')
print('ππππππππππππππ')
print('<<<<{welcome_pesan}>>>')
print('*______________*')

nama_user = input('masukan nama anda')
saldo = 0
depo = input('silakan top up mas ')
uang_anda = saldo + int(depo)

pilihan_usr = int(input('pilih angka dari 1-10'))

if uang_anda > 10000:
  print(pilihan_usr)
else:
  return

if pilihan_usr == no_gacor:
  print('selamat {nama_user} pilihan anda dengan nomor {no_gacor} benar.')
else:
  print('maaf anda memilih pilihan yang salah,yang benar adalah {no_gacor}.')

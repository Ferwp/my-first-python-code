print('tipe data skalar => tipe data sederhana')
anak1 = 'fernanda'
anak2 = 'wahyu'
anak3 = 'pratama'
anak4 = 'ferwp'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['fernanda', 'wahyu', 'pratama', 'ferwp']
print(anak)
anak.append('Limo') #perintah ini masuk kedalam tampilan akhir baris di bawah
print(anak)

print('\nsapa anak ke-2 ')
print(f'Hai {anak[1]}!')

print('\n sapa semua anak')
for a in anak: #a dijadikan var pada perintah for, pengganti var anak
    print(f'hai {a}!')

print('\nsapa semua anak cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. hai {anak[a]} !')
    #fungsi a+1 adalah perulangan untuk mencetak angka depan, dimulai dengan a=0+1 sampai jumlah anak
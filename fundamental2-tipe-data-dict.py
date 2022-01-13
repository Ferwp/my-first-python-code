"""
tipe data dictionary sekedar menghubungakan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak' : 'son', 'istri' : 'wife', 'ayah' : 'father', 'ibu' : 'mother'}

print(kamus_ind_eng) #menampilkan teks yg ada di var kamus_ind_eng
print(kamus_ind_eng['ayah']) #memanggil kata yang ada di var tsb ayah=father
print(kamus_ind_eng['ibu']) #memanggil kata yang ada di var tsb ibu=mother

print('\nData ini dikirimkan oleh server gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
# \n berfungsi untuk spasi ke bawah

data_dari_server_gojek = {
    'tanggal': '2022-01-13',
    'driver_list': [
        {'nama': 'Fernanda', 'jarak': 10},
        {'nama': 'wahyu', 'jarak': 50},
        {'nama': 'pratama', 'jarak': 150},
        {'nama': 'ferwp', 'jarak': 200},
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")

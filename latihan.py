data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("no. 1")
for i,j in data_panen.items():
    print(f"Lokasi: {j['nama_lokasi']}\nHasil panen padi: {j['hasil_panen']['padi']}\nHasil panen jagung: {j['hasil_panen']['jagung']}\nHasil panen kedelai: {j['hasil_panen']['kedelai']}\n")

print("no. 2")
for i,j in data_panen.items():
    if i == 'lokasi2':
        print(f"Hasil panen jagung {i}: {j['hasil_panen']['jagung']}\n")

print("no. 3")
for i,j in data_panen.items():
    if i == 'lokasi3':
        print(f"Nama {i}: {j['nama_lokasi']}\n")

print("no. 4")
data_padi = 0
data_kedelai = 0
for i,j in data_panen.items():
    data_padi += j['hasil_panen']['padi']
    data_kedelai += j['hasil_panen']['kedelai']
print(f"Total padi dari seluruh lokasi: {data_padi}")
print(f"Total kedelai dari seluruh lokasi: {data_kedelai}\n")

print("no. 5")
padi_kedelai = data_padi + data_kedelai
print(f"Total padi dan kedelai dari semua lokasi: {padi_kedelai}\n")

print("no. 6")
for i,j in data_panen.items():
    if j['hasil_panen']['padi'] > 1300:
        perhatian = f"{i} memerlukan perhatian khusus"
    else:
        perhatian = f"{i} tidak memerlukan perhatian khusus"
    print(f"Lokasi: {j['nama_lokasi']}\nHasil panen padi: {j['hasil_panen']['padi']}\nHasil panen jagung: {j['hasil_panen']['jagung']}\nHasil panen kedelai: {j['hasil_panen']['kedelai']}\n{perhatian}\n")
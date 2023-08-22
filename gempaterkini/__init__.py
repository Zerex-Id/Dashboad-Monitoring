def ekstraksi_data():
    """

    Tanggal: 21 Agustus 2023
    Waktu: 17:01:23 WIB
    Magnitudo: 5.0
    Kedalaman: 465 km
    Lokasi: LS=7.60  BT=120.50
    Pusat Gempa: 112 km TimurLaut RUTENG-MANGGARAI-NTT
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '21 Agustus 2023'
    hasil['waktu'] = '17:01:23 WIB'
    hasil['magnitudo'] = 5.0
    hasil['kedalaman'] = '465 km'
    hasil['lokasi'] = {'ls': 7.60, 'bt': 120.50}
    hasil['pusat gempa'] = '112 km TimurLaut RUTENG-MANGGARAI-NTT'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat Gempa: {result['pusat gempa']}")

# if __name__ == '__main__':
#     print('ini adalah gempa terkini')

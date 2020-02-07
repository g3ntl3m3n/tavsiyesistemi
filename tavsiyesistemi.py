import math
ornek_veri = {
    'Ahsen Tekdemir': {
        'Breaking Bad': '9.5',
        'Dark': '9.2',
        'Big Bang Theory' : '8.3',
        'Rick and Morty' : '9.1'
    },
    'Mucahit Ozturk': {
       'Breaking Bad' : '8.3',
        'Dark' : '8.0',
        'Big Bang Theory' : '7.6',
        'Rick and Morty' : '9.4'
    },
    'İbrahim Yilmaz': {
       'Breaking Bad' : '9.3',
        'Dark' : '9.0',
        'Big Bang Theory' : '8.8',
        'Rick and Morty' : '9.1'
    },
    'Ananas Kafa': {
       'Breaking Bad' : '9.9',
        'Dark' : '9.8',
        'Big Bang Theory' : '9.6',
        'Rick and Morty' : '9.8'
    },
    'Armut Herif': {
       'Breaking Bad' : '9.3',
        'Dark' : '9.5',
        'Big Bang Theory' : '8.1',
        'Rick and Morty' : '8.7'
    },

}

def OklidBenzerligi(kisi1, kisi2):
    ortak_oylanan_filmler = [veri for veri in ornek_veri[kisi1] if veri in ornek_veri[kisi2]]
    oylananlar = [(ornek_veri[kisi1][veri],ornek_veri[kisi2][veri])
                  for veri in ortak_oylanan_filmler]
    uzaklik = [pow(oylanan[0] - oylanan[1], 2) for oylanan in oylananlar]
    return 1 / (1 + sum(uzaklik))

def TavsiyeEt(kisi, benzer_sayisi):
    degerlendirme_skorlari = [(OklidBenzerligi(kisi, diger), diger) for diger in ornek_veri
                              if diger != kisi]
    degerlendirme_skorlari.sort()
    degerlendirme_skorlari.reverse()
    degerlendirme_skorlari = degerlendirme_skorlari[0:benzer_sayisi]

    tavsiyeler = {}

    for benzerlik, diger in degerlendirme_skorlari:
        secilmis = ornek_veri[diger]
        for veri in secilmis:
            if veri not in ornek_veri[kisi]:
                agirlik = benzerlik * secilmis[veri]

                if veri in tavsiyeler:
                    s, agirliklar = tavsiyeler[veri]
                    tavsiyeler[veri] = (s + benzerlik, agirliklar+[agirlik])
                else:
                    tavsiyeler[veri] = (benzerlik, [agirlik])

    for i in tavsiyeler:
        benzerlik, film = tavsiyeler[i]
        tavsiyeler[i] = sum(film) / benzerlik

        return tavsiyeler


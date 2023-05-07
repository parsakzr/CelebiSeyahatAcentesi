class bilet:
    def __init__(self, date, price):
        self.date=date
        self.price=price


class flightTicket(bilet):
    def __init__(self, date ,price):
        super().__init__(date,price)

class hotelBooking(bilet):
    def __init__(self, date ,price, bolge):
        super().__init__(date,price)
        self.bolge = bolge

class Musteri:
    def __init__(self, musteri_bilgileri):
        self.musteri_Bilgileri = musteri_bilgileri
        self.puan = 0

    def yazdir(self):
        print(f"Musteri bilgileri; {self.musteri_Bilgileri}")
        print(f"puan; {self.puan}")

    def puan_ekle(self,puan):
        self.puan+=puan

    def puan_sil(self,puan):
        self.puan-=puan

class Firma:
    def __init__(self, isim):
        self.isim = isim
        self.bilet = []

    def yazdir(self):
        print(f"İsim; {self.isim}")

    def bilet_ara(self):
        pass#ret price

    def bilet_satis_sistemi(self):
        pass

class Otel:
    def __init__(self, isim):
        self.isim = isim
        self.bolgeler = []
        self.bilet = []

    def bolge_ekle(self, bolge_ismi):
        self.bolgeler.append(bolge_ismi)

    def yazdir(self):
        print(f"İsim; {self.isim}")
        print("Bolgeler:")
        for bolge in self.bolgeler:
            print(bolge, end=", ")
        print("\n")

    def tatil_ara(self):
        pass #return price

    def tatil_satis_sistemi(self):
        pass

class Acente:
    def __init__(self, isim):
        self.isim = isim
        self.firmalar = []
        self.oteller = []
        self.musteriler = []
        self.kasa = 0
        #self.cek= []

    def firma_olustur(self, firma_ismi):
        self.firmalar.append(Firma(firma_ismi))

    def otel_olustur(self, otel_ismi, bolge_ismi):
        for otel in self.oteller:
            if otel.isim == otel_ismi:
                otel.bolge_ekle(bolge_ismi)
                break
        else:
            yeni_otel = Otel(otel_ismi)
            yeni_otel.bolge_ekle(bolge_ismi)
            self.oteller.append(yeni_otel)

    def musteri_olustur(self, musteri_ismi):
        self.musteriler.append(Musteri(musteri_ismi))

    def yazdir(self):
        print(f"\n İsim; {self.isim}")
        print(f"Kasa; {self.kasa}")
        print("\n \n Firmalar;")
        for firma in self.firmalar:
            firma.yazdir()
        print("\n \n Oteller;")
        for otel in self.oteller:
            otel.yazdir()
        print("\n \n Musteriler;")
        for musteri in self.musteriler:
            musteri.yazdir()

    def tatil_listele(self):
        pass

    def rezerve_et(self):
        pass

    def odeme_al(self):
        pass

def arayuz(acenta):
    print("Gorevli Arayuzu \n")
    islem_tipi = input("Tatil icin 1 \n"
                       "Yolculuk icin 2 ")
    if islem_tipi == 1:
        input_gitmek_istedigi_bolge = input("Müşterinin gitmek istediği bölgeyi giriniz: ")
        input_tarih = input("Müşterinin gitmek istediği tarihi giriniz: ")
        # uygun otelleri listele
        # musteri secim yapsin
        # musteri onayi alinirsa rezervasyon yap
        # odeme alinirsa otele bilgi ilet
        print("tatil islemleri")
    else:
        input_firma_ismi = input("Müşteri hangi firma ile gitmek istiyor: ")
        input_tarih = input("Müşterinin gitmek istediği tarihi giriniz: ")
        input_bulundugu_bolge = input("Müşterinin şu an bulunduğu bölgeyi giriniz: ")
        input_gitmek_istedigi_bolge = input("Müşterinin gitmek istediği bölgeyi giriniz: ")
        # ilgili firmanin bilet satis sistemine aktar
        # boyle bir bilet varsa fiyati musteriye goster
        # musteri onay verirse odeme al firmayı bilgilendir
        print("bilet islemleri")


if __name__ == '__main__':
    # veritabanindan bilgileri cekip dizilere aktar ve tanimlamalari yap
    sehirler = ["İstanbul", "Ankara", "İzmir", "Bursa", "Adana", "Antalya", "Konya", "Gaziantep", "Şanlıurfa", "Bodrum"]
    firmalar = ["Türk Hava Yolları", "Pegasus Havayolları", "AnadoluJet"]
    oteller = [
        ("Hilton", "İstanbul", "Ankara"),
        ("Marriott", "Ankara"),
        ("Sheraton", "İzmir", "Adana", "Konya"),
        ("Holiday Inn", "Antalya"),
        ("Ritz Carlton", "Bodrum")
    ]
    musteriler = ["Bilal"]
    acente = Acente("Uçan Türk Özel Havayolu")

    for firma in firmalar:
        acente.firma_olustur(firma)

    for otel in oteller:
        for i in range(1, len(otel)):
            acente.otel_olustur(otel[0], otel[i])

    for musteri in musteriler:
        acente.musteri_olustur(musteri)

    # acente.yazdir()
    arayuz(acente)

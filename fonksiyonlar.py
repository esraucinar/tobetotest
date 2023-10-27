
#birçok sayfada bu kredileri kullanmam gerekseydi, fonksiyon ile onu isimlendirir, ihtiyaç olduğunda çağırırdık.


def kredileriListele():
    krediler=["hızlı kredi","maaşını halkbank'tan alanlara özel","mutlu emekli ihtiyaç kredisi"]
    for kredi in krediler:
        print(kredi)
#bu kodları çalıştırdığımda hiçbir şey olmaz;çünkü burada sadece tanım yapıldı. 

kredileriListele()      #üst taraftaki tanım, bu ise üstte yazılanı çağırma.şayet listede bir öğe iptal olursa, sadece tanımlanan yerden silmek yeterli. 

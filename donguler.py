krediler=["hızlı kredi","maaşını halkbank'tan alanlara özel","mutlu emekli ihtiyaç kredisi"]

#alias=takma değer, o an ki gezdiği değer(kredi için)
for kredi in krediler:
    print(kredi)

#krediler uzunluğunda döndür demek. 
for i in range(len(krediler)):  
    print(i)

#eğer değerleri görmek istersek, krediler dizisini yazdırırız.parantez içindeki i, tek tek dizideki kredilerin temsili.
for i in range(len(krediler)):
    print(krediler[i])
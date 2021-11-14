import math
while True:
    try:
        arac_s = int(input("Araç Sayısı: "))
    except:
        print("Error")
    a2 = 0
    for i in range(arac_s):
        i2 = i + 1
        a = int(input("Araç Şarj Kapasitesi " + str(i2) + ":"))
        a2 = a2 + a
        ort_sarj = a2 / arac_s

    watT_l = int(input("Toplam Watt(kW): "))
    last_c = int(input("Aracın Şarj Gereksinimi(kw): "))
    rr = watT_l / arac_s
    rr2 = last_c / arac_s
    sonuc = rr * rr2
    print(str(sonuc) + "kW")

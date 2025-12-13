"""
BULANIK MANTIK İLE ARAÇ YAKIT TÜKETİMİ TAHMİNİ

Girdiler:
- Araç Hızı (km/s)
- Motor Sıcaklığı (°C)
- Yol Eğimi (%)

Çıktı:
- Yakıt Tüketimi (L/100km)

Yöntem:
- Mamdani Bulanık Çıkarım Sistemi
- Üçgensel Üyelik Fonksiyonları
- Genişletilmiş Kural Tabanı (12 kural)
- Ağırlık Merkezi (Centroid) Durulama
"""

# ==================================================
# GEREKLİ KÜTÜPHANELER
# ==================================================

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


# ==================================================
# EVREN KÜMELERİ (DEĞİŞKEN ARALIKLARI)
# ==================================================

hiz = np.arange(0, 201, 1)                 # Araç hızı (km/s)
motor_sicakligi = np.arange(50, 121, 1)    # Motor sıcaklığı (°C)
yol_egimi = np.arange(-10, 11, 1)          # Yol eğimi (%)

yakit_tuketimi = np.arange(0, 21, 1)       # Yakıt tüketimi (L/100km)


# ==================================================
# ÜYELİK FONKSİYONLARI
# ==================================================

# --- Araç Hızı ---
hiz_dusuk = fuzz.trimf(hiz, [0, 0, 60])
hiz_orta = fuzz.trimf(hiz, [40, 90, 140])
hiz_yuksek = fuzz.trimf(hiz, [120, 200, 200])

# --- Motor Sıcaklığı ---
sicaklik_dusuk = fuzz.trimf(motor_sicakligi, [50, 50, 75])
sicaklik_normal = fuzz.trimf(motor_sicakligi, [70, 90, 110])
sicaklik_yuksek = fuzz.trimf(motor_sicakligi, [100, 120, 120])

# --- Yol Eğimi ---
egim_asagi = fuzz.trimf(yol_egimi, [-10, -10, 0])
egim_duz = fuzz.trimf(yol_egimi, [-2, 0, 2])
egim_yukari = fuzz.trimf(yol_egimi, [0, 10, 10])

# --- Yakıt Tüketimi ---
yakit_az = fuzz.trimf(yakit_tuketimi, [0, 0, 7])
yakit_orta = fuzz.trimf(yakit_tuketimi, [5, 10, 15])
yakit_fazla = fuzz.trimf(yakit_tuketimi, [12, 20, 20])


# ==================================================
# ÜYELİK FONKSİYONLARI GÖRSELLEŞTİRME
# ==================================================

def uyelik_fonksiyonu_ciz(x, uyelikler, etiketler, baslik, x_etiketi):
    """Üyelik fonksiyonlarını grafik olarak çizer"""
    plt.figure(figsize=(8, 4))
    for u, e in zip(uyelikler, etiketler):
        plt.plot(x, u, label=e)

    plt.title(baslik)
    plt.xlabel(x_etiketi)
    plt.ylabel("Üyelik Derecesi")
    plt.legend()
    plt.grid(True)
    plt.show()


# ==================================================
# BULANIK ÇIKARIM ve KURAL TABANI
# ==================================================

def yakit_tuketimi_hesapla(hiz_degeri, sicaklik_degeri, egim_degeri):
    """Bulanık mantık ile yakıt tüketimi tahmini yapar"""

    # -------- BULANIKLAŞTIRMA --------
    hiz_d = fuzz.interp_membership(hiz, hiz_dusuk, hiz_degeri)
    hiz_o = fuzz.interp_membership(hiz, hiz_orta, hiz_degeri)
    hiz_y = fuzz.interp_membership(hiz, hiz_yuksek, hiz_degeri)

    sic_d = fuzz.interp_membership(motor_sicakligi, sicaklik_dusuk, sicaklik_degeri)
    sic_n = fuzz.interp_membership(motor_sicakligi, sicaklik_normal, sicaklik_degeri)
    sic_y = fuzz.interp_membership(motor_sicakligi, sicaklik_yuksek, sicaklik_degeri)

    egim_a = fuzz.interp_membership(yol_egimi, egim_asagi, egim_degeri)
    egim_d = fuzz.interp_membership(yol_egimi, egim_duz, egim_degeri)
    egim_y = fuzz.interp_membership(yol_egimi, egim_yukari, egim_degeri)

    # -------- IF–THEN KURALLARI --------

    # Az yakıt
    k1 = np.fmin(hiz_d, egim_d)
    k2 = np.fmin(hiz_d, egim_a)
    k3 = np.fmin(hiz_o, egim_a)

    # Orta yakıt
    k4 = np.fmin(hiz_o, egim_d)
    k5 = np.fmin(hiz_o, sic_n)
    k6 = np.fmin(hiz_y, egim_a)
    k7 = np.fmin(hiz_d, sic_y)

    # Fazla yakıt
    k8 = np.fmin(hiz_y, egim_y)
    k9 = np.fmin(hiz_y, sic_y)
    k10 = np.fmin(hiz_o, egim_y)
    k11 = np.fmin(hiz_d, sic_d)
    k12 = np.fmin(hiz_y, egim_d)

    # -------- ÇIKTI ÜYELİK FONKSİYONLARI İLE KESME --------
    yakit_az_kesilmis = np.fmin(yakit_az, np.fmax(k1, np.fmax(k2, k3)))
    yakit_orta_kesilmis = np.fmin(
        yakit_orta,
        np.fmax(k4, np.fmax(k5, np.fmax(k6, k7)))
    )
    yakit_fazla_kesilmis = np.fmin(
        yakit_fazla,
        np.fmax(k8, np.fmax(k9, np.fmax(k10, np.fmax(k11, k12))))
    )

    # -------- BİRLEŞTİRME --------
    birlesik_cikti = np.fmax(
        yakit_az_kesilmis,
        np.fmax(yakit_orta_kesilmis, yakit_fazla_kesilmis)
    )

    # -------- DURULAMA --------
    sonuc = fuzz.defuzz(yakit_tuketimi, birlesik_cikti, 'centroid')

    return sonuc, birlesik_cikti


# ==================================================
# DURULAMA (DEFUZZIFICATION) GRAFİĞİ
# ==================================================

def durulama_grafigi_ciz(birlesik_cikti, sonuc, baslik):
    """Durulama sonucunu grafik üzerinde gösterir"""
    plt.figure(figsize=(8, 4))

    plt.plot(yakit_tuketimi, yakit_az, 'b--', label='Az')
    plt.plot(yakit_tuketimi, yakit_orta, 'g--', label='Orta')
    plt.plot(yakit_tuketimi, yakit_fazla, 'r--', label='Fazla')

    plt.fill_between(yakit_tuketimi, 0, birlesik_cikti,
                     alpha=0.4, color='orange', label='Birleşik Çıktı')

    plt.axvline(x=sonuc, color='k', linewidth=2,
                label=f'Sonuç = {sonuc:.2f} L/100km')

    plt.title(baslik)
    plt.xlabel("Yakıt Tüketimi (L/100km)")
    plt.ylabel("Üyelik Derecesi")
    plt.legend()
    plt.grid(True)
    plt.show()


# ==================================================
# ANA PROGRAM
# ==================================================

if __name__ == "__main__":

    # --- Üyelik Fonksiyonları ---
    uyelik_fonksiyonu_ciz(hiz, [hiz_dusuk, hiz_orta, hiz_yuksek],
                          ["Düşük", "Orta", "Yüksek"],
                          "Araç Hızı Üyelik Fonksiyonları", "Hız (km/s)")

    uyelik_fonksiyonu_ciz(motor_sicakligi,
                          [sicaklik_dusuk, sicaklik_normal, sicaklik_yuksek],
                          ["Düşük", "Normal", "Yüksek"],
                          "Motor Sıcaklığı Üyelik Fonksiyonları", "Sıcaklık (°C)")

    uyelik_fonksiyonu_ciz(yol_egimi,
                          [egim_asagi, egim_duz, egim_yukari],
                          ["Yokuş Aşağı", "Düz", "Yokuş Yukarı"],
                          "Yol Eğimi Üyelik Fonksiyonları", "Eğim (%)")

    uyelik_fonksiyonu_ciz(yakit_tuketimi,
                          [yakit_az, yakit_orta, yakit_fazla],
                          ["Az", "Orta", "Fazla"],
                          "Yakıt Tüketimi Üyelik Fonksiyonları", "L/100km")

    # --- SENARYO TESTLERİ ---
    senaryolar = [
        ("Senaryo 1: Orta hız, normal sıcaklık, hafif yokuş", 90, 90, 3),
        ("Senaryo 2: Düşük hız, düşük sıcaklık, düz yol", 40, 60, 0),
        ("Senaryo 3: Yüksek hız, yüksek sıcaklık, yokuş yukarı", 140, 110, 8)
    ]

    for ad, h, s, e in senaryolar:
        sonuc, birlesik = yakit_tuketimi_hesapla(h, s, e)

        print(ad)
        print(f"Girdiler → Hız: {h} km/s, Sıcaklık: {s} °C, Eğim: {e} %")
        print(f"Tahmini Yakıt Tüketimi: {sonuc:.2f} L/100km\n")

        durulama_grafigi_ciz(birlesik, sonuc, ad)
        
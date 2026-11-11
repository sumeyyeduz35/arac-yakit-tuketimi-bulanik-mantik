
# Araç Yakıt Tüketimi Tahmini - Bulanık Mantık
# Vehicle Fuel Consumption Estimation Using Fuzzy Logic

Python ile geliştirilmiş, Mamdani bulanık çıkarım sistemini kullanarak araç yakıt tüketimini tahmin eden kural tabanlı bir model.

A Python-based, rule-driven fuel consumption estimation model using the Mamdani fuzzy inference method.

**Teknolojiler / Technologies:** Python | NumPy | scikit-fuzzy | Matplotlib

---

# Türkçe

## Proje Hakkında

Bu proje, araçların yakıt tüketimini farklı sürüş koşullarına göre tahmin etmek amacıyla bulanık mantık yaklaşımı kullanılarak geliştirilmiştir.

Model; araç hızı, motor sıcaklığı ve yol eğimi gibi üç farklı giriş değişkenini değerlendirerek tahmini yakıt tüketimini L/100 km cinsinden hesaplar.

Geleneksel kesin sınırlar yerine bulanık kümeler ve dilsel kurallar kullanılarak farklı sürüş koşullarının yakıt tüketimi üzerindeki etkisi modellenmiştir.

Proje, Mamdani bulanık çıkarım sisteminin Python üzerinde uygulanmasını ve sonuçların görselleştirilmesini göstermektedir.

## Kullanılan Teknolojiler

| Teknoloji | Kullanım Amacı |
|---|---|
| Python | Modelin geliştirilmesi |
| NumPy | Sayısal hesaplamalar |
| scikit-fuzzy | Bulanık mantık işlemleri |
| Matplotlib | Üyelik fonksiyonlarının ve sonuçların görselleştirilmesi |

## Modelin Giriş ve Çıkış Değişkenleri

Model üç giriş değişkeni ve bir çıkış değişkeninden oluşmaktadır.

| Değişken | Aralık | Birim |
|---|---|---|
| Araç Hızı | 0–200 | km/sa |
| Motor Sıcaklığı | 50–120 | °C |
| Yol Eğimi | -10 ile +10 | % |
| Yakıt Tüketimi (Çıktı) | 0–20 | L/100 km |

Giriş değişkenleri düşük, orta/normal ve yüksek gibi dilsel kategorilerle temsil edilmektedir.

Yol eğimi ise yokuş aşağı, düz ve yokuş yukarı olmak üzere üç bulanık kümeye ayrılmıştır.

## Bulanık Mantık Yöntemi

Projede Mamdani bulanık çıkarım yöntemi kullanılmaktadır.

Modelin çalışma süreci dört temel aşamadan oluşur.

### 1. Bulanıklaştırma (Fuzzification)

Sayısal giriş değerleri, üçgensel üyelik fonksiyonları kullanılarak bulanık kümelere dönüştürülür.

Her girişin ilgili bulanık kümelere ait olma derecesi hesaplanır.

### 2. Kural Tabanı (Rule Base)

Sistem, farklı sürüş koşullarını değerlendirmek amacıyla tanımlanmış 12 IF–THEN kuralını kullanır.

Örnek kurallar:

- Araç hızı düşük ve yol düz ise yakıt tüketimi azdır.
- Araç hızı orta ve motor sıcaklığı normal ise yakıt tüketimi ortadır.
- Araç hızı yüksek ve yol yokuş yukarı ise yakıt tüketimi fazladır.
- Araç hızı düşük ve motor sıcaklığı düşük ise yakıt tüketimi fazladır.

Kuralların değerlendirilmesinde minimum ve maksimum operatörleri kullanılır.

### 3. Birleştirme (Aggregation)

Aktif kuralların oluşturduğu çıktı kümeleri birleştirilerek tek bir bulanık çıktı kümesi elde edilir.

### 4. Durulama (Defuzzification)

Birleştirilmiş bulanık çıktı, ağırlık merkezi (Centroid) yöntemi kullanılarak sayısal bir yakıt tüketimi tahminine dönüştürülür.

Sonuç L/100 km cinsinden ifade edilir.

## Senaryo Analizleri

Kaynak kodda üç farklı sürüş senaryosu tanımlanmıştır.

| Senaryo | Hız | Motor Sıcaklığı | Yol Eğimi |
|---|---|---|---|
| Orta hız, normal sıcaklık, hafif yokuş | 90 km/sa | 90 °C | %3 |
| Düşük hız, düşük sıcaklık, düz yol | 40 km/sa | 60 °C | %0 |
| Yüksek hız, yüksek sıcaklık, yokuş yukarı | 140 km/sa | 110 °C | %8 |

Program çalıştırıldığında her senaryo için tahmini yakıt tüketimi hesaplanır ve ilgili bulanık çıktı grafiği oluşturulur.

## Görselleştirme

Matplotlib kullanılarak aşağıdaki grafikler program tarafından oluşturulur:

- Araç hızı üyelik fonksiyonları
- Motor sıcaklığı üyelik fonksiyonları
- Yol eğimi üyelik fonksiyonları
- Yakıt tüketimi üyelik fonksiyonları
- Senaryolara ait birleşik bulanık çıktı ve durulama grafikleri

Grafikler, çıkarım sürecinin yorumlanmasını kolaylaştırmak amacıyla kullanılır.

## Proje Yapısı

```text
arac-yakit-tuketimi-bulanik-mantik/
├── src/
│   └── fuzzy_model.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Kurulum ve Çalıştırma

### Gereksinimler

- Python 3
- pip

### 1. Projeyi Klonlama

```bash
git clone https://github.com/sumeyyeduz35/arac-yakit-tuketimi-bulanik-mantik.git
cd arac-yakit-tuketimi-bulanik-mantik
```

### 2. Bağımlılıkları Yükleme

```bash
python -m pip install -r requirements.txt
```

### 3. Programı Çalıştırma

```bash
python src/fuzzy_model.py
```

Program, tanımlanan senaryoların tahmini yakıt tüketimlerini terminalde gösterir ve Matplotlib grafiklerini oluşturur.

## Modelin Sınırları

Bu proje, bulanık mantık yönteminin yakıt tüketimi tahmini problemine uygulanmasını gösteren kural tabanlı bir modeldir.

- Tahminler önceden tanımlanmış üyelik fonksiyonları ve kurallara dayanır.
- Model gerçek araç verileriyle eğitilmiş bir makine öğrenmesi modeli değildir.
- Gerçek yakıt tüketimi; araç tipi, motor hacmi, sürüş tarzı ve çevresel koşullar gibi ek faktörlerden etkilenebilir.
- Tahminlerin gerçek ölçümlerle doğrulandığına ilişkin bir performans analizi sunulmamaktadır.

## Proje Durumu

Modelin kaynak kodu, bulanık çıkarım kuralları, senaryo hesaplamaları ve görselleştirme bileşenleri geliştirilmiştir.

Proje, Python ile bulanık mantık sistemlerinin tasarlanması ve uygulanması üzerine yapılmış bir çalışmadır.

---

# English

## About the Project

This project implements a rule-based fuzzy logic model to estimate vehicle fuel consumption under different driving conditions.

The model evaluates three input variables:

- Vehicle speed
- Engine temperature
- Road slope

These inputs are processed using a Mamdani fuzzy inference system to estimate fuel consumption in liters per 100 kilometers (L/100 km).

Instead of relying on strictly defined numerical boundaries, the system represents driving conditions through fuzzy sets and linguistic rules.

The project demonstrates fuzzy inference implementation and result visualization using Python.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Model implementation |
| NumPy | Numerical computations |
| scikit-fuzzy | Fuzzy logic operations |
| Matplotlib | Membership function and output visualization |

## Input and Output Variables

The model consists of three input variables and one output variable.

| Variable | Range | Unit |
|---|---|---|
| Vehicle Speed | 0–200 | km/h |
| Engine Temperature | 50–120 | °C |
| Road Slope | -10 to +10 | % |
| Fuel Consumption (Output) | 0–20 | L/100 km |

Triangular membership functions are used to represent linguistic categories such as low, medium, normal, and high.

Road slope is represented by downhill, flat, and uphill fuzzy sets.

## Fuzzy Inference Method

The system uses the Mamdani fuzzy inference approach.

The inference process consists of four main stages.

### 1. Fuzzification

Numerical input values are mapped to fuzzy sets using triangular membership functions.

Membership degrees are calculated for the corresponding linguistic categories.

### 2. Rule Evaluation

The model includes 12 predefined IF–THEN rules describing relationships between driving conditions and fuel consumption.

Example rules:

- If vehicle speed is low and the road is flat, fuel consumption is low.
- If vehicle speed is medium and engine temperature is normal, fuel consumption is medium.
- If vehicle speed is high and the road is uphill, fuel consumption is high.
- If vehicle speed is low and engine temperature is low, fuel consumption is high.

Minimum and maximum operators are used during fuzzy rule evaluation and combination.

### 3. Aggregation

The output fuzzy sets produced by active rules are combined into a single aggregated fuzzy set.

### 4. Defuzzification

The aggregated fuzzy set is converted into a numerical fuel consumption estimate using the Centroid method.

The final result is expressed in L/100 km.

## Test Scenarios

Three driving scenarios are defined in the source code.

| Scenario | Speed | Engine Temperature | Road Slope |
|---|---|---|---|
| Medium speed, normal temperature, slight uphill | 90 km/h | 90 °C | 3% |
| Low speed, low temperature, flat road | 40 km/h | 60 °C | 0% |
| High speed, high temperature, uphill | 140 km/h | 110 °C | 8% |

For each scenario, the program calculates an estimated fuel consumption value and visualizes the aggregated fuzzy output.

## Visualization

The application generates the following plots using Matplotlib:

- Vehicle speed membership functions
- Engine temperature membership functions
- Road slope membership functions
- Fuel consumption membership functions
- Aggregated fuzzy output and defuzzification results

These visualizations help illustrate and interpret the fuzzy inference process.

## Project Structure

```text
arac-yakit-tuketimi-bulanik-mantik/
├── src/
│   └── fuzzy_model.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Usage

### Requirements

- Python 3
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/sumeyyeduz35/arac-yakit-tuketimi-bulanik-mantik.git
cd arac-yakit-tuketimi-bulanik-mantik
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the Model

```bash
python src/fuzzy_model.py
```

The program prints the estimated fuel consumption for the predefined scenarios and generates Matplotlib plots.

## Model Limitations

This project demonstrates the application of fuzzy logic to a fuel consumption estimation problem.

- Predictions depend on predefined membership functions and inference rules.
- The system is not a machine learning model trained on real-world vehicle data.
- Actual fuel consumption may depend on additional factors such as vehicle type, engine specifications, driving behavior, and environmental conditions.
- No quantitative validation against real-world fuel consumption measurements is provided.

## Project Status

The fuzzy inference implementation, rule base, scenario calculations, and visualization components have been developed.

This project demonstrates practical implementation of fuzzy logic systems using Python.

# 🚀 Fibonacci Serisi (Memoization ile)

Fibonacci sayıları, **her terimin kendisinden önceki iki terimin toplamı** olduğu bir sayı sistemidir.  
Bu proje, Python kullanarak **memoization (önbellekleme)** tekniği ile optimize edilmiş bir **Fibonacci serisi hesaplama fonksiyonu** içermektedir. 

## 📌 Özellikler
- **Rekürsif Fibonacci hesaplaması**
- **Memoization (önbellekleme) ile optimizasyon**
- **O(n) zaman karmaşıklığı**, yani klasik rekürsif yönteme göre **çok daha hızlıdır!** 🚀
- **Negatif giriş kontrolü!** ❌ `n < 0` için hata mesajı verir.

---

## 📥 Kurulum ve Kullanım

Bu projeyi kullanmak için aşağıdaki adımları takip edebilirsiniz.

### 1️⃣ **Python'u indirin ve yükleyin**  
**Python'u indirin ve yükleyin**: [Python Resmi Sitesi](https://www.python.org/downloads/)

### 2️⃣ **Depoyu Klonlayın**
```bash
git clone https://github.com/epatayb/fibonacci-memoization.git
cd fibonacci-memoization
```
### 3️⃣ **Uygulamayı çalıştırın:**
Uygulamayı çalıştırın:
   ```bash
   python fibonacci.py
   ``` 

### ✅ Memoization Neden Önemli?
Klasik rekürsif Fibonacci fonksiyonu O(2ⁿ) zaman karmaşıklığına sahiptir.  
Bu versiyon O(n) zaman karmaşıklığına sahiptir, çünkü her Fibonacci değeri sadece bir kez hesaplanır ve memo sözlüğüne kaydedilir.  
Önceden hesaplanan değerleri tekrar hesaplamaya gerek kalmaz! 🚀  

## ⚠️ Negatif Giriş Kontrolü
Fonksiyon negatif girişlerde hata fırlatır:
```bash
Fibonacci serisinin kaçıncı adımını görmek istiyorsunuz?: -5
ValueError: Hata: Fibonacci serisi için negatif bir sayı girilemez!
```

## 📌 Örnek Kullanım
komut satırında çalıştırarak istediğiniz sayıyı öğrenebilirsiniz.
```bash
Fibonacci serisinin kaçıncı adımını görmek istiyorsunuz?: 6
Sonuç: 8   
```

## 🎯 Katkıda Bulunma
Eğer projeye katkı sağlamak istiyorsanız:

1. Depoyu forklayın
2. Yeni bir dal (branch) oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi yapın ve commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. GitHub üzerinden bir pull request gönderin.🚀

---
Bu projeye katkı sağladığınız için teşekkürler! 😊

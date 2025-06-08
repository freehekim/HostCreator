# 🛡️ HostCreator – Kişisel Reklam ve Takipçi Engelleme Hosts Sistemi

🚀 **HostCreator**, birden fazla reklam engelleyici kaynak listesini birleştirip, sadeleştirilmiş ve optimize edilmiş tek bir `hosts` dosyası üretmek için oluşturulmuş otomatik sistemdir.

---

## 📦 Özellikler

✅ Tüm kaynaklardan günlük olarak verileri çeker  
✅ Yorum satırlarını temizler (`#`)  
✅ `127.0.0.1` adreslerini otomatik olarak `0.0.0.0` ile değiştirir  
✅ Aynı domain için tekrar eden girişleri **tek satıra indirger**  
✅ GitHub Actions ile otomatik güncellenir  
✅ AdAway, AdGuard Home, Pi-hole vb. sistemlerle uyumludur

---

## 🌐 Raw Hosts Linki

Aşağıdaki linki destekleyen sistemlere doğrudan ekleyebilirsin:

```
https://raw.githubusercontent.com/bhcavusoglu/HostCreator/main/hosts
```

---

## 📥 Nasıl Kullanılır?

### 🔸 AdAway için:
1. AdAway uygulamasını aç
2. **Host kaynakları** bölümüne git
3. `+` butonuna bas → şu ayarlarla ekle:
   - **URL**: yukarıdaki link
   - **Tip**: `URL`
   - **Biçim**: `BLOCK`
4. Uygula ve keyfine bak 😎

### 🔸 Pi-hole / AdGuard Home için:
- Custom block list bölümüne yukarıdaki URL’yi yapıştırman yeterli.

---

## 🔁 Güncelleme Sıklığı

🕒 Sistem her gün otomatik olarak güncellenir (saat 04:00 Türkiye saatiyle).  
🔁 Manuel tetiklemek istersen GitHub → **Actions** → `Run workflow` diyebilirsin.

---

## ➕ Kaynak Ekleme

Yeni bir kaynak eklemek için `urls.txt` dosyasına sadece URL’sini eklemen yeterli.  
Otomatik olarak bir sonraki güncellemeye dahil edilir.

---

## 🤝 Katkıda Bulun

PR’lara ve önerilere açığız!  
Whitelist/blacklist desteği, kullanıcı arayüzü ve bildirim sistemleri yakında 🎯

---

## ✨ Hazırlayan

👤 [Hakan](https://github.com/bhcavusoglu)  
📅 Başlangıç: 2025  
🔐 Root kullanıcılar için optimize edilmiştir.

---

📌 **Not:** Bu sistem yalnızca kişisel eğitim ve test amaçlıdır. Ticari kullanım için değildir.

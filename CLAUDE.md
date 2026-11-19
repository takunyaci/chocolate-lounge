# Chocolate Lounge & Coffee — chocolateloungecoffee.com

Tek sayfalık, statik tanıtım sitesi (Çayeli + Ardeşen şubeleri). Build aracı yok.

## Akış
- Düzenleme SADECE `kaynak/sablon.html` üzerinde yapılır, sonra `python3 kaynak/insa.py`
  çalıştırılır → `public/index.html` üretilir. `public/index.html` elle düzenlenmez.
- `main`'e push = otomatik yayın: sunucu (Hetzner 95.217.232.105) 2 dakikada bir
  `/usr/local/bin/chocolate-guncelle` ile repoyu çeker, `public/` → `/var/www/chocolateloungecoffee/`.
- Push sonrası Cloudflare önbelleği eski sürümü tutabilir (HTML için kısa süreli).

## Sunucu (DİKKAT: QR menü sistemiyle aynı sunucu)
- 80/443'ü `qr-menu-nginx` konteyneri tutuyor (/var/www/qr-menu). menu.idrydigital.com ve
  idrydigital.com de orada — iki şubenin menüsü buradan yayınlanıyor, kesinti kabul edilemez.
- nginx ayarı: /var/www/qr-menu/nginx.conf (bizim bloklar: `sunucu/nginx-chocolate.conf`).
  Değişiklikten sonra: `docker exec qr-menu-nginx nginx -t && docker exec qr-menu-nginx nginx -s reload`
- ⚠ `docker-compose` 1.29.2 yeni Docker ile uyumsuz: konteyneri yeniden oluştururken
  `KeyError: 'ContainerConfig'` verip eskiyi DURDURUYOR (19 Kas 2026'da menü 2-3 dk kapandı).
  Konteyner yeniden oluşturmak gerekirse önce `docker rm -f qr-menu-nginx`, sonra `docker-compose up -d --no-deps nginx`.
- SSL: Let's Encrypt (webroot /var/www/certbot), certbot.timer yeniliyor,
  deploy hook `/etc/letsencrypt/renewal-hooks/deploy/reload-qr-menu-nginx.sh` nginx'i reload ediyor.
- DNS: Cloudflare (Proxied, SSL Full strict).

## İçerik kuralları
- Tatlı odaklı (kahve odaklı değil). Ana mesaj: "Sürekli taze sunum", donuk değil sıcak sunum.
- Menü sitede yok; idrydigital menülerine link: Çayeli / Ardeşen ayrı (seçim penceresi).
- Belgeler (`public/belgeler/`): TC kimlik no, karekod ve baba adı MASKELİ. Yeni belge eklerken
  orijinal PDF asla repoya/siteye konmaz; önce TC/karekod maskelenir, gözle kontrol edilir.
- E-posta sayfa kaynağında "@" ile birleşik geçmez ([at] + JS ile kopyalama).
- Logo: `kaynak/logo-ic.svgfrag` (PDF'ten vektör), `<symbol id="logo">` ile kullanılır.

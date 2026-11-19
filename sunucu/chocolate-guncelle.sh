#!/bin/sh
# Sunucuda /usr/local/bin/chocolate-guncelle olarak durur, cron 2 dakikada bir çalıştırır.
# GitHub'daki main dalında yeni commit varsa public/ klasörünü canlı site klasörüne kopyalar.
# Not: Bu dosyanın repodaki hali sadece referanstır; sunucu repodan script ÇALIŞTIRMAZ.
set -e
REPO=/opt/chocolate-lounge
HEDEF=/var/www/chocolateloungecoffee
cd "$REPO"
git fetch -q origin main
YENI=$(git rev-parse origin/main)
ESKI=$(cat "$HEDEF/.surum" 2>/dev/null || true)
[ "$YENI" = "$ESKI" ] && exit 0
git reset -q --hard origin/main
rsync -a --delete --exclude .surum "$REPO/public/" "$HEDEF/"
chmod -R a+rX "$HEDEF"
echo "$YENI" > "$HEDEF/.surum"
logger -t chocolate-guncelle "yayinlandi $YENI"

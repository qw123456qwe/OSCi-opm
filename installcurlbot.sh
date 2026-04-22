#!/bin/bash

echo "🤖 CurlBot o‘rnatilmoqda..."

pip install requests --quiet

BASE="https://raw.githubusercontent.com/qw123456qwe/OSCi-opm/main"

echo "📥 Fayllar yuklanmoqda..."

curl -sSL $BASE/curlbot.py -o curlbot.py
curl -sSL $BASE/context.py -o context.py
curl -sSL $BASE/plugins.py -o plugins.py

echo "🚀 Tayyor!"
echo "👉 ishga tushirish: python botim.py"

#!/bin/bash

echo "🤖 CurlBot o‘rnatilmoqda..."

pip install requests --quiet

echo "📥 curlbot.py yuklanmoqda..."

curl -O https://raw.githubusercontent.com/qw123456qwe/OSCi-opm/main/curlbot/curlbot.py

echo "✅ Tayyor!"
echo ""
echo "👉 Endi o‘zing bot yozasan:"
echo ""
echo "from curlbot import CurlBot"
echo "bot = CurlBot('TOKEN')"
echo "bot.start()"

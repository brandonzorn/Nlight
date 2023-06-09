#!/bin/sh
[ -e package ] && rm -r package
[ -e dist ] && rm -r dist
[ -e Nlight.deb ] && rm -r Nlight.deb

. venv/bin/activate
pyinstaller --noconfirm --windowed --name "Nlight" "main.py"

mkdir -p package/opt
mkdir -p package/usr/share/applications
mkdir -p package/usr/share/icons/hicolor/scalable/apps

cp -r dist/Nlight package/opt/Nlight
cp pkg_res/Nlight.svg package/usr/share/icons/hicolor/scalable/apps/Nlight.svg
cp pkg_res/Nlight.desktop package/usr/share/applications

find package/opt/Nlight -type f -exec chmod 644 -- {} +
find package/opt/Nlight -type d -exec chmod 755 -- {} +
find package/usr/share -type f -exec chmod 644 -- {} +
chmod +x package/opt/Nlight/Nlight

fpm -C package -s dir -t deb -n "nlight" -v 1.9.6 --license mit --depends libxcb-cursor0 --description "Open source manga and ranobe reading application" --url "https://github.com/brandonzorn/Nlight" --architecture native --maintainer "brandonzorn <v.klimenko.2137@gmail.com>" -p dist/Nlight.deb

#!/bin/sh

DEB_FILE=Nlight.deb
RPM_FILE=Nlight.rpm
TAR_FILE=Nlight.tar.zst

[ -e package ] && rm -r package
[ -e dist ] && rm -r dist
[ -e $RPM_FILE ] && rm -r $RPM_FILE
[ -e $TAR_FILE ] && rm -r $TAR_FILE
[ -e $DEB_FILE ] && rm -r $DEB_FILE


. venv/bin/activate
sudo apt install ruby-dev build-essential && sudo gem i fpm -f
pip install -r requirements.txt
pip install pyinstaller

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


function make_package()
{
  local DESCRIPTION="Open source manga and ranobe reading application"
  local URL="https://github.com/brandonzorn/Nlight"
  local MAINTAINER="brandonzorn <v.klimenko.2137@gmail.com>"
  local PACKAGE_TYPE=$1
  local FILE_NAME=$2
  fpm -C package -s dir -t $PACKAGE_TYPE -n "nlight" -p dist/$FILE_NAME --license mit --architecture native --version 1.10.0.5 --description "$DESCRIPTION" --url "$URL" --maintainer "$MAINTAINER"
}

make_package deb $DEB_FILE

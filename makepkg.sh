#!/bin/sh

DEB_FILE = Nlight.deb
RPM_FILE = Nlight.rpm
TAR_FILE = Nlight.tar.zst

[ -e package ] && rm -r package
[ -e dist ] && rm -r dist
[ -e $RPM_FILE ] && rm -r $RPM_FILE
[ -e $TAR_FILE ] && rm -r $TAR_FILE
[ -e $DEB_FILE ] && rm -r $DEB_FILE


. venv/bin/activate
pyinstaller --noconfirm --windowed --name "Nlight" --key "6w9z$C&F)J@NcQfTjWnZr4u7x!A%D*" "main.py"

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


make_package()
{
  FPM_EXECUTABLE_PATH = /home/bzorn/.local/share/gem/ruby/3.0.0/bin/fpm
  DESCRIPTION = "Open source manga and ranobe reading application"
  URL = "https://github.com/brandonzorn/Nlight"
  MAINTAINER = "brandonzorn <v.klimenko.2137@gmail.com>"
  PACKAGE_TYPE = $1
  FILE_NAME = $2
  $FPM_EXECUTABLE_PATH -C package -s dir -t $PACKAGE_TYPE -n "nlight" -v 1.9.9 --license mit --description $DESCRIPTION  --url $URL --architecture native --maintainer @MAINTAINER -p dist/$FILE_NAME
}

make_package deb $DEB_FILE
make_package rpm $RPM_FILE
make_package pacman $TAR_FILE

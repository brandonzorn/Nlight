nuitka ^
  --onefile ^
  --windows-console-mode=disable ^
  --follow-imports ^
  --enable-plugin=pyside6 ^
  --product-version="1.10.4.0" ^
  --file-version="1.10.4.0" ^
  --company-name="brandonzorn" ^
  --product-name="Nlight" ^
  --windows-icon-from-ico="pkg_res/Nlight.ico" ^
  -o "Nlight" ^
  --output-dir=build_nuitka/ ^
  main.py

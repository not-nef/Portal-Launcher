rmdir /Q /S build
rmdir /Q /S dist
pyinstaller src/main.py --onefile --windowed --collect-data sv_ttk
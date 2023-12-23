from cx_Freeze import setup, Executable
import sys

build_exe_options = {
    "include_files": ['icon.ico','customer_page.py','expenses_page.py','invoice_page.py','invoice_products.py',
                        'procurement_page.py','product_page.py','supplier_page.py','images/','bills/','procBills/']
}

executable = Executable(
    script="main_page.py",
    base=None,  # Set to None for a console application or "Win32GUI" for a GUI application
    icon='icon.ico'
)

setup(
    name="biz_buddy",
    version="1.0",
    description="POS and inventory app ",
    options={"build_exe": build_exe_options},
    executables=[executable]
)
base = 'Win32GUI' if sys.platform == 'win32' else None
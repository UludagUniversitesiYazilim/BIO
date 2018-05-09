from cx_Freeze import setup, Executable
import os

executable = Executable( script = "main.py" )
include_files = [r"C:\Program Files\Python36\DLLs\tcl86t.dll",
                 r"C:\Program Files\Python36\DLLs\tk86t.dll"]

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36\tcl\tk8.6'

# Add certificate to the build

setup(
    name = "BIO",
    version = "0",
    options = {"build_exe": {"include_files" :include_files, 
				"includes" : ["queue"],
				"packages":["idna","tkinter", "requests"]}},
	requires = ["requests", "BeautufulSoup4"],
    executables = [executable]
)

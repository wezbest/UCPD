#!/usr/bin/env python3.12

'''
For viewing the bytecode files - 
'''

# For viewing the bytecode
# from uncompyle6.main import decompile
import dis

# Disassembly one


def view_bytecode(file_path):
    with open(file_path, 'rb') as file:
        bytecode = file.read()
        dis.dis(bytecode)


# Example usage:
view_bytecode('tmp/f.pyc')

# Diassembling two


# def decompile_pyc_to_py(pyc_path, py_path):
#     with open(pyc_path, "rb") as pyc_file, open(py_path, "w") as py_file:
#         # The magic number and timestamp are part of the .pyc file header
#         # These need to be read from the file before decompilation
#         magic_number = pyc_file.read(4)
#         pyc_file.read(4)  # Timestamp
#         if hasattr(magic_number, 'hex'):
#             magic_number = int.from_bytes(magic_number, byteorder='little')
#         # The bytecode is everything that follows
#         bytecode = pyc_file.read()
#         # Decompile the bytecode
#         decompile(magic_number, bytecode, py_file)


# Example usage:
# decompile_pyc_to_py('tmp/f.pyc', 'tmp/fdiassemble.py')

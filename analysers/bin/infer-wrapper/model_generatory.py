#!/usr/bin/python

headers = [
    "stdbool.h",
    "alloca.h",
]

types = [
    "bool",
    "short",
    "int",
    "char",
    # "sector_t",
    ("ulong", "unsigned long"),
    ("uchar", "unsigned char"),
    ("ushort", "unsigned short"),
    ("uint", "unsigned int"),
    ("long", "long int"),
    ("ulonglong", "unsigned long long"),
]

with open("models.c", "w") as f:
    for header in headers:
        f.write(f"#include<{header}>\n")

    f.write("\n")
    for t in types:
        if isinstance(t, tuple):
            c_name = t[1]
            sv_name = t[0]
        else:
            c_name = t
            sv_name = t

        f.write(f"{c_name} __VERIFIER_nondet_{sv_name}() {{\n")
        f.write(f"  {c_name} x;\n")
        f.write(f"  return x;\n")
        f.write(f"}}\n\n")

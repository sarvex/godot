"""Functions used to generate source files during build time

All such functions are invoked in a subprocess on Windows to prevent build flakiness.

"""
import os
import os.path
from platform_methods import subprocess_main


def make_fonts_header(target, source, env):
    dst = target[0]

    with open(dst, "w", encoding="utf-8") as g:
        g.write("/* THIS FILE IS GENERATED DO NOT EDIT */\n")
        g.write("#ifndef _DEFAULT_FONTS_H\n")
        g.write("#define _DEFAULT_FONTS_H\n")

            # Saving uncompressed, since FreeType will reference from memory pointer.
        for i in range(len(source)):
            with open(source[i], "rb") as f:
                buf = f.read()

            name = os.path.splitext(os.path.basename(source[i]))[0]

            g.write(f"static const int _font_{name}_size = {len(buf)}" + ";\n")
            g.write(f"static const unsigned char _font_{name}" + "[] = {\n")
            for j in range(len(buf)):
                g.write("\t" + str(buf[j]) + ",\n")

            g.write("};\n")

        g.write("#endif")


if __name__ == "__main__":
    subprocess_main(globals())

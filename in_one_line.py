import re

res = ""
funcs = dict()

VAR_SET_RE = re.compile("""^([\\w]*) = ([\\w\\s:\\(\\)\\=\\-\\+]*)$""")
with open("a.py", "r") as f:
    lines = f.readlines()
    print(len(lines))
    for line in lines:
        line = line.strip()
        # print(repr(line))
        if not line.startswith("#"):
            s = VAR_SET_RE.search(line)
            if s:
                # print(s.group(1), "=", s.group(2))
                new_def = s.group(2)
                for func_name, func_def in funcs.items():
                    new_def = re.sub("""\\b{}\\b""".format(func_name), "({})".format(func_def), new_def)
                # print(s.group(1), "->", new_def)
                funcs[s.group(1)] = new_def
            elif line:
                print("LAL")
                res = line
                for func_name, func_def in funcs.items():
                    res = re.sub("""\\b{}\\b""".format(func_name), "({})".format(func_def), res)
                # print(line, "\n->", res)

print(res)
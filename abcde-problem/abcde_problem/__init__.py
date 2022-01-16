__version__ = "0.1.0"

from os import EX_SOFTWARE

for e in range(10):
    e_str = str(e)
    t_str = e_str + e_str + e_str + e_str + e_str + e_str
    t = int(t_str)

    for a in range(10):
        if a == e:
            continue
        a_str = str(a)
        for b in range(10):
            if b == e or b == a:
                continue
            b_str = str(b)
            for c in range(10):
                if c == e or c == b or c == a:
                    continue
                c_str = str(c)

                for d in range(10):
                    if d == e or d == c or d == b or d == a:
                        continue
                    d_str = str(d)
                    op1_str = a_str + b_str + c_str + d_str + e_str
                    op1 = int(op1_str)
                    result = op1 * a
                    if result == t:
                        print("******** MATCH *********")
                        print(f"{op1} * {a} = {result}")
                        print(f"a = {a}")
                        print(f"b = {b}")
                        print(f"c = {c}")
                        print(f"d = {d}")
                        print(f"e = {e}")
                        break
                    else:
                        pass
                        # print(f"{op1_str} * {a_str} = {result}")

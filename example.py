import BaseX as b
config = {
    0: [64, 2],
    1: [32, 3]
}

EnD = b.B_EnD("ascii", config)

val = EnD.encode("hello")
print(val)
print(EnD.decode(val))
# bytes

s = b"seq"
print(type(s))

# bytearray

s = bytearray("seq", "utf-8")
print(type(s))
s.extend(b"abc")
print(s)
s.append(97)
print(s)

# encoding e decoding

x = "sequenza"
y = x.encode("utf-8")
print(type(y))

z = y.decode("utf-8")
print(type(z))

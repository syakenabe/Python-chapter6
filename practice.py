print("""
        line one
        line two
        line three
        """)

author = "Kafka"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])

print(author[-1])

a = "Cat"
b = " in"
c = " the"
d = " hat"

print(a+b+c+d)

print(a*3)

ex1 = "We hold these truths ...."
print(ex1.upper())

ex2 = "SO IT GOES"
print(ex2.lower())

ex3 = "four score and ...."
print(ex3.capitalize())

print("こんにちは、{}".format("ウィリアム・フォークナー"))

name = "ウィリアム・フォークナー"
print("こんにちは、{}".format(name))

#what = input("何が:")
#when = input("いつ:")
#where = input("どこで:")
#do = input("どうした:")
#r = "{}は{}に{}で{}。".format(what, when, where, do)
#print(r)

ex4 = "水たまりを飛び越えたんだ。3メートルもあったんだぜ！"
print(ex4.split("。"))

first_three = "abc"
result = "+".join(first_three)
print(result)

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = "".join(words)
print(one)

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one = " ".join(words)
print(one)

s = "   the   "
s = s.strip()

equ = "All animals are equal."
equ = equ.replace("a","@")
print(equ)

print("animals".index("m"))

try:
    "animals".index("z")
except:
    print("Not found.")

print("Cat" in "Cat in the hat")
print("Bat" in "Cat in the hat")
print("Bat" not in "Cat in the hat")

print("彼女は\"そうだね\"といった。")
print("彼女は'そうだね'といった。")
print('彼女は"そうだね"といった。')

print("line1\nline2\nline3")

fict = ["トルストイ", "カミュ", "オーウェル", "ハクスリー", "オースティン"]
print(fict[0:3])

ivan = "死の代わりにひとつの光があった。"
print(ivan[0:6])
print(ivan[6:16])
print(ivan[:6])
print(ivan[6:])
print(ivan[:])

# ticket = 123456
# print((" ".join(str(ticket)[:3])).split(" "))



x = "880005553535-перевод:100"
t = (" ".join(x.split("-"))).split(":")
print(t[0].split(" ")[1])
print(t)
print(int(t[1]))

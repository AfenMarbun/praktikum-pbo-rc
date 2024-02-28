biodata = '''Nama : Rustian Afencius Marbun
NIM : 122140155
Resolusi Saya di Tahun ini : Upgrade programming skill'''

with open("Me.txt", "w") as file:
    file.write(biodata)

with open("Me.txt", "r") as file:
    content = file.read()
    print(content)

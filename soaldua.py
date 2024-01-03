def common_letter(kata: str):
  # Menghitung frekuensi kemunculan setiap huruf dalam kata
  jumlah_huruf = {}

  for huruf in kata:
    jumlah_huruf[huruf] = jumlah_huruf.get(huruf, 0) + 1

  # Mengembalikan huruf dengan frekuensi kemunculan tertinggi
  return "Huruf yang sering muncul \"" + max(jumlah_huruf, key=jumlah_huruf.get) + "\" dari kata \"" + kata + "\""

print(common_letter("Hello kamoo"))
print(common_letter("Hello"))


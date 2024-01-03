def check_palindrom(kata: str):
  # Menghapus spasi dan karakter non-alfabet
  kata = "".join(c for c in kata if c.isalnum()).lower()

  # Membalik kata, awal. akhir/sejumlah. -1 dibalik
  reversed_word = kata[::-1]

  # Membandingkan kata asli dengan kata yang dibalik
  return kata.capitalize() + (" Palindrom" if kata == reversed_word else " Bukan Palindrom")

print(check_palindrom("Hello"))
print(check_palindrom("level"))

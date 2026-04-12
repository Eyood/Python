import random
print("Game tebak angka rahasia dengan custom range")
lowest = int(input("Masukkan range terkecil: "))
highest = int(input("Masukkan range terbesar: "))
if highest < lowest:
  print("Pastikan nilai range terbesar lebih besar dari range terkecil =_=")
if highest >= lowest:
  number = random.randint(lowest, highest)
  game = "berjalan"
  guess_count = 0
  score = highest - lowest + 1
  while game == "berjalan":
    print(f"Tebak angka {lowest} sampe {highest}\n")
    guess = int(input("Masukkan angka rahasia: "))
    guess_count += 1
    print("========================================")
    if guess < number:
      print(f"\nangka rahasia lebih besar dari {guess}")
    elif guess > number:
      print(f"\nangka rahasia lebih kecil dari {guess}")
    else:
      final_score = str(score / guess_count)
      print(f"\nSelamat, {guess} adalah angka rahasia nya, anda mendapatkan {final_score} poin")
      try:
        with open("score.txt", "a") as file:
          file.write(f"\n{final_score}")
        with open("score.txt", "r") as file:
          lines = file.readlines()
          score_total = sum(float(line.strip()) for line in lines[1:])
          lines[0] = str(score_total) + "\n"
        with open("score.txt", "w") as file:
          file.writelines(lines)
          score_total = sum(float(line.strip()) for line in lines[1:])
          lines[0] = str(score_total) + "\n"
          print(f"Total poin anda adalah {score_total}\n\n========================================")
          break
      except FileNotFoundError:
        with open("score.txt", "w") as file:
          file.write(f"\n{final_score}")
          print(f"Total poin anda adalah {final_score}\n\n========================================")
          break

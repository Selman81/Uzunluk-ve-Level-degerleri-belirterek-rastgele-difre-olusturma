import random
import string
def generate_password(length, level, output=[]):
    chars = string.ascii_letters

    if level > 1:
        chars = "{}{}".format(chars, string.digits)

    if level > 2:
        chars = "{}{}".format(chars, string.punctuation)

    for i in range(length):
        output.append(random.choice(chars))

    return "".join(output)

print(("-" * 30) + "\n Rastgele Şifre Oluşturucu \n" + ("-" * 30))

password_length = int(input("Uzunluk Ne Kadar Olsun ? : "))

password_level = int(input("Şiddeti Kaç Olsun ? : "))

password = generate_password(password_length, password_level)

print("\nSenin İçin Oluşturulmuş Şifre : {}".format(password))
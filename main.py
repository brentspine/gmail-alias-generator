"""
  ===========================================
  GMAIL ALIAS GENERATOR
  Free to use, copy only with credit

  Replit:      https://replit.com/@brentspine/GenerateGmailAliases
  GitHub:      https://github.com/brentspine/gmail-alias-generator
  License:     https://github.com/brentspine/gmail-alias-generator/blob/main/LICENSE

  Made by:     Brentspine
  Year:        2024
  Website:     https://brentspine.de
  Mail:        brentspine.dev (át) gmail.com
  Twitter:     @brentspine
  Instagram:   @brentspine
  ===========================================
"""

from itertools import product
import random
import string
import time
import os

#Config
max_dot_percentage = 0.43
min_scramble_length = 7
max_scramble_length = 12
do_plus_scramble = True


def on_exit():
  print(" ")
  print("Goodbye!")
  exit()


def print_license(upper_hr=True, lower_hr=True):
  if upper_hr:
    print("=" * 35)
  print("\033[1mGMAIL ALIAS GENERATOR\033[0m")
  print("Free to use, copy only with credit")
  print("Made by:     Brentspine")
  print("Year:        2024")
  print("Website:     https://brentspine.de")
  print("Mail:        brentspine.dev (át) gmail.com")
  print("Twitter:     @brentspine")
  print("Instagram:   @brentspine")
  if lower_hr:
    print("=" * 35)


def gen_plus_alias():
  email_provider = "@googlemail.com" if random.randint(
      1, 3) == 1 else "@gmail.com"
  return user_original + "+" + rchar(
      random.randint(min_scramble_length,
                     max_scramble_length)) + email_provider


def rchar(a):
  r = ""
  characters = string.ascii_letters + "1234567890"
  for _ in range(a):
    r += random.choice(characters)
  return r


def gen_all_patterns(l):
  combinations = list(product([0, 1], repeat=l))
  return combinations


while True:
  print("Please enter a valid gmail address (Keep empty for example)")
  address = input("")
  address = "example.mail@gmail.com" if len(address) <= 0 else address

  if "@gmail.com" not in address and "@googlemail.com" not in address:
    print("Invalid gmail address\n")
    continue
  user_original = address.split("@")[0]
  user = address.split("@")[0].replace(".", "")
  domain = "@" + address.split("@")[1].replace("@googlemail.com", "@gmail.com")
  if len(user) <= 2:
    print("Invalid gmail address\n")
    continue

  addresses = []
  all_patterns = gen_all_patterns(len(user) - 1)
  for pattern in all_patterns:
    r = user[0]
    i = 0
    dots = 0
    for c in pattern:
      if c == 1:
        dots += 1
    if dots / (len(user) - 2) >= max_dot_percentage:
      continue
    for c in pattern:
      i += 1
      if c == 0:
        r += user[i]
        continue
      r += "." + user[i]
    # print(r+domain + "         " + str(pattern))
    addresses.append(r + domain)
    addresses.append(r + "@googlemail.com")

  if do_plus_scramble:
    for i in range(len(addresses)):
      addresses.insert((i * 2) + 1, gen_plus_alias())

  for caddress in addresses:
    print(caddress)
  print(" ")

  print_license()

  print(" ")
  print("Generated " + str(len(addresses)) + " addresses that forward to " +
        address)
  print("Longer addresses will result in more aliases")
  print(" ")
  time.sleep(2)

  while True:
    print("=" * 35)
    print("0 - How does it work?")
    print("1 - Generate more aliases")
    print("2 - Generate aliases for another address")
    print("3 - Export to file")
    print("4 - Print all generated addresses")
    print("5 - Exit program")
    print("6 - License")
    print("=" * 35)
    option = input("Please select an option: ").replace(" ", "")

    if option == "0":
      print("")
      print("You can generate aliases for your Gmail address in multiple ways")
      print("Here are the 3 options this program uses")
      print(" ")
      print("\033[1mAdding dots in between the username\033[0m")
      print(
          " -> When receiving mails, Google removes all dots from your address"
      )
      print(
          " -> This is why we can add random dots accross the address to \"scramble it\""
      )
      print(" -> In this case we have the following rules")
      print(
          "     - Don't add dots at the beginning or end and only before the @ sign"
      )
      print("     - Don't surpass the threshold of " +
            (str(max_dot_percentage)).replace("0.", "").replace("0,", "") +
            " % dots")
      print("     - Don't have 2 dots in a row (exam..ple@gmail.com)")
      print(
          " -> Example: exam.plema.il@gmail.com forwards to example.mail@gmail.com"
      )
      print(" ")
      print("\033[1mAlternating between domains\033[0m")
      print(" -> @gmail.com and @googlemail.com are basically the same")
      print(" -> We can still use both addresses on one service")
      print(" -> Meaning we essentially double our alias amount")
      print(
          " -> Example: example.mail@googlemail.com forwards to example.mail@gmail.com"
      )
      print("")
      print("\033[1mAdding a + at the end of our username\033[0m")
      print(" -> Gmail also has a built-in functionality for alias generation")
      print(
          " -> We can add a + sign at the end of our username and everything between it and the @ will be ignored"
      )
      print(
          " -> Example: example.mail+g34d@gmail.com forwards to example.mail@gmail.com"
      )
      print(" ")
      print("\033[1mExamples\033[0m")
      print(
          " -> e.xamp.lemai.l+89dfgascb@googlemail.com forwards to example.mail@gmail.com"
      )
      print(
          " -> m.y.c.ooladdres.s+xyz69@gmail.com forwards to my.cool.address@gmail.com"
      )
      print("")
      print("Press enter to continue")
      input("")

    elif option == "1":
      inp_amount = 0
      while True:
        inp_amount = input("Please select the amount: ")
        try:
          inp_amount = int(inp_amount)
        except ValueError:
          print("")
          print("Not an integer, try again!")
          continue
        if inp_amount >= 999999:
          print("")
          print("Choose something smaller!")
        elif inp_amount <= 0:
          print("")
          print("Please generate at least one more alias...")
        else:
          break
      for i in range(inp_amount):
        addresses.append(gen_plus_alias())
      print("")
      print("Appended " + str(inp_amount) + " additionally aliases")
      print("")
      time.sleep(0.5)
    elif option == "2":
      doit = False
      while True:
        print("This will wipe all addresses, continue? (y/n)")
        inp = input("")
        if inp == "n":
          break
        if inp != "y":
          print("Try again...")
          continue
        doit = True
        break
      if not doit:
        print("")
        continue
      print(" ")
      print(" ")
      break

    elif option == "3":
      print("What should the output file be called?")
      path_inp = input()
      if not path_inp.endswith(".txt"):
        path_inp += ".txt"
      file_path = path_inp.replace("/", "").replace("\\", "").replace("\n", "")
      mode = "w"
      if os.path.exists(file_path):
        while True:
          print(
              "File already exists, do you want to append or overwrite? (a/w)")
          mode = input("")
          if mode != "a" and mode != "w":
            print("Try again...")
            continue
          mode_string = "append" if mode == "a" else "write"
          print("Using " + mode_string + " mode")
          break
      with open(file_path, mode) as file:
        for c in addresses:
          file.write("%s\n" % c)
      print("Successfully saved to " + file_path)
      print("")

    elif option == "4":
      for caddress in addresses:
        print(caddress)
      print("")
      print("In total " + str(len(addresses)) + " addresses that forward to " +
            address)
      print("")
      time.sleep(2)

    elif option == "5":
      on_exit()
    elif option == "6":
      print("")
      print_license()
      time.sleep(2)
      print(" ")
    else:
      print("Option not found...")
      time.sleep(1)

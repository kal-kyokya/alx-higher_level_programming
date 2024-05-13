#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Dj", "Mère")
say_my_name("Alliance", "Soeur")
say_my_name("The", "Dem")
say_my_name("Matutina", "Stella")

try:
    say_my_name(6, "god")
except Exception as err:
    print(err)

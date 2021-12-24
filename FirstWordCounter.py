# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 00:39:02 2021

@author: BusraA
"""
textBox = input("Please write a text. We will count of the words.\n")
choice = int(input("1 - Counting letters \n2 - Counting words\n3 - Both of them.\n"))
letters = list(textBox)
words = list(textBox.split())

if choice == 1:
    print(len(letters))
elif choice == 2:
    print(len(words))
elif choice == 3:
    print("Numbers of letters: "+ str(len(letters)) + "\nNumbers of words: "+str(len(words)))
else:
    print("Invalid choice.")
#!/usr/bin/env python
#-*- coding:utf-8 -*-


sayi1 = input("1. sayı: ")
sayi2 = input("2. sayı: ")
islem = raw_input("İşlemi giriniz (+,-,*,/): ")
if islem == "+":
 sonuc = sayi1 + sayi2
 print "sonuç = ", sonuc
 
elif islem == "-":
 sonuc = sayi1 - sayi2
 print "sonuç= ", sonuc

elif islem == "*":
 sonuc = sayi1 * sayi2
 print "sonuç= ", sonuc

elif islem == "/" and sayi2 != 0::
 sonuc = sayi1 / sayi2
 print "sonuç= ",sonuc

else:
 print "Hatalı giriş yaptınız!"
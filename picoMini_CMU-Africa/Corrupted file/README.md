# Corrupted file
## Category: Forensics, picoMini by CMU-Africa, browser_webshell_solvable
### Author: Yahaya Meddy

### Description
This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?
Download the file <a href="https://challenge-files.picoctf.net/c_amiable_citadel/8646393bf40c0026e51065e57963b604edf0a9a73371e01d1af2865c050d3e68/file">here</a>.

### Write-Up
Jadi kita diberikan sebuah file yang rusak. Ketika dicek menggunakan xxd hasilnya serperti ini kurang lebih

```
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/forensicpicoCTF/Corruptedfile]
└─$ xxd file | head -10
00000000: 5c78 ffe0 0010 4a46 4946 0001 0100 0001  \x....JFIF......
00000010: 0001 0000 ffdb 0043 0008 0606 0706 0508  .......C........
00000020: 0707 0709 0908 0a0c 140d 0c0b 0b0c 1912  ................
00000030: 130f 141d 1a1f 1e1d 1a1c 1c20 242e 2720  ........... $.' 
00000040: 222c 231c 1c28 3729 2c30 3134 3434 1f27  ",#..(7),01444.'
00000050: 393d 3832 3c2e 3334 32ff db00 4301 0909  9=82<.342...C...
00000060: 090c 0b0c 180d 0d18 3221 1c21 3232 3232  ........2!.!2222
00000070: 3232 3232 3232 3232 3232 3232 3232 3232  2222222222222222
00000080: 3232 3232 3232 3232 3232 3232 3232 3232  2222222222222222
00000090: 3232 3232 3232 3232 3232 3232 3232 ffc0  22222222222222..
```
Ada yang menarik di headernya, yaitu signature untuk JFIF file. Tapi sebenarnya ini hanyalah sebuah masalah magic bytes yang tidak tepat. Contoh jika kita download sample image jfif maka ketika kita cek hasil headernya seperti ini

```
└─$ xxd sample1.jfif| head -10
00000000: ffd8 ffe0 0010 4a46 4946 0001 0100 0001  ......JFIF......
00000010: 0001 0000 ffdb 0043 0003 0202 0302 0203  .......C........
00000020: 0303 0304 0303 0405 0805 0504 0405 0a07  ................
00000030: 0706 080c 0a0c 0c0b 0a0b 0b0d 0e12 100d  ................
00000040: 0e11 0e0b 0b10 1610 1113 1415 1515 0c0f  ................
00000050: 1718 1614 1812 1415 14ff db00 4301 0304  ............C...
00000060: 0405 0405 0905 0509 140d 0b0d 1414 1414  ................
00000070: 1414 1414 1414 1414 1414 1414 1414 1414  ................
00000080: 1414 1414 1414 1414 1414 1414 1414 1414  ................
00000090: 1414 1414 1414 1414 1414 1414 1414 ffc0  ................
```
terlihat untuk start imagenya berbeda di 2 bytes awal. ini juga sejalan dengan deskripsi challenge "Maybe a couple of bytes could make all the difference." jadi kita coba sesuaikan start bytesnya dan cek hasilnya

Disini aku menggunakan hexedit online dan aku mengubah dua bytes awal menjadi ffd8. setelah itu coba save as dan cek hasilnya
<img width="872" height="806" alt="image" src="https://github.com/user-attachments/assets/b8de4cab-ba19-45f9-9bd7-5c29e286cac5" />

Terlihat kita berhail mengubahnya menjadi sebuah standard wrapper untuk JPEG image dan sekarang sudah bisa kita buka

```
─$ file recover.jfif 
recover.jfif: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 800x500, components 3
```

Dan kita mendapatkan sebuah flag dari gambar ini: picoCTF{r3st0r1ng_th3_by73s_939a65f5}
<img width="1787" height="797" alt="image" src="https://github.com/user-attachments/assets/09041711-23af-45a8-a885-29ea2d4b58b3" />

**Flag: picoCTF{r3st0r1ng_th3_by73s_939a65f5}**

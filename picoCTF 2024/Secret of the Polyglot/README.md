# Secret of the Polyglot
## Category: Easy, Forensics, picoCTF 2024, shell, browser_webshell_solvable, qr_code 
### AUTHOR: JEFFERY JOHN

### Description
The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?
Download the suspicious file <a href="https://artifacts.picoctf.net/c_titan/98/flag2of2-final.pdf">here</a>.

### Write-Up
Di challenge kali ini kita mendapatkan sebuah file pdf yang ketika dibuka mendapatkan potongan flag: 1n_pn9_&_pdf_1f991f77}. Jadinya kita perlu cari satu potongan lagi. Ketika kita cek raw hex dari file ini

Kita tau kalau ini adalah signature dari PNG file. Tapi ketika di cek lebih dalam, kita mendapati adanya signature pdf juga
```
└─$ xxd flag2of2-final.pdf | head -10
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0032 0000 0032 0806 0000 001e 3f88  ...2...2......?.
00000020: b100 0001 8569 4343 5049 4343 2070 726f  .....iCCPICC pro
00000030: 6669 6c65 0000 2891 7d91 3d48 c340 1cc5  file..(.}.=H.@..
00000040: 5f53 a5a2 1511 3b88 0866 a80e 6241 54c4  _S....;..f..bAT.
00000050: 51ab 5084 0aa1 5668 d5c1 e4d2 2f68 d290  Q.P...Vh..../h..
00000060: a4b8 380a ae05 073f 16ab 0e2e ceba 3ab8  ..8....?......:.
00000070: 0a82 e007 88ab 8b93 a28b 94f8 bfa4 d022  ..............."
00000080: d683 e37e bcbb f7b8 7b07 08d5 22d3 acb6  ...~....{..."...
00000090: 7140 d36d 3311 8b8a a9f4 aa18 7845 1704  q@.m3.......xE..
```

```
00000390: 6082 2550 4446 2d31 2e34 0a25 c7ec 8fa2  `.%PDF-1.4.%....
000003a0: 0a25 2549 6e76 6f63 6174 696f 6e3a 2070  .%%Invocation: p
000003b0: 6174 682f 6773 202d 502d 202d 6453 4146  ath/gs -P- -dSAF
000003c0: 4552 202d 6443 6f6d 7061 7469 6269 6c69  ER -dCompatibili
000003d0: 7479 4c65 7665 6c3d 312e 3420 2d71 202d  tyLevel=1.4 -q -
000003e0: 502d 202d 644e 4f50 4155 5345 202d 6442  P- -dNOPAUSE -dB
000003f0: 4154 4348 202d 7344 4556 4943 453d 7064  ATCH -sDEVICE=pd
00000400: 6677 7269 7465 202d 7373 7464 6f75 743d  fwrite -sstdout=
00000410: 3f20 2d73 4f75 7470 7574 4669 6c65 3d3f  ? -sOutputFile=?
00000420: 202d 502d 202d 6453 4146 4552 202d 6443   -P- -dSAFER -dC
00000430: 6f6d 7061 7469 6269 6c69 7479 4c65 7665  ompatibilityLeve
00000440: 6c3d 312e 3420 3f0a 3520 3020 6f62 6a0a  l=1.4 ?.5 0 obj.
00000450: 3c3c 2f4c 656e 6774 6820 3620 3020 522f  <</Length 6 0 R/
00000460: 4669 6c74 6572 202f 466c 6174 6544 6563  Filter /FlateDec
00000470: 6f64 653e 3e0a 7374 7265 616d 0a78 9c2b  ode>>.stream.x.+
```

Jika raw data dari png dan pdf digabung, itu tidak akan rusak, selama pdf signature masih masuk di dalam 1024 byte pertama file. PDF parser itu membaca file dari bawah ke atas. Karena itu ketika kita ubah file ini menjadi ekstensi png, maka kita bisa melihat gambar. Sedangkan ketika ekstensinya pdf, maka computer akan membuka tools pdf dan membaca datanya sebagai pdf

**Flag: picoCTF{f1u3n7_1n_pn9_&_pdf_1f991f77}**

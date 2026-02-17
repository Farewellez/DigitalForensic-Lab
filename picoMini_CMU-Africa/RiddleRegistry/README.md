# Riddle Registry
## Category: Easy, Forensic, picoMini By CMU-Africa, brwoser_webshell_solveable
### Author: Prince Niyonshuti N.

### Description
Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not <br>
everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered. <br>
Find the PDF file here <a href="https://challenge-files.picoctf.net/c_amiable_citadel/aa8b61ad4587052b730bc07906352e33d5a803f25708e2c8c115147039541a76/confidential.pdf">Hidden Confidential Document</a> and uncover the flag within the metadata.

### Write-Up
Di challenge ini aku langsung buka pdf pake libre-office karena aku pake linux. Tapi isinya kaya gini

<img width="1380" height="872" alt="image" src="https://github.com/user-attachments/assets/df783771-add8-41cb-bf7e-30a7e3e26311" />

Anjay, gampang bet pikirku. Karena aku kira isi dari stream content yang disembunyikan itu adalah potongan flag, tapi waktu aku copy-paste isinya seperti ini

```
dapibus posuere velit aliquet. Aenean lacinia bibendum nulla sed consectetur. Fusce dapibus, 
risus. Curabitur blandit tempus porttitor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
The author have done a great and good job 
No flag here. Nice try though!
```
Ternyata hanya red herring, tapi waktu aku cek lagi petunujuk di pdf ada kata ini

```
If you're still reading this, I’ll tell you a secret: the answer might not be here after all... 
```
Jadi kemungkinan aku perlu coba oprec lebih dalam, di sini aku dapat base64 encoded text dengan strings commands

```
┌──(w4llnut_07㉿kali)-[~/…/CTF/Platform/forensicpicoCTF/RiddleRegistry]
└─$ strings confidential.pdf | head -20
%PDF-1.7
1 0 obj
/Type /Pages
/Count 1
/Kids [ 4 0 R ]
endobj
2 0 obj
/Producer (PyPDF2)
/Author (cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0\075)
endobj
3 0 obj
/Type /Catalog
/Pages 1 0 R
endobj
4 0 obj
/Type /Page
/Resources <<
/Font <<
/F1 5 0 R
/F2 8 0 R
```
yaitu metadata dari author, kalau kita decode maka hasilnya adalah picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}

**Flag: picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}**

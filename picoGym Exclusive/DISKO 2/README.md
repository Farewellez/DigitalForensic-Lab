# DISKO 2
## Category: Medium, Forensics, picoGym Exclusive
### Author: Darkraicg492

### Description
Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone!
Download the disk image <a href="https://artifacts.picoctf.net/c/540/disko-2.dd.gz">here</a>.

### Write-Up
Jadi kita cukup berpatok pada kalimat "The right one is Linux!". Ketika kita cek filenya dengan binwalk kita tahu ini adalah 1 image disk utuh dan bukan partisi dari suatu image. Jadi kita harus menggunalan "mmls" terlebih dahulu untuk melihat partisi dari image ini

```
└─$ binwalk3 disko-2.dd

                                                                                                               /tmp/disko-2.dd
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DECIMAL                            HEXADECIMAL                        DESCRIPTION
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
0                                  0x0                                DOS Master Boot Record, partition: Linux, partition: FAT32, image size: 60817408 bytes
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

Dari isni kita tahu kalau tabel partisi linux memiliki start: 0000002048 dan end: 0000053247. Karena sudah dapat offsetnya, sekarang kita bisa extract offset tersebut dengan "dd" command
```
┌──(w4llnut_07㉿kali)-[/tmp]
└─$ mmls disko-2.dd
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000053247   0000051200   Linux (0x83)
003:  000:001   0000053248   0000118783   0000065536   Win95 FAT32 (0x0b)
004:  -------   0000118784   0000204799   0000086016   Unallocated

└─$ dd if=disko-2.dd of=partisi_linux.img bs=512 skip=2048 count=51200
51200+0 records in
51200+0 records out
26214400 bytes (26 MB, 25 MiB) copied, 0.117401 s, 223 MB/s
```

setelah kita dapat tabel partisi linuxnya, sekarang kita hanya perlu strings dan grep flag format untuk chall ini yaitu picoCTF

```
└─$ strings partisi_linux.img | grep -i "pico"                        
picoCTF{4_P4Rt_1t_i5_a93c3ba0}
piconv
_ZN13QsciScintilla10apiContextEiRiS0_
:/icons/appicon
piconv
piconv
piconv
# $Id: piconv,v 2.8 2016/08/04 03:15:58 dankogai Exp $
piconv -- iconv(1), reinvented in perl
  piconv [-f from_encoding] [-t to_encoding]
  piconv -l
  piconv -r encoding_alias
  piconv -h
B<piconv> is perl version of B<iconv>, a character encoding converter
a technology demonstrator for Perl 5.8.0, but you can use piconv in the
piconv converts the character encoding of either STDIN or files
Therefore, when both -f and -t are omitted, B<piconv> just acts
```

**Flag: picoCTF{4_P4Rt_1t_i5_a93c3ba0}**

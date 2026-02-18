# Verify
## Category: Easy, Forensic, picoCTF 2024, grep, browser_webshell_solveable, checksum

### Author: Jeffery John

### Description
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.
Additional details will be available after launching your challenge instance. 

### Write-Up
Jadi di sini kasus forensicnya sedikit berbeda seperti sebelumnya dan kita diberikan sebuah ip untuk connect via ssh

```
-─$ ssh -p 59721 ctf-player@rhea.picoctf.net

The authenticity of host '[rhea.picoctf.net]:59721 ([3.136.191.228]:59721)' can't be established.
ED25519 key fingerprint is: SHA256:QKdv+RGJL0UYRDM66IiGQ5dsXOX7DQFqB7umTylh+IU
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:6: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[rhea.picoctf.net]:59721' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
ctf-player@rhea.picoctf.net's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.8.0-1021-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ ls
checksum.txt  decrypt.sh  files
```
ketika kita cek isi dari checksum.txt kita akan dapat sebuah checksum untuk sebuah file: b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2 dan isi dari direktori files, berisi banyak sekali file palsu dan ada 1 file asli yang harus disamakan checksumnya. kita bisa pakai teknik pipe dan grep untuk menyesuaikan checksum yang benar

```
ctf-player@pico-chall$ find ./files/ -type f -exec sha256sum {} + | grep "b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2"
b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2  ./files/451fd69b
```

Setelah dapat file yang benar, yaitu ./files/451fd69b kita bisa gunakan script decrypt yang sudah disediakan server

```
ctf-player@pico-chall$ ./decrypt.sh ./files/451fd69b
picoCTF{trust_but_verify_451fd69b}
```
**Flag: picoCTF{trust_but_verify_451fd69b}**

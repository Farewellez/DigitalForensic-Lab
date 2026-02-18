# Ph4nt0m 1ntrud3r
## Category: Easy, Forensic, picoCTF 2025, browser_webshell_solveable
### Author: Prince Niyonshuti N.

### Description
A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.
To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!
Find the PCAP file here Network Traffic PCAP file and try to get the flag.

### Write-up
Sebenarnya tanpa membuka wireshark dan modal strings, kita bisa dapat flag yang diencode dengan algoritma base64

```
└─$ strings myNetworkTraffic.pcap                
X5w4OZo=:
H7DUfjk=:
ob0o5i0=:
y50ZdmI=:
y1vZtpY=:
hBFmx3U=:
b0gkDEE=:
fQ==:
cGljb0NURg==:
8WXUPlw=:
KWH98Vc=:
kpRM1Ck=:
ZTEwZTgzOQ==:
6dmdW8U=:
XzM0c3lfdA==:
FNoN3tc=:
bnRfdGg0dA==:
LJzhGLY=:
tXcY/Ew=:
YmhfNHJfOA==:
ezF0X3c0cw==:
FUiWx28=
```
beberapa itu adalah string sampah tapi beberapa lagi itu potongan flag

```
X5w4OZo=: _.89.
fQ==: }
cGljb0NURg==: picoCTF
ZTEwZTgzOQ==: e10e839
XzM0c3lfdA==: _34sy_t
bnRfdGg0dA==: nt_th4t
YmhfNHJfOA==: bh_4r_8
ezF0X3c0cw==: {1t_w4s
```
**Flag: picoCTF{1t_w4snt_th4t_34sy_tbh_4r_8e10e839}**

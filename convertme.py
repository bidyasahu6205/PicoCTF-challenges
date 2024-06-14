Description
Run the Python script and convert the given number from decimal to binary to get the flag.
Download Python script

diva_bs-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/24/convertme.py
--2024-06-14 00:49:08--  https://artifacts.picoctf.net/c/24/convertme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.128, 3.160.22.16, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1189 (1.2K) [application/octet-stream]
Saving to: 'convertme.py'

convertme.py           100%[===========================>]   1.16K  --.-KB/s    in 0s      

2024-06-14 00:49:08 (654 MB/s) - 'convertme.py' saved [1189/1189]

diva_bs-picoctf@webshell:~$ ls
README.txt  convertme.py
diva_bs-picoctf@webshell:~$ python convertme.py 
If 79 is in decimal base, what is it in binary base?
Answer: 1001111
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_722f6b39}


Here we run the python file and answer a question to get the flag
wget - download the file from the internet via link.
python file_name - used this syntax to run the python file.
then we converts the 79 (base 10 i.e decimal) to 1001111 (base 2 i.e binary)

we can use a online converter or do it manually 
64 32 16 8 4 2 1
1  0  0  1 1 1 1

64+32+16+8+4+2+1 = 79

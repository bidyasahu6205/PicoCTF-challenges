Description
Run the runme.py script to get the flag. Download the script with your browser or with wget in the webshell.
Download runme.py Python script

diva_bs-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/34/runme.py
--2024-07-27 05:18:42--  https://artifacts.picoctf.net/c/34/runme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.16, 3.160.22.128, 3.160.22.92, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.16|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: 'runme.py'

runme.py               100%[===========================>]     270  --.-KB/s    in 0s      

2024-07-27 05:18:42 (101 MB/s) - 'runme.py' saved [270/270]

diva_bs-picoctf@webshell:~$ ls
README.txt  runme.py
diva_bs-picoctf@webshell:~$ python runme.py 
picoCTF{run_s4n1ty_run}
diva_bs-picoctf@webshell:~$ 

- In this challenge we were supposed to run the python scrip that was given
- To run a python file we give a command
      python python_file_name
and tada we found the flag.

# SMS-BOMBER
pip3 install -r requirements.txt

# SETUP FOR WINDOWS

<b> STEPS</b></br>
1. Download Windows Expert Bundle from the following link:<br/>
https://www.torproject.org/download/tor/
2. Unzip the <b>Tor</b> folder and place it in the root of drive <b>C</b>
3. Open the <b>Command Prompt</b> or <b>Windows Powershell</b> as <b>Administator</b> and type <b>echo( > C:\Tor\torrc</b>
4. Now generate a hashed password by typing tor <b>--hash-password <<i>your password</i></b>>
5. Open the <b>C:\Tor\torrc</b> file in your favourite text editor and paste following lines:<br/> <b>ControlPort 9051</b><br/><b>HashedControlPassword <<i>your generated hash</i>></b>
  
6. Lastly, type <b>C:\Tor\tor.exe --service install -options -f "C:\Tor\torrc"</b>



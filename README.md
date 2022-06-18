# SMS-BOMBER
pip3 install -r requirements.txt

<h2>SETUP FOR WINDOWS</h2>

<b> STEPS</b></br>
1. Download <b>Windows Expert Bundle</b> from the following link:<br/>
https://www.torproject.org/download/tor/
2. Unzip the <b>Tor</b> folder and place it in the root of drive <b>C</b>
3. Open the <b>Command Prompt</b> or <b>Windows Powershell</b> as <b>Administator</b> and type <b>echo( > C:\Tor\torrc</b>
4. Now generate a hashed password by typing <b>C:\Tor\tor.exe --hash-password <<i>your password</i></b>>
5. Open the <b>C:\Tor\torrc</b> file in your favourite text editor and paste following lines:<br/> <b>ControlPort 9051</b><br/><b>HashedControlPassword <<i>your generated hash</i>></b>
  
6. Lastly, type <b>C:\Tor\tor.exe --service install -options -f "C:\Tor\torrc"</b>

<h2>SETUP FOR LINUX</h2>

<b> STEPS</b></br>
1. Type <b>sudo apt update && sudo apt upgrade && sudo apt install tor</b> in terminal.
2. Start the tor service by typing <b>sudo service tor start</b>
3. Now generate a hashed password by typing <b>tor --hash-password <<i>your password</i></b>>
4. Type <b>nano /etc/tor/torrc</b> and uncomment the <b>ControlPort 9051 and HashedControlPassword <<span>paste the generated hash></span></b> lines and save it.
5. At last, type <b>sudo service tor restart</b>

<h2>SETUP FOR TERMUX</h2>

<b> STEPS</b></br>
1. Type <b>apt update && apt upgrade && apt install tor && apt install termux-services</b> in termux.
3. Restart your shell and type <b>sv up tor</b>
4. Now generate a hashed password by typing <b>tor --hash-password <<i>your password</i></b>>
5. Type <b>nano $PREFIX/etc/tor/torrc</b> and uncomment the <b>ControlPort 9051 and HashedControlPassword <<span>paste the generated hash></span></b> lines and save it.
6. Finally, type <b>sv restart tor</b>

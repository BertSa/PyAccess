## Installation
`sudo apt-get install xclip`

`sudo visudo`

`echo $1 | sudo tee /sys/module/hid_apple/parameters/fnmode`

Check if exist
`find /sys/module/hid_apple/parameters/fnmode`
```bash
#monitor
pacmd set-default-source 1
#built-in mic
pacmd set-default-source 2
```
```bash
nohup python /home/<username>/tray.py &
```
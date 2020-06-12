# how_to_keep_a_spinner_spinning
https://www.youtube.com/watch?v=ez-7cllNlLA

## installation

You need to install following packages :

```
sudo apt install python3-pip
sudo apt install python3-opencv
pip3 install picamera
sudo apt-get install python3-rpi.gpio
sudo apt-get install libatlas-base-dev

```
### Stuff you might want to do
Optionnaly, you can install vim :

```sudo apt install vim```

I also installed a ftp, as it was the easiest way for me to get images sample
```
sudo apt install proftpd
```
You then have to edit the config file :
```
sudo vim /etc/proftpd/proftpd.conf
```
-> uncomment 'DefaultRoot' line

### Back to set up
You have to check that your raspberry camera is on :
```
sudo raspi_config
```

Then chose  5.Interfacing option, and then P1 Camera (reboot may be needed)

### pluging camera and motor

see setup.jpg

### Check if code is working

once you cloned the repository, you can separately try the camera and the motor with
```
python3 camera.py
sudo python3 motor.py
```
camera.py should create img0.png and img1 png in curent directory

## executing main script

```
 sudo pyhon3 machine_v1.py
```

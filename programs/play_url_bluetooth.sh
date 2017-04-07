#!/bin/bash
# play_url_bluetooth.sh: Play a mp3 file that comes from a URL
#                        thought a Bluetooth Speaker
play() { 
   MPLAYER=/var/packages/AudioStation/target/bin/mplayer
   DEVICE_BLU=bluez_sink.00_21_3C_6D_37_01
   ADM_PASSWD=YOUR_ADMIN_PASSWORD

   wget -q --no-check-certificate $1 -O /tmp/test.mp3
   echo $ADM_PASSWD | sudo -kS $MPLAYER -ao pulse::$DEVICE_BLU -really-quiet \
   -noconsolecontrols -srate 44100 -channels 2 -volume 90 /tmp/test.mp3 \
   > /dev/null 2>&1
}
play $1

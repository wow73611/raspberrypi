# A simple command line tool to control pin 12 turn on/off

    sudo python cmd.py usbon
    sudo python cmd.py usboff


# A simple web server to control pin 12 turn on/off

    sudo python web.py
    curl http://127.0.0.1/usbon
    curl http://127.0.0.1/usboff


# Install avahi

    sudo apt-get install avahi-daemon
    sudo update-rc.d avahi-daemon defaults


# Copy multiple.service to /etc/avahi/services/


# Running avahi daemon

    sudo service avahi-daemon restart
    ssh pi@raspberrypi.local


# Using GPIO by wiringPi

    git clone git://git.drogon.net/wiringPi
    cd wiringPi
    ./build

    gpio -g mode 18 out
    gpio -g mode write 18 1


# Using GPIO by shell script

    echo "18" > /sys/class/gpio/export
    echo "out" > /sys/class/gpio/gpio18/direction
    echo 1 > /sys/class/gpio/gpio18/value


# Using GPIO by pigpio

    wget abyz.co.uk/rpi/pigpio/pigpio.zip
    unzip pigpio.zip
    cd PIGPIO
    make
    make install

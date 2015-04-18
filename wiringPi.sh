#!/bin/bash

gpio mode 1 out
while true; do
    gpio write 1 1
    sleep 0.5
    gpio write 1 0
    sleep 0.5
done

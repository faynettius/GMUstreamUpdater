#!/bin/sh
echo "Enter IP:"
read ip
echo "Enter Port:"
read port
python clientWindow.py $ip $port

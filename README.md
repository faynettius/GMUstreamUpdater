# GMUstreamUpdater
This program was made to update all of the text on the screen of OBS as long as OBS is reading the text files it creates.

# Network Capabilities
If you want to transfer the stream updater data from one computer to another on the same wifi/ethernet network, you can run `runServer.bat` or `runServer.sh` and they will prompt you for a port to host it on. Once it is successfully hosted, you will see the ip and port on the stream updater. 
Once you know the port and ip address, go to the client computer and run `runClient.bat` or `runClient.sh`, then input the IP and the port. To test locally, you can run both on your computer and set your client ip as "localhost"

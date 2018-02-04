# Challenge Overview/Objective
The objective of this challenge is to analyse a packet capture (.pcap file) and discover all the hidden messages within it.

All of the messages are the names of famous films. To complete the challenge you must provide A) a list of all the film names, B) the network protocol in which you found them.

There are 7 film names to be found. 


# Getting Started
Clone this repository.

`git clone http://github.com/iain-mc/pcapchallenge`

Wireshark can be used to analyse .pcap files, so you may wish to install it.

`sudo apt-get update`

`sudo apt-get install wireshark`

Once you have Wireshark installed, open it then click File -> Open and select capture1.pcap.

# Hints
Some are very easy to find, for example just looking for plaintext in the payload of common transport protocols.

Some are a bit more tricky as the data can be split across many TCP packets, encoded in formats such as JPEG, etc..   

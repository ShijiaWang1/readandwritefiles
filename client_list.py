from typing import Counter


infile = open("clients.txt", "r")

client_file = infile.read()

counter = 1
for client in client_file:
    print(counter, ".", client.rstrip("\n"), sep="")
    counter += 1

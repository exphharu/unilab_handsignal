import client3
import time

cli = client3.InetClient()

"""
for i in range(0, 100, 1):0

    time.sleep(1)
    cli.send(str(i*100))
"""
while True:
    var = input("variable : ")
    if var == "0":
        cli.send(str(var)) 
    elif var == "40":
        cli.send(str(var))
    elif var == "80":
        cli.send(str(var))
    elif var == "-40":
        cli.send(str(var))
    elif var == "-80":
        cli.send(str(var))        
    else:
        cli.send('0')

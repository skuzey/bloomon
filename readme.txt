The flow of program:

1. main.py looks for a text file named input.txt, in the same folder
2.

You can find the test codes in test_* files


p.s Please keep in mind that, I am a Java expert and I don't use Python in pro capacity.
So, I am not an expert on Python best practices.
I originally coded in Java and converted into Python afterwards.


to build docker image on the root folder of the code:
$ docker build . -t bloomwild-sk


To run image:
$ docker run -a stdout -a stdin -it bloomwild-sk


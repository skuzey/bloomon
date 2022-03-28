# Bloomon assesment

## How to build and run

1. Checkout/download the code to your local
2. Go to the root folder of the project from terminal / command line
3. Build the docker file in the root folder of the project: ```docker build . -t bloomwild-sk```
5. Run the docker image: ```docker run -a stdout -a stdin -it bloomwild-sk```
6. Program runs and expect you to enter data using the console, prompting: ```Ready. You can start writing the designs and flowers..```
7. Enter the designs and flowers line by line, as instructed by the pdf file
8. The program will output the created bouquets. (i.e. as soon as a bouquet is ready, not at the end of the execution)
9. Enter "q" to quit the program

### Additional Info

1. Program is running based on the assumptions given in the assesment.pdf, there are no extra validation checks. 
2. For high flower quantities, the program starts to get slow. And although it may seem responsive and still accepting input from the command line, it actually is not. (*total max quantities around <20 run under 1 sec. e.g AS10a10b11, AS6a6b7c11, AS4a4b5c5d11*). 
3. You can find test codes in the test* files. In order to run them, you need to locally setup python.




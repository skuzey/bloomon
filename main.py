from design import Design
from worker import Worker


def process_input():
    designs = []
    read_designs = True

    print("Ready. You can start writing the designs and flowers..")
    while True:
        line = input()
        if line == "q":
            print("Quitting!")
            break
        if read_designs:
            if line == "":
                read_designs = False
                worker = Worker(designs)
            else:
                designs.append(Design(line))
        else:
            bouquet = worker.flower_received(line)
            if bouquet:
                print(bouquet)


if __name__ == '__main__':
    process_input()

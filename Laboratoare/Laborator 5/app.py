import utils


if __name__ == '__main__':
    while True:
        input_received = input()
        if input_received == 'q':
            break
        else:
            print(utils.process_item(int(input_received)))
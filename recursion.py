counter = 0
def count_to_five():
    global counter
    print(counter)
    if counter == 5:
        return
    counter += 1
    count_to_five()

count_to_five()
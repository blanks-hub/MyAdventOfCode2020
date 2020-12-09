import math

f = open('day5input')
f = [line for line in f]

def seatID(seatinput):
    row = (0, 127)
    seat = (0, 7)

    rowstr = seatinput[:7]
    seatstr = seatinput[7:]

    # Algorithm to determine row
    for i in range(len(rowstr)-1):
        if rowstr[i] == "F":
            row = (row[0], row[0] + math.floor((row[1] - row[0]) / 2)) # front; lower half
        elif rowstr[i] == "B":
            row = (row[0] + math.ceil((row[1] - row[0]) / 2), row[1]) # back; upper half
    if rowstr[6] == "F":
        row = row[0]
    elif rowstr[6] == "B":
        row = row[1]

    # Algorithm to determine seat

    for i in range(len(seatstr) - 1):
        if seatstr[i] == "L":
            seat = (seat[0], seat[0] + math.floor((seat[1] - seat[0]) / 2))  # front; lower half
        elif seatstr[i] == "R":
            seat = (seat[0] + math.ceil((seat[1] - seat[0]) / 2), seat[1])  # back; upper half
    if seatstr[2] == "L":
        seat = seat[0]
    elif seatstr[2] == "R":
        seat = seat[1]

    return row * 8 + seat

if __name__ == '__main__':


    # Part One
    seatlst = list()
    for seatinput in f:
        seatlst.append(seatID(seatinput))
    print("Max: ", max(seatlst))

    # Part Two
    seatlst.sort()
    myseat = set(range(seatlst[0], seatlst[-1])) - set(seatlst) # Creating one set with all the sets and one of the seats
    print("My seat: ", myseat)                                  # The set difference of them is my seat
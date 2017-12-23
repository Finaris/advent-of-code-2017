# Utility functions to be used in all days.
def file_contents_from_day(day):
    """ Opens a specified file for a day and returns a list of each of its lines.

    :param day: Number of the day whose file we are to open.
    :return: List of each line in the file.
    """
    return [line.strip().split("\t") for line in open("inputs/input" + str(day))]


# Day 1
def matching_sum_part1(captcha):
    """ Finds the sum of all pairs of numbers which are the same and consecutive.

    i.e. 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and third matches fourth.

    :param captcha: Sequence of numbers to check.
    :return: An integer sum that meet the required specifications.
    """
    digit_sum = 0
    # Check for all digits except the last.
    for i in range(len(captcha)-1):
        if captcha[i] == captcha[i+1]:
            digit_sum += int(captcha[i])
    # Do a special check on the last digit.
    if captcha[len(captcha)-1] == captcha[0]:
        digit_sum += int(captcha[0])
    return digit_sum


def matching_sum_part2(captcha):
    """ Finds the sum of all pairs of numbers which match the number ahead half of the list's length (circular list).

    i.e. 1212 produces 6 as each digit is equal to the number 2 items ahead.

    :param captcha: Sequence of numbers to check.
    :return: An integer sum that meet the required specifications.
    """
    digit_sum, captcha_length = 0, len(captcha)
    # Iterate through and check for each digit.
    for i in range(len(captcha)):
        if captcha[i] == captcha[int((i + captcha_length / 2) % captcha_length)]:
            digit_sum += int(captcha[i])
    return digit_sum


# Day 2
def checksum_part1(spreadsheet):
    """ Calculates the checksum of a given "spreadsheet". This is done by adding the difference of the maximum
        and minimum values of each row in the spreadsheet.

    :param spreadsheet: List of lists (containing ints) representing a spreadsheet.
    :return: Integer checksum of a given spreadsheet.
    """
    running_checksum = 0
    for row in spreadsheet:
        # Set defaults for the smallest and largest values in a given row.
        smallest, largest = int(row[0]), int(row[0])
        for entry in row:
            if int(entry) > largest:
                largest = int(entry)
            elif int(entry) < smallest:
                smallest = int(entry)
        running_checksum += (largest - smallest)
    return running_checksum


def checksum_part2(spreadsheet):
    """ Calculates the checksum of a given "spreadsheet". This is done by summing the quotient for the only two
        divisible entries in each row.

    :param spreadsheet: List of lists (containing ints) representing a spreadsheet.
    :return: Integer checksum of a given spreadsheet.
    """
    running_checksum = 0
    for row in spreadsheet:
        # Sort the row for convenience.
        row = [int(entry) for entry in row]
        row = sorted(row, reverse=True)
        quotient = None
        # Iterate through every comparision of each entry.
        for i in range(len(row)):
            for j in range(i+1, len(row)):
                if row[i] % row[j] == 0:
                    quotient = int(row[i] / row[j])
                    break
            if quotient is not None:
                break

        running_checksum += quotient
    return running_checksum


# Day 3
def steps_part1(inp):
    """ Calculates the Manhattan Distance of a spiral of value "input" to the center tile (1).

    :param inp: Value in the spiral we are finding the Manhattan distance to 1 of.
    :return: Minimum amount of steps needed.
    """
    count = 1
    while count ** 2 < inp:
        count += 2
    return count // 2 + \
        min(i for i in [inp - ((count ** 2 - i * (count - 1)) - count // 2) for i in range(4)] if i >= 0)

if __name__ == "__main__":
    # Day 1
    # day1 = file_contents_from_day(1)
    # answer = matching_sum_part1(day1[0][0])
    # answer = matching_sum_part2(day1[0][0])

    # Day 2
    # day2 = file_contents_from_day(2)
    # answer = checksum_part1(day2)
    # answer = checksum_part2(day2)
    # print(answer)

    # Day 3
    answer = steps_part1(347991)
    print(answer)

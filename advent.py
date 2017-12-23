# Utility functions to be used in all days.
def file_contents_from_day(day):
    """ Opens a specified file for a day and returns a list of each of its lines.

    :param day: Number of the day whose file we are to open.
    :return: List of each line in the file.
    """
    with open("inputs/input" + str(day)) as f:
        return f.readlines()


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

if __name__ == "__main__":
    # Day 1
    # day1 = file_contents_from_day(1)
    # answer = matching_sum_part1(day1[0])
    # answer = matching_sum_part2(day1[0])

    # Day 2
    pass

from humanfriendly import parse_size, InvalidSize


def byte_str_to_int(raw_str):
    """
    Converts data size strings like "4.8M" to an integer representation
    :param raw_str: Human friendly string of data size
    :return: Integer representation of data size
    """

    try:
        res = parse_size(raw_str)
    except InvalidSize:
        print "Could not parse {}".format(raw_str)
        res = 0
    return res


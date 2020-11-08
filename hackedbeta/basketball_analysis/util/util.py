# HackED Beta 2020
# Author: Albert Dinh

import statistics


def get_vertical_index(typi, category):
    """ Take a user input for what datatype and category

    Index reference from the user
    0: Totals
    1: Per-game
    2: Per-36-Min
    3: Per-100-Possession
    4: Advanced

    :param typi: a type of file
    :param category: a string input by the user to extract from a file
    :return:
    """
    if typi in [0, 1, 2, 3, 4]:
        # FIXME Could add more if needed
        if category == 'AGE':
            return 2
        elif category == 'GAMES':
            return 4


def get_list_names(season_data):
    """ Take in a dictionary object (class sznAnalysis)
    :return:
        name_list: a list of player names
    """
    name_players = list(season_data.keys())[1:]

    return name_players


def get_wanted_parameter(season_data, names, index_para):
    """ Take in a list of players' names, a wanted parameter and return
    :param season_data: a dictionary of players' statistics
    :param names: a list of players' names
    :param index_para: index of the wanted parameter depending on the file
    :return:
        a_list_of_wanted_para: a list of wanted parameter for each player
    """
    a_list_of_wanted_para = []
    for name in names:
        stat_for_player = season_data[name]
        para = stat_for_player[index_para]
        a_list_of_wanted_para.append(para)

    return a_list_of_wanted_para


def compute_median(a_para_list):
    """Take in a list and compute the median
    :param a_para_list: a list of parameters for all player
    """
    num_lt = [float(i) for i in a_para_list]
    median_para = statistics.median(num_lt)

    return median_para


def compute_stdev(a_para_list):
    """ Take in a list and returns its standard deviations
    :param a_para_list: a list of parameters for all player
    :return:
    """
    num_lt = [float(i) for i in a_para_list]
    std_ev = statistics.stdev(num_lt)

    return std_ev


if __name__ == '__main__':
    pass
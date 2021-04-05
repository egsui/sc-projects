"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
-----------------
Name: Yujing Wei
"""

import sys


def add_data_for_name(name_data, year, rank, name):

    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    if name in name_data:                               # This name has already in dict of 'name_data'.
        if year in name_data[name]:                     # This name has already been added in this year.
            if int(name_data[name][year]) > int(rank):  # If same name in both girls and boys ranking in same year,
                name_data[name][year] = rank            # keep the rank of the higher one.
        else:
            name_data[name][year] = rank                # Same name in different years.
    else:
        name_data[name] = {year: rank}                  # This name first time shows in rank.


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:              # Open and read the 'filename' file as f.
        line_lst = []                           # Create a empty list 'line_lst' to store lists of lines.
        for line in f:                          # Tokenize lines in file.
            new_line = []                       # Create a empty list 'new_line' to store elements in a line.
            line = line.split(',')              # Split the line with ','. ex. ['1', '   A', 'B   ']
            for ele in line:                    # Remove blank space in elements of line. ex. ['1', 'A', 'B']
                new_line.append(ele.strip())    # Append data to list 'new_line'.
            line_lst.append(new_line)           # Append 'new_line' to 'line_lst'. ex. [['1990'], ['1', 'A', 'B'], ...]

        for i in range(len(line_lst)):          # Get data from line_lst.
            if i >= 1:                          # Except line_lst[0], which contains only 'year'.
                year = line_lst[0][0]           # Year
                rank = line_lst[i][0]           # Rank
                name1 = line_lst[i][1]          # Boy's name at 'rank' in 'year'.
                add_data_for_name(name_data, year, rank, name1)
                name2 = line_lst[i][2]          # Girl's name at 'rank' in 'year'.
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)
    return name_data                # Return name_data(dict)


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    target_names = []                       # An empty list to store names with target.
    for name in name_data:                  # Check every name in dict 'name_data'.
        target = target.lower()             # Set 'target' into lowercase.
        lower_name = name.lower()           # Set 'name' into lowercase.
        if target in lower_name:            # Search names with target in dict 'name_data'.
            target_names.append(name)       # Then, append names with target to list 'target_names'.
    return target_names                     # Return list 'target_names'.


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()

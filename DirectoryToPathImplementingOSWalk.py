import os

# the file separator, Matches the OS that runs the script.
OS_FILE_SEP = os.sep


def generate_sub_directories_list(path, directories_list):
    """
    This function updates a list received as input with all sub directories
    full paths.
    The function runs on the directory tree in a dfs manner.
    It checks if the path received is a directory path, If so it runs in a for
    loop on all the sub directories in the current directory(It gets the list using
    the os.listdir method) and it calls The function recursively with the path, file separator
    and the sub directory name all concatenated.
    when the function gets to a "dead end" meaning no sub directory exists, It appends it to
    the sub directories list.
    :param path: The current path on which we want to append its sub directories.
    :param directories_list: The list of the sub directories path.
    :return: The function doesn't return anything it just updates the list.
    """
    if os.path.isdir(path):
        # os.listdir() returns a list with all sub directories in current level.
        for dir in os.listdir(path):
            generate_sub_directories_list(path + OS_FILE_SEP + dir, directories_list)
        directories_list.append(path)


def directory_path_to_list(directory_path):
    """
    The function first checks if the path given as input is a valid path and if it
    refers to a directory, If not it throws a corresponding exception.
    If the tests mentioned above are correct then the function initializes an empty list and
    calls another function that updates the entire list of paths and if the list contains
    the original path then it removes it.
    :param directory_path: The path of the directory.
    :return: The function returns a list of all paths of the sub directories of the path given
    as input.
    """
    # checks if the path exists.
    if os.path.exists(directory_path) is False:
        raise Exception('Invalid path')

    # checks if the path refers to a directory.
    elif os.path.isdir(directory_path) is False:
        raise Exception('The path is not referring to a directory')

    # initializes an empty list.
    directories_list = []
    directory_path = os.path.abspath(directory_path)
    # calls the function that updates the list.
    generate_sub_directories_list(path=directory_path, directories_list=directories_list)

    # removes the original directory if it is in the list.
    if directory_path in directories_list:
        directories_list.remove(directory_path)
    return directories_list

import os


def create_list_from_directory_path(directory_path):
    """
    This function creates a list of all subdirectories of a certain directory received.
    The function first checks if the path given as input is a valid path and if it
    refers to a directory, If not it throws a corresponding exception.
    If the tests mentioned above are correct then the function creates a list from
    all subdirectories using the os.walk method with list comprehension.
    The function returns a list of all subdirectories(full paths).
    :param directory_path: The path of the directory.
    :return: List of all subdirectories of a directory path given as input.
    """
    # checks if the path exists.
    if os.path.exists(directory_path) is False:
        raise Exception('Invalid path')

    # checks if the path refers to a directory.
    elif os.path.isdir(directory_path) is False:
        raise Exception('The path is not referring to a directory')

    directory_path = os.path.abspath(directory_path)
    # creates a list using the os.walk() method
    directories_list = [root for root, dirs, files in os.walk(directory_path, topdown=False) if os.path.isdir(root)
                        and root != directory_path]
    return directories_list

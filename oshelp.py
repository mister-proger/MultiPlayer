import os


def directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def files(path, extension):

    filenames = os.listdir(path)

    filenames_without_extension = []

    for filename in filenames:

        if filename.endswith('.' + extension):

            filename_without_extension = os.path.splitext(filename)[0]

            filenames_without_extension.append(filename_without_extension)

    return filenames_without_extension


def get_absolute_path(relative_path):

    current_file = os.path.abspath(__file__)

    absolute_path = os.path.join(os.path.dirname(current_file), relative_path)

    return absolute_path

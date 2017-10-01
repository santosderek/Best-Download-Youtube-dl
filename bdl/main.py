from argparse import ArgumentParser
from subprocess import run
from os import chdir
from logging import Logger

""" State and Examine Given Working Directory """
WORKING_DIR = 'D:\Youtube DL Videos'

""" Change Working Directory """
chdir(WORKING_DIR)

""" Youtube-DL Command """
YOUTUBE_DL_COMMAND = 'youtube-dl --prefer-ffmpeg -f bestvideo+bestaudio --merge-output mkv'


def parse_arguments():
    """ Parse Arguments at startup """
    parser = ArgumentParser(description='Feed me youtube url.')
    parser.add_argument('urls', metavar='urls', type=str, nargs='*')
    return parser.parse_args()


def download_url(url: str):
    """ Create subprocess of Youtube-DL command """
    command = YOUTUBE_DL_COMMAND + ' ' + url
    run(command)


def main():
    """ Main function """
    arguments = parse_arguments()

    for url in arguments.urls:
        print('Downloading:', url)
        url = str(url)
        download_url(url)


if __name__ == "__main__":
    main()

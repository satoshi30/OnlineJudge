import configparser
import subprocess
import os
import shutil

from oj_commands import online_submit

conf = configparser.ConfigParser()
conf.read('settings.ini')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Online Judge Tools Commands')
    parser.add_argument('-l', '--language', type=str, default=conf['info']['language'], help='Language Option [python, pypy]')
    args = parser.parse_args()
    online_submit(args.language)
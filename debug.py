import logging
import configparser
import os
import sys
from importlib import import_module
import time

import glob


formatter = '[%(levelname)s]  %(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

conf = configparser.ConfigParser()
try:
    conf.read('settings.ini')
except Exception as e:
    logging.info('{e} : {}'.format('settings error'))

CD = 'oj'
URL = conf['info']['url']
DIR = conf['info']['dir']
EXECUTE_FILE = os.path.join(DIR, 'main.py')

def debug_test():
    test_dir = os.path.join(DIR, 'test')

    input_samples = sorted(glob.glob(os.path.join(test_dir, '*.in')))
    output_samples = sorted(glob.glob(os.path.join(test_dir, '*.out')))

    file_list = [os.path.basename(input_file) for input_file in input_samples]
    file_num_list = list(range(len(input_samples)))
    while True:
        print('Which sample to try?')
        print(file_list)
        print('Please input index number. index: {}'.format(file_num_list))
        choice = int(input())
        if choice in file_num_list:
            break

    input_file = input_samples[choice]
    print('Input : {}'.format(os.path.basename(input_file)))

    with open(input_file, 'r') as f:
        for line in f:
            print(line, end='')

    output_file = output_samples[choice]
    print('Output : {}'.format(os.path.basename(output_file)))

    with open(output_file, 'r') as f:
        for line in f:
            print(line, end='')

    time.sleep(2)
    print('Debugger Start')
    module_dir = DIR.replace('/', '.')
    module = import_module(module_dir[2:] + '.main')

    with open(input_file, 'r') as f:
        sys.stdin = f
        module.main()

    print('Debugger Finish')

if __name__ == '__main__':
    debug_test()




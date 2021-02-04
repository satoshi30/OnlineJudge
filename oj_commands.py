import configparser
import subprocess
import os
import shutil


conf = configparser.ConfigParser()
conf.read('settings.ini')

CD = 'oj'
URL = conf['info']['url']
DIR = conf['info']['dir']
EXECUTE_FILE = os.path.join(DIR, 'main.py')

def get_samples():
    usage = 'download'
    command = [CD, usage, URL]
    test_dir = os.path.join(DIR, './test')
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
        subprocess.run(command)
    else:
        subprocess.run(command)
    shutil.move('./test', DIR)
    print('#'*30)
    print(f'GET SAMPLES in {DIR}')

def judge_test():
    usage = 'test'
    arg_option1 = '-d'
    arg_option2 = '-c'
    command = [CD, usage, arg_option1, os.path.join(DIR, 'test/'), arg_option2, "python "+EXECUTE_FILE]
    subprocess.run(command)
    print('#' * 30)
    print(f'JUDGE TEST in {DIR}')

def online_login():
    usage = 'login'
    command = [CD, usage, URL]
    subprocess.run(command)

def online_submit(language):
    usage = 'submit'
    arg_option = '--guess-python-interpreter'
    if language == 'python':
        command = [CD, usage, URL, EXECUTE_FILE]
    elif language == 'pypy':
        command = [CD, usage, URL, EXECUTE_FILE, arg_option, language]
    else:
        raise Exeption('プログラム言語は python もしくは pypy を指定する必要あり')
    subprocess.run(command)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Online Judge Tools Commands')
    parser.add_argument('-u', '--usage', type=str, help='Usage Option [download, test, login, submit]')
    parser.add_argument('-l', '--language', type=str, default='python', help='Language Option [python, pypy]')
    args = parser.parse_args()
    # print(args.usage)
    if args.usage == 'download':
        get_samples()
    elif args.usage == 'test':
        judge_test()
    elif args.usage == 'login':
        online_login()
    elif args.usage == 'submit':
        online_submit(args.language)
    else:
        raise Exeption('Usage must be chosen from [download, test, login, submit]')

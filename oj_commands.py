import configparser
import subprocess
import os
import shutil

conf = configparser.ConfigParser()
conf.read('settings.ini')

CD = 'oj'
URL = conf['info']['url']
DIR = conf['info']['dir']
EXECUTE_FILE = os.path.join(DIR, conf['info']['main'])
LANGUAGE = conf['info']['language']

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
    arg_option1 = '--directory'
    arg_option2 = '--command'
    if LANGUAGE in ['python', 'pypy']:
        command = [CD, usage, arg_option1, os.path.join(DIR, 'test/'), arg_option2, f'python {EXECUTE_FILE}']
        subprocess.run(command)
    elif LANGUAGE in ['gcc', 'clang']:
        cwd = os.getcwd()
        os.chdir(DIR)
        cwd2 = os.getcwd()
        command = ['g++', conf['info']['main']]
        subprocess.run(command)
        # time.sleep(2)
        print('compile finish')
        command = [CD, usage]
        subprocess.run(command)
        os.chdir(cwd)
    else:
        raise Exception()
    subprocess.run(command)
    print('#' * 30)
    print(f'JUDGE TEST in {DIR}')

def online_login():
    usage = 'login'
    command = [CD, usage, URL]
    subprocess.run(command)

def online_submit(language):
    # https://github.com/online-judge-tools/oj/blob/master/onlinejudge_command/main.py
    usage = 'submit'
    if language == 'python':
        command = [CD, usage, URL, EXECUTE_FILE]
    elif language == 'pypy':
        command = [CD, usage, URL, EXECUTE_FILE, '--guess-python-interpreter', language]
    elif language == 'gcc':
        command = [CD, usage, URL, EXECUTE_FILE]
    elif language == 'clang':
        command = [CD, usage, URL, EXECUTE_FILE, '--guess-cxx-compiler', language]
    else:
        raise Exeption('プログラム言語は python, pypy, gcc, clang を指定する必要あり')
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

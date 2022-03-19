import os
import shutil
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Language')
    parser.add_argument('-l', '--language', type=str, default='python', help='Language Option [python, pypy, c++]')
    args = parser.parse_args()
    if args.language in ['python', 'pypy']:
        main_file = "main.py"
    elif args.language in ['gcc', 'clang']:
        main_file = "main.cpp"
    else:
        raise Exception()

    url = input('Paste the url in problem : ')
    split_url = url.split('/')

    if 'atcoder' in split_url[2].lower():
        website = 'atcoder'
        contest = split_url[4].lower()
        problem = split_url[6].lower()
        print(f'url       : {url}')
        print(f'website   : {website}')
        print(f'contest   : {contest}')
        print(f'problem   : {problem}')

        dir = f'./{website}/{contest}/{problem}'

        with open('settings.ini', mode='w') as f:
            f.write('[info]\n')
            f.write(f'website = {website}\n')
            f.write(f'url = {url}\n')
            f.write(f'dir = {dir}\n')
            f.write(f'language = {args.language}\n')
            f.write(f'main = {main_file}\n')

        # 問題のディレクトリを作成
        os.makedirs(dir, exist_ok=True)
        # main.pyを問題ディレクトリへ配置
        file_dir = os.path.join(dir, main_file)
        if not os.path.exists(file_dir):
            shutil.copyfile(f'./default_main/{main_file}', os.path.join(dir, main_file))

        from oj_commands import get_samples
        from oj_commands import online_login
        # sampleを取得する
        get_samples()
        # loginする
        online_login()
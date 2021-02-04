import os
import shutil

if __name__ == '__main__':
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

        # 問題のディレクトリを作成
        os.makedirs(dir, exist_ok=True)
        # main.pyを問題ディレクトリへ配置
        file_dir = os.path.join(dir, 'main.py')
        if not os.path.exists(file_dir):
            shutil.copyfile('./default_main.py', os.path.join(dir, 'main.py'))

        from oj_commands import get_samples
        from oj_commands import online_login
        # sampleを取得する
        get_samples()
        # loginする
        online_login()
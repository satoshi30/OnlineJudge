# 競技プログラミングを行う上での典型作業を自動化
- [online-judge-tools/oj](https://github.com/online-judge-tools/oj) を利用して作成
- 言語 : python 3.8.2
- 対応しているwebサイト
    - [AtCoder](https://atcoder.jp/home)
    - **他のサイトは利用状況に応じて追加していく**
      
# 使い方
1. 必要なライブラリをインストール
    ```
    pip install requirements.txt
    ```
   
2. 問題をセッティング 
    ```
    python settings.py
    ```
    - 問題のURLの入力が求められるので、URLを入力
    - ABC190-Aをやる場合は、https://atcoder.jp/contests/abc190/tasks/abc190_a を入力
    - 以下のようにファイルが配置される
      ```
      OnlineJudge
      ├── atcoder
      │     └── abc190
      │         └── abc190_a
      │             ├── test    （問題のサンプルデータ）
      │             │   ├── sample-1.in      
      │             │   ├── sample-1.on      
      │             │   └──     .
      │             └── main.py （問題に応じて編集作成するファイル）
      ├── settings.ini      （settings.pyでセットした内容を記録するファイル）
      │
      ├── oj_commands.py    （コマンドを呼び出すファイル）
      ├── default_main.py   （main.pyのコピー元ファイル）
      ├── functions.py      （役立つ関数を保存）
      ├── requirements.txt
      └── README.md
      ```
    
3. `main.py`を編集し回答を作成 
   
4. サンプルデータにてテスト
    ```
    python oj_commands.py -u test
    ```
   
5. 回答を提出
    python で提出
    ```
    python oj_commands.py -u submit
    ```
    pypy で提出
    ```
    python oj_commands.py -u submit -l pypy
    ```
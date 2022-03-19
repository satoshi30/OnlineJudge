# 競技プログラミングを行う上での典型作業を自動化
- [online-judge-tools/oj](https://github.com/online-judge-tools/oj) を利用して作成
- 言語 : python 3.8.2
  - M1チップのMacはpython 3.9.7
- 対応しているwebサイト
    - [AtCoder](https://atcoder.jp/home)
    - **他のサイトは利用状況に応じて追加していく**
      
# 使い方
1. 必要なライブラリをインストール
    ```
    pip install -r requirements.txt
    ```
   
2. 問題をセッティング
    ```
    python settings.py -l python
    ```
    - 引数 -l は以下言語指定を行ってください
      - ['python', 'pypy', 'clang', 'gcc']
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
        │             └── main.py or main.cpp（問題に応じて編集作成するファイル）
        ├── functions         （役立つ関数を保存）
        │     ├── functions.py
        ├── default_main      （main.py or main.cppのコピー元ファイル）
        │     ├── main.py
        │     └── main.cpp
        ├── oj_commands.py    （Online-Judge-Toolsのコマンドを呼び出す）
        ├── settings.py       （問題設定時の実行ファイル）
        ├── test.py           （サンプルデータでのテスト実行ファイル）
        ├── submit.py         （提出時の実行ファイル）
        ├── debug.py          （デバック時の実行ファイル）
        ├── requirements.txt
        └── README.md
        ```
    
3. `main.py`or `main.cpp`を編集し回答を作成 
   
4. サンプルデータにてテスト
    ```
    python  test.py
    ```
    - PyCharm の Debugger を利用している場合、以下で行えます
    ```
    python debug.py
    ```
   
5. 回答を提出
    ```
    python submit.py
    ```
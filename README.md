mySampleSocketIO
====
socketIOを行う自己的なサンプルプログラム

## Description
[Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)ライブラリを使用したsocket.ioを行う自己的なサンプルプログラム

ブロードキャスト送信と特定の人へ送信する機能を有している

## Demo

<img width="959" alt="01" src="https://user-images.githubusercontent.com/13119897/59559018-ff2a2b00-9039-11e9-9876-bb645ad5959f.PNG">

メッセージが空欄だとDialogにてエラーエラーメッセージがでる

メッセージに文字を入力して送信すると接続されているクライアントにすべて送信される（brodcast）

送信先を指定すると送信をしたいクライアントへメッセージを送信する（いない場合はエラーが帰ってくる）



## Requirement
### Server
* [Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)

### Client
* [live-server](https://www.npmjs.com/package/live-server)

## Usage
### server

1. start
    ```bash
    $ cd server
    $ python app.py
    ```

2. open browser

    http://localhost:8000/

### client

1. start
    ```bash
    $ cd client
    $ live-server .
    ```

2. open browser

    http://localhost:8080/

## Install

### server
```bash
$ pip install flask-socketio
$ pip install -r https://raw.githubusercontent.com/miguelgrinberg/Flask-SocketIO/master/example/requirements.txt
```

### client
```bash
$ yarn global add live-server
# npm install -g live-server 
```

## Licence
This software is released under the MIT License, see LICENSE.

## Author
[Twitter](https://twitter.com/momijinn_aka)

[Blog](http://www.autumn-color.com/)
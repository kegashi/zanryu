# 残留スクリプト
## 必要環境
- python

## Git clone `残留スクリプト`
`$ git clone git@github.com:kegashi/zanryu.git`


## Change Directory
`$ cd zanryu`

## `zanryu(.sh)` に実行権限を与える
`$ chmod +x zanryu`

## 設定ファイルを書き加える
`$ vim config.txt`

## 実行する
`$ ./zanryu`

## shellの種類と保存場所に合わせてPATHを設定する
(zshで/Users/zukky/Documents下に保存した場合)

`$ echo "export PATH=/Users/zukky/Documents/zanryu:\$PATH"  >> ~/.zshrc`

`$ source ~/.zshrc`

## 実行する
`$ zanryu`

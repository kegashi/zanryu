# 残留スクリプト
## 必要環境
- python

## Git clone `残留スクリプト`
`$ git clone https://github.com:kegashi/zanryu.git`

## import `mechanize`
`$ pip install mechanize`

## Change Directory
`$ cd zanryu`

## `zanryu(.sh)` に実行権限を与える
`$ chmod +x zanryu`

## 設定ファイルを書き加える
`$ vim config.txt`

## shellの種類と保存場所に合わせてPATHを通す
(zshで/Users/zukky/Documents下に保存した場合)

`$ echo "export PATH=/Users/zukky/Documents/zanryu:\$PATH"  >> ~/.zshrc`

`$ source ~/.zshrc`

## 実行する
`$ zanryu`

# 残留スクリプト
## 必要環境
- python

## Git clone `残留スクリプト`
`$ git clone https://github.com:kegashi/zanryu.git`

## install `mechanize`
`$ pip install mechanize`

## Change Directory
`$ cd zanryu`

## Edit Config file
`$ vim config.txt`

## Shellの種類と保存場所に合わせてPATHを通す
`$ echo "export PATH=(cloneしたパス)/zanryu:\$PATH"  >> ~/.設定ファイル`

(例:zshで/Users/zukky/Documents下に保存した場合)

`$ echo "export PATH=/Users/zukky/Documents/zanryu:\$PATH"  >> ~/.zshrc`

## 設定ファイルを反映させる
`$ source ~/.zshrc`

## 実行する
`$ zanryu`

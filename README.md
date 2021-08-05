# kubota-cancellation-monitoring
Kubota-summer-internship-cancellation-monitoring

## 説明
クボタのサマーインターン情報からAM6:00-PM24:00の間1時間ごとにサマーインターンの空き情報を取得し、キャンセルが出た場合はLINE_NOTIFYのAPIを通じてキャンセル情報を通知する。

## 開発環境
OS: MacOS<br>
Python: 3.8.5<br>
GoogleChrome: 92.0.4515.107<br>

## インターン情報の取得について
Pythonのライブラリであるselenium, chromedriver-binaryを使用しております。

## LINE NOTIFY API
LINEのNotify APIを用いて、空席ができた場合のみ通知を行う。<br>
https://notify-bot.line.me/ja/


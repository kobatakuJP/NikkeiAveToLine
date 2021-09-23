# NikkeiAveToLine

日経平均をlineに通知する。（あとで汎用的にする）

## 準備

### 環境変数

ローカル環境なら`.env`、パブリック環境ならsecretの仕組みを活用する。

#### TARGET_STOCK_NAME

必須。  
`yahoo_finance_api2`で使用する株式コードを記載する。  
日経平均の場合は`^N225`

#### LINEBOT_ACCESS_TOKEN

必須。  
`line developer`で取得したボットチャネルのアクセストークン。  

#### DEBUG

任意。ローカル環境では設定推奨。  
`true`でフラグON。  
このフラグがONの場合デバッグモードになる。lineの通知が自分宛てのみになったりする。

#### MY_LINE_ID

任意、`DEBUG`設定時は必須。  
自分のLINEのユーザーIDを設定しておくと自分にだけ通知が飛ぶので良き。  

#### .envの設定例

```
TARGET_STOCK_NAME=^N225
LINEBOT_ACCESS_TOKEN=/XXXXXXX/....(結構長い)
DEBUG=true
MY_LINE_ID=U123456789XXXXXX
```

## 実行

`$ pipenv run exec`

## 利用ライブラリ

- [yahoo-finance-api2](https://github.com/pkout/yahoo_finance_api2)
- [line-bot-sdk](https://github.com/line/line-bot-sdk-python)
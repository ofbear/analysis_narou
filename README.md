# 概要
下記APIを利用し、[小説家になろう][2]の言語解析を行うツールです。
- [COTOHA API Portal][1]
- [なろう小説API][3]

# 利用法
## 設定ファイル
```
conf.json
```
上記ファイルに設定値を入力してください。
```
{
    "cotoha" : {
        "clientId" : "AAAA",
        "clientSecret" : "AAAA"
    },
    "narou" : {
        "out": "json",
        "lim": "100",
        "order": "dailypoint"
    }
}
```
cotoha項目にはCOTOHAから発行された設定値。

narou項目には検索する際の条件を設定してください。

## コマンド
| オプション | 必須/任意 | 値 | 内容 |
| - | - | - | - |
| r | 任意 | なんでもOK | なろう小説情報の再取得 |
| f | 必須 | k / s | k:キーワード抽出 / s:類似度算出 |


[1]:https://api.ce-cotoha.com/contents/index.html
[2]:https://syosetu.com/
[3]:https://dev.syosetu.com/man/api/

# タグサジェスチョン


## 準備

```
# 仮想環境作成
  python -m venv venv

  # 仮想環境有効化
  source venv/bin/activate

  # 依存関係インストール
  pip install -r requirements.txt

  # スクリプト実行
  python article_scraper.py
```

## 使い方

### (0) 準備

- このリポジトリを取得する
- Claude Code が使える状態にする
- 2回目の利用の場合は、artcleフォルダ内のファイル、article-tags.htl、tags.md を削除しておく

以下のコマンドを使って、Python実行環境を作る（これが難しいと感じる人も多いかも）。とりあえず、他に影響を及ぼさないために、以下では、pyenv を使う例。

```
> python -m venv venv
> source venv/bin/activate
```

※ 次回からは、 `> source venv/bin/activate` を実行する

Visual Studio Code でひらけば、自動的に実行される（と思う）。


### (1) 記事の取得

事前に、sitemap.xml のURLを取得しておく。以下のコマンドを **通常のターミナルで** 実行すると、尋ねられるので、入力する。

```
> python article_scraper.py
```

自動的に、artcleフォルダが作成される。そのフォルダに、記事が保存されます。


### (2) タグ候補を作成する

以下のプロンプトを修正して（例えば、URLなど）、Claude Codeのターミナルで実行する。

```
articleディレクトリに保存されているファイルは、 https://toieelabjournal.substack.com/ の記事です。この記事を読み込んで、タグの設計を考えて、提案してください。提案内容は、tags.md に保存してください。
```

### (3) 各記事のタグを決定し、その一覧を作る

以下のプロンプトを、Claude Code のターミナルで実行する。

```
それぞれの記事（articleディレクトリに保存）に、どのタグ(tags.mdを参照)を割り当てるべきかを提案してください。

## 最終成果物

次のような形式の記事一覧。以下は、Markdownで書いているが、実際は、見やすいHTMLファイルを生成してください。保存名は、article-tags.html にしてください。なお、リンクは別ウィンドウで開く設定（target="_blank"）、タグは、クリックしたらコピーできるようにしてください。

- [タイトル](https://toieelabjournal.substack.com/p/ファイル名（拡張子なし）)  `タグ1`、`タグ2`、`タグ3`、・・・

```

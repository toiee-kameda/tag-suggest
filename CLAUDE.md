# Tag Suggest プロジェクト

## プロジェクト概要
toiee Lab Journalの記事を分析し、効果的なタグシステムを設計・提案するプロジェクト。記事の自動収集からタグ付けまでの一連のワークフローを構築しました。

## 作業内容

### 1. 記事収集システムの構築
- **ファイル**: `article_scraper.py`
- **機能**: https://toieelabjournal.substack.com/feed からRSSフィードを取得し、各記事のコンテンツを自動収集
- **取得内容**:
  - 記事タイトル（`<h1 class="post-title published">`）
  - 記事サブタイトル（`<h3 class="subtitle">`）
  - 記事本文（`class="body markup"`内のHTML）
- **保存形式**: `article/` フォルダに Markdown形式で保存（ファイル名: URLスラッグ.md）
- **HTML→Markdown変換**: markdownifyライブラリを使用

**依存関係**: `requirements.txt`
```
requests
beautifulsoup4
feedparser
markdownify
```

### 2. 記事分析とタグシステム設計
- **ファイル**: `tags.md`
- **分析対象**: 20記事の内容を詳細分析
- **主要テーマ**:
  - AI ツールの活用法と比較（Claude、ChatGPT、Perplexity等）
  - 非エンジニア向けのAI教育（Vibe Coding）
  - ビジネス業務の自動化・効率化
  - 学習ファシリテーション理論
  - 具体的なツール活用（WordPress、Gmail、freee等）

**設計したタグカテゴリ**:
1. **AIツール・プラットフォーム**: claude, chatgpt, perplexity, claude-code等
2. **対象オーディエンス**: 非エンジニア, 初心者, 中級者, ビジネス活用
3. **活用用途・業務分野**: 業務効率化, コンテンツ作成, プログラミング, 経理・会計等
4. **コンテンツタイプ**: ハウツー, ニュース, 理論・概念, ワークショップ等
5. **テクニカルタグ**: wordpress, vibe-coding, gmail, automation等
6. **学習・教育手法**: ラーニングファシリテーション, 対話型学習, ごめんねメソッド等

### 3. 記事タグ付けとHTML生成
- **ファイル**: `article-tags.html`
- **機能**: 全20記事に適切なタグを割り当て、見やすいHTMLページを生成
- **特徴**:
  - クリック可能なタグ（クリップボードコピー機能付き）
  - レスポンシブデザイン
  - タグカテゴリ説明とレジェンド
  - 統計情報表示（20記事、102タグ割り当て、平均5.1タグ/記事）
  - ホバーエフェクトとアニメーション

## 実行方法

### 記事収集
```bash
# 仮想環境作成・有効化
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係インストール
pip install -r requirements.txt

# 記事収集実行
python article_scraper.py
```

### 結果確認
- 収集された記事: `article/` ディレクトリ
- タグシステム設計: `tags.md`
- タグ付け結果: `article-tags.html` をブラウザで開く

## プロジェクト成果物

1. **article_scraper.py** - RSS記事自動収集スクリプト
2. **requirements.txt** - Python依存関係
3. **article/** - 収集された20記事（Markdown形式）
4. **tags.md** - タグシステム設計書
5. **article-tags.html** - タグ付け結果の可視化HTML

## 技術スタック
- **Python**: 記事収集とデータ処理
- **Libraries**: requests, beautifulsoup4, feedparser, markdownify
- **HTML/CSS/JavaScript**: タグ表示とインタラクション
- **Markdown**: ドキュメント管理

## 今後の拡張可能性
- 新記事の自動タグ付け
- タグ使用統計の分析
- SEO効果測定
- 関連記事推薦システム
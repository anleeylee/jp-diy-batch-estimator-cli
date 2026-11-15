# 日本DIY・リフォーム向け バッチ数量見積もり CLI

> **関連サイト：[SumaiTools（住まいの建築・リフォーム・DIY 計算器サイト）](https://sumaitools.com/)** — 本リポジトリは、同サイトで公開されている計算器のオフライン版コンパニオン実装です。

## Description

住宅リフォーム・DIY の材料数量を CSV から一括算出するオフライン CLI。面積・坪数・タイル枚数・フローリング枚数・クロス巻数・モルタル量・木材重量をまとめて出力します。計算器ポータル: https://sumaitools.com/

**Repository topics:** `python` `cli` `japan` `construction` `renovation` `diy` `estimating` `material-quantity`

## 日本語

### このツールについて

ウェブの計算器（[SumaiTools（住まいの建築・リフォーム・DIY 計算器サイト）](https://sumaitools.com/)）は1件ずつの対話計算向けです。この CLI は、現場の部屋リスト CSV をまとめて読み込み、複数室の数量を一括でオフライン算出して CSV/JSON に書き出します。店舗価格やロス率のように根拠のない既定値は置かず、未入力項目は空欄のまま残します。

### 機能

- 矩形・三角・円・台形の面積と坪（1 m² = 400/121 坪、法令値）を計算
- タイル枚数（目地込みピッチ・ロス加算）、フローリング枚数、クロス巻数を一括算出
- モルタル/コンクリート容積と、樹種別気乾比重による木材重量を計算
- CSV 入力 → CSV / JSON 出力。依存ライブラリ不要（Python 標準ライブラリのみ）
- 未入力・計算不能な項目は警告として行末に記録し、結果を推定値として明示

### インストール / Requirements

```bash
# Python 3.10+
git clone https://github.com/anleeylee/jp-diy-batch-estimator-cli.git
cd jp-diy-batch-estimator-cli
python -m pip install -r requirements.txt
```

### 使い方 / Usage

```bash
python -m jp_batch_estimator.cli --input examples/rooms_sample.csv --output report.csv --format csv
```

Python パッケージとして実行する場合は `src/` を PYTHONPATH に追加してください。

### リポジトリ構成

```
jp-diy-batch-estimator-cli/
├── src/jp_batch_estimator/
│   ├── cli.py
│   ├── geometry.py
│   ├── interior.py
│   ├── lumber.py
│   └── concrete.py
├── examples/rooms_sample.csv
├── tests/
├── index.html
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── .gitignore
└── sitemap.xml
```

### 注意事項

- 本ツールの数値は機械計算値であり、施工店の判断・現場実測が優先されます。
- 木材重量は体積×比重の算出値で、構造計算・許容応力度には使用できません。
- 価格の全国平均を主張しません。材料費の試算は別リポジトリの原価見積もり CLI を参照してください。

## English

### About

The web calculator portal ([SumaiTools — Japanese home construction, renovation & DIY calculators](https://sumaitools.com/)) handles one interactive case at a time. This CLI reads a room list CSV, computes quantities for many rooms offline, and writes CSV/JSON. No hard-coded defaults are invented for store prices or loss factors; missing inputs stay blank.

### Features

- Area (rectangle/triangle/circle/trapezoid) and tsubo conversion with the statutory 400/121 factor
- Tile count with joint-inclusive pitch and cut allowance; flooring pieces; wallpaper rolls
- Mortar/concrete volume and lumber weight from verified species air-dry densities
- CSV in, CSV/JSON out; standard library only, no third-party dependencies
- Missing or infeasible items are recorded as warnings instead of being filled with guesses

### Usage

See the Japanese command above; the CLI accepts the same arguments and writes CSV / JSON output.

### Notes

- Figures are mechanical estimates; site measurement and the contractor's judgement prevail.
- Lumber weight is volume × density, not a structural design value.
- The tool does not claim any national average price.

## Source portal

- Calculator web portal: [SumaiTools — Japanese home construction, renovation & DIY calculators](https://sumaitools.com/)
- Open data sets: companion Kaggle datasets published alongside this repository.

## License

MIT — see [LICENSE](LICENSE). Contribution guidelines: [CONTRIBUTING.md](CONTRIBUTING.md).
Release history: [CHANGELOG.md](CHANGELOG.md).

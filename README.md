
# About: Notebooks for Elasticsearch README

Literate Computing for Reproducible Infrastructure: Elasticsearch運用をJupyter + Ansibleでおこなう際のお手本Notebookです。

このリポジトリでは、Elasticsearch( https://www.elastic.co/jp/products/elasticsearch )の環境を構築し、運用するためのNotebook例を紹介しています。

**なお、これらのNotebookはNIIクラウドチーム内で行っている作業の考え方を示すためのもので、環境によってはそのままでは動作しないものもあります。**

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)


## Elasticsearchとは？
Elasticsearchは、リアルタイムにデータを検索/分析するための分散型の全文検索エンジンであり、次のような特徴を持っています。

1. __リアルタイム分析__  
収集したデータをリアルタイムに検索/分析することができます。  
また、高速に検索できるため、他のBIツールのように事前に分析項目を決めなくても、すでに蓄積されたデータに対してインタラクティブな分析をすることが可能です。

2. __クラスタリングが容易__  
クラスタリングを想定した設計が行われており、他のミドルウェアを利用せずにクラスタを組むことができます。  
ノードを追加することによりスケールアウトできるため、必要な処理性能や可用性などに応じたコントロールが容易です。

3. __ドキュメント指向、スキーマフリー__  
データベースであれば、データをレコードの単位で管理しますが、
Elasticsearchではドキュメントと呼ばれる構造化されたJSONデータの形式で管理します。  
すべてのフィールドはデフォルトでインデックスされるため、簡単かつ高速に検索できます。  
また、このドキュメントはスキーマを決めずに投入することもできるため、すぐに使い始めることができます。  
なお、ログデータのような構造化されていないデータを投入する際には、Logstashなどを用いてJSON形式に加工して保持することになります。

4. __REST API__  
Elasticsearchはシンプルで使いやすいREST APIを提供しています。  
検索処理や登録処理（indexing）だけでなく、インデックスやマッピングの定義、クラスタ管理やメンテナンスなど、Elasticsearchのクラスタ・ノードに対する操作は、ほぼすべてAPIを通じて実施できます。

5. __オープンソース__  
Elasticsearchはオープンソース製品として開発されています。  
ライセンスはApache License Version 2.0です。  
ただし、一部のプラグインを利用するためにはサブスクリプション契約（兼サポート契約）を結ぶ必要があります。

参考）[Elasticsearch公式ページ]( https://www.elastic.co/jp/products )

## 前提条件
このNotebookで前提にしているOS/ミドルウェアのバージョンは次の通りです。

| OS/ミドルウェア | バージョン |
|----|----|
|Elasticserach|elasticsearch-5.0.0-1.noarch|
|Logstash|logstash-5.0.0-1.noarch|
|Ansible|2.2.0.0|
|OS|CentOS Linux release 7.2.1511|
|JDK|jdk1.8.0_112-1.8.0_112-fcs.x86_64|


## お手本Notebook

お手本NotebookはこのNotebookと同じディレクトリにあります。

特に、**[00_Prerequisites for Literate Computing via Notebooks](00_Prerequisites for Literate Computing via Notebooks.ipynb)は、お手本Notebookが適用可能なNotebook環境、Bind対象であるかどうかを確認するためのNotebook**です。はじめに実施して、これらのお手本Notebookが利用可能な状態かを確認してみてください。

### お手本Notebookの構成
このNotebookは、以下のような構成になっています。

1. [Elastic Stackの構築手順](01_Setup.ipynb)
2. [サーチエンジンとしての利用手順(検索)](02_Search.ipynb)
3. [サーチエンジンとしての利用手順(集計)](03_Aggregation.ipynb)
4. [サーチエンジンとしての利用手順(データ蓄積)](04_Store_Data.ipynb)
5. [サーチエンジンとしての利用手順(インデックス設計)](05_Indexing.ipynb)
6. [サーチエンジンとしての利用手順(運用)](06_Manual-Operation.ipynb)
7. [トラブルシューティング](07_Troubleshooting.ipynb)

1台構成のElastic Stackの構築手順については、は次を利用してください。
1. [Elastic Stackの構築手順(1台構成)](01_Setup_1server.ipynb)

## お手本Notebookの一覧

現在、このNotebook環境からアクセス可能なNotebookの一覧を参照するには、以下のセルを実行(`Run cell`)してください。Notebookファイルへのリンクが表示されます。


```python
import re
import os
from IPython.core.display import HTML

ref_notebooks = filter(lambda m: m, map(lambda n: re.match(r'([0-9][0-9a-z]+_.*)\.ipynb', n), os.listdir('.')))
ref_notebooks = sorted(ref_notebooks, key=lambda m: m.group(1))
HTML(''.join(map(lambda m: '<div><a href="{name}" target="_blank">{title}</a></div>'.format(name=m.group(0), title=m.group(1)),
                 ref_notebooks)))
```




<div><a href="00_Prerequisites for Literate Computing via Notebooks.ipynb" target="_blank">00_Prerequisites for Literate Computing via Notebooks</a></div><div><a href="01_Setup.ipynb" target="_blank">01_Setup</a></div><div><a href="01_Setup_1server.ipynb" target="_blank">01_Setup_1server</a></div><div><a href="02_Search.ipynb" target="_blank">02_Search</a></div><div><a href="03_Aggregation.ipynb" target="_blank">03_Aggregation</a></div><div><a href="04_Store_Data.ipynb" target="_blank">04_Store_Data</a></div><div><a href="05_Indexing.ipynb" target="_blank">05_Indexing</a></div><div><a href="06_Manual-Operation.ipynb" target="_blank">06_Manual-Operation</a></div><div><a href="07_Troubleshooting.ipynb" target="_blank">07_Troubleshooting</a></div>



## お手本Notebookと証跡Notebook

お手本Notebookを使う場合は、お手本をコピーし、そのコピーを開きます。このように、**お手本と作業証跡は明確に分けながら作業をおこないます。**

また、お手本をコピーする際は、 `YYYYMMDD_NN_` といった実施日を示すプレフィックスを付加することで、後で整理しやすくしています。

## 実際にお手本Notebookを使ってみる

以下のJavaScriptを実行することで、簡単にお手本から作業用Notebookを作成することもできます。

以下のセルを実行すると、Notebook名のドロップダウンリストと[作業開始]ボタンが現れます。
[作業開始]ボタンを押すと、お手本Notebookのコピーを作成した後、自動的にブラウザでコピーが開きます。
Notebookの説明を確認しながら実行、適宜修正しながら実行していってください。


```python
from datetime import datetime
import shutil

def copy_ref_notebook(src):
    prefix = datetime.now().strftime('%Y%m%d') + '_'
    index = len(filter(lambda name: name.startswith(prefix), os.listdir('.'))) + 1
    new_notebook = '{0}{1:0>2}_{2}'.format(prefix, index, src)
    shutil.copyfile(src, new_notebook)
    print(new_notebook)

frags = map(lambda m: '<option value="{name}">{title}</option>'.format(name=m.group(0), title=m.group(1)),
            ref_notebooks)
HTML('''
<script type="text/Javascript">
    function copy_otehon() {
        var sel = document.getElementById('selector');
        IPython.notebook.kernel.execute('copy_ref_notebook("' + sel.options[sel.selectedIndex].value + '")',
                       {'iopub': {'output': function(msg) {
                           window.open(msg.content.text, '_blank')
                       }}});
    }
</script>
<select id="selector">''' + ''.join(frags) + '</select><button onclick="copy_otehon()">作業開始</button>')
```





<script type="text/Javascript">
    function copy_otehon() {
        var sel = document.getElementById('selector');
        IPython.notebook.kernel.execute('copy_ref_notebook("' + sel.options[sel.selectedIndex].value + '")',
                       {'iopub': {'output': function(msg) {
                           window.open(msg.content.text, '_blank')
                       }}});
    }
</script>
<select id="selector"><option value="00_Prerequisites for Literate Computing via Notebooks.ipynb">00_Prerequisites for Literate Computing via Notebooks</option><option value="01_Setup.ipynb">01_Setup</option><option value="01_Setup_1server.ipynb">01_Setup_1server</option><option value="02_Search.ipynb">02_Search</option><option value="03_Aggregation.ipynb">03_Aggregation</option><option value="04_Store_Data.ipynb">04_Store_Data</option><option value="05_Indexing.ipynb">05_Indexing</option><option value="06_Manual-Operation.ipynb">06_Manual-Operation</option><option value="07_Troubleshooting.ipynb">07_Troubleshooting</option></select><button onclick="copy_otehon()">作業開始</button>



## お手本のアーカイブ

以下のセルで、お手本NotebookのZIPアーカイブを作成できます


```python
ref_notebooks = filter(lambda m: m, map(lambda n: re.match(r'([A-Z][0-9][0-9a-z]+_.*)\.ipynb', n), os.listdir('.')))
ref_notebooks = sorted(ref_notebooks, key=lambda m: m.group(1))
!zip ref_notebooks-{datetime.now().strftime('%Y%m%d')}.zip *.ipynb {' '.join(map(lambda n: '"' + n.group(0) + '"', ref_notebooks))} logstash_conf/* playbooks/*.yml sample_data/* images/* 
```

      adding: 00_Prerequisites for Literate Computing via Notebooks.ipynb (deflated 83%)
      adding: 01_Setup.ipynb (deflated 82%)
      adding: 01_Setup_1server.ipynb (deflated 84%)
      adding: 02_Search.ipynb (deflated 93%)
      adding: 03_Aggregation.ipynb (deflated 93%)
      adding: 04_Store_Data.ipynb (deflated 88%)
      adding: 05_Indexing.ipynb (deflated 78%)
      adding: 06_Manual-Operation.ipynb (deflated 94%)
      adding: 07_Troubleshooting.ipynb (deflated 86%)
      adding: Readme.ipynb (deflated 72%)
      adding: logstash_conf/csv.conf (deflated 53%)
      adding: logstash_conf/document_id.conf (deflated 55%)
      adding: logstash_conf/geoip.conf (deflated 47%)
      adding: logstash_conf/json.conf (deflated 32%)
      adding: logstash_conf/json_multiline.conf (deflated 44%)
      adding: logstash_conf/ltsv.conf (deflated 81%)
      adding: logstash_conf/main.conf (deflated 53%)
      adding: logstash_conf/multi_line.conf (deflated 78%)
      adding: logstash_conf/single_line.conf (deflated 78%)
      adding: logstash_conf/tsv.conf (deflated 53%)
      adding: logstash_conf/useragent.conf (deflated 38%)
      adding: playbooks/install_elasticsearch.yml (deflated 36%)
      adding: playbooks/install_elasticsearch_1server.yml (deflated 36%)
      adding: playbooks/install_jdk.yml (deflated 48%)
      adding: playbooks/install_jdk_1server.yml (deflated 48%)
      adding: playbooks/install_logstash.yml (deflated 33%)
      adding: playbooks/install_logstash_1server.yml (deflated 33%)
      adding: playbooks/send_sampledata-kai.yml (deflated 28%)
      adding: playbooks/send_sampledata.yml (deflated 23%)
      adding: playbooks/set_iptables-rule.yml (deflated 56%)
      adding: playbooks/set_kernelparameter.yml (deflated 38%)
      adding: playbooks/start_1server.yml (deflated 31%)
      adding: playbooks/start_cluster.yml (deflated 33%)
      adding: sample_data/geoip.csv (deflated 79%)
      adding: sample_data/geoip.json (deflated 79%)
      adding: sample_data/mapping.txt (deflated 77%)
      adding: sample_data/multi_line.txt (deflated 61%)
      adding: sample_data/single_line.txt (deflated 43%)
      adding: sample_data/tokyo2015.csv (deflated 74%)
      adding: sample_data/useragent.txt (deflated 39%)
      adding: sample_data/weather.csv (deflated 62%)
      adding: sample_data/weather.json (deflated 89%)
      adding: sample_data/weather.ltsv (deflated 50%)
      adding: sample_data/weather.tsv (deflated 62%)
      adding: sample_data/weather_multiline.json (deflated 90%)
      adding: images/01_1server.png (deflated 10%)
      adding: images/01_5server.png (deflated 23%)
      adding: images/01_basic_concept.png (deflated 17%)
      adding: images/01_node_type.png (deflated 7%)
      adding: images/01_server_construction.png (deflated 10%)
      adding: images/03_pipeline.png (deflated 16%)
      adding: images/images.pptx (deflated 18%)


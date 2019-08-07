## 環境構築
- 下記を実行（Ubuntu 18.04.2 LTSにおいて実施）
```
<最新化>
sudo apt update
sudo apt upgrade
sudo apt-get update
sudo apt-get upgrade

<python3で仮想環境構築>
sudo apt-get install python3-venv
python3 -m venv .env
```

## 環境変数の設定
- 下記を実行
```
sudo apt-get install direnv
vi ~/.bashrc
  echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
  export EDITOR=vi
source ~/.bashrc
direnv edit .
  export XXXX=xxxx
  …
```

### 環境変数の設定値
|Key|Value|Description|
|:---|:---|:---|
|FLICKR_API_KEY|********|flickr-apiで画像をDLするためのキー|
|FLICKR_API_SECRET_KEY|********|flickr-apiで画像をDLするためのキー|
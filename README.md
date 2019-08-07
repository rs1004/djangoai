# 環境構築
- 下記を実行（Ubuntu 18.04.2 LTSにおいて実施）
```
<最新化>
sudo apt update
sudo apt upgrade
sudo apt-get update
sudo apt-get upgrade

<python3.7で仮想環境構築>
sudo apt-get install python3.7
sudo apt-get install python3.7-venv

python3.7 -m venv .env

<pip3のインストール>
sudo apt install python3-pip
vi ~/.bashrc
  alias pip='/usr/bin/pip3'
```

# 環境変数の設定
- 下記を実行
```
sudo apt-get install direnv
vi ~./bashrc
  echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
  export EDITOR=vi
source ~./bashrc
direnv edit .
  export XXXX = xxxx
  …
```
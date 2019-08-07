# 環境構築
- 下記を実行（Ubuntu 18.04.2 LTSにおいて実施）
```
sudo apt update
sudo apt upgrade
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install python3.7
sudo apt-get install python3.7-venv

python3.7 -m venv .env
```

# 環境変数の設定
- 下記を実行
```
sudo apt-get install direnv
vi ~./bashrc
  echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
  echo 'export EDITOR=vim' >> ~/.bashrc
source ~./bashrc
direnv edit .
  export XXXX = xxxx
  …
```
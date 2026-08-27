# MQTT Sample

Python と Mosquitto を使った MQTT の Publish / Subscribe サンプル。

## 構成

```text
Publisher
    ↓
Mosquitto Broker
    ↓
Subscriber
```

## 環境

* Linux
* Python 3
* Mosquitto
* paho-mqtt
* VPN / Private Network

## Setup

### Mosquitto

```bash
sudo dnf install mosquitto
sudo systemctl enable --now mosquitto
```

確認:

```bash
systemctl status mosquitto
ss -lntp | grep 1883
```

### Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install paho-mqtt
```

## Run

Subscriber:

```bash
python subscriber.py
```

Publisher:

```bash
python publisher.py
```

使用する topic:

```text
sensor/temperature
```

## Remote Subscribe

別マシンから Broker に接続するため、Mosquitto に listener を設定。

`/etc/mosquitto/mosquitto.conf`:

```conf
include_dir /etc/mosquitto/conf.d
```

`/etc/mosquitto/conf.d/remote.conf`:

```conf
listener 1883
allow_anonymous true
```

反映:

```bash
sudo systemctl restart mosquitto
```

確認:

```bash
ss -lntp | grep 1883
```

外部接続可能な場合:

```text
0.0.0.0:1883
[::]:1883
```

必要に応じて firewall で `1883/tcp` を許可する。

別マシン側では `subscriber.py` の Broker をサーバーの Private IP に変更する。

```python
BROKER = "100.x.x.x"
```

## Multiple Subscribers

同じ topic を複数の Subscriber から購読できることを確認。

```text
                 +--> Subscriber A
Publisher --> Broker
                 +--> Subscriber B
```

## 躓いたポイント

### Broker が localhost のみで Listen

初期状態:

```text
127.0.0.1:1883
[::1]:1883
```

`listener 1883` を設定して外部接続可能にした。

### `conf.d` が読み込まれていなかった

`conf.d` に設定を追加しただけでは反映されなかったため、

```conf
include_dir /etc/mosquitto/conf.d
```

を/etc/mosquitto/mosquitto.confに追加した。

## 今回確認したこと

* Mosquitto Broker の起動
* Python から Publish / Subscribe
* topic を使ったメッセージ配信
* 複数 Subscriber での同時受信
* 別マシンから Private Network 経由で Subscribe
* Mosquitto の外部 Listen 設定

## Next

* 複数 topic
* wildcard (`+`, `#`)
* JSON payload
* QoS
* Retained Message
* 認証
* TLS


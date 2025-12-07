#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time

# 1. 設定 MQTT 回呼函式
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"連線成功！代碼: {reason_code}")
    client.subscribe("test/topic1")

def on_message(client, userdata, msg):
    print(f"收到訊息！\n主題: {msg.topic}\n內容: {msg.payload.decode()}")
    # 收到訊息後，斷開連線結束測試
    client.disconnect()

# 2. 建立客戶端並設定（使用最新的回調 API 版本）
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

def main():
# 3. 連線 (localhost 代表連本機)
    print("正在連線到 MQTT Broker...")
    client.connect("localhost", 1883, 60)

    # 4. 啟動監聽迴圈
    client.loop_start()

    # 5. 發送測試訊息
    time.sleep(1) # 等待連線穩定
    print("正在發送測試訊息...")
    client.publish("test/topic1", "Hello RPi 5, MQTT is working!")

    # 6. 等待接收
    time.sleep(2)
    client.loop_stop()
    print("測試結束")

if __name__ == "__main__":
    main()
import argparse
import psutil
import socket
import time
import paho.mqtt.client as mqtt

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-host', type=str, default='1', help='mqtt host')
parser.add_argument('-port', type=int, default=1883, help='mqtt port')
parser.add_argument('-interval', type=int, default=10, help='interval')
args = parser.parse_args()

class CpuAgent:
    def __init__(self, host, port):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.connect(host, port)
        self.client.loop_start()
        self.mqtt_status = False


    def on_connect(self,client, userdata, flags, rc):
        self.mqtt_status = True

    def publish_memory_metrics(self, interval):
        hostname = socket.gethostname()
        while True:
            memory_percent = psutil.virtual_memory().percent
            self.client.publish(f"{hostname}/memory/usage", memory_percent)
            time.sleep(interval)
            
    def publish_metrics(self):
        hostname = socket.gethostname()
        while True:
            cpu_percent = psutil.cpu_percent()
            self.client.publish(f"{hostname}/cpu/usage", cpu_percent)
            time.sleep(args.interval)
    def publish_disk_metrics(self):
        hostname = socket.gethostname()
        while True:
            disk_percent = psutil.disk_usage('/').percent
            self.client.publish(f"{hostname}/disk/usage", disk_percent)
            time.sleep(args.interval)

    def publish_network_metrics(self):
        hostname = socket.gethostname()
        while True:
            net_io_counters = psutil.net_io_counters()
            self.client.publish(f"{hostname}/network/bytes_sent", net_io_counters.bytes_sent)
            self.client.publish(f"{hostname}/network/bytes_recv", net_io_counters.bytes_recv)
            time.sleep(args.interval)

import socket
import threading
import socketserver
import json
from datetime import datetime
import psycopg2
from urllib.parse import urlsplit
from os import environ

KEYS = (
    'level',  # VARCHAR(16),
    'ts',  # TIMESTAMP ,
    'remote_addr',  # VARCHAR(32),
    'remote_port',  # SMALLINT,
    'method',  # VARCHAR(8),
    'path',  # TEXT,
    'query',  # TEXT,
    'duration',  # REAL,
    'size',  # INTEGER,
    'status'  # SMALLINT
)

STMT = "INSERT INTO AccessLog.Log (level, ts, remote_addr, remote_port, method, path, query, duration, size, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TCPRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        with psycopg2.connect(
            host='postgres-db',
            dbname='AccessLog',
            user=environ.get('POSTGRES_USER'),
            password=environ.get('POSTGRES_PASSWORD')
        ) as conn:
            while True:
                data = json.loads(self.rfile.readline())

                data.update(data['request'])
                data.update(urlsplit(data['uri'])._asdict())
                data['ts'] = datetime.fromtimestamp(data['ts'])
                remote_addr, remote_port = data['remote_addr'].split(':')
                data['remote_addr'] = remote_addr
                data['remote_port'] = int(remote_port)

                cur = conn.cursor()
                cur.execute(STMT, [data[k] for k in KEYS])
                conn.commit()


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 3030

    server = ThreadedTCPServer((HOST, PORT), TCPRequestHandler)
    with server:
        ip, port = server.server_address
        print(ip, port)

        server_thread = threading.Thread(target=server.serve_forever)
        server.serve_forever()

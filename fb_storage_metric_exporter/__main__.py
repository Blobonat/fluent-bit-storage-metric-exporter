import time
import sys

from prometheus_client import start_http_server, REGISTRY
from .collector import StoreCollector


def main():
    if len(sys.argv) < 4:
        print "Usage: <EXPORTER-PORT> <FB-HOST> <FB-PORT>"
        sys.exit(1)

    fb_host = sys.argv[2]
    try:
        fb_port = int(sys.argv[3])
    except ValueError:
        print "<FB-PORT> must be an integer"
        sys.exit(1)
    try:
        server_port = int(sys.argv[1])
    except ValueError:
        print "<EXPORTER-PORT> must be an integer"
        sys.exit(1)

    collector = StoreCollector(fluent_bit_host=fb_host, fluent_bit_port=fb_port)
    REGISTRY.register(collector)
    start_http_server(server_port)
    while True:
        time.sleep(30)  # Server runs in daemon thread


if __name__ == '__main__':
    main()

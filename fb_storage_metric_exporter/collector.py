from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily

from .util import request_fb_storage_metrics
from .parser import byte_str_to_int


class StoreCollector(object):
    def __init__(self, fluent_bit_host, fluent_bit_port):
        self.fb_host = fluent_bit_host
        self.fb_port = fluent_bit_port

    def collect(self):
        """
        Collects Fluent Bit storage layer metrics available under /api/v1/storage
        :return: Gauge metrics for storage layer
        """

        data = request_fb_storage_metrics(fb_host=self.fb_host, fb_port=self.fb_port)

        # storage_layer
        if "storage_layer" in data:
            yield GaugeMetricFamily("fluentbit_storage_chunks", "Amount of currently used chunks",
                                    value=data["storage_layer"]["chunks"]["total_chunks"])
            yield GaugeMetricFamily("fluentbit_storage_chunks_mem", "Amount of chunks currently in memory",
                                    value=data["storage_layer"]["chunks"]["mem_chunks"])
            yield GaugeMetricFamily("fluentbit_storage_chunks_fs", "Amount of chunks currently in filesystem",
                                    value=data["storage_layer"]["chunks"]["fs_chunks"])
            yield GaugeMetricFamily("fluentbit_storage_chunks_fs_up", "Amount of chunks currently up",
                                    value=data["storage_layer"]["chunks"]["fs_chunks_up"])
            yield GaugeMetricFamily("fluentbit_storage_chunks_fs_down", "Amount of chunks currently down",
                                    value=data["storage_layer"]["chunks"]["fs_chunks_down"])

        # input_chunks
        if "input_chunks" in data:
            overlimit = GaugeMetricFamily("fluentbit_storage_input_overlimit",
                                          "Memory buffer limit reached for input", labels=["name"])
            mem_bytes = GaugeMetricFamily("fluentbit_storage_input_mem_bytes",
                                          "Currently used memory buffer for input in bytes", labels=["name"])
            limit_bytes = GaugeMetricFamily("fluentbit_storage_input_limit_bytes",
                                            "Memory buffer limit for input in bytes", labels=["name"])

            chunks = GaugeMetricFamily("fluentbit_storage_input_chunks",
                                       "Amount of chunks currently used for input", labels=["name"])
            chunks_fs_up = GaugeMetricFamily("fluentbit_storage_input_chunks_fs_up",
                                             "Amount of chunks for input currently up", labels=["name"])
            chunks_fs_down = GaugeMetricFamily("fluentbit_storage_input_chunks_fs_down",
                                               "Amount of chunks for input currently down", labels=["name"])
            chunks_busy = GaugeMetricFamily("fluentbit_storage_input_chunks_busy",
                                            "Amount of chunks for input currently busy", labels=["name"])
            busy_bytes = GaugeMetricFamily("fluentbit_storage_input_busy_bytes",
                                           "Size of chunks for input currently busy in bytes", labels=["name"])

            for input_name, stats in data["input_chunks"].iteritems():
                overlimit.add_metric([input_name], int(stats["status"]["overlimit"]))
                mem_bytes.add_metric([input_name], byte_str_to_int(stats["status"]["mem_size"]))
                limit_bytes.add_metric([input_name], byte_str_to_int(stats["status"]["mem_limit"]))

                chunks.add_metric([input_name], stats["chunks"]["total"])
                chunks_fs_up.add_metric([input_name], stats["chunks"]["up"])
                chunks_fs_down.add_metric([input_name], stats["chunks"]["down"])
                chunks_busy.add_metric([input_name], stats["chunks"]["busy"])
                busy_bytes.add_metric([input_name], byte_str_to_int(stats["chunks"]["busy_size"]))

            yield overlimit
            yield mem_bytes
            yield limit_bytes
            yield chunks
            yield chunks_fs_up
            yield chunks_fs_down
            yield chunks_busy
            yield busy_bytes

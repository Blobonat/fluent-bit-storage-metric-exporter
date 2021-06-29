# Fluent Bit Storage Metric Exporter

Fluent Bit provides storage layer metrics under `api/v1/storage`, but unfortunately these are only available as JSON and therefore can't be scraped by Prometheus.

This exporter runs as own web server, parses the storage layer metrics and provides them in a Prometheus compatible format.  

## Setup

This exporter ist written to run with Python 2.7.

### Installation

In order to install the exporter run `pip install .`

### Start Exporter

To start the exporter run `python -m fb_storage_metric_exporter  <EXPORTER-PORT> <FB-HOST> <FB-PORT>`

`python -m fb_storage_metric_exporter 8080 127.0.0.1 2020` will start the exporter on port `8080` and the original storage metrics are requested from `127.0.0.1:2020/api/v1/storage`.

## Provided Metrics

All metrics are provided as gauge.

### Storage Layer Metrics

- fluentbit_storage_chunks
- fluentbit_storage_chunks_mem
- fluentbit_storage_chunks_fs
- fluentbit_storage_chunks_fs_up
- fluentbit_storage_chunks_fs_down

### Input Metrics

These metrics are provided for each running input plugin. You have to configure an alias in your Fluent Bit settings to set proper names for the plugins.

- fluentbit_storage_input_overlimit
- fluentbit_storage_input_mem_bytes
- fluentbit_storage_input_limit_bytes
- fluentbit_storage_input_chunks
- fluentbit_storage_input_chunks_fs_up
- fluentbit_storage_input_chunks_fs_down
- fluentbit_storage_input_chunks_busy
- fluentbit_storage_input_busy_bytes
import requests

FB_ENDPOINT = "api/v1/storage"


def request_fb_storage_metrics(fb_host, fb_port):
    """
    Requests Fluent Bit /api/v1/storage API endpoint and parses JSON
    :param fb_host: Host of Fluent Bit
    :param fb_port: Port of Fluent Bit
    :return: Parsed JSON of /api/v1/storage
    """
    conn_url = "http://{}:{}/{}".format(fb_host, fb_port, FB_ENDPOINT)
    try:
        resp = requests.get(url=conn_url)
    except requests.exceptions.ConnectionError as e:
        print "Could not establish connection to FB: {}".format(e.message)
        return {}
    if resp.status_code != 200:
        print "Received unexpected status code {} requesting /api/v1/storage".format(resp.status_code)
        return {}
    return resp.json()

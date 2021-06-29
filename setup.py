from setuptools import setup


setup(
    name="fb_storage_metric_exporter",
    version="0.1.0",
    packages=[
        "fb_storage_metric_exporter",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=[
        "prometheus-client",
        "humanfriendly",
        "requests"
    ],
)

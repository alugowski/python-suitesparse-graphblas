"""
Find and print the latest version of SuiteSparse:GraphBLAS as published in this repo:
https://github.com/DrTimothyAldenDavis/GraphBLAS
"""

import json
from urllib.request import urlopen
from urllib.error import URLError

# fetch release data from GraphBLAS repo
for retry in range(5):
    try:
        with urlopen("https://api.github.com/repos/DrTimothyAldenDavis/GraphBLAS/releases/latest") as url:
            latest_release = json.load(url)
            break
    except URLError:
        # sleep before trying again
        from time import sleep
        sleep(1)

version = latest_release["tag_name"].lstrip("v")
print(version)
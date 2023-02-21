import requests

GAME_REQUEST_HEADER = {
        "X-Unity-Version": "2018.4.27f1",
        "Accept-Encoding": "gzip"
    }

def request_manifest(version: str) -> bytes | None:
    url = f"https://asset-starlight-stage.akamaized.net/dl/{version}/manifests/Android_AHigh_SHigh"
    resp = requests.get(url, headers=GAME_REQUEST_HEADER)
    resp.raise_for_status()
    return resp.content

def request_db(hash):
    url = f"https://asset-starlight-stage.akamaized.net/dl/resources/Generic/{hash[:2]}/{hash}"
    resp = requests.get(url, headers=GAME_REQUEST_HEADER)
    resp.raise_for_status()
    return resp.content


if __name__ == "__main__":
    man = request_manifest("10097000")
    print(f"manifest size is {len(man)} bytes")
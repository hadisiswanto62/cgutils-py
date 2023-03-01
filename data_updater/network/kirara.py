import requests
import logging

logger = logging.getLogger(__name__)


def request_truth_version() -> str | None:
    url = "https://starlight.kirara.ca/api/v1/info"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json().get("truth_version", None)


def _request_card_img_resource(res_type: str, card_id: int) -> bytes:
    url = f"https://hidamarirhodonite.kirara.ca/{res_type}/{card_id}.png"
    resp = requests.get(url)
    resp.raise_for_status()
    logger.info(f"Card icon for {card_id} retrieved.")
    return resp.content


def request_card_icon(card_id: int) -> bytes:
    return _request_card_img_resource("icon_card", card_id)


if __name__ == "__main__":
    print(request_truth_version())

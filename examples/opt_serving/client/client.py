import requests
from typing import Dict, Optional

DEFAULT_URL = "https://opt.alpa.ai/completions"


class Client(object):

    def __init__(
        self,
        url: Optional[str] = None,
    ) -> None:
        if url is None:
            url = DEFAULT_URL

        self._url = url

    def generate(
        self,
        prompt: str,
    ) -> Dict:
        pload = {
            "prompt": prompt,
        }
        result = requests.post(
            self._url,
            json=pload)

        return result.json()

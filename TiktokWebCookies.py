import requests

def get_ttwid():
    """
    Fetches the 'ttwid' cookie from TikTok's signup page.
    This cookie is often required for authenticated or semi-authenticated requests to TikTok's endpoints.
    """
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/123.0.0.0 Safari/537.36'
        ),
        'Referer': 'https://www.tiktok.com/',
        'Accept': (
            'text/html,application/xhtml+xml,application/xml;'
            'q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
            'application/signed-exchange;v=b3;q=0.7'
        ),
        'Accept-Language': 'en-US,en;q=0.9',
    }

    response = requests.get('https://www.tiktok.com/signup', headers=headers)

    for cookie in response.cookies:
        if cookie.name == 'ttwid':
            return cookie.value
    return None


def get_mstoken():
    """
    Fetches the 'msToken' cookie by making a preflight OPTIONS request to TikTok's tracking endpoint.
    This cookie may be necessary for sending telemetry or analytics data to TikTok services.
    """
    headers = {
        'Origin': 'https://www.tiktok.com',
        'Access-Control-Request-Method': 'POST',
        'Access-Control-Request-Headers': 'x-mssdk-info',
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/123.0.0.0 Safari/537.36'
        ),
        'Referer': 'https://www.tiktok.com/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    response = requests.options('https://mssdk-va.tiktok.com/web/report', headers=headers)

    for cookie in response.cookies:
        if cookie.name == 'msToken':
            return cookie.value
    return None


if __name__ == "__main__":
    print("msToken:", get_mstoken())
    print("ttwid:", get_ttwid())

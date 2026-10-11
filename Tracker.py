import feedparser, requests, os

# GitHub secret se lega - tumhe yaha likhne ki zarurat nahi
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

HANDLES = [
    "realDonaldTrump",
    "federalreserve",
    "narendramodi",
    "FinMinIndia",
    "OPECSecretariat",
    "RBI",
    "elonmusk"
]
KEYWORDS = ["India", "tariff", "Russian oil", "OPEC", "crude", "repo rate", "SEBI", "FII", "downgrade"]

def send_msg(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=data)

# Free Nitter instances - ek fail ho to dusra
NITTERS = ["nitter.poast.org", "nitter.privacydev.net"]

for handle in HANDLES:
    try:
        for nitter in NITTERS:
            rss_url = f"https://{nitter}/{handle}/rss"
            feed = feedparser.parse(rss_url)
            if len(feed.entries) > 0:
                latest = feed.entries[0]
                tweet_text = latest.title

                for word in KEYWORDS:
                    if word.lower() in tweet_text.lower():
                        msg = f"""🚨 <b>TREMOR ALERT!</b>
<b>Kaun:</b> @{handle}
<b>Loc:</b> {"Outside India (USA) - NUCLEAR" if handle in ["realDonaldTrump","federalreserve","OPECSecretariat"] else "Inside India"}
<b>Tweet:</b> {tweet_text}

<b>Impact:</b> Nifty 0.6%+ / BankNifty 0.8%+ / MCX Crude 1.2%+ expected
<b>Stocks:</b> ONGC, RELIANCE, INFY, BANKNIFTY

<b>Time:</b> Auto check via GitHub
"""
                        send_msg(msg)
                        print(f"Alert sent for {handle}")
                        raise StopIteration # ek alert ke baad next handle pe jao
                break # RSS mil gaya to next handle
    except StopIteration:
        continue
    except Exception as e:
        print(f"Skip {handle}: {e}")
        continue

print("Check done")

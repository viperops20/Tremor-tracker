import feedparser, requests, os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

HANDLES = [
    # 1. GLOBAL TREMOR - 1 tweet = $Trillion move
    "realDonaldTrump",
    "federalreserve",
    "elonmusk",
    "HindenburgRes", # Adani crash wala
    "BillAckman",
    "Carl_C_Icahn",
    "michaeljburry", # TheBigShort - crash warning

    # 2. INDIAN POLICY TREMOR - Nifty direct
    "PMOIndia",
    "narendramodi",
    "nsitharaman",
    "FinMinIndia",
    "RBI",
    "DasShaktikanta",
    "SEBI_India",
    "OPECSecretariat",
    "USTradeRep",

    # 3. NEWS BREAKER - Algo fastest
    "business", # 【entity-Bloomberg¦canonical_name=Bloomberg】 main
    "【entity-Reuters¦canonical_name=Reuters】",
    "【entity-ReutersIndia¦canonical_name=Reuters】",
    "CNBCTV18Live",
    "moneycontrolcom",
    "ETNOWlive",
    "BBGIndia"
]

KEYWORDS = [
    "India", "tariff", "Russian oil", "OPEC", "crude", "repo rate",
    "SEBI", "FII", "sanction", "Adani", "short", "crash", "downgrade",
    "earnings", "block deal", "bulk deal", "GST", "Capital Gains",
    "inflation", "rate hike", "ban", "fraud"
]

def send_msg(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=data)

NITTERS = ["nitter.poast.org","nitter.privacydev.net","nitter.fdn.fr"]

for handle in HANDLES:
    try:
        for nitter in NITTERS:
            rss_url = f"https://{nitter}/{handle}/rss"
            feed = feedparser.parse(rss_url)
            if len(feed.entries) > 0:
                tweet_text = feed.entries[0].title
                for word in KEYWORDS:
                    if word.lower() in tweet_text.lower():
                        msg = f"🚨 <b>TREMOR ALERT!</b>\n<b>Source:</b> @{handle}\n<b>Trigger:</b> {word}\n<b>Tweet:</b> {tweet_text}\n\n<b>Action:</b> Check Nifty/BankNifty/Oil stocks"
                        send_msg(msg)
                        break
                break
    except:
        continue
        # TEST MESSAGE - Har run pe ayega ki bot zinda hai
send_msg(f"✅ Bot Live! {len(HANDLES)} handles scanned at 09:xx AM - No tremor now. All clear.")
print(f"Scanned {len(HANDLES)} handles - Done")

print(f"Scanned {len(HANDLES)} handles - Done")

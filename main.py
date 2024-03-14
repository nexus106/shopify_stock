import os
import requests
import lxml.html
from dotenv import load_dotenv

load_dotenv()


def send_line_notify(notification_message):
    line_notify_token = os.environ.get("LINE_NOTIFY_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {line_notify_token}"}
    data = {"message": f"{notification_message}"}
    requests.post(line_notify_api, headers=headers, data=data)


url = "https://hihatt.myshopify.com/products/hihatt-distribution-centre-t-shirt?variant=42713737986179"

response = requests.get(url)
html = lxml.html.fromstring(response.content)

stock = html.xpath("//*[@id='AddToCart--product-template']/span")

if "売り切れ" in stock[0].text:
    print("売り切れ")
    send_line_notify("売り切れ")
else:
    print("在庫あり")
    send_line_notify("在庫あり " + url)

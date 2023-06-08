from pypresence import Presence
import time

client_id = "1116497150323474513"

RPC = Presence(client_id)

RPC.connect()


RPC.update(
    state="HI, I'm busy, maybe, you can check <3",
    large_image="calendar",
    buttons=[{"label": "Check my Calendar :)", "url": "https://calendar.google.com/calendar/embed?src=uv.angroys%40gmail.com&ctz=Europe%2FChisinau"}]
)



while True:
    time.sleep(60)
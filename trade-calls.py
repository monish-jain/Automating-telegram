from telethon import TelegramClient, events
api_id = 'your id'
api_hash = 'your hash'

client = TelegramClient('anon' , api_id , api_hash)

@client.on(events.NewMessage)
async def handler(event):
    chat_id = event.chat_id
    lst = [-1211127657, -1331930496, -1432894333, -1491733472, -1365342296, -1348184574, -1284622666, -1335514329, -1451574494, -1448812977, -1412460783, -1328902742, -1250847851, -508036769, -1505558977, -1578935580, -1337305205, -1387893163, -1274283273, -1303238692, -1432894333, -1415085207]
    if chat_id in lst:
        msg = event.raw_text
        print(type(msg))
        lst2 = ['buy', 'sell', 'Buy', 'Sell', 'BUY', 'SELL']
        res = msg.split()
        for i in res:
            if i in lst2:
                await client.send_message(-514132540, msg)
                break

client.start()
client.run_until_disconnected()

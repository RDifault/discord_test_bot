import requests, datetime, asyncio, time, random

start = time.time()

while True:
    
    #Testing
    # payload = {
    # 'content': "Ngen"
    # }
    
    #Gacha Bola boy
    payload = {
    'content': "<@668075833780469772> claim"
    }

    header = {
    'authorization': 'NTIzMTMxMjUwODE1NDAyMDAw.GhIXhG.Z5K3SXnYWCrTFP0wvZ5l_VepgWEvyJ-q4X-qB8'
    }

    #Gacha Bola boy
    r = requests.post('https://discord.com/api/v9/channels/1040452108807307314/messages', data=payload, headers=header)

    #Test Server
    # r = requests.post('https://discord.com/api/v9/channels/1062736094883479552/messages', data=payload, headers=header)

    seconds = [3609, 3617, 3633, 3641, 3663, 3699, 3714]

    test = [10, 15, 20]

    chosen_test = random.choice(test)

    chosen_rand = random.choice(seconds)

    def countdown_timer(timer):

        while(timer):
            mins, secs = divmod(timer, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print("Next Claim: ", timeformat, end='\r')
            time.sleep(1)
            timer -= 1
    
    countdown_timer(chosen_rand)

    # time.sleep(chosen_test - ((time.time() - start) % chosen_test)) 




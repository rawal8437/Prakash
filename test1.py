import requests as s

resp = s.post('https://app.magmail.eu.org/get_keys', json={'link':'https://cpvod.testbook.com/659ba2ba1ffd3734c48d6498/playlist.m3u8'})

print(resp.text)


headers = {
                    'Host': 'https://app.magmail.eu.org/get_keys',
                    
                    'user-agent': 'Mobile-Android',
                    
                    'device-id': 'c28d3cb16bbdac01',
                    'device-details':
                    'Xiaomi_Redmi 7_SDK-32',
                    'accept-encoding': 'gzip, deflate, br',
                    
                    
                }

                params = (('url', f'{url}'), )

                response = requests.get(
                    'https://app.magmail.eu.org/get_keys',
                    headers=headers,
                    params=params)
                # print(response.json())
                url1 = response.json()['url']
            else:
                url1 = url

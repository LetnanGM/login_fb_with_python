import os, sys, time, random, requests
from bs4 import BeautifulSoup as bs

url = 'http://www.facebook.com/login.php'

useragent = "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

def Login():
    username = input("[+] phone or email : ")
    pasw = input("[+] Password : ")
    
    try:
        ses = requests.Session()
        ses.headers.update({
            'User-Agent': useragent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en_US',
            'cache-control': 'max-age=0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1'
        })

        with ses.get(url) as response_bodyH:
            inspectt = bs(response_bodyH.text, 'html.parser')
            lsd_key = inspectt.find('input', {'name': 'lsd'})['value']
            jazoest_key = inspectt.find('input', {'name': 'jazoest'})['value']
            m_ts_key = inspectt.find('input', {'name': 'm_ts'})['value']
            li_key = inspectt.find('input', {'name': 'li'})['value']
            
            try_number_tag = inspectt.find('input', {'name': 'try'})
            try_number_key = try_number_tag['value'] if try_number_tag else ''

            unrecognized_tries_key = inspectt.find('input', {'name': 'unrecognized_tries'})['value']
            bi_xrwh_key = inspectt.find('input', {'name': 'bi_xrwh'})['value']

        data = {
            'lsd': lsd_key,
            'jazoest': jazoest_key,
            'm_ts': m_ts_key,
            'li': li_key,
            'try': try_number_key,
            'unrecognized_tries': unrecognized_tries_key,
            'bi_xrwh': bi_xrwh_key,
            'email': username,
            'pass': pasw,
            'login': 'Log In'
        }
        
        response_bodyH = ses.post(url, data=data, allow_redirects=True, timeout=300)
        open("response.html", "wb").write(response_bodyH.content)
        cookie = str(ses.cookies.get_dict())
        if 'checkpoint' in cookie:
            sys.exit("Akun kamu terkena checkpoint! oleh facebook")
        elif 'c_user' in cookie:
            print(f"\nSuccessfully Log in!")
            informasi = f"""
            [+] Berikut informasi akun :
               </> Cookie : {cookie}
               </> token : (ga gw kasih awokawok)
               </> username : {username}
               </> password : {pasw}
            [+]
            """
            print(informasi)
        else:
            print(f"Tidak dapat log in!, username atau password salah!")
            sys.exit(0)
    except requests.exceptions.ConnectionError:
        print("jaringan kamu buruk nih")
        sys.exit(0)
    except KeyboardInterrupt:
        print("program dihentikan dengan ctrl+c!")
        sys.exit(0)

Login()

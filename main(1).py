from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from random import choice
import requests
from datetime import datetime
import schedule

###############################
group_link = "https://splus.ir/joingroup/AHVkWc1uzikM1_xEyngFkw"
group_id = "-1007693401"
###############################
error_log = []





POWER = "ON"


fohsh = '''کیر 
کون
کث 
 کص
اوبی
اوبنی
جنده
حرومزاده
مادر سگ
پدر سگ
خارکصته
بی ناموص
حشری
پورن
سکس
سوپر
ایتا
روبیکا
سگ
بی پدر
بی مادر
بی پدر مادر
بی همه چیز
حرومی
حرومزاده
حروم خور
جاکش
دیوث
پوفیوز
کسکش
کصکش
کثکش 
بی بوته
بوته
کص ننت
کیرم تو کص ننت
مادر جنده
ننه جنده
مادر خرمی
مادرتو گاییدم
مادر قهوه
کص مادرت
کص
کیرم تو پدرت
توقف کص ننت
ننت زیر پامه
ننه کسه
ننه کسع
کیر همه اعضای گروه تو کص ننت
کیر رفیقام تو کص ننت
لاشی
مادر لاشی
پدر لاشی
پدر سگ
مادر سگ
خارتو گاییدم
خواهرتو گایدم
پدر کونی
مادرتو کردم
کص عمت
گایید
احمق
عوضی
بی شعور
 شتر 
گراز
گاو 
کص
مص
موس
کیر عرب
عرب کیر
کص مخ
کص گیج
ک.ص.م.خ
ک.ی.ر
بیشعور
ثلام
صلام
خبم
خبی
سیلام
سلم
خبی
خبم
ثلام
ثلم
سلوم'''

firefox_driver_path = 'geckodriver'
service = Service(firefox_driver_path)

firefox_options = Options()
firefox_options.headless = True  
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-gpu")


driver = webdriver.Firefox(service=service, options=firefox_options)


driver.get(f"https://web.splus.ir/#{group_id}")
try:
    phone_number = input("Your phone number :")
    phone_input = driver.find_element(By.ID , "sign-in-phone-number")
    phone_input.click()
    phone_input.send_keys(phone_number)
    driver.find_element(By.CLASS_NAME , "Button").click()
    sleep(3)
    code = input("Your Code :")
    code_input = driver.find_element(By.ID , "sign-in-code")
    code_input.click()
    code_input.send_keys(code)
    sleep(2)
    input("The robot has successfully turned on ✅ (enter to start)")
except:
    print("Error : please restart the bot ❌🔄")



def Send_msg(text):

    ActionChains(driver).context_click(msg_element).perform()
    sleep(0.1)
    reply_option = driver.find_element(By.XPATH, "//div[text()='پاسخ']")
    reply_option.click()
    sleep(0.1)


    message_input = driver.find_element(By.ID,"editable-message-text")

    
    message_input.click()  
    message_input.send_keys(text)

    
    sleep(0.2)

    
    send_button = driver.find_element(By.CSS_SELECTOR,".Button.send.default.secondary.round.click-allowed")

    
    send_button.click()


    

banner = f"""لــینک گــروه :

{group_link}

مارو به دوستاتون معرفی کنید!"""

help = '''کارایی که میتونم انجام بدم :
1 - خوش‌آمد گویی به کاربران جدید
2 - خداحافظی با کاربرانی که از گروه خارج میشوند
3 - قابلیت ضد لینک ( حذف لینک ها )
4 - قابلیت " بگو " ( میتوانید حرف های ربات را کنترل کنید )
5 - ارسال لـینک گروه با دستور " لـینک گروه "
6 - ارسال جـوک با دستور " جـوک "
7 - ارسال داسـتان با دستور " داسـتان "
8 - ارسال زمان به روز با دستور " سـاعت "
9 - ارسال تاریخ با دستور " d‌ate/ "
10 - ارسال بیوگرافی برای اکانت ها با دستور " bio/ "
11 - ارسال دانستنی با دستور " danesh/ "
12 - تعامل با کاربر ( ساده )
13 - قابلیت ماشین حساب با دستور /math 10+10'''
msg = []
last_lenth = 0
# messages = driver.find_elements(By.CSS_SELECTOR, ".message-content-wrapper .message-content.text .content-inner .message-meta-data-position .fix-word-bubble .contWrap")

message_input = driver.find_element(By.ID,"editable-message-text")

###########################
message_input.click()  
message_input.send_keys("ربات روشن شد !\nنوروزتان پیروز 🥳برای اطلاع از دستورات بات میتوانید دستور 'راهنما' را ارسال کنید.")

    
sleep(1)

    
send_button = driver.find_elements(By.CSS_SELECTOR,".Button.send.default.secondary.round.click-allowed")[0]

    
send_button.click()
#####################
while True:
    
    try:
        msg_element = None
            
        messages = driver.find_elements(By.CSS_SELECTOR, ".message-list-item")#-item
        messages = messages[-1]

        
            
        

        if messages.get_attribute("class").find("ActionMessage") != -1:
            msg_element = messages.find_element(By.CSS_SELECTOR, "span")
            type = "glass"
            
        else:
            msg_element = messages.find_element(By.CSS_SELECTOR, ".text-content")
                # except:
                #     msg_element = message.find_element(By.CSS_SELECTOR, ".message-content-wrapper .message-content.text .content-inner .message-meta-data-position .fix-word-bubble .contWrap")
            type = "normal"

        try:
            is_admin = messages.find_element(By.CSS_SELECTOR, ".admin-title")
        except:
            pass
        # try:
        #     embedMsg = messages.find_element(By.CSS_SELECTOR, ".EmbeddedMessage")
        # except:
        #     pass
        # if embedMsg:
        #         try:
        #             is_admin = messages.find_element(By.CSS_SELECTOR, ".admin-title")
        #         except:
        #             pass
        #         replied_message = messages.find_element(By.CSS_SELECTOR, ".message-subheader .EmbeddedMessage")
        #         if (msg_element.text == "/ban" ):
        #             reply_text = embedMsg.find_element(By.CSS_SELECTOR, ".last-message-text-style").text
        #             title_name = replied_message_sender = embedMsg.find_element(By.CSS_SELECTOR, ".message-title").text
        #             replied_message.click()
        #             sleep(0.5)
        #             messages_now = driver.find_elements(By.CSS_SELECTOR, ".message-list-item")
        #             for i in messages_now:
        #                 title__name = i.find_element(By.CLASS_NAME , "message-title-name")
                        
        #             replied_message_element = messages_now.find_element(By.CLASS_NAME , "message-title-name")
        #             if replied_message_element.text == title_name:
                        
        #                 print(reply_text , "\n" , title_name)
        #                 Send_msg("با موفقیت بن شد")
#########################################################
        # except Exception as e:
        #     error = e
        #     pass
                    
            

            # message = messages[-1]
            # if message.get_attribute("class").find("ActionMessage") != -1:
            #     msg_element = message.find_element(By.CSS_SELECTOR, "span")
            #     type = "glass"
            # else:
            #     msg_element = message.find_element(By.CSS_SELECTOR, ".message-content .content-inner .message-meta-data-position .fix-word-bubble .contWrap")
            #     type = "normal"

            
        last_message_element = msg_element
        last_msg = last_message_element.text
        Len_last_msg = len(last_msg)
        if type == "glass":
            last_msg = last_message_element.text
        elif type == "normal":
            last_msg = last_msg[0:Len_last_msg-6]
        last_lenth = len(msg)
        hello_list = ["ســلام عزیزم !" , "ســلام ! خـوبی؟" , "ســلام به روی ماهت😍" , "درود بر تو !", "سـلام به روی ماهت! گروه بدون تو صفا نداره." , "سـلام قشنگم!"]
        last_message = last_message_element.text.strip()
        if last_msg == "/ON" and is_admin and POWER == "ON":
            pass

        if POWER=="OFF" and last_message == "/ON" and is_admin:
            POWER = "ON"
            Send_msg("ربات با موفقیت فعال شد✅")

        if last_message=="/OFF" and is_admin and POWER=="ON":
            POWER = "OFF"
            Send_msg("ربات خاموش شد 💤")

        if POWER == "ON":
            if "پیوست" in last_msg and type == "glass":
                Send_msg("🥳😍سـلام برادر😂👍عیدت مبارک")
            if (("http://" in last_msg) or ("https://" in last_msg) or ("www." in last_msg) or (".com" in last_msg) or (".ir" in last_msg) or (".io" in last_msg))  :
                if (group_link in last_msg):
                    pass
                else :
                    ActionChains(driver).context_click(last_message_element).perform()
                    sleep(0.1)
                    delete_option = driver.find_element(By.XPATH, "//div[text()='حذف']")
                    delete_option.click()
                    sleep(0.1)
            
            
                    confirm_button = driver.find_element(By.XPATH, "//button[text()='حذف']")
                    confirm_button.click()

            elif "ترک کرد" in last_msg and type=="glass":
                left_message = "خدا پشت پناهت"
                Send_msg(left_message)
            elif "بگو" in last_msg[:3]:
                word = last_msg[3:]
                Send_msg(word)
            elif "سلام" in last_msg[:10]:
                Send_msg(choice(hello_list))
            elif "لینک گروه" in last_msg:
                Send_msg(banner)
            elif "جوک" in last_msg:
                joke = requests.get("http://api.codebazan.ir/jok/").text
                Send_msg(joke)
            elif "سازندت" in last_msg:
                Send_msg("من توسط **امیرعلی امامی** ساخته شدم")
            elif "راهنما" in last_msg[:6] :
                Send_msg(help)
            elif "داستان" in last_msg:
                dastan = requests.get("http://api.codebazan.ir/dastan/").text
                Send_msg(dastan)
            elif " ریم" in last_msg:
                Send_msg("ععععع.چرا؟؟؟؟\nبزار تو گروه بمونه چکارش داری؟؟")
            elif "ساعت" in last_msg:
                time_now = datetime.now().strftime("%H:%M:%S")
                Send_msg(f"همین الان سـاعت :\n {time_now}\nمیباشد.")
            elif "ربات" == last_msg:
                Send_msg("جانم؟منو صدا زدی؟")
            elif "خوبی" in  last_msg:
                Send_msg("هعی.آره ، خوبم")
            elif "پشمام" in last_msg or "برگام" in last_msg:
                Send_msg("نگو وای برگـام وای پشمـام .\nبگو 'چه جالب !'")
            elif "چیکار می تونی بکنی" in last_msg or "چه کار می تونی بکنی" in last_msg:
                Send_msg(help)
            elif "/date" in last_msg:
                date_object = requests.get("http://api.codebazan.ir/time-date/?td=date").text
                Send_msg(date_object)
            elif "/math" in last_msg:
                math = last_msg[5:]
                javab = eval(math)
                Send_msg(javab)
                    
                    
            elif "/bio" in last_msg[:8]:
                bio = requests.get("https://api.codebazan.ir/bio/").text
                Send_msg(bio)
            elif "/danesh" in last_msg[:12]:
                danestani = requests.get("http://api.codebazan.ir/danestani/").text
                Send_msg(danestani)
            elif "/wiki " in last_msg[:6]:
                query = last_msg[6:]
                try:
                    respone = (requests.get("http://api.codebazan.ir/wiki/?search={}".format(query))[:1000]) + "\t ..."
                    Send_msg(respone)
                except:
                    pass


            for i in fohsh.split("\n"):
                if  i in last_msg:
                    ActionChains(driver).context_click(last_message_element).perform()
                    sleep(0.1)
                    delete_option = driver.find_element(By.XPATH, "//div[text()='حذف']")
                    delete_option.click()
                    sleep(0.1)
            
            
                    confirm_button = driver.find_element(By.XPATH, "//button[text()='حذف']")
                    confirm_button.click()
                
            else :
                pass

            
    
    except Exception as e:
        print(e)

    sleep(0.1)
        
driver.quit()

from selenium import webdriver
import time, sys
from random import randint
from twilio.rest import Client
import pandas as pd

sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import error_handling, open_chrome

def twilio():
    global client
    twilio_dict = pd.read_pickle('../../../API Keys/Twilio_API.p')
    twilio_acc = list(twilio_dict.values())[0]
    twilio_cred = list(twilio_dict.values())[1]
    client = Client(twilio_acc, twilio_cred)  # For Twilio

def text_me(message):
    twilio_number = '+19562653630'
    jamie_number = '+19568214550'
    valeria_number = '+19564370322'
    #phone_number = '+1%s' % input('What is your phone number?')

    client.messages.create(to=valeria_number,
                           from_=twilio_number,
                           body=message)


insta_list = ['https://instagram.com/p/Bjc3iyFBCC6/', 'https://www.instagram.com/p/BjZaFeTF7HU/', 'https://instagram.com/p/BjeqadDhzrb/', 'https://instagram.com/p/Bi0sQhggEF9/', 'https://www.instagram.com/p/Bjehh8MHZ2A/', 'https://instagram.com/p/Bjep4h-nuHV/', 'https://instagram.com/p/Bjeo9-rHSc7/', 'https://instagram.com/p/BjVaQNlHTAq/', 'https://www.instagram.com/p/BjNoo5pHezr/', 'https://instagram.com/p/BjesfoRBfGz/', 'https://instagram.com/p/Bjev5-zAWHw/', 'https://www.instagram.com/p/Bjc8jY5nsOV/', 'https://instagram.com/p/BjcBcBJn__q/', 'https://www.instagram.com/p/BjIHJovhtYV', 'https://instagram.com/p/BjezFw2lp9_/', 'https://instagram.com/p/Bjey7loAITB/', 'https://www.instagram.com/p/Bje1MB4FgcA/', 'https://www.instagram.com/p/Bje1qBGnZ0V/', 'https://www.instagram.com/p/BjdiqP5HbE5/', 'https://instagram.com/p/Bje2tzhh43b/', 'https://www.instagram.com/p/BjeoxyhFvtB/', 'https://instagram.com/p/Bje4gOXjn7e/', 'https://instagram.com/p/Bje4TOJhXg7/', 'https://www.instagram.com/p/Bje3G2iBSPq/', 'https://instagram.com/p/Bje4q2bByW8/', 'https://instagram.com/p/Bje6hqwFE-D/', 'https://instagram.com/p/Bje7IucAagY/', 'https://www.instagram.com/p/Bje7vVPgROf/', 'https://www.instagram.com/p/Bje596KlizS/', 'https://www.instagram.com/p/BjdDgb_BUF5/', 'https://www.instagram.com/p/BjbNpTRggZ5/', 'https://www.instagram.com/p/Bje9HrhhP0b/', 'https://www.instagram.com/p/Bje8LC2AUK8/', 'https://www.instagram.com/p/Bjctf6rBpFR/', 'https://www.instagram.com/p/BjfALB1gQ3K/', 'https://www.instagram.com/p/BjfBBiJjt-Y/', 'https://www.instagram.com/p/BjehmZnh3cz/', 'https://www.instagram.com/p/BjfB6bEhUyC/', 'https://instagram.com/p/BjfD7xSB0NQ/', 'https://instagram.com/p/Bjcpp8tH3Ux/', 'https://www.instagram.com/p/Bjd3LUBli44/', 'https://instagram.com/p/Bje_riGFdeN/', 'https://instagram.com/p/BjfG5hwgwK7/', 'https://www.instagram.com/p/BjfHAYOBh6G/', 'https://instagram.com/p/BjfGa7Ah7JX/', 'https://instagram.com/p/BjfHBcth5na/', 'https://www.instagram.com/p/BjfHU0HBwbc/', 'https://instagram.com/p/Bje1Yq5H3__/', 'https://www.instagram.com/p/BjfCJ3YjSZI/', 'https://www.instagram.com/p/BjfHPHOAT22/', 'https://www.instagram.com/p/Bjec2nDDVls/', 'https://instagram.com/p/BjfBP-LnrWo/', 'https://instagram.com/p/BjfEGofl9Nu/', 'https://www.instagram.com/p/BjfJHUPBB5P/', 'https://www.instagram.com/p/BjevLVXnj8m/', 'https://www.instagram.com/p/Bje49MylDnu/', 'https://instagram.com/p/BjfLUJohd3G/', 'https://www.instagram.com/p/BjfJ3y5ABUU/', 'https://www.instagram.com/p/BjfF72EA_y1/', 'https://www.instagram.com/p/BjdwFnqBQss/', 'https://www.instagram.com/p/BjfMTiVHnjS/', 'https://www.instagram.com/p/BjfLjlHgFBt', 'https://instagram.com/p/BjfNbcmHxb9/', 'https://www.instagram.com/p/BjeFecPhQCq/', 'https://www.instagram.com/p/BjfOCh_jBcl/', 'https://www.instagram.com/p/BjfN9CiBB6w/', 'https://www.instagram.com/p/Bjezx_JHoi6/', 'https://www.instagram.com/p/BjexTTDAIJZ', 'https://instagram.com/p/BjfOZJzByFs/', 'https://www.instagram.com/p/BjfOrUDBe1L/', 'https://instagram.com/p/BjfDI49FoAI/', 'https://www.instagram.com/p/BjdMTlmAJyr/', 'https://instagram.com/p/BjfJ-bpha94/', 'https://www.instagram.com/p/BjfPeGYhdkz/', 'https://instagram.com/p/BjfQKiDlOna/', 'https://www.instagram.com/p/BjfPuGMh-bd/', 'https://www.instagram.com/p/BjfQ8P0lLuD/', 'https://instagram.com/p/BjfR21VH2Nf/', 'https://www.instagram.com/p/BjfRb3-lE6i/', 'https://www.instagram.com/p/BjfRiW5hb9x/', 'https://instagram.com/p/BjfSiAvlKyo/', 'https://www.instagram.com/p/BjfRs7LDXey/', 'https://www.instagram.com/p/BjfSxl8hW5x/', 'https://instagram.com/p/BjfJkmxnBeW/', 'https://instagram.com/p/BjfTUIlngxa/', 'https://www.instagram.com/p/BjfETHIHHLK/', 'https://instagram.com/p/BjfSfl-BYXU/', 'https://instagram.com/p/BjfU5c2hJII/', 'https://instagram.com/p/BjfUtqXBEVw/', 'https://instagram.com/p/BjfVgfsFN0w/', 'https://www.instagram.com/p/BjckOEQhpUJ/', 'https://www.instagram.com/p/BjfQeeYAuUo/', 'https://www.instagram.com/p/BjfWJDJDFEn', 'https://www.instagram.com/p/BjQ1jfzH8oh/', 'https://instagram.com/p/BjfOrl2nzRf/', 'https://www.instagram.com/p/BjfV6Q7nfpp/', 'https://instagram.com/p/BjfXqOmBmsl/', 'https://www.instagram.com/p/Bjd1LuOBWDX/', 'https://www.instagram.com/p/BjfHykuBkyA/', 'https://www.instagram.com/p/BjfO4eCDIgb/', 'https://www.instagram.com/p/BjfZxVHB3F-/', 'https://www.instagram.com/p/Bjc_Uh-H8Jo/', 'https://www.instagram.com/p/BjfcOj7BGpc/', 'https://instagram.com/p/BjfccS3BFHc/', 'https://instagram.com/p/BjfdHd-jflD/', 'https://www.instagram.com/p/BjfawNDBDsB/', 'https://www.instagram.com/p/BjfdzJuAcxs/', 'https://www.instagram.com/p/BjfeMzpDZs9/?taken-by=femmeennoir', 'https://www.instagram.com/p/BjfGq2NDl35/', 'https://www.instagram.com/p/BjffWC5lfux/', 'https://instagram.com/p/BjcwGm9FSiK/', 'https://instagram.com/p/BjfhTb_H-g7/', 'https://www.instagram.com/p/Bjfg9N4HFqe/', 'https://www.instagram.com/p/Bjfhg-PnW6m/', 'https://www.instagram.com/p/BjfhyTpnDcJ/', 'https://instagram.com/p/BjfdYjABr3c/', 'https://www.instagram.com/p/Bjfi4f2hU54/', 'https://www.instagram.com/p/BjfCucbBRmr/', 'https://instagram.com/p/BjfjT2Xnoeq/', 'https://www.instagram.com/p/BjfiBD7BOvp', 'https://www.instagram.com/p/BjfJK4xnelx/', 'https://instagram.com/p/Bjfli75nePr/', 'https://www.instagram.com/p/Bjcs1isgV9M/', 'https://www.instagram.com/p/BjeVZy2BMMv/', 'https://www.instagram.com/p/BjdU2AQn09R/', 'https://www.instagram.com/p/BjfjVFRAsLX/', 'https://instagram.com/p/BjflPWcg-4p/', 'https://instagram.com/p/Bjfn6w9BbTn/', 'https://www.instagram.com/p/Bjd0v3kHxtz/', 'https://www.instagram.com/p/Bjfncgsh8XV/', 'https://www.instagram.com/p/BjSjrhKlXPH/', 'https://instagram.com/p/BjfjEVNhIpP/', 'https://www.instagram.com/p/BjdZBCgBYLD/', 'https://www.instagram.com/p/BjfpmJZASaQ/', 'https://www.instagram.com/p/BjfnNeSH1kd/', 'https://www.instagram.com/p/BjfjFnqDNF_/', 'https://www.instagram.com/p/Bjfp5yrB0gD/', 'https://instagram.com/p/BjdWSgOF_er/', 'https://www.instagram.com/p/BgVKCWTHNYj/', 'https://instagram.com/p/BjfaYYJjuiv/', 'https://www.instagram.com/p/BjfeB48lUyh/', 'https://instagram.com/p/BjfyLoNDDMW/', 'https://instagram.com/p/BjfvyHUgOdn/', 'https://instagram.com/p/BjfsGmSHP9H/', 'https://instagram.com/p/BjftKbnBR8A/', 'https://www.instagram.com/p/BjdmdSoBaZN/', 'https://www.instagram.com/p/BjfzUfLBbY1/', 'https://www.instagram.com/p/Bjfzk_4FfGs/', 'https://www.instagram.com/p/BjfPYGSh2-H/', 'https://www.instagram.com/p/BjalEmonTKS/', 'https://www.instagram.com/p/BjfzhEMBG-E/', 'https://instagram.com/p/Bjf13a6nYCT/', 'https://www.instagram.com/p/BjfYFCPlYbZ/', 'https://instagram.com/p/Bjf38OOHWVq/', 'https://www.instagram.com/p/BjfANVIln5m/', 'https://www.instagram.com/p/BjfvGh2nbab/', 'https://www.instagram.com/p/Bjf5_IRHzgN/', 'https://www.instagram.com/p/Bjf3qsPh-2L/', 'https://www.instagram.com/p/BjfSM2hAKWH/', 'https://www.instagram.com/p/BjfuRVmhc2K/', 'https://www.instagram.com/p/Bjf7oHilVZo/', 'https://www.instagram.com/p/Bjf9a56hkZO/', 'https://www.instagram.com/p/BjeUR-0nnuz/', 'https://www.instagram.com/p/BjfTilsHyUW/', 'https://www.instagram.com/p/Bjf8X3SHHtb/', 'https://www.instagram.com/p/Bjf_lsxBCVo/', 'https://www.instagram.com/p/BjdAgnCFfHL/', 'https://www.instagram.com/p/BjgAS7BBEuV/', 'https://instagram.com/p/BjgBd-dh4zK/', 'https://instagram.com/p/BjgCGQzF-sj/', 'https://www.instagram.com/p/BjfHMa0HIB1/', 'https://www.instagram.com/p/BjfBN8TFDtt/', 'https://instagram.com/p/BjdzSFblL1X/', 'https://instagram.com/p/BaxhpM9B9HA/', 'https://www.instagram.com/p/Bjfv9IYj__k/', 'https://instagram.com/p/Bjf21AwBkjf/', 'https://www.instagram.com/p/BjfjRx6hPpE/', 'https://instagram.com/p/BjgFsD3hBWy/', 'https://instagram.com/p/Bjfj1G2BmJb/', 'https://instagram.com/p/BjgFR4uD1ff/', 'https://instagram.com/p/BjgHKYqnWIj/', 'https://www.instagram.com/p/BjgGxIVHm8w/', 'https://www.instagram.com/p/Bjcx2f9h7-k', 'https://instagram.com/p/BjflrwYH9OM/', 'https://instagram.com/p/BjgJVNOFl_E/', 'https://instagram.com/p/BjXvGEqlJJb/', 'https://instagram.com/p/BjgJx66lvMP/', 'https://instagram.com/p/BjfYMv5BuoY/', 'https://www.instagram.com/p/BjgHzUAB0Bv/', 'https://instagram.com/p/BjfGYllhy8s/', 'https://instagram.com/p/BjaafzADzmD/', 'https://instagram.com/p/BjgL9H5n81J/', 'https://www.instagram.com/p/BjgMbV2g6JQ/', 'https://instagram.com/p/BjgKPcTBZ19/', 'https://instagram.com/p/BjgM-HJBlkv/', 'https://instagram.com/p/Bjfps5tgaRi/', 'https://www.instagram.com/p/BjgNFMZhDpb/', 'https://www.instagram.com/p/BjgNuZajWNN/', 'https://www.instagram.com/p/BjgOG2cgC2s/', 'https://www.instagram.com/p/BjdSoSSANWs/', 'https://instagram.com/p/BjgFih0hWWa/', 'https://www.instagram.com/p/BjgPZ-Bn2AU/', 'https://www.instagram.com/p/BjdYmCIBo18/', 'https://www.instagram.com/p/Bjc9q02H8Oz/', 'https://www.instagram.com/p/BjgIJ1UjDQI/', 'https://instagram.com/p/BjfjczSh-8i/', 'https://www.instagram.com/p/BjgTdDOBh1l/', 'https://www.instagram.com/p/BjfW0wjBzWv/', 'https://instagram.com/p/BjgLlrZh7L5/', 'https://instagram.com/p/BjgWWOjHbPx/']
print(len(insta_list))














twilio()

didnt_like = []
def like_unlike_check():
    like_elem = driver.find_elements_by_xpath("//a[@role = 'button']/span[text()='Like']")
    liked_elem = driver.find_elements_by_xpath("//a[@role = 'button']/span[text()='Unlike']")

    if len(like_elem) == 1:
        driver.execute_script(
            "document.getElementsByClassName('" + like_elem[0].get_attribute("class") + "')[0].click()")
        print('--> Image Liked!')
        time.sleep(2)
    elif len(liked_elem) == 1:
        print('--> Already Liked!')
    else:
        print('--> Invalid Like Element!')

driver = open_chrome('Liking_pics_Profile')

count = 0
for insta_picture in insta_list:
    count+= 1
    print(count, insta_picture)
    try:
        driver.get(insta_picture)
        like_unlike_check()
        time.sleep(randint(29,35))
    except:
        didnt_like.append(insta_picture)
        time.sleep(4)

text = 'Facebook pod likes complete!... We liked: ' + str(len(insta_list)) + ' pictures'
text_me(text)
print('didnt like', didnt_like)
driver.close()
print('Complete')

# ADD ABOVE TO FIX URLs
'''
# Fixing URLs
updated_insta_list = []
for url in insta_list:
    the_u = url.find('?u=')
    url = url[the_u+3:]

    url = url.replace('%3A' ,':')
    url = url.replace('%2F', '/')
    url = url.replace('%3F', '?')
    url = url.replace('%3D', '=')

    amper = url.find('&')
    updated_insta_list.append(url[:amper])

print(updated_insta_list)
'''
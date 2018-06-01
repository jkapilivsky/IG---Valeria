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


insta_list = ['https://www.instagram.com/p/BjUq1R_AKvy/', 'https://instagram.com/p/BjcHrOyBEtV/', 'https://www.instagram.com/p/BjG5u4BBlbF', 'https://instagram.com/p/BjcEK22l5-w/', 'https://www.instagram.com/p/BjaHG2vBMy8/', 'https://www.instagram.com/p/BjcJfPYnoVJ/', 'https://instagram.com/p/BjcLIBNlOnD/', 'https://www.instagram.com/p/BjcLXqeF7uP/', 'https://instagram.com/p/BjZMgZxBImC/', 'https://instagram.com/p/BjaoG7fhPWY/', 'https://www.instagram.com/p/BjbQmIXhNlR/', 'https://www.instagram.com/p/BjcKS-blD_F/', 'https://instagram.com/p/BjcOfR4F9DM/', 'https://instagram.com/p/BjcN9vohVgH/', 'https://instagram.com/p/BjcPTJDBVdm/', 'https://www.instagram.com/p/BjcP1IWgL4U/', 'https://www.instagram.com/p/BjcROteAEG3/', 'https://instagram.com/p/BjcR35CFLk7/', 'https://instagram.com/p/BjcRlU4lprg/', 'https://www.instagram.com/p/BjYbIdFBqDy/', 'https://instagram.com/p/BjcTgB2BJA0/', 'tps://www.facebook.com/groups/theladieslounge101/permalink/239836360112687/', 'https://instagram.com/p/BjXlZmVHJsK/', 'https://instagram.com/p/BjXvGEqlJJb/', 'https://www.instagram.com/p/BjcVDkFB8Pq/', 'https://instagram.com/p/BjcWuKHncjI/', 'https://www.instagram.com/p/BjcXzVjBpbI/', 'https://www.instagram.com/p/BjbkpfFF4oM/', 'https://www.instagram.com/p/Bjby5a8h14u/', 'https://instagram.com/p/BjZ1W-4BlDV/', 'https://instagram.com/p/BjcZvvVFiej/', 'https://instagram.com/p/BjcZ8dNBaan/', 'https://www.instagram.com/p/BjcaGp5hb4b/', 'https://www.instagram.com/p/Bja9WeYHRDd/', 'https://instagram.com/p/BjcauSRHGj-/', 'https://instagram.com/p/BjcdfOwFsYB/', 'https://www.instagram.com/p/BjcYyryA14c/', 'https://instagram.com/p/BjcdcX5F3a1/', 'https://www.instagram.com/p/BjceFxIhrsa/', 'https://www.instagram.com/p/BjceGvvhpKh/', 'https://www.instagram.com/p/BjcdWD-hrcC/', 'https://www.instagram.com/p/BjcdszRAicW/', 'https://www.instagram.com/p/BjZ10Xegh8F/', 'https://www.instagram.com/p/Bjcel-hFYOP/', 'https://www.instagram.com/p/BjYQcTAD1T1/', 'tps://www.facebook.com/groups/theladieslounge101/permalink/239836360112687/', 'https://www.instagram.com/p/BjcgB74l1Zh/', 'https://www.instagram.com/p/BjX1j5_hHg9/', 'https://instagram.com/p/Bjch_PHHnS1/', 'https://www.instagram.com/p/Bjcf4HWBi7X/', 'https://www.instagram.com/p/BjcajOln0N4/', 'https://www.instagram.com/p/Bjcg4T7ByxS/', 'https://instagram.com/p/Bjcj_nGnWFs/', 'https://instagram.com/p/BjbfzDAn7b5/', 'https://instagram.com/p/BjclEGxgeqf/', 'https://instagram.com/p/Bjck99gl0Tu/', 'https://instagram.com/p/BjcjmCHh2Zn/', 'https://www.instagram.com/p/BjcFdcAHMNC/', 'https://instagram.com/p/BjcmmWXnA70/', 'https://instagram.com/p/BjdK-Cfnmuz/', 'https://www.instagram.com/p/BjclXlmBUd3/', 'https://instagram.com/p/Bjcn312HS5y/', 'https://www.instagram.com/p/BjcpEwrlK2f/', 'https://www.instagram.com/p/BjbOCi-DTk0/', 'https://www.instagram.com/p/BjbFWnOHr0n/', 'https://www.instagram.com/p/BjcMRvNABJC', 'https://www.instagram.com/p/BjbDGlcjepO/', 'https://www.instagram.com/p/BjcqjAaBSr-/', 'https://www.instagram.com/p/Bjb8lZ6BjV8/', 'https://instagram.com/p/BjcorVDBjnO/', 'https://www.instagram.com/p/Bjb8Q9NgMzs/', 'https://www.instagram.com/p/BjcrsjDB0YG/', 'https://www.instagram.com/p/Bjcsa-2FSo0/', 'https://www.instagram.com/p/BjcoBcYFNu0', 'https://www.instagram.com/p/BjaOROJh58K/', 'https://www.instagram.com/p/BjcuVpJArCw/', 'https://www.instagram.com/p/BjcstoWB-iq/', 'https://www.instagram.com/p/Bjcu5Z7gd9T/', 'https://www.instagram.com/p/BjaYYg3H3lp', 'https://www.instagram.com/p/BjbGs-qnzJz/', 'https://instagram.com/p/BjcxAQ9ASdB/', 'https://www.instagram.com/p/BjaZVn_l6Vd/', 'https://instagram.com/p/BjcxnGAhxtI/', 'https://www.instagram.com/p/BjbDquhAs_U/', 'https://instagram.com/p/BjcyPSMFdYa/', 'https://www.instagram.com/p/BjcxnxOhy3y/', 'https://www.instagram.com/p/BjcRXm4nzyg/', 'https://www.instagram.com/p/BjcwGe3AN_u/', 'https://www.instagram.com/p/Bjc0U2FBnNw/', 'https://instagram.com/p/Bjc1ZNIHAQG/', 'https://instagram.com/p/Bjc2u8ElF_l/', 'https://www.instagram.com/p/Bjc2guwnENc/', 'https://www.instagram.com/p/Bjc3KZkg6QC/', 'https://www.instagram.com/p/Bjc3W2HHu_C/', 'https://www.instagram.com/p/Bjapvfshsa8/', 'https://www.instagram.com/p/BjZtG73BhgL/', 'https://www.instagram.com/p/BjZvdFMhaHq/', 'https://www.instagram.com/p/BjcM1R0h3Gb/', 'https://www.instagram.com/p/BjcLEvbBnU3/', 'https://www.instagram.com/p/Bjc6wbTBdl5/', 'https://instagram.com/p/Bjc7KmFH4kx/', 'https://instagram.com/p/BjbsMC1H1L5/', 'https://www.instagram.com/p/Bjc8k8GAtMb/', 'https://www.instagram.com/p/Bjbi6JlnQbJ/', 'https://www.instagram.com/p/Bjc9LFIH04N/', 'https://instagram.com/p/Bjci0sTHv77/', 'https://www.instagram.com/p/Bjc9kyBHKAw/', 'https://www.instagram.com/p/Bjc4nhjHFVc', 'https://www.instagram.com/p/Bjc9wwplAmL/', 'https://instagram.com/p/Bjc-bgCB3fk/', 'https://instagram.com/p/Bjc-exvlLcc/', 'https://www.instagram.com/p/Bjc_QRljESt/', 'https://instagram.com/p/Bjc-TNIh0y2/', 'https://www.instagram.com/p/Bjc_mxMAbuQ', 'https://instagram.com/p/Bjc4tBGlhq6/', 'https://www.instagram.com/p/BjdAHIBnM1g/', 'https://instagram.com/p/BjdARWChvG1/', 'https://www.instagram.com/p/Bjc-Yw8Alyc/', 'https://instagram.com/p/Bjc_5XIH2MF/', 'https://www.instagram.com/p/Bjc-d-rhNXh/', 'https://www.instagram.com/p/BjcyMkbFQv3/', 'https://instagram.com/p/Bjc9RcThMPJ/', 'https://instagram.com/p/Bjc9eqFHnwZ/', 'https://instagram.com/p/BjdBxQ3loOG/', 'https://www.instagram.com/p/BjdAtFWHVHH/', 'https://instagram.com/p/BjdCaj8hndf/', 'https://www.instagram.com/p/Bjatga_hNCx/', 'https://www.instagram.com/p/BjdDgb_BUF5/?taken-by=cassandralyndee', 'tps://www.facebook.com/grace.cheung.28?fref=gc', 'https://instagram.com/p/Bjc-qcDBPGb/', 'https://instagram.com/p/BjdFeNjBD8P/', 'https://www.instagram.com/p/BjdF9QdH624/?taken-by=piotrowskapaulina', 'https://www.instagram.com/p/BjdGfw6lQux/', 'https://www.instagram.com/p/BjdHEKmhdzy/', 'https://instagram.com/p/BjdGiiQBsEZ/', 'https://www.instagram.com/p/BjdBPhQA8Ne/', 'https://www.instagram.com/p/Bjc_Uh-H8Jo/', 'https://www.instagram.com/p/BjdH_DxAQJ-/', 'https://www.instagram.com/p/BjdIeOtlVsd/', 'https://instagram.com/p/BjdJRkLlNjc/', 'https://instagram.com/p/BjdKgGCBGbK/', 'https://instagram.com/p/BjdK9G9hKyT/', 'https://instagram.com/p/BjdMDR9ho10/', 'https://www.instagram.com/p/BjdMlGuD_1u/', 'https://instagram.com/p/BjdMQLAl_u7/', 'https://www.instagram.com/p/BjYKtvQlXWZ/', 'https://www.instagram.com/p/BjdLOkGgwii/', 'https://www.instagram.com/p/BjXRoQzjXw0/', 'https://www.instagram.com/p/BZ9jdSiAqyI', 'tps://www.facebook.com/profile.php?id=100007547205650', 'https://instagram.com/p/BjcrFTzAvEY/', 'https://www.instagram.com/p/BjcaAbonQBD/', 'https://www.instagram.com/p/BjdQAsVgI29/', 'https://www.instagram.com/p/Bjc_pMdlC9j/?hl=en%26taken-by=beatsbykd', 'https://instagram.com/p/BjdPTrtBSt9/', 'https://www.instagram.com/p/BjczC-gh1f4/', 'https://www.instagram.com/p/BjdRnvHFvFm/?taken-by=housegleaves', 'https://www.instagram.com/p/BjdSoSSANWs', 'https://instagram.com/p/BjaSgmJHC0D/', 'https://www.instagram.com/p/BjdU-GcH0td/', 'https://www.instagram.com/p/BjdTg3xFIny/', 'https://instagram.com/p/BjcbDNOhBFq', 'https://instagram.com/p/BjdWEAcBJoq/', 'https://www.instagram.com/p/BjdWzSJnvmr/', 'https://instagram.com/p/BfojaVcFlla/', 'https://www.instagram.com/p/BjdPJ9-nlxy/', 'https://instagram.com/p/BjdXHUyHSyY/', 'https://instagram.com/p/BjdWXAxl1Yg/', 'https://www.instagram.com/p/BjdP77HhOJn/', 'https://www.instagram.com/p/BjdXP3al6mb/', 'https://www.instagram.com/p/BjdYkxXFgS1/', 'https://instagram.com/p/BjdBDINlRZQ/', 'https://instagram.com/p/BjdY2MyFTsm/', 'https://www.instagram.com/p/BjdZBCgBYLD/', 'https://instagram.com/p/Bjdas3TjnOK/', 'tps://www.instagram.com/p/BjdX42VHTVI', 'https://www.instagram.com/p/BjV3AFKhNTu/', 'https://www.instagram.com/p/BjdaeaaAwao/', 'https://instagram.com/p/Bjdb5GeB49Q/', 'https://instagram.com/p/Bjc9TsEjtFm/', 'https://instagram.com/p/BjdcGdeBxdO/', 'https://www.instagram.com/p/Bjdc81vHO9h/', 'https://instagram.com/p/BjdcodFhtfe/', 'https://www.instagram.com/p/BjXSOoJFkCN/', 'https://www.instagram.com/p/Bjdd_loH6oc/', 'https://www.instagram.com/p/BjccTkElNrU/', 'https://www.instagram.com/p/Bjc-h6Eh8i8/', 'https://instagram.com/p/BjdfP23gF3u/', 'https://instagram.com/p/BjdgfJInlEp/', 'https://www.instagram.com/p/BjdgsR0lUjU/', 'https://www.instagram.com/p/Bjc6Iyyn1aK/', 'https://www.instagram.com/p/BjdLtOlBGsR/', 'https://instagram.com/p/BjddMOugVxf/', 'https://www.instagram.com/p/BjdM74FA7c8/', 'https://instagram.com/p/BjdiICfhZuN/', 'https://instagram.com/p/Bjdi6iaFxSz/', 'https://www.instagram.com/p/Bjc-Lf9FdBE/', 'https://www.instagram.com/p/BjdRQztHMKg/', 'https://www.instagram.com/p/BjdjVHKj5b7/', 'https://instagram.com/p/BjdkOfilv_d/', 'https://instagram.com/p/Bjdk-N9nWxf/', 'https://instagram.com/p/BjdlQwBALoF/', 'https://instagram.com/p/BjdlH0VBKlx/', 'https://www.instagram.com/p/BjdhkikBQVd/', 'https://instagram.com/p/BjaG1MRB6zz/', 'https://instagram.com/p/BjdnadZHR8Q/', 'https://www.instagram.com/p/BjdneTLAcD3/', 'https://www.instagram.com/p/Bjdnq_YHZwT/', 'https://www.instagram.com/p/Bjdnq_sjisc/', 'https://instagram.com/p/Bjcq4NlBe1c/', 'https://www.instagram.com/p/BjdpccCAVQu/', 'https://instagram.com/p/BjdqSA1glZM/', 'https://instagram.com/p/BjdqhGQlgoR/', 'https://www.instagram.com/p/Bjdq8biDaab/', 'https://instagram.com/p/BjdrSh1hXkG/', 'https://www.instagram.com/p/Bjdqx8XlFFt/', 'https://www.instagram.com/p/BjdqAuDHd1E/', 'https://www.instagram.com/p/BjTMsolHFNP/', 'https://www.instagram.com/p/BjcKnqGDmGe/', 'https://www.instagram.com/p/BjdueQEBCv2/', 'https://www.instagram.com/p/BjduhXqhO-B/', 'https://www.instagram.com/p/BjdeCRRBBp0/', 'https://instagram.com/p/Bjd22vcHp_0/', 'https://www.instagram.com/p/BjdoSdKD7E7']
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
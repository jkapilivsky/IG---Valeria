from selenium import webdriver
import time, sys

sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import twilio, text_me, error_handling, open_chrome

insta_list = ['https://instagram.com/p/Bitt-u6HbLD/', 'https://www.instagram.com/p/BitHkADAL3Z/?taken-by=easyweddings', 'https://instagram.com/p/Bitbrz5gXvB/', 'https://www.instagram.com/p/BiryDyEgGYJ/', 'https://instagram.com/p/Bis9YIjD0DE/', 'https://www.instagram.com/p/BitZSjrgbaU/', 'https://www.instagram.com/p/BisIaZ5lKmD/', 'https://instagram.com/p/Bitn9SdFxWM/', 'https://instagram.com/p/BiswarrHu56/', 'https://instagram.com/p/Bit15BUn0lm/', 'https://instagram.com/p/Bit1o0Ih_jY/', 'https://www.instagram.com/p/BiRJQFeBa0B/', 'https://instagram.com/p/BitvPsqnzPV/', 'https://www.instagram.com/p/BituG7vnnCA/?taken-by=cocuspocushq', 'tps://www.facebook.com/deborah.perlman.31?fref=gc', 'https://instagram.com/p/BisTD8xAA3B/', 'https://instagram.com/p/Bit5EeUABUY/', 'https://www.instagram.com/p/Bitxhm0nWLF/', 'https://www.instagram.com/p/Bit5fU_H9L6/', 'https://www.instagram.com/p/Bit9HiBHNvg/', 'https://www.instagram.com/p/Bit78QThTgK/', 'https://instagram.com/p/BittjayhBM2/', 'https://instagram.com/p/Bit-UDPH2Zc/', 'https://instagram.com/p/Bit0ue8hT8c/', 'https://instagram.com/p/BitLFutHtin/', 'https://instagram.com/p/BitPARIhTX8/', 'https://www.instagram.com/p/BisEJwcno_0/?taken-by=heyitsjenna', 'https://instagram.com/p/Bit_88JB3z_/', 'https://instagram.com/p/BitRajzBIXw/', 'https://instagram.com/p/BiuAMxKBaJ6/', 'https://www.instagram.com/p/BiuAZwChabZ/?taken-by=carlycloses', 'https://instagram.com/p/BiuBf1HBhAf/', 'https://www.instagram.com/p/Bit5ZonAoSy/', 'https://instagram.com/p/BiuDClWh9mZ/', 'https://www.instagram.com/p/BiaGOPthEzl/', 'https://www.instagram.com/p/BiuD3jIBQo2/?hl=en%26taken-by=autumlove__', 'https://instagram.com/p/BitqNQ-lho5/', 'https://instagram.com/p/BiuFcrTFiFX/', 'https://instagram.com/p/BiuFYaLAlVn/', 'https://instagram.com/p/BiuH_KJhtXs/', 'https://www.instagram.com/p/BiuIktpl4PN/', 'https://www.instagram.com/p/BisewaThf95/?taken-by=thisladyrides', 'https://instagram.com/p/BitaBCiHDuN/', 'https://www.instagram.com/p/Bitg3mSBOja/', 'https://www.instagram.com/p/Birz0biBH9B/', 'https://instagram.com/p/BiuLFWLFYsZ/', 'https://instagram.com/p/BiuMBSKBjEK/', 'https://instagram.com/p/BiuHT0onuOR/', 'https://instagram.com/p/BiuMw4NFayv/', 'https://www.instagram.com/p/BiuIkc_niFb/?taken-by=pennysuecockrell1976', 'https://instagram.com/p/BiuMDyFhUll/', 'https://www.instagram.com/p/BitXJPyF9iZ/', 'https://www.instagram.com/p/BiuMgijhBcV/', 'https://instagram.com/p/BiuNNpRhQrL/', 'https://www.instagram.com/p/Bircj5-ALDD/?taken-by=linethmm', 'https://instagram.com/p/BiuLAhLF8Fp/', 'https://www.instagram.com/p/BiuPZ_VhG64/?hl=en%26taken-by=bookishbrat', 'https://instagram.com/p/Bip8V3gAzH7/', 'https://instagram.com/p/BiuSmUUlxTo/', 'https://www.instagram.com/p/BiuR9USnatM/', 'https://www.instagram.com/p/BiuSgy5hUxS/?hl=fi%26taken-by=millatawast', 'https://www.instagram.com/p/BiuN5K9gdta/', 'https://www.instagram.com/p/BisEYFXBijh/?taken-by=30daysofgreekfood', 'https://www.instagram.com/p/BisYi65AJM3/', 'https://www.instagram.com/p/BiuWHTagzup/?taken-by=annieopenshaw', 'https://instagram.com/p/BirWlCzHXBx/', 'https://www.instagram.com/p/BiuWCVoh2qj/?taken-by=milkandhugs', 'https://www.instagram.com/p/BiuWbUPHD79/?taken-by=living.life.to.the.t', 'https://instagram.com/p/BiuWs4KnPh3/', 'https://www.instagram.com/p/BiuUsC9AHlY/', 'https://www.instagram.com/p/BipbpB2nbgB/', 'https://www.instagram.com/p/BiuZRIJA6cL/', 'https://instagram.com/p/BiuaF74F0B1/', 'https://instagram.com/p/BiubfEUBeUI/', 'https://instagram.com/p/BiuQY4ln0tD/', 'https://www.instagram.com/p/BiLPBBKhpNm/', 'https://www.instagram.com/p/BiuYk2-B0gk/?taken-by=hellohannahcho', 'https://instagram.com/p/BiuKYzthnuF/', 'https://instagram.com/p/Biucd-VAMv6/', 'https://www.instagram.com/p/Biue4eDAMo7/', 'https://www.instagram.com/p/Biue8DwHu_0/?taken-by=thefibreseed', 'https://www.instagram.com/p/BiuZEEOht8W/', 'https://www.instagram.com/p/BipN-mlHgMt/?taken-by=kimbodianspeaks', 'https://www.instagram.com/p/BiuacXHFJZu/', 'https://www.instagram.com/p/BimKN5IHg3C/', 'https://instagram.com/p/BiufBFpH17F/', 'https://instagram.com/p/BiuXLS9hgZo/', 'https://instagram.com/p/BiuiMOOh4oy/', 'https://instagram.com/p/BiuioqchJdh/', 'https://instagram.com/p/BiuiybmHhdy/', 'https://instagram.com/p/BiugAU6nlSE11h5gwSJA9N_JEjNUanvCthFxeQ0/', 'https://www.instagram.com/p/BisexJqH2VB/', 'https://www.instagram.com/p/BiuX_-uBSam/', 'https://www.instagram.com/p/Biumc2iBbs3/', 'https://www.instagram.com/p/Bit6rqblgxC/?taken-by=beatsbykd', 'https://instagram.com/p/BiuoEIUhJ0Y/', 'https://www.instagram.com/p/Biuo2h6BHIO/', 'https://www.instagram.com/p/BiupKsFBTL9', 'https://www.instagram.com/p/BiupiT3jJ4B/?taken-by=futuremissfit', 'https://www.instagram.com/p/Biugo9AgpM4/?taken-by=justadanishgirl_', 'https://instagram.com/p/BiuqF7hFAwa/', 'https://www.instagram.com/p/BinC_2xB_hf/?taken-by=travelingmom', 'https://www.instagram.com/p/BiuOpXJn21q/?taken-by=3somechocolates', 'https://instagram.com/p/BiukeyGgMm9/', 'https://instagram.com/p/Biurl4flEUP/', 'https://instagram.com/p/Biujf62Bljt/', 'https://www.instagram.com/p/BaGlFbygL8f/?taken-by=aryannepadilha', 'tps://www.facebook.com/profile.php?id=100007547205650', 'https://www.instagram.com/p/BiuI0ZRghA0', 'https://instagram.com/p/BiuvbeChja0/', 'https://www.instagram.com/p/BiujcsNBZ_7/', 'https://instagram.com/p/BiuwSMOhSoJ/', 'https://www.instagram.com/p/BiuxMHlhhxt/', 'https://instagram.com/p/BiukMsoAbq_/', 'https://instagram.com/p/Bit9MP8hGox/', 'https://www.instagram.com/p/Biu13aoFrrC/', 'https://www.instagram.com/p/Biur6dXn2-Y/', 'https://instagram.com/p/BiurNZAlnKy/', 'https://www.instagram.com/p/BiuhCtbDxT6/', 'https://instagram.com/p/BiutXwUBO5S/', 'https://www.instagram.com/p/Biu42uGh5gm/?taken-by=themoderngirl', 'https://instagram.com/p/Biu5Sd0AOWi/', 'https://instagram.com/p/BiutKPZF9vk/', 'https://www.instagram.com/p/Biu4nVZhamW/', 'https://instagram.com/p/Biu6brIhpU6/', 'https://instagram.com/p/Biu4tyXHlFc/', 'https://www.instagram.com/p/BiugHQdHgRY/?taken-by=befree_designs', 'https://www.instagram.com/p/Biu2TH6htbp/?taken-by=beautifulday_blog', 'https://www.instagram.com/p/Bipm-v-HPMb/?taken-by=ana__s__world', 'https://www.instagram.com/p/Biu9Wmyh9IJ/', 'https://instagram.com/p/Biuel5DARNA/', 'https://www.instagram.com/p/Biu-OuplhKI/', 'https://www.instagram.com/p/BiuetsznDGx/', 'https://instagram.com/p/BivAnt-hne_/', 'https://www.instagram.com/p/Biu-1x9Aho2/?taken-by=alittledelight', 'https://instagram.com/p/Biu39tOlNDf/', 'https://instagram.com/p/BivFRpSHAB0/', 'https://www.instagram.com/p/Biu_UMyjzPU/?taken-by=mommyneedsabottle', 'https://www.instagram.com/p/Biu4BYQhIvp/', 'https://instagram.com/p/BivIijsALgv/', 'https://instagram.com/p/BivHlQ3hruA/', 'https://instagram.com/p/BivIzlcFJG3/', 'https://www.instagram.com/p/BivJHJrnL1z/', 'https://instagram.com/p/BivJtRfH-Zk/', 'https://instagram.com/p/BivEfmHB4f2/', 'https://instagram.com/p/Biu2dzkFc0M/', 'https://www.instagram.com/p/Biu9BuohUSG/?taken-by=meghankaraan', 'https://instagram.com/p/BivK6rsAmFF/', 'https://www.instagram.com/p/BiurVkMBOm2', 'https://instagram.com/p/BivK55-lvJz/', 'https://www.instagram.com/p/Biu56LeBy_2', 'https://instagram.com/p/Biu8czLneXk/', 'https://instagram.com/p/BivFFr-nQw_/', 'https://www.instagram.com/p/BivOAouB13p/?taken-by=livelearnluxeit', 'https://www.instagram.com/p/Biu1bgKldR3/', 'https://www.instagram.com/p/BivE19UFgHr/?taken-by=easyweddings', 'https://instagram.com/p/BispjBlB653/', 'https://instagram.com/p/BivQG0RnSGS/', 'https://instagram.com/p/BivJHTijowd/', 'https://www.instagram.com/p/BiuT5sjB3eq/', 'https://instagram.com/p/BivSnDPglqz/', 'https://www.instagram.com/p/BiuMd6fhLu5/', 'https://instagram.com/p/BivHrjmhelN/', 'https://www.instagram.com/p/Bimh1TfhLk7/', 'https://www.instagram.com/p/BivVu5shjLC/', 'https://www.instagram.com/p/BivWj4xHi3P/', 'https://www.instagram.com/p/BivWy_AHSwr/', 'https://instagram.com/p/BiqKXXIltOE/', 'https://instagram.com/p/BivUpA0FhRw/', 'https://www.instagram.com/p/BivXdqVBSn4/?taken-by=healthyhappyandfitchic', 'https://www.instagram.com/p/BivWc3xnDU9/?taken-by=jessecoulter', 'https://www.instagram.com/p/BiLOWw7nxNJ/', 'https://instagram.com/p/BivAS-Rht5W/', 'https://www.instagram.com/p/BircvzMH85a/', 'tps://www.facebook.com/groups/theladieslounge101/permalink/231135210982802/']



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
        time.sleep(20)
    except:
        didnt_like.append(insta_picture)
        time.sleep(4)

text_me('Facebook likes complete!')
print('didnt like', didnt_like)
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
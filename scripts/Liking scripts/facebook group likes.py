from selenium import webdriver
import time, sys

sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import twilio, text_me, error_handling, open_chrome

insta_list = ['https://www.instagram.com/p/Bip8V3gAzH7/?taken-by=massholemommy', 'https://instagram.com/p/BiwKQkshRa-/', 'https://www.instagram.com/p/BiuFrZWA70-/', 'https://www.instagram.com/p/Biv5qp8lc0A/', 'https://instagram.com/p/BiuapjUnjYY/', 'https://www.instagram.com/p/BiwHc2vh_Hm/?taken-by=cessang24', 'https://instagram.com/p/BivvYjVnsce/', 'https://www.instagram.com/p/Biu-l62B5FJ/?taken-by=nyfoodiefamily', 'https://www.instagram.com/p/BiUrvY7hMzk/', 'https://instagram.com/p/Bivctj9HNoP/', 'https://instagram.com/p/BiwXbo5A0F6/', 'https://instagram.com/p/BivWOdvlQ3s/', 'https://instagram.com/p/BiwWHePB_kr/', 'https://www.instagram.com/p/BiwXz93hI0h/', 'https://instagram.com/p/BiwZIGeF5TX/', 'https://www.instagram.com/p/BiwRm01HvBc/', 'https://www.instagram.com/p/BiuhfiCB4uc/', 'https://www.instagram.com/p/BiwYbIyhUwf/?taken-by=heyitsjenna', 'https://www.instagram.com/p/BivswhXHfXB/?taken-by=cocuspocushq', 'https://instagram.com/p/BirrNAGF612/', 'https://instagram.com/p/BiwLZrbBpH1/', 'https://www.instagram.com/p/Biwt5zbHsSp/', 'https://www.instagram.com/p/Biud0fMg0lI/?taken-by=linethmm', 'https://instagram.com/p/BiwcnxjgnnE/', 'https://www.instagram.com/p/BiwAfDXB04d/', 'https://www.instagram.com/p/BiqOsp7AC14/?taken-by=easyweddings', 'https://instagram.com/p/BiwfPE_niZ5/', 'https://instagram.com/p/BiwfFmEB0cg/', 'https://instagram.com/p/Biwfg82leiQ/', 'https://www.instagram.com/p/Biwc_bzheA8/', 'https://www.instagram.com/p/BirB9gUAXPk/', 'https://www.instagram.com/p/BiwdY-XH_1H/?taken-by=thetaleofmummyhood', 'https://instagram.com/p/BiwhH0Gl8LM/', 'https://www.instagram.com/p/BivyNW1lhjH/', 'https://www.instagram.com/p/Biwaw3qAjji/', 'https://instagram.com/p/BiwjlLNH8y4/', 'https://instagram.com/p/BiuTwWigS8C/', 'https://www.instagram.com/p/BiwkgM8FZUY/', 'https://www.instagram.com/p/Biwkd9UBa3N/?taken-by=ellascribbles', 'https://www.instagram.com/p/Biv3R-uhTGq/', 'https://instagram.com/p/BiwmVxTHeA5/', 'https://www.instagram.com/p/Biwnq1QgXIo', 'https://www.instagram.com/p/Biwo4h-gNqs/', 'https://instagram.com/p/BiwoVWKhjkF/', 'https://instagram.com/p/BiwpSckF00s/', 'https://www.instagram.com/p/BiwgGuHHj-x/', 'https://instagram.com/p/BiwloXSgVy7/', 'https://instagram.com/p/BiuDQCTgC-W/', 'https://www.instagram.com/p/BiwqiR9ln16/', 'https://www.instagram.com/p/BivXPJuhaQN/', 'https://instagram.com/p/BisnVjrh7Fq/', 'https://instagram.com/p/Bir4vL0hcBR/', 'https://www.instagram.com/p/BipF4solQHG/', 'https://instagram.com/p/BiwseuznOmX/', 'https://instagram.com/p/BiwqwsQhQOU/', 'https://instagram.com/p/BiwqSKNlZxu/', 'https://instagram.com/p/Biwk5bUAp5w/', 'https://www.instagram.com/p/BiwrttFh-SE/', 'https://www.instagram.com/p/Bivn1BcHBFh/?taken-by=perksofbeautyblog', 'https://instagram.com/p/BiwsHNhh5rx/', 'https://instagram.com/p/Biwt5zkHksj/', 'https://instagram.com/p/Biwt5zbHsSp/', 'https://www.instagram.com/p/BikoTmtjVxy/', 'https://instagram.com/p/BiwrlIhF9ws/', 'https://instagram.com/p/BiwvZa_lwVy/', 'https://instagram.com/p/BiwvvAEgOCj/', 'https://www.instagram.com/p/BiwwzPtjLBq/?taken-by=merakirijah', 'https://www.instagram.com/p/Biqb4SGhP0B/?taken-by=all_things_jaz', 'https://www.instagram.com/p/Biwi3Jwn1FY/?taken-by=3somechocolates', 'https://www.instagram.com/p/BiwxOKKHcy5/', 'https://www.instagram.com/p/Biwxae0lkoF/', 'https://instagram.com/p/Biwx0poFVOX/', 'https://www.instagram.com/p/Biwx0lbg7pQ/', 'https://www.instagram.com/p/BiwtZRih0oh/', 'https://instagram.com/p/BiwHYyThexZ/', 'https://www.instagram.com/p/BitBP9PgEjf/?hl=en%26taken-by=beaudazzledbeauty', 'https://www.instagram.com/p/BiwZcrCgxko/', 'https://instagram.com/p/Biw0_CTBNVM/', 'https://www.instagram.com/p/Biw1YcLBrUX/?taken-by=mississippimiracleclay', 'https://www.instagram.com/p/BiwzpzeHOTX/?taken-by=racheljanelloyd', 'https://www.instagram.com/p/BivfcskFRtH/?taken-by=bloggersarahj', 'https://instagram.com/p/Biw2xI1naXH/', 'https://www.instagram.com/p/Biw1ytkgPkV/', 'https://instagram.com/p/BiwzqTnh9pE/', 'https://www.instagram.com/p/Biw3Z7ij829/?taken-by=simplysaidy', 'https://instagram.com/p/BiuJ8Vihi5m/', 'https://www.instagram.com/p/Biw4LYNhouG/', 'https://instagram.com/p/Biw3cgHHG62/', 'https://instagram.com/p/Biw2p3wF286/', 'https://www.instagram.com/p/BirgyIUHK7g/', 'https://www.instagram.com/p/Biw1gQhADTB/?taken-by=eastendtaste', 'https://www.instagram.com/p/Biw5dP4nEdj/', 'https://instagram.com/p/Biw6vVeFdHE/', 'https://instagram.com/p/Biw18Kchc-T/', 'https://www.instagram.com/p/BiupKsFBTL9/', 'https://www.instagram.com/p/Biw8m_1BDdn/?hl=fi%26taken-by=millatawast', 'https://www.instagram.com/p/Biw8C0hAYZD/?taken-by=alittledelight', 'https://instagram.com/p/Biw84MABIIg/', 'https://instagram.com/p/BivIzlcFJG3/', 'https://instagram.com/p/Biw9ThGnCAl/', 'https://www.instagram.com/p/Biw028th-Xh/?taken-by=beauty4free2u', 'https://www.instagram.com/p/BipmmP7BSYl/', 'https://www.instagram.com/p/Biw3L_LBli-/', 'https://www.instagram.com/p/Biueox8B8bL/', 'https://www.instagram.com/p/BirVWs0jcnz/?taken-by=martine_nike', 'https://www.instagram.com/p/BiveXDbnEqe/', 'https://www.instagram.com/p/BiekCbbHJci/', 'https://instagram.com/p/Biw5sAmncE-/', 'https://instagram.com/p/BixA67IAFMQ/', 'https://www.instagram.com/p/BixCKmIHJCK/?taken-by=brunchandslay', 'https://www.instagram.com/p/BixCSo4hPql/?taken-by=carlycloses', 'https://www.instagram.com/p/Biw6hHbAR0E/?taken-by=jesscramsey1', 'https://www.instagram.com/p/BixCw2ZA-gI/', 'https://www.instagram.com/p/Bim1APjhLcq/?taken-by=zionsdenapparel', 'https://instagram.com/p/BivalJrhpse/', 'https://www.instagram.com/p/Bitq1aBFeix/?taken-by=rosner_official', 'https://instagram.com/p/BixB1fKB5y1/', 'https://www.instagram.com/p/BixFiSEBaZU/', 'tps://www.facebook.com/se.belle.5?fref=gc', 'https://instagram.com/p/BixFbeWhDRA/', 'https://instagram.com/p/BiwwJ7Eg3tS/', 'https://instagram.com/p/BixHLENBIiY/', 'https://instagram.com/p/BixH9dwg47C/', 'https://www.instagram.com/p/BixH0z2l5sp/?taken-by=lilli_magalde', 'https://instagram.com/p/BixG3v1HU4V/', 'https://www.instagram.com/p/BixIlJRnXBx/', 'https://www.instagram.com/p/Biw-3YhgASh/?taken-by=justadanishgirl_', 'https://instagram.com/p/BixJwFqltPm/', 'https://www.instagram.com/p/BipoGKjnwjA/?taken-by=martinngo_photo', 'https://www.instagram.com/p/BixLSDZHiaL/', 'https://www.instagram.com/p/BixLm-oBQ2C/', 'https://www.instagram.com/p/BixL8XoHOTK/', 'https://www.instagram.com/p/BitZSjrgbaU/', 'https://instagram.com/p/BixMgqFgIzL/', 'https://www.instagram.com/p/BixMICgBA7i/', 'https://www.instagram.com/p/BixMa-xhwGK/?taken-by=yogafaceskincare', 'https://www.instagram.com/p/BixMhG8lSFu/?taken-by=gymwithkim_', 'https://www.instagram.com/p/BixLqjwlrXM/?taken-by=whatkatysaiduk', 'https://www.instagram.com/p/BixNloBhoAu/', 'https://instagram.com/p/BixODQJBG62/', 'https://www.instagram.com/p/BixOyzegJCw/?taken-by=annieopenshaw', 'https://instagram.com/p/BixPK3PFrrT/', 'https://instagram.com/p/Bis9YIjD0DE/', 'https://instagram.com/p/BixLjY_Hb86/', 'https://www.instagram.com/p/BiwQZedD83m/', 'https://instagram.com/p/BixM3LuhiM_/', 'https://instagram.com/p/BixLS9chDq8/', 'https://instagram.com/p/Biw6mvAAbyB/', 'https://www.instagram.com/p/BixReHUAP2t/?taken-by=karthikagupta', 'https://www.instagram.com/p/BixNEWCBB9l/', 'https://www.instagram.com/p/BixMuBWBo_-/?taken-by=ana__s__world', 'https://www.instagram.com/p/BixRqp3n6fu/?taken-by=itsbeanxcream', 'https://instagram.com/p/BixSVubhyIh/', 'https://instagram.com/p/BixRy2xl7Fh/', 'https://www.instagram.com/p/BixP226BO7N/', 'https://www.instagram.com/p/BixSxcEB8_C/?taken-by=hellohannahcho', 'https://www.instagram.com/p/BixR3gQlzAR/', 'https://instagram.com/p/BixUkGsBN2Q/', 'https://www.instagram.com/p/Biw6UDNHDTN/', 'https://www.instagram.com/p/BivQ6MGB6x9/', 'https://www.instagram.com/p/BiwXsG4Akr8/?hl=fi%26taken-by=littlerwdstudio', 'https://www.instagram.com/p/BixDSE_Afii/?taken-by=whatthegirlssayblog', 'https://www.instagram.com/p/BixYY0bFdpi/', 'https://www.instagram.com/p/BixX9SFAuHT/?taken-by=livelearnluxeit', 'https://www.instagram.com/p/BixAoLBFnw0/', 'https://instagram.com/p/Biv189qFJqu/', 'https://instagram.com/p/BixZ2QXhVD8/', 'https://instagram.com/p/BixTCqehl-a/', 'https://www.instagram.com/p/BixafknnLIU/', 'https://instagram.com/p/BixbTCLlOAa/', 'https://instagram.com/p/Bixc1MIFMGi/', 'https://www.instagram.com/p/Bixc0TLBoR8/?taken-by=healthyhappyandfitchic', 'https://www.instagram.com/p/BirwZTtgpEs/?taken-by=ellisrebel13', 'https://www.instagram.com/p/Bixd2cXDK0Y/?taken-by=neluthecurious', 'https://instagram.com/p/BiuNaBRHjlU/', 'https://instagram.com/p/BixifF0Hxic/', 'https://www.instagram.com/p/BixiS1jHFdz/', 'https://www.instagram.com/p/BiutQrIh7gQ/', 'https://www.instagram.com/p/BixQRXNBFV_/', 'https://instagram.com/p/BixbwbpFTaZ/', 'https://instagram.com/p/BixlaUvhxRF/', 'https://instagram.com/p/Bixkw_8Bo1k/', 'https://www.instagram.com/p/BixmOIllih6/?taken-by=fitnessfatale', 'https://www.instagram.com/p/Bixb5l_huQI/', 'https://www.instagram.com/p/BixnKMtFQtJ/?hl=en%26taken-by=wunderhausgermanshepherds', 'https://www.instagram.com/p/Bixo7b3BGAn/', 'https://www.instagram.com/p/BixVRWNAAXc/', 'https://www.instagram.com/p/BixqszenBne/?taken-by=living.life.to.the.t', 'https://www.instagram.com/p/BivWy_AHSwr/', 'https://www.instagram.com/p/BixqHpzgTZZ/?taken-by=love.erickacastanos', 'https://instagram.com/p/BivG2rgF_t2/', 'https://www.instagram.com/p/BixtdXMhLyT/?taken-by=beautybyish', 'https://www.instagram.com/p/BixtocanJpS/', 'https://www.instagram.com/p/Bixk1Q-BgwC/?taken-by=sugarspiceandglitter', 'https://www.instagram.com/p/Bixvn1kAZgq/?taken-by=upgrade_events_by_ingrid', 'https://instagram.com/p/Bixwh2vHnzP/', 'https://www.instagram.com/p/BiurCZnjQpf/?taken-by=femmeennoir', 'https://www.instagram.com/p/BixwgXfFTFh/?taken-by=easyweddings', 'https://www.instagram.com/p/BixxDk3hBTJ/?hl=en%26taken-by=reneepiane', 'https://www.instagram.com/p/BixeW3qBH6S/', 'https://www.instagram.com/p/Bixx2JtFl1P/', 'https://www.instagram.com/p/BiqjUvmDsfJ/', 'https://instagram.com/p/Bix0-ZeHB77/', 'https://instagram.com/p/Bix06Luhz1B/', 'https://www.instagram.com/p/Bix0f53lqxF/?taken-by=beatsbykd', 'https://www.instagram.com/p/Bix2AlzHhLe/?taken-by=saulcervantess', 'https://instagram.com/p/Biw3wGGFCvD/', 'https://instagram.com/p/Bix3qF5nR3O/', 'https://instagram.com/p/BixK19djwnf/', 'https://www.instagram.com/p/Bix5ZrKA4Oq', 'https://instagram.com/p/BiryIj2HLzq/', 'https://instagram.com/p/Bix1pAXhW8d/', 'https://www.instagram.com/p/Bix6euynOv7/', 'https://instagram.com/p/Bix8A_bFaM5/', 'https://instagram.com/p/Bix7gATgrkt/']



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
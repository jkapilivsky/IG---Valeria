from selenium import webdriver
import time, sys

sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import twilio, text_me, error_handling, open_chrome

insta_list = ['https://www.instagram.com/p/BisBjg3gCq2/?taken-by=massholemommy', 'https://www.instagram.com/p/BiyvJUMlEMm/?hl=en%26taken-by=elenaland13', 'https://www.instagram.com/p/BiyaHDUAQDq/', 'https://www.instagram.com/p/BiZ3eVrB_0i/', 'https://instagram.com/p/BiyVozcH7Bo/', 'https://www.instagram.com/p/Biy5Wp7ANlY/?hl=fi%26taken-by=littlerwdstudio', 'https://instagram.com/p/Bis5kU7gOkZ/', 'https://www.instagram.com/p/BiyprzJgopv/', 'https://instagram.com/p/BisFbBLhrNV/', 'https://www.instagram.com/p/Bigi9Mrl3wp/?hl=en%26taken-by=wunderhausgermanshepherds', 'https://instagram.com/p/Biy9aIFhczY/', 'https://instagram.com/p/BixCphhhQTY/', 'https://www.instagram.com/p/BiyLF2AHT_B/', 'https://instagram.com/p/Biy64swB2_j/', 'https://www.instagram.com/p/BiyWqVzgmts/', 'https://www.instagram.com/p/Biy_3tCnRcp/?taken-by=oyhz', 'https://instagram.com/p/BiybuNOnQ9v/', 'https://instagram.com/p/BiyNdkfHkfe/', 'https://www.instagram.com/p/BizBv1PnOMP/', 'https://instagram.com/p/Bix2AcphDpJ/', 'https://instagram.com/p/BizCe_iAwed/', 'https://instagram.com/p/BizBZlGAVEe/', 'https://www.instagram.com/p/Biw5qyVByY_/', 'https://instagram.com/p/BiyycvcA64n/', 'https://instagram.com/p/BizDU4EjHQs/', 'https://www.instagram.com/p/Bi0fU2pH5UC/', 'https://www.instagram.com/p/Bix8GfkhbRW/', 'https://www.instagram.com/p/BizFZOXHHBa/?taken-by=thetaleofmummyhood', 'https://www.instagram.com/p/BizGGaKnRR3/?taken-by=thefibreseed', 'https://instagram.com/p/Biw9j0Bh9yA/', 'https://www.instagram.com/p/BizFw-ng3SS/', 'https://www.instagram.com/p/BilKGDYBt6q/', 'https://instagram.com/p/BizIwfegB8m/', 'https://www.instagram.com/p/Biud0fMg0lI/?taken-by=linethmm', 'https://www.instagram.com/p/BizJ2qehhD3/', 'https://www.instagram.com/p/BizJsmNhDp1/', 'https://www.instagram.com/p/Biy_jzyAcwK', 'https://instagram.com/p/BizLBIWhmJF/', 'https://instagram.com/p/BizKmUqh30A/', 'https://www.instagram.com/p/BixyCUZn4VL/?taken-by=jessecoulter', 'https://www.instagram.com/p/BizGA9dB2hc/?taken-by=heyitsjenna', 'https://instagram.com/p/BizLv_kF7cW/', 'https://www.instagram.com/p/BiyisPilC00/', 'https://instagram.com/p/BizLb0nA7oC/', 'https://instagram.com/p/BiyK460HOK1/', 'https://www.instagram.com/p/BieTHqiBbOc/?taken-by=comebackmomma', 'https://www.instagram.com/p/BizPlVXhhdG/', 'https://www.instagram.com/p/BizPYk4FZNN/', 'https://www.instagram.com/p/BizPqyIj2Fv/?taken-by=merakirijah', 'https://www.instagram.com/p/BizPQFxBH8e/?hl=en%26taken-by=autumlove__', 'https://instagram.com/p/BizQhmnj_zw/', 'https://www.instagram.com/p/BivlLq-jDhQ/', 'https://instagram.com/p/BizSlnWhyBA/', 'https://instagram.com/p/BizTSqQl0lN/', 'https://instagram.com/p/BizAlHEnPCg/', 'https://www.instagram.com/p/BixxExyhnn8/?taken-by=all_things_jaz', 'https://www.instagram.com/p/BizEcMqBWrK/?taken-by=carlycloses', 'https://instagram.com/p/Bix9zSVnIuo/', 'https://instagram.com/p/BizQtUOhhFr/', 'https://instagram.com/p/BizVfIuhqPw/', 'https://instagram.com/p/BizUddClzg3/', 'https://instagram.com/p/BizRIP5lYIc/', 'https://instagram.com/p/BizVx0ilVNh/', 'https://www.instagram.com/p/Bix9XeflNLU/', 'https://instagram.com/p/BizW-9klLnl/', 'https://instagram.com/p/BizXLrDHLND/', 'https://www.instagram.com/p/BizXdwHATuk/?taken-by=realbalanced', 'https://instagram.com/p/BizYrruHmuO/', 'https://instagram.com/p/Biw5zZUH7Uc/', 'https://www.instagram.com/p/BizPsAagNpW/?taken-by=eastendtaste', 'https://www.instagram.com/p/BizYL4LlXSs/', 'https://www.instagram.com/p/BizZe0Vgjli/', 'https://instagram.com/p/BiyHjcnBrcB/', 'https://www.instagram.com/p/BizZHCChVc8/', 'https://www.instagram.com/p/BizXlRejUCY', 'https://www.instagram.com/p/BizaKi6Heqg/', 'https://www.instagram.com/p/Bix7gATgrkt', 'https://instagram.com/p/BizbuxulF9M/', 'https://instagram.com/p/BizYsrMAsGN/', 'https://www.instagram.com/p/BizbmYmh1vt/', 'https://instagram.com/p/BizcM5hAN4R/', 'https://instagram.com/p/BizcjO5BN7F/', 'https://instagram.com/p/BizGNc8lTC0/', 'https://instagram.com/p/BipKiLCnlCt/', 'https://instagram.com/p/BizVMNRHVVu/', 'https://www.instagram.com/p/BizdmrygzCq', 'https://instagram.com/p/BizcldiF8W4/', 'https://www.instagram.com/p/Bizd39ABd9K/', 'https://www.instagram.com/p/BizYo6LBZdH/?taken-by=mississippimiracleclay', 'https://instagram.com/p/BizeGjVh-ZR/', 'https://www.instagram.com/p/Bize033BiaN/?taken-by=milkandhugs', 'https://instagram.com/p/Bizel8gB-ce/', 'https://www.instagram.com/p/Biy2BeeFsiR/?taken-by=whatkatysaiduk', 'https://www.instagram.com/p/BgOrcVABbGy/?taken-by=casthedesigner', 'https://www.instagram.com/p/BizbB87Ag9c/', 'https://www.instagram.com/p/Bizh0NNB7Eb/?hl=fi%26taken-by=millatawast', 'https://instagram.com/p/Bizd580gvqO/', 'https://www.instagram.com/p/BizjE_MBEe9/', 'https://www.instagram.com/p/BizhTG9F8MD/', 'https://www.instagram.com/p/BiziKJBnCoG/', 'https://www.instagram.com/p/BixSxcEB8_C/?taken-by=hellohannahcho', 'https://www.instagram.com/p/BizMn2pDWnZ/', 'https://instagram.com/p/BizmaNblQr1/', 'https://www.instagram.com/p/Biw028th-Xh/?hl=en%26taken-by=beauty4free2u', 'https://www.instagram.com/p/BizSlC_AHsk/', 'https://www.instagram.com/p/Bizo0j2htbT/', 'https://instagram.com/p/BiyyofBB_2p/', 'https://www.instagram.com/p/BizpdC7n76q/', 'https://www.instagram.com/p/BizqmmvFkNQ/?taken-by=bl00bear54', 'https://instagram.com/p/BizrDwfH1a5/', 'https://www.instagram.com/p/BizqzjZn0k2/?taken-by=thestylishmommy', 'https://www.instagram.com/p/BizL41LhxG0/?taken-by=worldsokayestmomblog', 'https://www.instagram.com/p/Bizq6xRB2jb/', 'https://www.instagram.com/p/BiyawI8Bb4R/', 'https://www.instagram.com/p/BizA7-8lz-j/?taken-by=rosner_official', 'https://www.instagram.com/p/BizoLdiDoTW/', 'https://instagram.com/p/Bizn949nepj/', 'https://www.instagram.com/p/Bize_PBH_Sm/', 'https://www.instagram.com/p/BiztuWUDD6W', 'https://www.instagram.com/p/Bit__JAnHDT/', 'https://www.instagram.com/p/Biztlo7nBo3/?taken-by=martinngo_photo', 'https://www.instagram.com/p/Bizvk3DlGba/', 'https://instagram.com/p/BizvNFohrl-/', 'https://www.instagram.com/p/BizvKjgB2si/', 'https://www.instagram.com/p/Bizu_T-hZR5/', 'https://www.instagram.com/p/BizwRxvnvUQ/', 'https://instagram.com/p/BizwJE0B2d7/', 'https://www.instagram.com/p/BiztRfuBcBp/?taken-by=alyssa.and.co', 'https://www.instagram.com/p/Bizwry0gZuI/', 'https://www.instagram.com/p/BizwxkGnwfH', 'https://www.instagram.com/p/Biy5TDjjXue/?taken-by=futuremissfit', 'https://instagram.com/p/BizxgMLAr-E/', 'https://instagram.com/p/BizxKb_B-q7/', 'https://www.instagram.com/p/Bizx3OhhNBc/?taken-by=aryannepadilha', 'tps://www.facebook.com/profile.php?id=100007547205650', 'https://www.instagram.com/p/Bizx4Q-nOMw/?taken-by=kaysalin', 'https://www.instagram.com/p/BizxNxRhFqm/?taken-by=ana__s__world', 'https://instagram.com/p/BizzmmAFRrC/', 'https://www.instagram.com/p/BizziszgPjb/?taken-by=livelearnluxeit', 'https://instagram.com/p/Bizy3zRBDwk/', 'https://www.instagram.com/p/Bizqo85HN4X/?taken-by=eatlivetraveldrink', 'https://instagram.com/p/BizxPPwB7in/', 'https://instagram.com/p/Biz0S3OB6kM/', 'https://www.instagram.com/p/BizUITEh3QY/?taken-by=wildflower_honey', 'https://instagram.com/p/Bizx7PYByw4/', 'https://instagram.com/p/Biz05t9FVbF/', 'https://instagram.com/p/Biz3yB7H4dn/', 'https://www.instagram.com/p/BiupKsFBTL9/', 'https://www.instagram.com/p/BizxgMYhOkJ/?taken-by=beingecomomical', 'https://instagram.com/p/Biz4tZVjLbE/', 'https://www.instagram.com/p/Biz4QDNj217/', 'https://www.instagram.com/p/BizzgmEFHas/?hl=en%26taken-by=beatsbykd', 'https://instagram.com/p/Biz6szYhF5H/', 'https://www.instagram.com/p/Biw-9t4F23S/?taken-by=gretabrinkley', 'https://instagram.com/p/Biz8Uh_HVdc/', 'https://instagram.com/p/Biviuw8B66H/', 'https://www.instagram.com/p/BizerrvBLGB/', 'https://instagram.com/p/BizxNHTFFdm/', 'https://instagram.com/p/Biz-CqMlNLX/', 'https://www.instagram.com/p/Biz9cfXBrv0/?taken-by=arevook', 'https://www.instagram.com/p/Biz9lRIHy21/?taken-by=olordeprimavera', 'https://www.instagram.com/p/Biz_aGxlHGR/', 'https://www.instagram.com/p/Biz__MOlgsh/', 'https://www.instagram.com/p/Bio2EW_A4BJ/?taken-by=annieopenshaw', 'https://instagram.com/p/BiznAAzg1pw/', 'https://www.instagram.com/p/Bi0CPTTgu4B/', 'https://www.instagram.com/p/Biz2vkzBXAn/', 'https://www.instagram.com/p/Bi0DDbeFTdY/?taken-by=artestilebeauty', 'https://www.instagram.com/p/Biuq9ojhWVL/', 'https://www.instagram.com/p/Bi0FJO0n--7/', 'https://instagram.com/p/Biy6_WZAZv4/', 'https://instagram.com/p/Bi0FFAOAf-Z/', 'https://instagram.com/p/BisRvvTl6QQ/', 'https://instagram.com/p/Bi0GGc1hXDj/', 'https://www.instagram.com/p/Bi0GFA3gKAs/', 'https://instagram.com/p/Bi0GkZ6n8Uf/', 'https://www.instagram.com/p/BizvUjgg33z/?taken-by=ruth.klein', 'https://www.instagram.com/p/Biz6rTWHRU0/', 'https://www.instagram.com/p/Bi0HEzBHsoJ/', 'https://www.instagram.com/p/Bi0CQpXDZDl/?taken-by=neluthecurious', 'https://instagram.com/p/Bi0Ht02Be39/', 'https://www.instagram.com/p/Bi0HxA0g0PK/?taken-by=aly_maughan', 'https://www.instagram.com/p/BixDSE_Afii/?taken-by=whatthegirlssayblog', 'https://www.instagram.com/p/Bi0I8X-DjVB/', 'https://www.instagram.com/p/Bi0JoHbDeKv/', 'https://www.instagram.com/p/BimqxhRDq7Q/', 'https://www.instagram.com/p/Biw--voHgmY/?taken-by=pennysuecockrell1976', 'https://instagram.com/p/Biy4q0wBAde/', 'https://www.instagram.com/p/Bizh71qnFJA/', 'https://www.instagram.com/p/Bi0LcjJnfeI/?taken-by=uhhleesaa', 'https://www.instagram.com/p/Bi0KmmintGU/?taken-by=themoderngirl', 'https://www.instagram.com/p/BizRCU6h-w7/?taken-by=healthyhappyandfitchic', 'https://instagram.com/p/Bi0Pebjnhu2/', 'https://www.instagram.com/p/Bi0LMOkhTAF/', 'https://instagram.com/p/Bizf4TEB6oE/', 'https://www.instagram.com/p/BizorDrhdUT/', 'https://www.instagram.com/p/BiyBNVyBmLN/?taken-by=zionsdenapparel', 'https://instagram.com/p/Bi0Rc4vBexV/', 'https://www.instagram.com/p/Bi0NwoWAk5w/?taken-by=love.erickacastanos', 'https://www.instagram.com/p/Bi0UVHNno6y/', 'https://www.instagram.com/p/Bi0WNAMjvu_/', 'https://instagram.com/p/Bi0Wkf1hvaZ/', 'https://www.instagram.com/p/BisewaThf95/?taken-by=thisladyrides', 'https://www.instagram.com/p/BiiABzuhvck/', 'https://instagram.com/p/Bizo1GcFs6A/', 'https://instagram.com/p/BixM1DnH9bG/', 'https://www.instagram.com/p/Bi0Zn2aBxIO/', 'https://www.instagram.com/p/Bi0aqLMgTeU/?taken-by=bellabucchiotti', 'https://instagram.com/p/Bi0bOWblQGr/', 'https://www.instagram.com/p/Bi0djSJnzSF/', 'https://instagram.com/p/Bi0NpjZFJiv/', 'https://www.instagram.com/p/Bi0czrph6lW/', 'https://instagram.com/p/Bi0apiyhdY2/', 'https://www.instagram.com/p/Bi0a5fsAJqW/?taken-by=fitxbrit']


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
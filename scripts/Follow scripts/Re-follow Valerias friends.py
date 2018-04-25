from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from twilio.rest import Client
import datetime
import pickle
import pandas as pd
from random import *
import sys, logging
import numpy as np
from operator import sub
#
sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import sleep, twilio, text_me, error_handling, open_chrome


def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'new FOLLOW script', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))
#
def search_famous_person(ursname):
    # Search bar
    search = driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input''')
    search.clear()
    search.send_keys(ursname)
    search.send_keys(Keys.ENTER)
    sleep()
    # Goes to first person in search
    search_results = driver.find_elements_by_class_name('_ndl3t')
    search_results[0].click()
    sleep()

following_list = ['graciejudson', 'chezkakae', 'yolandaolivares10', 'duckieofficial', 'nyane', 'ysnvrg1925',
                  'kaitlyn_hieb', 'sherlockchang', 'jamientran', 'emitchell__', 'simplicially', 'chelseaboo989',
                  'flamingmonk', 'jayperez67', 'monica.mangar', '_sophisticat', 'chaguirre92', 'haipei_h', 'liliaperezmar',
                  'rosendosalazar', 'rayraymichaela', 'chris96boostedcobra', 'shanearia_lashay', 'jameymlane72',
                  'nikkim.ellenburg', 'andrea_kutie_91', '_kea_cam_', 'laquittalynn', 'lady.amori', 'leann.madison.wambles',
                  'smithzachary01', 'amandaregisterwatkins', 'courtneynicholee_', 'annieleelou', 'tga12_',
                  'blondie_2553', 'arielsmith_16', 'belen_cisneros', 'milyn1997', 'muratcan7401', 'cgtay11',
                  'devincassady14', 'travis_cassady', 'jdixonn', 'lyndeeweathington', 'lilmatt09', 'emc__________',
                  'jazminv114', 'cbroeckert', 'jmend.1', 'crappicorn01', 'maochoa8', 'tinastsang', 'ajpaulson91',
                  'jodirt25', 'sofi.lops', 'anacaren_02', 'valerie_anyssa', 'miss.syg', 'cyarine', 'samshigeru',
                  'laura_igonzalez', 'kahrlitos', 'skinnyrecords20', 'maissie44', 'kleimer_hernandez', 'julllliiieee_',
                  'melysaalanis', 'alekkxia', 'jorona24', 'jesus_.hdz92', 'gqka_', 'lajoiedevivre_7', 'miro_cassetta',
                  'vaantiti', 'ash_and_jessica', 'alondramtz83', 'trisarahightops', 'leticiamendozaz', 'ivaz', 'h.marieee',
                  'davidbaeklol', 'jen_smith18', 'lalaparktexas', 'abelv2009', 'haleighhoude', 'rpannullo',
                  'official_timshumar', 'ernesto.barajas7', 'lmkillips', 'drolee_draws', 'adrienhope', 'diego_prida',
                  'destiny.a.rodriguez', 'allisonlfloyd', 't3thinktank', 'tony_235', 'l_castillo23', 'masarap_nyc',
                  'juliem104', 'juliovill93', 'lupy1020', 'jme_fer', 'immabard', 'dannykapilivsky', 'sifuentesgracie',
                  'amanda_a_w', 'gmdn16', 'jortega102389', 'elpollogarza', 'yaniracantu', 'stevewillis36', 'dummycopy',
                  'lizethkatz', 'noel.like.christmas', 'liliaperezmar10', 'lynette_espino', 'janinnapena_', 'jbgaitan',
                  'anisagisselle', 'danie_jameson', 'tacocider', 'salanis31', 'ceby7', 'anais_m27', 'joethemaker', 'slkdesign',
                  'astro_paulina', 'santhana_s', 'huntermassad', 'resendezhugo', 'ray_cartagena', 'itsayanaresendez',
                  'lizz_bethh', 'li_xi_money', 'sinpingku', 'valeenewilson', 'claire_barrera24', 'claudssssy',
                  'riyo_ryoju_fukushiro', 'papitasswag', 'misa_misam', 'jonatantamez', 'katford', 'edzerrscott',
                  'javiermartinez6819', 'aftr_hrs_', 'pinche.morena18', 'pothadog', 'rickandmortyrickstaverse',
                  'roaringbear', 'stephpiperis', 'whochen', 'chicanojoel', 'rey_montemayor', 'marveoo', 'amelllii',
                  'jocelyng8', 'eliudgarrodri', 'rita13longoria2', 'kassyrmz0614', 'noobananners_', 'jonpena4',
                  'angelvidaljr', 'emmmie.s', 'justlisathings', 'fabyy45', 'iajlove', 'connor_teddy', 'cindyyarely7',
                  '_orange_you_glad_', 'dreamer299', 'tylermaxson', 'ryanthecreator4', 'melissagarza_06', 'valeriadgarcia',
                  'ka_rinag', 'alexis_m53', 'jenndfrancis', 'dantehec', 'auror_alex', 'brockdavis', 'socialdistillery',
                  'dust23', 'catsamarista', '_evelynn5', 'bydelao12', 'alo_mc', 'dinorah_elisa', 'mayraluera',
                  'gaby_ramirez20', 'nattap5', '__natstagram__', 'osbertbazan', 'deya_montemayor', 'leana.c',
                  'jessica.alaniz', 'sandra_fluti', 'ner0lee', 'j_salinas23', 'emmanuelzaarate_official', 'omar15k',
                  'wanderlxsting_', 'josecoellojr', 'eperez55', 'melindalinay', 'cassiesarahi', 'o.t_09', 'karianazuzuel',
                  'adriansolis2010', 'elmagophoto', '_lamancion', 'mallelycantu', 'shannoroni', 'ydma3', 'jesusguerra4.inc',
                  'ismeniapark', 'mybabiesmileskillme', 'angelbfmv13', 'jenny_ibarra_', 'beccab0907', 'sr_worldwide',
                  'madmex956', 'angela_warrior', 'abs_923', 'bonjourjesuissasha', 'tiff_garcia5', 'jgarza_1195',
                  'bgarcia_78', 'marie_n_eddie', 'bertoo_g', 'c_hoofard', 'jh3_holy', 'bianca020315', 'gisele_89',
                  'yayadelara', 'alxrayo', 'lopezlopez03', 'raiceball', 'frankrios95', 'robert.gzz13', 'odsolis88',
                  'annelleglz079', 'sergi_solo16', 'edd_ster_', 'rox2.2', 'andreayg_', 'a_montemayorg', 'beealan11',
                  'mayy_geee', 'armando_garcia29', 'jessica_rdgz13', 'jackiegarcia18', 'loreida14', 'anaismor11',
                  'alorockstar', 'alexyrios', 'andisalazar', 'jaymcneilmusic', '_eemanuel', 'onildapompa', 'ricardhu_ali',
                  'aaronbarriosfans', 'lexihouses', 'jjgarza7', 'kretana326', 'edith_0924', 'msyazminsoto', 'lee_c24',
                  'alex11_garcia', 'paolafaride26', 'vanesio33', 'yolanda.yadira', 'jestra_93', 'bee_anca76',
                  'hail_for_days', '_skittlez_skittlez', 'macantu22', 'perladelao', 'nachiio', 'yiselchisel', 'i5210',
                  'marco15s', 'anaylezamora', 'lupe_flores_42', 'jynava', 'aljanndra', 'mayteisastarrr', 'lrios1990',
                  'littleowl_17', 'edgarrios', 'julieta_v', 'sarah_gi27', 'kiarajanylet', 'malanis09', 'herre22',
                  'carliosr', 'toughduckling', 'biancalioness', 'nancya9', 'kyn_04', 'elsa.ma.rmz', 'alexandrianic_',
                  'anafalcon', 'alyssalomas25', 'alekchia', 'naysaramirezz', 'priscillaa_sg', 'nellyb93', 'toneh_garza',
                  'alexxgil', 'paolajalanis', '_keylatte_', 'therealfoodstamp', 'cantu293', 'roland_rockz', 'houston_94',
                  'fooly_uly', 'vna_c', 'bbydeb', 'amylynnloera', 'lacho13', 'marsmtz24', 'april_salinas23', 'isaigomez',
                  'erikkalizz', 'kevinyeoh1130', 'lupethunaa', 'randy_8a', 'allpachino', 'marlaalvrz', 'mely9312',
                  'erikaruribe', 'angelvill', 'clari_idette', 'victoryiscontagiouss', 'zey_delao', 'ivan_cano_', 'jmoya96',
                  'charlie_garciali', 'roxyloufreebush', '56_red', 'mariela_lizette', 'coach.castillo', 'eradios',
                  'missdanielaaa', 'yarii_igle', 'fear_no_evil_21', 'elmagoart', 'abelibarra228', '_wicho10', 'ohlivita',
                  'smiles_911', 'andrex581', 'agonzalezjr5', 'vicktoriuh', 'satanas20', 'atchee14loera', 'knightcab23',
                  'thejess_ter', 'jos_y', 'gloriiajanette0214', 'rosaepr', 'efgarcia95', 'julietahinojosa', '_monserratt23',
                  'xxzarinamxx', '_marleeee24', 'luisruiz38', 'greg.pena', 'adanaramirez', 'abballa1', 'kassyliz',
                  'erniewormie', 'delao27', 'tacosdelengua', 'isidroiii', 'starkiss_27', 'marcos_got_a_gun', 'briceno_paul',
                  'ashngar', 'rgone12', 'lauren_analy', 'mgbigred', 'rreyesz36', 'pcano1994', 'cris.c__', 'adaexplainsitall',
                  'luisedtr', 'jon_cruz88', 'madchicanita', 'satou912']
#


df = pickle.load(open('../../data/Instagram_data.p', 'rb'))
of_df = df[df['status'].isin(['official_friend'])]
of_df = of_df['username']

friend_list = of_df.tolist()

#remove_from_search = []
rem1 = []

#remove_from_search = rem1 + rem2 + rem3 + rem4

#friend_list = [item for item in friend_list if item not in remove_from_search]
errors = 10
list_that_didnt_follow = []
list_that_followed = []
while errors > 0:
    try:
        if len(friend_list) == 0:
            print('ALL DONE!')
            quit()
        count = 0
        remove_from_search = rem1 + \
                             list_that_followed + list_that_didnt_follow
        friend_list = [item for item in friend_list if item not in remove_from_search]

        #twilio()
        friend_list = sorted(friend_list, key=lambda x: random())
        print('friends left', len(friend_list))
        global search
        global search_results
        global driver
        driver = open_chrome('Extra_Profile')

        for x in friend_list:

            search_famous_person(x)

            # Check if they found hashtag
            try:
                driver.find_element_by_class_name('_kwqc3')
                list_that_didnt_follow.append(x)
                continue
            except NoSuchElementException:
                if friend_list.index(x) == len(friend_list) - 1:
                    break
                pass

            # Check if they found a location
            try:
                driver.find_element_by_class_name('_thew0')
                list_that_didnt_follow.append(x)
                continue
            except NoSuchElementException:
                if friend_list.index(x) == len(friend_list) - 1:
                    break
                pass

            # Check if they found a Sorry, this page isn't available.
            try:
                driver.find_element_by_class_name('error-container')
                driver.find_element_by_xpath('''/html/body/div/div[1]/header/div/div[1]/a''').click()
                time.sleep(3)
                list_that_didnt_follow.append(x)
                continue
            except NoSuchElementException:
                if friend_list.index(x) == len(friend_list) - 1:
                    continue
                pass

            # Makes sure we are liking the right person!
            try:
                username_found = driver.find_element_by_xpath(
                    '''//*[@id="react-root"]/section/main/article/header/section/div[1]/h1''').text
                if x != username_found:
                    if friend_list.index(x) == len(friend_list) - 1:
                        print("didn't follow:", x)
                        list_that_didnt_follow.append(x)
                        break
                    continue
            except:
                continue

            try:
                follow_button = driver.find_element_by_class_name('_qv64e')
                sleep()
            except:
                print(x, 'already followed?')
                continue

            if follow_button.text == 'Follow':
                follow_button.click()
                print(x, 'FOLLOWED!')
                list_that_followed.append(x)
                count += 1
                sleep()
            else:
                print(x, 'is already followed!')
                list_that_didnt_follow.append(x)

            sleep()

            if (count + 1) % 11 == 0:  # Sleeps for 6 minutes every 10 unfollow
                print('SLEEP TIME! for 1 minutes')
                time.sleep(1 * 60)
            else:
                continue

    except Exception as err:
        print(err)
        print('CHECK ERROR LIST')
        driver.close()
        print('didnt', list_that_didnt_follow)
        print('followed', list_that_followed)
        #text_me('check your laptop!')
        errors -= 1
        if errors == 0:
            quit()


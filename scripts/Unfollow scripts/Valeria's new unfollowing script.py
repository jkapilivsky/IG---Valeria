from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import timeit
import datetime
from twilio.rest import Client
import pickle
import pandas as pd
from random import *
import sys, logging

sys.path.insert(0, 'C:/Users/jamie/PycharmProjects/Instagram/Insta files/scripts/Functions')
from Insta_functions import sleep, twilio, text_me, error_handling

def open_chrome():
    global driver
    global client
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-data-dir=C:/Users/jamie/PycharmProjects/Instagram/Profiles/Extra_Profile - Copy")  # Path to your chrome profile
    driver = webdriver.Chrome(executable_path='../../assets/chromedriver', chrome_options=options)
    driver.get("https://www.instagram.com/")
    sleep()

def log_into_instagram(username, password):
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a''').click()
    time.sleep(3)

    # Input username
    user = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/div/input''')
    user.clear()
    user.send_keys(username)

    # Input password
    pw = driver.find_element_by_xpath(
        '''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/input''')
    pw.clear()
    pw.send_keys(password)

    pw.send_keys(Keys.ENTER)
    time.sleep(3)

def repeat_down_arrow(number_of_times):
    count = 0
    while count < number_of_times:
        driver.find_element_by_class_name('_lfwfo').send_keys(Keys.ARROW_DOWN)
        time.sleep(1.5)
        count += 1

def repeat_space_bar(number_of_times):
    count = 0
    while count < number_of_times:
        driver.find_element_by_class_name('_2g7d5').send_keys(Keys.SPACE)
        time.sleep(1)
        count += 1

def remove_k_m_periods_commas(value):
    value = value.replace('k', '')
    value = value.replace('m', '')
    value = value.replace('.', '')
    value = value.replace(',', '')
    return value

def error_log(err):
    error_log = pickle.load(open("../../data/Instagram_error_log.p", "rb"))
    df = pd.DataFrame([[err, 'Valeria new unfollowing script', str(datetime.datetime.now())]],
                      columns=['error message', 'script', 'time_stamp'])
    error_log = error_log.append(df)
    pickle.dump(error_log, open("../../data/Instagram_error_log.p", "wb"))

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
error = 3
while error > 0:
    try:
        open_chrome()
        twilio()


        start = timeit.default_timer()

        # go to profile
        driver.find_element_by_xpath('''//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a''').click()
        sleep()

        # Following number
        # following_amount = driver.find_element_by_xpath(
        #     '''//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[3]/a/span''').text
        #
        # following_amount = remove_k_m_periods_commas(following_amount)  # Deletes the comma when over 1,000
        # following_amount = int(following_amount)  # Turns the text into an integer

        # Click unfollowing list
        driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/header/section/ul/li[3]''').click()
        sleep()

        driver.back()
        sleep()

        # Click unfollowing list
        driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/header/section/ul/li[3]''').click()
        sleep()

        repeat_space_bar(100)

        count = 0
        for people in range(0, 350, 1):
            unfollow_button = driver.find_elements_by_class_name('_qv64e')
            name = driver.find_elements_by_class_name('_2g7d5')

            # Checks if the person's name is in Valeria's official following_list
            if name in following_list:
                print('Valeria\'s friend!!!')
                continue

            unfollow_button[people+1].click()
            time.sleep(2.5)
            count += 1

            if (people+1) % 16 == 0:  # Sleeps for 15 minutes every 16 unfollow
                print(people, 'Unfollowed: Waiting 11 minutes')
                time.sleep(11*60)

            if (people+1) % 25 == 0:  # Catches up for scrolling
                driver.find_element_by_class_name('_2g7d5').send_keys(Keys.SPACE)

            print('unfollowed:', name[people+1].text)

            # Begin pickle
            data = pickle.load(open("../../data/Instagram_data.p", "rb"))
            df = pd.DataFrame([[name[people+1].text, 'Unfollowed', str(datetime.datetime.now())]],
                              columns=['username', 'status', 'time_stamp'])
            data = data.append(df)
            pickle.dump(data, open("../../data/Instagram_data.p", "wb"))
            # End pickle

        stop = timeit.default_timer()
        print('Unfollowed: ', count, ' people!')
        print('Minutes: ', (stop - start)/60)
        driver.close()

    except Exception as err:
        issue = error_handling()
        error_log(issue)
        driver.close()
        error -= 1
        text_me('oldschool | Unfollow stopped working!')
        print('error!')



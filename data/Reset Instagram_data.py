import pandas as pd
import datetime
import numpy as np

date = datetime.date.today()

df = pd.read_pickle('Instagram_data.p')

df = df.iloc[0:0]
df.to_pickle('Instagram_data.p')
quit()
'''
make sure to change the original pickle file name first!!
'''

# TODO - add back friends!
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
                  'luisedtr', 'jon_cruz88', 'madchicanita', 'satou912', 'kaitlyn_hieb', 'haleighhoude', 'h.marieee',
                  'adrienhope']
#


for friends in following_list:
    df_friend = pd.DataFrame([[friends, 'official_friend', date, 'friend']], columns=['username', 'status', 'time_stamp', 'acquisition'])
    df = df.append(df_friend)


df.to_pickle('Instagram_data.p')
print('Complete')
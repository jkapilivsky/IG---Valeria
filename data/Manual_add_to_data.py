import pickle, datetime
import pandas as pd

df = pickle.load(open('Instagram_data.p', 'rb'))
print(df.count())
quit()
of_df = df[df['status'].isin(['official_friend'])]
off_df = of_df['username']
friend_list = off_df.tolist()  # 306

# list = ['bee_anca76', 'nachiio', 'bossbabediva' ,'ali__peace',
#         'lizhdezhdez', '_.anitaaaaa', 'celianac95', 'dbrownisawful',
#         '_orange_you_glad_', 'amelllii', 'alejalatormenta', 'adrienhope',
#         'alondraycarlos04', 'h.marieee', 'haleighhoude', 'ivaz', 'alchemicals_',
#         'thatsillywalker', 'candacequeencreative', 'fatimaa_02', 'claudssssy',
#         'jen_smith18' ,'aleenkhouryy', 'j_go3', 'jonatantamez', 'emmmie.s',
#         'shiv_kalwan', '_mainente', 'jodirt25', 'sofi.lops', 'anacaren_02',
#         'valerie_anyssa', 'miss.syg', 'cyarine', 'samshigeru', 'laura_igonzalez',
#         'kahrlitos', 'skinnyrecords20', 'maissie44', 'kleimer_hernandez', 'julllliiieee_',
#         'melysaalanis', 'alekkxia' ,'jesus_.hdz92', 'gqka_', 'lajoiedevivre_7', 'miro_cassetta',
#         'vaantiti', 'davidbaeklol', 'abelv2009', 'diego_prida', 'destiny.a.rodriguez',
#         'allisonlfloyd', 'tony_235', 'l_castillo23', 'masarap_nyc', 'juliem104',
#         'liliaperezmar10', 'itsayanaresendez', 'rickandmortyrickstaverse',
#         'justlisathings', 'ydma3','bertoo_g', 'andreayg_', 'aaronbarriosfans',
#         'macantu22', 'agonzalezjr5', 'adanaramirez', 'abballa1', 'erniewormie',
#         'delao27', 'tacosdelengua', 'isidroiii', 'starkiss_27' ,'marcos_got_a_gun',
#         'briceno_paul', 'ashngar', 'lauren_analy' ,'mgbigred', 'rreyesz36','cris.c__',
#         'adaexplainsitall', 'luisedtr' ,'jon_cruz88', 'breathingstorm', 'satou912',
#         'eltiny_76', 'heraaclioo', 'clarimia_21']

list = ['nyane']

# print('friend_list:', len(friend_list))  # 89
# print('list:', len(list))

data2 = pd.DataFrame()

for names in list:
    # Begin pickle
    df_new = pd.DataFrame(
        [[names, 'official_friend', str(datetime.datetime.now())]],
        columns=['username', 'status', 'time_stamp'])
    data2 = data2.append(df_new)

#TODO - make sure to append TO df not of_df (of_df just to make sure the count goes up for official friends.. right now at 327)
final_df = df.append(data2)
final_df.drop_duplicates(subset='username', keep='last', inplace=True)

print(final_df.count())


#pickle.dump(final_df, open("Instagram_data.p", "wb"))
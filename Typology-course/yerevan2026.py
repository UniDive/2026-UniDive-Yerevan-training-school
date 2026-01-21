from pyglottolog import Glottolog
glottolog = Glottolog('glottolog') # The directory where you placed your downloaded copy
x = glottolog.languoid('gheg1238') # x = glottolog.languoid('aln') would also work but is slower
print(x.name, x.iso, x.glottocode)


for glottocode in ['gheg1238', 'indo1319', 'erev1240']:
    x = glottolog.languoid(glottocode)
    print(x.name, x.iso, x.level)


x = glottolog.languoid('kais1242')
print(x.name, x.level.id, x.iso)
print(x.ethnologue_comment)

glottolog.languoid('gheg1238').name
#'Gheg Albanian'  

languoids = [l for l in glottolog.languoids()]
len(languoids)                                                          
#27111

languages = [l for l in glottolog.languoids() if l.level.id == 'language']
len(languages)  
#8618


glottolog.languoid('gheg1238').names
#{'multitree': ['Albanesisch', 'Albanian', 'Albanian, Gheg', 'Arber', 'Arbresh', 'Arnaut', 'Geg', 'Gheg', 'Gheg Albanian', 'Guegue', 'Shgip', 'Shqipēri', 'Shquipni', 'Škip'], 'lexvo': ['Albanés guego [es]', 'Dialectul Gheg [ro]', 'Gegijski jezik [hr]', 'Gegisch [de]', 'Gegiska [sv]', 'Gegë [sq]', 'Gheg Albanian [en]', 'Guègue [fr]', 'Γκεγκική διάλεκτος [el]', 'Геги [bg]', 'Гегский диалект албанского языка [ru]', 'ゲグ方言 [ja]'], 'hhbib_lgcode': ['Albanian of Zadrima', 'Albanian-Gheg', 'Gegskaja', 'Gheg', 'Malsia Madhe', 'NW Gheg', 'Northeast Geg Albanian from southern Kosovo', 'Südgegischen']}


glottolog.languoid('gheg1238').countries
#[Country(id='AL', name='Albania'), Country(id='BG', name='Bulgaria'), Country(id='ME', name='Montenegro'), Country(id='MK', name='North Macedonia'), Country(id='RO', name='Romania'), Country(id='RS', name='Serbia')]


(glottolog.languoid('gheg1238').latitude, glottolog.languoid('gheg1238').longitude)
#(42.317, 21.3837)


glottolog.languoid('gheg1238').endangerment
#Endangerment(status=AES(ordinal=1, id='safe', name='not endangered', egids='<=6a', unesco='safe', elcat='at risk/safe', reference_id='hh:hel:Hammarstrom:Visualization', icon='ca2f49b'), source=AESSource(id='E28', name='Ethnologue 28', url='https://www.ethnologue.com/', reference_id='hh:h:Ethnologue:28', pages=None), comment='Albanian, Gheg (aln-aln) = 4 (Educational).')
glottolog.languoid('madi1261').endangerment
#Endangerment(status=AES(ordinal=3, id='definite', name='shifting', egids='7', unesco='definitely endangered', elcat='threatened/endangered', reference_id='hh:hel:Hammarstrom:Visualization', icon='sf19903'), source=AESSource(id='ElCat', name='The Catalogue of Endangered Languages (ELCat)', url='http://endangeredlanguages.com', reference_id='hh:hel:Campbell:ElCat', pages=None), comment='Madi (4241-grg) = Endangered (20 percent certain, based on the evidence available) [Lewis 2009](cldf:lewis:ed:09)')

glottolog.languoid('mbab1239').timespan
#(1985, 1985)
glottolog.languoid('clas1249').timespan
#(400, 1100)
glottolog.languoid('mero1237').timespan
#(-250, 300)


import pandas
df = pandas.read_csv('e28.tab', sep='\t', keep_default_na=False, index_col = "ISO 639-3")
df.loc["kbr"]
#Also indigenous in                                                          
#Also spoken in                                                              
#Alternate Names            Caafiti, Caffino, Kaffa, Kaffinya, Kaficho, Ke...
#Autonym                                                           Kafi noono
#Classification             Afro-Asiatic, Omotic, North, Gonga-Gimojan, Go...
#Country                                                             Ethiopia
#Dialects                   Kafa, Bosha (Garo). Bosha may be a distinct la...
#Digital Support                                            Ascending (0.21).
#Language Development       Literacy rate in L2: 22%. Taught in primary an...
#Language Resources                          OLAC resources in and about Kafa
#Language Status                                             4 (Educational).
#Language Use               Also use Amharic [amh]. Used as L2 by Nayi [noz].
#Location                   Southern Nations, Nationalities, and Peoples’ ...
#Member Languages                                                            
#Other Comments                      Traditional religion, Christian, Muslim.
#Population                 1,406,700, all users. L1 users: 1,360,000 (202...
#Population Numeric                                                   1360000
#Population Numeric (L2)                                                46700
#Timespan                                                                    
#Timespan Source                                                             
#Typology                                                                SOV.
#Writing                    Ethiopic script [Ethi], used in Church literat...
#code+name                                                         Kafa [kbr]
#name                                                                    Kafa
#Name: kbr, dtype: object
int(df.loc["kbr"]["Population Numeric"])
#1360000


x = glottolog.languoid('hye') #Eastern Armenian
x.parent #Gives the immediate parent
#<Family east2768>
x.children #Gives a list of the immediate children
#[<Dialect agul1245>, <Dialect arar1266>, <Dialect kara1458>, <Dialect khoi1249>]
x.ancestors #Gives an ordered list from the root up (but not including) to the current node                                                  
#[<Family indo1319>, <Family clas1257>, <Family arme1241>, <Family east2768>]



languages = [l for l in glottolog.languoids() if l.level.id == 'language']
len(languages)
#8618
canonical_languages = [l for l in languages if (l.ancestors + [l])[0].name not in ['Sign Language', 'Unclassifiable', 'Pidgin', 'Unattested', 'Artificial Language', 'Speech Register', 'Mixed Language', 'Bookkeeping']]
len(canonical_languages)
#7675




#Select the languages
languages = [l for l in glottolog.languoids() if l.level.id == 'language']
canonical_languages = [l for l in languages if (l.ancestors + [l])[0].name not in ['Sign Language', 'Unclassifiable', 'Pidgin', 'Unattested', 'Artificial Language', 'Speech Register', 'Mixed Language', 'Bookkeeping']]
languages_A = [l for l in canonical_languages if l.name.startswith("A")]

#Create the base map
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
plt.figure(figsize=(36,18))
ax = plt.axes(projection=ccrs.Mollweide()) #For Mollweide projection
#ax = plt.axes(projection=ccrs.PlateCarree()) #For Mercator projection
ax.coastlines(resolution="10m") #Use coastlines

#Plot the dots
plt.scatter([l.longitude for l in languages_A], [l.latitude for l in languages_A], transform=ccrs.PlateCarree(), facecolors='none', edgecolors = "blue", s = 10) #s is thickness

#Save
plt.savefig('yerevan2026map_test.png', bbox_inches='tight', pad_inches=0, dpi = 600)
plt.close()



kwomtari = glottolog.languoid('nucl1593')
kwomtari.sources
#[Reference(key='cldf:hammarstroem:forkel:etal:14', pages=None, trigger=None, endtag='**'), Reference(key='cldf:lewis:paul:etal:ed:15', pages=None, trigger=None, endtag='**'), Reference(key='cldf:spencer:08', pages=None, trigger=None, endtag='**'), Reference(key='hh:g:Honsbergeretal:Kwomtari', pages=None, trigger=None, endtag='**'), Reference(key='hh:he:Fyfe:Upper-Sepik', pages=None, trigger=None, endtag='**'), Reference(key='hh:hld:Lean:Sandaun', pages=None, trigger=None, endtag='**'), Reference(key='hh:hv:BassLoving:Amanab', pages=None, trigger=None, endtag='**'), Reference(key='hh:hv:Laycock:Sepik', pages=None, trigger=None, endtag='**'), Reference(key='hh:hv:Laycock:SkoKwomtariLeftMay', pages=None, trigger=None, endtag='**'), Reference(key='hh:hvs:Baron:Kwomtari', pages=None, trigger=None, endtag='**'), Reference(key='hh:w:Laycock:D16', pages=None, trigger=None, endtag='**'), Reference(key='sil16:50993', pages=None, trigger=None, endtag='**'), Reference(key='sil16:50994', pages=None, trigger=None, endtag='**'), Reference(key='sil16:50995', pages=None, trigger=None, endtag='**'), Reference(key='silpng:silpng1991-2000:1127', pages=None, trigger=None, endtag='**'), Reference(key='silpng:silpng1991-2000:1128', pages=None, trigger=None, endtag='**'), Reference(key='silpng:silpng1991-2000:1129', pages=None, trigger=None, endtag='**')]


import pycldf
asjp = pycldf.Dataset.from_metadata(r'dbs\asjp\asjp21_lexibank-asjp-0127953\cldf\cldf-metadata.json') #Specify where you placed your downloaded copy
for c in asjp.components:
    print(c)
   
#FormTable
#LanguageTable
#ParameterTable

localid_to_iso = {row['ID']: row['ISO639P3code'] for row in asjp['LanguageTable']}
parameterid_to_gloss = {row['ID']: row['Name'] for row in asjp['ParameterTable']}

for row in asjp['FormTable']:
    if localid_to_iso[row['Language_ID']] == 'hye':
        if parameterid_to_gloss[row['Parameter_ID']] == '*stone':
            print(row['Form'], row['Language_ID'])

#kh~or ARMENIAN
#kh~ar EASTERN_ARMENIAN


import pycldf
grambank = pycldf.Dataset.from_metadata(r'dbs\grambank\grambank-grambank-7ae000c\cldf\StructureDataset-metadata.json') #Specify where you placed your downloaded copy

for c in grambank.components:
    print(c) 
#ValueTable
#LanguageTable
#ParameterTable
#CodeTable

parameterid_to_name = {row['ID']: row['Name'] for row in grambank['ParameterTable']}
for row in grambank['ValueTable']:
    if row['Language_ID'] == 'nucl1235':
        print(parameterid_to_name[row['Parameter_ID']], row['Value'])
        
#Are there definite or specific articles? 1
#Do indefinite nominals commonly have indefinite articles? 1
#Are there prenominal articles? 0
#Are there postnominal articles? 1
#What is the order of numeral and noun in the NP? 1
#...

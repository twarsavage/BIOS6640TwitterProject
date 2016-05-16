
#English subset
finaleng = final.loc[(final['lang'] == 'en'),origTwCol] 


#lists
lbug = ['mosquito','bug','insect']


lstop = ['prevention','prevent','fight','combat','stop','eradicate','protect','vaccine',
    'contain','help']

lscience = ['scien','neuro','receptor','cell','microscopy','scientist','retinal','reservoirs',
     'microceph','nerve','defect','malphorm','research']

 
lpolit = ['politic','fund','congress','president','law','legislature','legal']
 
lspread = ['doomsday','panic','worried','worry','crisis','infect','exposed','exposure',
 'death','kill','outbreak','worse','damag','spread','endanger','threat','fatal',
 'risk']
 
lnews = ['news','case','report']

lolymp = ['olympic','rio 2016']

lreprod = ['reproduc','pregnant','newborn','baby','babies','birth','children']




#create flag filters
import re


def spread(text):
    for pattern in lspread:
        if re.search(pattern, text.lower()):
            return 1
    return 0
    
def bug(text):
    for pattern in lbug:
        if re.search(pattern, text.lower()):
            return 1
    return 0
    
def prevent(text):
    for pattern in lstop:
        if re.search(pattern, text.lower()):
            return 1
    return 0
    
def science(text):
    for pattern in lscience:
        if re.search(pattern, text.lower()):
            return 1
    return 0
    
def politic(text):
    for pattern in lpolit:
        if re.search(pattern, text.lower()):
            return 1
    return 0
    
def news(text):
    for pattern in lnews:
        if re.search(pattern, text.lower()):
            return 1
    return 0
    
def olymp(text):
    for pattern in lolymp:
        if re.search(pattern, text.lower()):
            return 1
    return 0
    
def reprod(text):
    for pattern in lreprod:
        if re.search(pattern, text.lower()):
            return 1
    return 0
    
#apply flag filters
finaleng['spreadflag'] = finaleng['text'].map(spread)
finaleng['prevent'] = finaleng['text'].map(prevent)
finaleng['bug'] = finaleng['text'].map(bug)
finaleng['science'] = finaleng['text'].map(science)
finaleng['politic'] = finaleng['text'].map(politic)
finaleng['news'] = finaleng['text'].map(news)
finaleng['olymp'] = finaleng['text'].map(olymp)
finaleng['reprod'] = finaleng['text'].map(reprod)



    
from datetime import datetime

def get_dict(text):
    b = {}
    try:
        with open(text,'r',encoding='utf-8') as f:
            text = f.read().split("\n\n")
    except:
        print("ЧТОТО НЕ ТАК!!!")
    for i in text:
        b.update({datetime.strptime(i[:17],'%d.%m.%Y;  %H:%M'):i[17:]})    
    return b 
        
def get_txt(text):
    for i, y in sorted(get_dict(text).items()):
        print(i.strftime('%d.%m.%Y; %H:%M')+y,end="\n\n")


text = 'diary.txt'
get_txt(text)
''' text =
'12.04.2008; 21:38
My 3rd battery is about to quit.
Its actually a really cool feeling to be isolated in this capable little spacecraft, looking out over the Earth, while typing this journal.
I wish my office had a view like this (although it does have the advantage of a bathroom down the hall!).

26.02.2008; 18:55
I can't believe I've been up here for 3 weeks already. It's been overwhelming in so many ways. '''
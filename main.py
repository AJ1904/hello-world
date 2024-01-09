# Import necessary libraries
from taipy.gui import Gui
from taipy.gui import Gui, navigate
from taipy.gui import Markdown
import pandas as pd
import random

# Reference used: Google Translate and https://mixable.blog/hello-world-in-74-natural-languages/
# Dictionary containing languages and their 'hello world' phrases
my_dict = {'Afrikaans':'Hello Wêreld!','Albanian':'Përshendetje Botë!','Amharic':'ሰላም ልዑል!','Arabic':'مرحبا بالعالم!','Armenia':'Բարեւ աշխարհ!','Basque':'Kaixo Mundua!','Belarussian':'Прывітанне Сусвет!','Bengali':'ওহে বিশ্ব!','Bulgarian':'Здравей свят!','Catalan':'Hola món!','Chichewa':'Moni Dziko Lapansi!','Chinese':'你好世界！','Croatian':'Pozdrav svijete!','Czech':'Ahoj světe!','Danish':'Hej Verden!','Dutch':'Hallo Wereld!','English':'Hello World!','Estonian':'Tere maailm!','Finnish':'Hei maailma!','French':'Bonjour monde!','Frisian':'Hallo wrâld!','Georgian':'გამარჯობა მსოფლიო!','German':'Hallo Welt!','Greek':'Γειά σου Κόσμε!','Hausa':'Sannu Duniya!','Hebrew':'שלום עולם!','Hindi':'नमस्ते दुनिया!','Hungarian':'Helló Világ!','Icelandic':'Halló heimur!','Igbo':'Ndewo Ụwa!','Indonesian':'Halo Dunia!','Italian':'Ciao mondo!','Japanese':'こんにちは世界！','Kazakh':'Сәлем Әлем!','Khmer':'សួស្តី​ពិភពលោក!','Kyrgyz':'Салам дүйнө!','Lao':'ສະ​ບາຍ​ດີ​ຊາວ​ໂລກ!','Latvian':'Sveika pasaule!','Lithuanian':'Labas pasauli!','Luxemburgish':'Moien Welt!','Macedonian':'Здраво свету!','Malay':'Hai dunia!','Malayalam':'ഹലോ വേൾഡ്!','Mongolian':'Сайн уу дэлхий!','Myanmar':'မင်္ဂလာပါကမ္ဘာလောက!','Nepali':'नमस्कार संसार!','Norwegian':'Hei Verden!','Pashto':'سلام نړی!','Persian':'سلام دنیا!','Polish':'Witaj świecie!','Portuguese':'Olá Mundo!','Punjabi':'ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ!','Romanian':'Salut Lume!','Russian':'Привет мир!','Scots Gaelic':'Hàlo a Shaoghail!','Serbian':'Здраво Свете!','Sesotho':'Lefatše Lumela!','Sinhala':'හෙලෝ වර්ල්ඩ්!','Slovenian':'Pozdravljen svet!','Spanish':'¡Hola Mundo!','Sundanese':'Halo Dunya!','Swahili':'Salamu Dunia!','Swedish':'Hej världen!','Tajik':'Салом Ҷаҳон!','Thai':'สวัสดีชาวโลก!','Turkish':'Selam Dünya!','Ukrainian':'Привіт Світ!','Uzbek':'Salom Dunyo!','Vietnamese':'Chào thế giới!','Welsh':'Helo Byd!','Xhosa':'Molo Lizwe!','Yiddish':'העלא וועלט!','Yoruba':'Mo ki O Ile Aiye!','Zulu':'Sawubona Mhlaba!','Oromo':'Akkam jirtu Addunyaa!','Quechua':'Hola Mundo!'}

# Create a list of unique first letters from language names and sort it
alphabets = sorted(list(set([language[0] for language in my_dict.keys()])))

# Define a function to get 'hello world' phrases for languages starting with a specific letter
def get_hello_world(language_first_letter):
    # Generate a DataFrame with languages and their 'hello world' phrases based on the first letter
    answer = []
    for language in my_dict.keys():
        if language[0] == language_first_letter:
            answer.append({'Language': language, 'Hello World!': my_dict[language]})
    return pd.DataFrame(answer)
    
# Define a function to count the number of languages that start with each letter
def get_counts():
    # Calculate the count of languages for each unique first letter
    counts = []
    for alphabet in alphabets:
        count = 0
        for language in my_dict.keys():
            if language[0] == alphabet:
                count += 1
        counts.append(count)
    return counts

# Generate chart data based on counts of languages by first letter
chart_data = pd.DataFrame({'Alphabet': alphabets, 'Count': get_counts()})

# Randomly select a first letter and retrieve languages and 'hello world' phrases for that letter
value=random.choice(alphabets)
data = get_hello_world(value)

# Define a function to update data based on selected first letter
def update_data(state):
    state.data = get_hello_world(state.value)
    
# Markdown for the GUI layout
root_md = Markdown("""
# <center>Hello World!</center>
<|toggle|theme|class_name=nolabel|>
<|{value}|slider|lov={alphabets}|width=100%|on_change=update_data|labels=True|text_anchor=top|hover_text=Select a letter|>

<br />

<|layout|columns=1fr 3fr 1fr|
<| |>

<|{data}|table|show_all|>

<| |>
|>

<|layout|columns=1fr 1fr 1fr|
<|{chart_data}|chart|title=Language Count Trend by First Letter|>

<|{chart_data}|chart|type=pie|values=Count|labels=Alphabet|title=Distribution of Languages by First Letter|>

<|{chart_data}|chart|type=bar|title=Number of Languages by First Letter|>
|>

""")

# Create and run the GUI with defined parameters
gui = Gui(page=root_md)
gui.run(run_browser=True, use_reloader=True, title="Hello world!")

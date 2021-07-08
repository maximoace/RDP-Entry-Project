from bs4 import BeautifulSoup
from time import sleep
from seleniumManager import SeleniumManager
from postDataManager import PostDataManager
from forms import Form


manager = SeleniumManager()
url = 'http://www.csa-ma.com.br'
manager.connect(url)

#Open the Blog section.
manager.click(manager.select_by_id('nav-item-1579'))
sleep(3)

#Clicks untill all posts are loaded.
while(manager.check_text_condition(manager.select_by_class('load-more'), 'Mais notícias')):
    manager.click(manager.select_by_class('load-more-button'))
    sleep(3)

#Get the posts and stores in a .csv file.
content = manager.select_by_class('posts')
dataManager = PostDataManager(BeautifulSoup(content.get_attribute('outerHTML'), 'html.parser'))
data_cluster = dataManager.cluster_data_by_class('post')
spreadsheet = dataManager.create_dataframe(data_cluster)

#Form functions and values to be inserted.
form = Form(
    'Maximo Arthuro Pacheco Aceituno',
    'Desafio RDP',
    '(98) 98441-1331',
    'UNDB',
    'maximoarthuro@gmail.com',
    'https://github.com/maximoace',

    'Porque acredito que seria uma boa oportunidade para ambos, \
que posso contribuir para o crescimento da empresa, e que \
ela possa permitir e incentivar meu desenvolvimento pessoal, \
para evoluirmos juntos.'
)
fields = manager.select_all_by_class('wpcf7-form-control')
manager.fill_form(fields, form)

#This sleep is just to take a look before closing.
sleep(15)

manager.terminate()
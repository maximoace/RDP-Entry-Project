from bs4 import BeautifulSoup, PageElement
from pandas import DataFrame

class PostDataManager():

    def __init__(self, soup:BeautifulSoup):
        self.soup = soup

    #Gets the data from the post elements,
    #Needs to be manually adjusted
    #if used on any website other than
    #http://www.csa-ma.com.br/blog-2/

    def get_post_title(self, post:PageElement):
        return post.find('a').string

    def get_post_date(self, post:PageElement):
        return post.find('p').string

    def get_post_content(self, post:PageElement):
        return post.find('p').string

    def get_post_imgurl(self, post:PageElement):
        try:
            img_url = post.find('img').get('src')
        except:
            img_url = "Sem imagem"
        finally:
            return img_url

    #Filters the tags that has important data and get them.
    def organize_post(self, post:PageElement):
        return [
            self.get_post_title(post.find('div', class_='post-title')),
            self.get_post_date(post.find('div', class_='post-date')),
            self.get_post_content(post.find('div', class_='post-excerpt')),
            self.get_post_imgurl(post)
        ]

    #Clusters all the data of same class elements into a List.
    def cluster_data_by_class(self, class_name):
        data_cluster = self.soup.find_all(class_=class_name)
        return data_cluster

    #Process the group of data received, filtering it individually.
    def process_post_data(self, data_cluster):
        data_list = list()
        for data in data_cluster:
            data_list.append(self.organize_post(data))
        return data_list

    #Eliminates useless columns with \n, \t e \r of the Dataframe
    def format_dataframe(self, df:DataFrame):
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)
        for column in df.columns:
            if not df[column].all():
                df.drop(column, axis=1, inplace=True)
        return df

    #Creates a Dataframe and stores it in the data.csv file
    def create_dataframe(self, data_cluster):
        data_list = self.process_post_data(data_cluster)
        df = self.format_dataframe(DataFrame(data_list))
        df.to_csv('data.csv')
        return df

    ### Gets and Sets ###

    def get_soup(self):
        return self.soup

    def set_soup(self, soup:BeautifulSoup):
        self.soup = soup
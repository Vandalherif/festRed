__author__ = 'ugur'
import datetime
import db_config
import team

class user_fun:

    def add_user(self,username,password,email):
        _user={"username":unicode(username),"password":unicode(password),"email":unicode(email)}
        db_config.users.insert_one(_user)

    def add_Website(self,email,website_id):

        db_config.users.update_one({"email":email},{'$push':{"websites":website_id}})



site_bilgi = team("onedio.com")
site_bilgi.name



class website_fun:
    def add_website(self,name,url):
        if db_config.websites.find({"url":url}).count()==0:
            _website={"name":unicode(name),"url":unicode(url),"last_change":datetime.datetime.now()}
            self.website_id=db_config.websites.insert_one(_website).inserted_id
    def add_cms_name(self,url,cms_name):
        db_config.websites.update_one({"url":url},{'$push':{"other": {"cms":cms_name}}})
    def add_rss_link(self,url,rss_link):
        db_config.websites.update_one({"url":url},{'$push':{"other": {"rss":rss_link}}})

    def add_rss2_link(self,url,rss2_link):
        db_config.websites.update_one({"url":url},{'$push':{"other": {"rss2":rss2_link}}})

    def add_rdf_link(self,url,rdf_link):
        db_config.websites.update_one({"url":url},{'$push':{"other": {"rdf":rdf_link}}})

    def add_atom_link(self,url,atom_link):
        db_config.websites.update_one({"url":url},{'$push':{"other": {"atom":atom_link}}})



website_fun().add_website("listelist","listelist.com")
website_fun().add_rss_link("listelist.com","feed")



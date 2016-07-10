'''
Created on Jul 6, 2016

@author: Alex
'''
from django.template import Template, Context

class SocialView(object):
    share_image = ""
    share_site_name = ""
    share_image_alt = ""
    share_description = ""
    share_title = ""
    share_twitter = ""
    twitter_share_image = ""
    share_image_alt = ""
    page_title = ""

    def extra_params(self,context):
        params = super(SocialView,self).extra_params(context)
        extra = {"social_settings":self.social_settings(params),
                 "page_title":self._page_title(params)}
        params.update(extra)
        return params
    
    def _page_title(self,context):
            c_context = Context(context)
            return Template(self.__class__.page_title).render(c_context)
    
    def social_settings(self,context):
        """
        run class social settings against template
        """
        cls = self.__class__
        
        c_context = Context(context)
        
        process = lambda x: Template(x).render(c_context)
            
        if cls.twitter_share_image:
            twitter_img = cls.twitter_share_image
        else:
            twitter_img = cls.share_image
            
        di = {'share_site_name':process(cls.share_site_name),
              'share_image':process(cls.share_image),
              'twitter_share_image':process(twitter_img),
              'share_image_alt':process(cls.share_image_alt),
              'share_description':process(cls.share_description),
              'share_title':process(cls.share_title),
              'share_image_alt':process(cls.share_image_alt),
              }
        
        return di
    
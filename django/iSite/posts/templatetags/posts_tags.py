from django import template
from ..models import Post

register = template.Library() 

@register.inclusion_tag('posts/snippets/recent_posts.html')
def recent_posts():
    return {
        # This is just an example query, your actual models may vary
        'post_list': Post.objects.all().order_by("-posted_on")[:2]
    }   
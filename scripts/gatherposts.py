"""
Gather posts from https://git.coding.net/hhbcarl/graycarl.me.git.
It's a letor project.
"""
import os
import sys
import yaml
import logging
from django.utils import dateparse
from collections import namedtuple


Post = namedtuple('Post', ['slug', 'title', 'content', 'summary', 'pub_date'])


class Gather(object):

    dumpto = 'blog/fixtures/collected.yaml'

    def __init__(self):
        self.posts = []

    def process(self, path):
        slug = os.path.basename(path).lower()
        with open(os.path.join(path, 'contents.lr')) as f:
            raw = f.read()
        sections = raw.split('\n---\n')
        assert len(sections) == 4
        for section in sections:
            if section.startswith('title: '):
                title = section[len('title: '):].strip()
            elif section.startswith('body:\n'):
                content = section[len('body:\n'):].strip()
            elif section.startswith('pub_date: '):
                pub_date = dateparse.parse_date(section[len('pub_date: '):])
            elif section.startswith('summary: '):
                summary = section[len('summary: '):].strip()
            else:
                raise RuntimeError('Unknown content: %s' % section)
        post = Post(slug, title, content, summary, pub_date)
        self.posts.append(post)

    def dump(self):
        data = []
        for index, post in enumerate(sorted(self.posts, key=lambda p: p.pub_date)):
            fields = {}
            item = dict(model='blog.post', pk=index, fields=fields)
            fields['slug'] = post.slug
            fields['title'] = post.title
            fields['summary'] = post.summary
            fields['content'] = post.content
            fields['created_at'] = '{} 00:00:00+08:00'.format(post.pub_date)
            fields['updated_at'] = '{} 00:00:00+08:00'.format(post.pub_date)
            data.append(item)
        s = yaml.dump(data, default_flow_style=False, allow_unicode=True)
        with open(self.dumpto, 'wb') as f:
            f.write(s.encode('utf-8'))


def main(path):
    g = Gather()
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if not os.path.isdir(item):
            logging.info('[%s] is not a directory, ignore.', item)
            continue
        logging.info('Start to process [%s]', item)
        g.process(item)
    g.dump()


if __name__ == '__main__':
    path = sys.argv[1]
    logging.basicConfig(level='INFO')
    main(path)

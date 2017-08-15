"""
Gather wikis from https://git.coding.net/hhbcarl/PsnWiki.git
It's a gollum wiki repository
"""
import os
import sys
import yaml
import logging
from datetime import datetime


def main(path):
    dumpto = 'wiki/fixtures/collected.yaml'
    data = []
    for item in os.listdir(path):
        if not item.endswith('.md'):
            logging.info('Ignore: %s', item)
            continue
        with open(os.path.join(path, item), 'rb') as f:
            content = f.read().decode('utf-8')
        title = item[:-3]
        data.append(dict(
            model='wiki.page',
            fields=dict(
                slug=title.lower(),
                title=title,
                content=content,
                visit_count=0,
                visit_last_at=None,
                created_at='{}+08:00'.format(datetime.now()),
                updated_at='{}+08:00'.format(datetime.now())
            )
        ))
    s = yaml.dump(data, default_flow_style=False, allow_unicode=True)
    with open(dumpto, 'wb') as f:
        f.write(s.encode('utf-8'))


if __name__ == '__main__':
    path = sys.argv[1]
    logging.basicConfig(level='INFO')
    main(path)

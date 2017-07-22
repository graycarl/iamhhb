# I am HHB

这是一个个人网站的实现，重新做这么个简单的项目，主要是为了配合最近的学习而进行的练习。

## TODO

- Adapt to Django
- Disable user/group management in admin
- Support reStructuredText
- Support Post.status
  - draft
  - published
  - hidden
- Internationalization and localization
- RSS/Atom
- Travis CI


## Deploy Notes

### Bower

使用了 Heroku 的两个 BuildPacks:

```
$ heroku buildpacks -a iamhhb
=== iamhhb Buildpack URLs
1. heroku/nodejs
2. heroku/python
```

让 Bower 正常工作，创建了 Package.json:

```json
{
  ...
  "scripts": {
    "postinstall": "node_modules/bower/bin/bower install"
  },
  ...
  "dependencies": {
    "bower": "^1.8.0"
  }
}
```

### Migrate

在 Procfile 里面添加了 Realse 命令来执行 Migration.

see: https://devcenter.heroku.com/articles/release-phase#getting-started

# I am HHB

[![Build Status](https://travis-ci.org/graycarl/iamhhb.svg?branch=master)](https://travis-ci.org/graycarl/iamhhb)

这是一个个人网站的实现，重新做这么个简单的项目，主要是为了配合最近的学习而进行的练习。

目的就是要打造一个没有任何妥协，完全合理的项目。


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
  "somekey": "somevalue",
  "scripts": {
    "postinstall": "node_modules/bower/bin/bower install"
  },
  "dependencies": {
    "bower": "^1.8.0"
  }
}
```

### Migrate

在 Procfile 里面添加了 Release 命令来执行 Migration.

see: https://devcenter.heroku.com/articles/release-phase#getting-started

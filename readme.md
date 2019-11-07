# 说明

Noweb 是 **Now Web** 的意思。其用意是希望能够以最快的速度进入到项目的业务开发中来，而不必把过多的精力放在了环境配置上。

该想法来自于公司总是指派“Demo 开发任务”。而我因恰饭之故，不得不为这十分之一的斗米折腰。只不过，办法总比困难多。既然学不会陶渊明归去来兮的怪径，我只得早早做好抽身于琐碎的打算。

关于 Noweb 究竟需要哪些基础配置——什么样的配置是雪中送炭，什么样的配置则只是锦上添花；少了会不会不够用，多了是否显得笨重——这些都需要慎重考虑，以及反复地实践才能知道。

着急也没用，就从现在开始吧！

# Usage

创建虚拟环境：
```bash
$ git clone ...
$ cd Noweb
$ python3 -m venv py
```

进入虚拟环境：
```bash
$ source py/bin/activate
```

安装 python 依赖包：
```bash
(py) $ pip install requirements.txt
```

启动项目：
```bash
(py) $ python web/manage.py runserver 0.0.0.0:80
```

退出虚拟环境：
```bash
(py) $ deactivate
```

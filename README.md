# mo-test

介绍： 这是一个基于 [Seldom](https://github.com/SeldomQA/seldom) 测试框架实现的自动化项目。

### 安装

```shell
pip install -r requirements.txt
```

### 目录结构

```shell
mo/
├── db_data/
│   ├── base.py
│   ├── xxx_data.py
├── test_data/
│   ├── xxx.json
├── test_cases/
│   ├── test_xxx.py
├── reports/
└── run.py
```

* `db_data/` 数据库配置，以及连接数据库初始化数据。
* `logs/` 测试日志。
* `reports/` 报告目录。
* `test_data/` 测试参数化数据目录。
* `test_cases/` 测试用例目录。
* `run.py` 运行测试用例主文件。

### 运行

```shell
❯ python .\run.py

```

### 依赖项目



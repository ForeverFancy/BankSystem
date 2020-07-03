# 银行业务管理系统实验报告

##### PB17000215 张博文

## 概述

### 系统目标

<!-- 主要开发目标 -->
实现一个银行业务管理系统，后台 DBMS 使用 MySQL，前端开发工具不限，可以是 C/S 架构也可以是 B/S 架构。要求系统实现时要保证数据之间的一致性、鲁棒性。

### 需求说明

<!-- 主要功能需求 -->
- 客户管理：提供客户所有信息的增、删、改、查功能； 如果客户存在着关联账户或者贷款记录，则不允许删除；
- 账户管理：提供账户开户、销户、修改、查询功能，包括储蓄账户和支票账户； 账户号不允许修改；
- 贷款管理：提供贷款信息的增、删、查功能，提供贷款发放功能； 贷款信息一旦添加成功后不允许修改； 要求能查询每笔贷款的当前状态（未开始发放、发放中、已全部发放） ； 处于发放中状态的贷款记录不允许删除；
- 业务统计：按业务分类（储蓄、 贷款）和时间（月、 季、 年）统计各个支行的业务总金额和用户数， 要求对统计结果同时提供表格和曲线图两种可视化展示方式。

### 本报告的主要贡献

<!-- 报告的主要内容 -->
给出本系统的总体设计和每个模块的设计思路，给出最后的实现和测试结果。

## 总体设计

### 系统模块结构

系统可以分为前端和后端两大模块：
- 后端使用 Django REST Framework，获取和新建数据资源通过 GET, POST 方法访问 `/api/{table_name}` 实现，修改和删除等操作通过 PUT, DELETE 方法访问 `/api/{table_name}/{primary_key}` 实现；
- 前端基于开源的 bootstrap 模板实现。通过 javascript 访问后端对应的 url 获取数据资源并渲染，同时将新建、修改和删除的数据通过访问对应的 url 实现。业务统计功能在获取数据之后，分别用 dataTables 和 chart.js 实现。

#### 后端

后端的主要文件及对应的功能如下：

```
BankManagement
├── __init__.py
├── admin.py
├── apps.py
├── migrations
├── models.py           # 构建数据库的表结构
├── serializers.py      # 对数据进行序列化操作
├── tests.py
├── urls.py             # 自动 URL 路由
└── views.py            # 根据请求返回对应的数据或者对数据进行对应的操作
```

后端的数据资源放在 `/api/{table_name}` 中，修改和删除通过访问 `/api/{table_name}/{primary_key}` 实现。

#### 前端

前端的主要文件及对应的功能如下：

```
BankFrontend
├── __init__.py
├── __pycache__
├── admin.py
├── apps.py
├── migrations
├── models.py
├── templates                           # 模板文件
│   └── BankFrontend
│       ├── dist
│       │   ├── 400.html
│       │   ├── 404.html
│       │   ├── 500.html
│       │   ├── banks.html
│       │   ├── charts.html
│       │   ├── checkaccounts.html
│       │   ├── customers.html
│       │   ├── departments.html
│       │   ├── employees.html
│       │   ├── index.html
│       │   ├── loanreleases.html
│       │   ├── loans.html
│       │   ├── savingaccounts.html
│       │   └── tables.html
│       └── index.html
├── tests.py
├── urls.py                             # 定义前端访问的 url
└── views.py                            # 访问对应的 url 时渲染对应的模板并返回
```

前端所需要的静态文件如下：

```
static
├── dist
│   ├── assets
│   │   ├── demo
│   │   └── img
│   ├── css
│   └── js
├── scripts
└── src
    ├── assets
    │   ├── demo
    │   └── img
    ├── js
    ├── pug
    │   ├── layouts
    │   │   └── includes
    │   │       ├── head
    │   │       └── navigation
    │   └── pages
    │       └── includes
    └── scss
        ├── layout
        ├── navigation
        │   └── sidenav
        └── variables
```



<!-- 给出本系统的模块结构图，包括各级子模块，以及模块之间的接口关系。定义每个模块的基本功能。 -->

### 系统工作流程

<!-- 给出系统工作流程图 -->

### 数据库设计

<!-- 给出数据库设计ER图，逻辑数据库结构，以及最终的物理数据库结构。如果采用了特殊的物理数据库结构设计，例如分表、增加了冗余属性等，要求解释理由。 -->

## 详细设计

### 后端

<!-- 给出该模块的输入、输出和程序流程图。 -->

### 前端

## 实现与测试

### 实现结果

<!-- 给出各个功能需求的实现界面和运行结果。 -->

### 测试结果

<!-- 给出各个功能需求的测试用例和测试结果。 -->

## 总结与讨论

<!-- 总结本系统开发过程中的主要收获、教训。 -->
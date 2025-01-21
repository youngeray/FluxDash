<p align="center">
	<img alt="logo" src="https://github.com/user-attachments/assets/9ce3fa2b-7751-4d20-b1e0-601eeb60291d">

</p>
<h1 align="center" style="margin: 30px 0 30px; font-weight: bold;">Flux Panel</h1>
<h4 align="center">基于FastAPI+Vue3，实现前后端分离的快速开发框架,支持自动生成代码</h4>
<p align="center">
    <a href="https://github.com/Richard0403/FluxPanel"><img src="https://img.shields.io/github/stars/Richard0403/FluxPanel?style=social"></a>
	  <img src="https://img.shields.io/github/license/mashape/apistatus.svg"></a>
    <img src="https://img.shields.io/badge/python-≥3.11-blue">
    <img src="https://img.shields.io/badge/MySQL-≥5.7-blue">
</p>

## 平台简介

FluxPanel是一套全部开源的快速开发平台，毫无保留给个人及企业免费使用。

* 前端采用Vue3、Element Plus，基于<u>[RuoYi-Vue3](https://github.com/yangzongzhuan/RuoYi-Vue3)</u>前端项目修改。
* 后端采用FastAPI、sqlalchemy、MySQL、Redis、OAuth2 & Jwt, 基于<u>[RuoYi-Vue3-FastAPI](https://github.com/insistence/RuoYi-Vue3-FastAPI)</u>后端项目修改。
* 权限认证使用OAuth2 & Jwt，支持多终端认证系统。
* 支持加载动态权限菜单，多方式轻松权限控制。
* 支持代码生成，一键生成前后端代码
* 特别鸣谢：<u>[RuoYi-Vue3](https://github.com/yangzongzhuan/RuoYi-Vue3)， [RuoYi-Vue3-FastAPI](https://github.com/insistence/RuoYi-Vue3-FastAPI)</u>

## 在线体验地址

[FluxPanel](https://fluxpanel.igiggle.cn)

用户名: admin

密码: admin123

## 内置功能

1.  用户管理：用户是系统操作者，该功能主要完成系统用户配置。
2.  角色管理：角色菜单权限分配、设置角色按机构进行数据范围权限划分。
3.  菜单管理：配置系统菜单，操作权限，按钮权限标识等。
4.  部门管理：配置系统组织机构（公司、部门、小组）。
5.  岗位管理：配置系统用户所属担任职务。
6.  字典管理：对系统中经常使用的一些较为固定的数据进行维护。
7.  参数管理：对系统动态配置常用参数。
8.  通知公告：系统通知公告信息发布维护。
9.  操作日志：系统正常操作日志记录和查询；系统异常信息日志记录和查询。
10.  登录日志：系统登录日志记录查询包含登录异常。
11.  在线用户：当前系统中活跃用户状态监控。
12.  定时任务：在线（添加、修改、删除）任务调度包含执行结果日志。
13.  服务监控：监视当前系统CPU、内存、磁盘、堆栈等相关信息。
14.  缓存监控：对系统的缓存信息查询，命令统计等。
15.  系统接口：根据业务代码自动生成相关的api接口文档。
16.  **代码生成：根据mysql数据表的结构，自动生成python代码和vue代码**
17.  表单构建：（开发中）

## 演示图
![image](https://github.com/user-attachments/assets/64560c6f-76b7-48d5-8ba0-60d48d612c9e)
![image](https://github.com/user-attachments/assets/9c7df633-835c-4a00-8936-9bbd7b7cbc29)
![image](https://github.com/user-attachments/assets/5725f43e-7de5-464f-9fa2-bdf49c720ae5)
![image](https://github.com/user-attachments/assets/cdf24d54-b281-4d79-a59a-a32580701e3b)

## 项目开发及发布相关

### 开发

```bash
# 克隆项目
git clone https://github.com/Richard0403/FluxPanel.git

# 进入项目根目录
cd FluxPanel
```

#### 前端

本地node版本为v18.20.5， 其他版本可做尝试，不保证均可正常运行
```bash
# 进入前端目录
cd flux-frontend

# 安装依赖
npm install 或 yarn --registry=https://registry.npmmirror.com

# 建议不要直接使用 cnpm 安装依赖，会有各种诡异的 bug。可以通过如下操作解决 npm 下载速度慢的问题
npm install --registry=https://registry.npmmirror.com

# 启动服务
npm run dev 或 yarn dev
```

#### 后端

建议使用aconda管理环境， python版本推荐3.11

```bash
# 进入后端目录
cd ruoyi-fastapi-backend
# 安装依赖环境, 建议使用aconda， python版本推荐3.11
pip3 install -r requirements.txt

# 配置环境
在.env.dev（开发环境）文件中配置开发环境的数据库和redis，
.env.prod未正式环境使用， 复制.env.dev-templates文件即可

# 运行sql文件
1.新建数据库flux-data(默认，可修改)
2.使用命令或数据库连接工具运行sql文件夹下的flux-data.sql

# 运行后端
python3 app.py --env=dev

```

#### 访问

```bash
# 默认账号密码
账号：admin
密码：admin123

# 浏览器访问
地址：http://localhost:80
```

### 发布

#### 前端

```bash
# 构建测试环境
npm run build:stage 或 yarn build:stage

# 构建生产环境
npm run build:prod 或 yarn build:prod
```

#### 后端

```bash
# 配置环境
在.env.prod文件中配置生产环境的数据库和redis

# 运行后端
python3 app.py --env=prod
```

## 交流与赞助

如果有对本项目及FastAPI感兴趣的朋友，欢迎加入微信群学习交流。如果你觉得这个项目帮助到了你，你可以请作者喝杯咖啡表示鼓励☕。扫描下面微信二维码添加微信备注Flux即可进群。
<table>
    <tr>
        <td><img alt="zsxq" src="https://github.com/user-attachments/assets/2fb5871b-5e60-4062-a539-f4af0b0d3f76"></td>
        <td><img alt="zanzhu" src="https://github.com/user-attachments/assets/2da30ef6-ec5d-408d-ae2f-467be117097c"></td>
    </tr>
</table>






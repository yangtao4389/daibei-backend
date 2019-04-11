### 正式使用说明
#### 1.conf_docker文件夹里的内容应该与manage.py 同级 
> `mv -f conf_docker/* . `
#### 2.创建docker image
> 如果已经创建过，记得删除： `rm -rf uwsgi_docker.sock`
> `docker build -t django_default:1.0 . `

#### 5.创建docker container
> `docker run -d -p 8800:80 --name online_daibei-backend --restart=always -v /home/code/online/daibei-backend:/home/code/app -v /home/logs/online/daibei-backend/docker:/home/logs -v /home/session/online/daibei-backend/docker:/home/session -v /home/cache/online/daibei-backend/docker:/home/cache  -v /home/logs/online/daibei-backend/docker/rabbitmq:/data/rabbitmq/mnesia django_default:1.0  `正式
    






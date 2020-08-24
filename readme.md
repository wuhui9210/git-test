# 生成密钥

##配置用户
git config --global user.name "WU"  

##配置邮箱
git config --global user.email "wuhui9210@163.com" 

##生成公钥
ssh-keygen -t rsa -C "wuhui9210@163.com"

##查看公钥
cat ~/.ssh/id_rsa.pub



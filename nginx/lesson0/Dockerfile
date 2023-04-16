FROM node

WORKDIR /app
COPY package.json  ./
RUN npm install
COPY . .
RUN npm run build
# 第二阶段：构建 Nginx 镜像
FROM nginx:1.23.4
# 复制构建好的 Vue.js 应用到 Nginx 的静态文件目录
COPY --from=0 /app/dist /usr/share/nginx/html
# 启动 Nginx 服务
CMD ["nginx", "-g", "daemon off;"]
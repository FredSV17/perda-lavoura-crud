#stage 1
FROM node:latest as node
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
FROM nginx:latest
COPY --from=node /app/dist/frontend /usr/share/nginx/html
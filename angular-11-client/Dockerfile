FROM node:20-alpine as angular
WORKDIR /ng-app
COPY package*.json ./
RUN npm ci
COPY . ./
RUN npm run build

FROM nginx:alpine
ARG name
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=angular /ng-app/dist/$name/. /usr/share/nginx/html/
EXPOSE 80

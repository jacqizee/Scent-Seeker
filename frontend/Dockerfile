# syntax=docker/dockerfile:1

FROM node:18.7.0-alpine

ENV NODE_ENV=development

WORKDIR /Users/Jacqueline/Development/Scent-Seeker/frontend

COPY . .

RUN yarn add react-scripts
RUN yarn

EXPOSE 3000
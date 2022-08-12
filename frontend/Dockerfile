# syntax=docker/dockerfile:1

FROM node:18.7.0-alpine

WORKDIR /Users/Jacqueline/Development/Scent-Seeker/frontend

COPY package.json package.json
COPY yarn.lock yarn.lock

RUN yarn start

COPY . .
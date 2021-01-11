FROM node:14.4.0-alpine3.10


# set work directory
WORKDIR /usr/src/app

ADD . /frontend

RUN yarn install

ENV PATH ./usr/src/app/node_modules/.bin/:$PATH

CMD ["yarn", "run", "start"]

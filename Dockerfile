# Used for easy compilation testing on Linux from a mac.
FROM python:3.7.1-alpine
  
RUN pip install --upgrade pip

RUN apk add --no-cache gcc g++ musl-dev linux-headers make libffi-dev openssl-dev git
RUN apk add --no-cache vim
RUN apk add --no-cache zsh

RUN addgroup -S app && adduser -S -G app app

COPY . .

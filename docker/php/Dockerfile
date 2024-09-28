FROM php:8.2-fpm

RUN apt-get update -y && apt-get install -y git libzip-dev unzip

RUN curl http://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

RUN docker-php-ext-install zip pdo_mysql

### PHP USER
ARG PUID=1000
ARG PGID=1000

RUN addgroup --gid $PGID phpgroup

RUN useradd -rm \
    -d /home/phpuser \
    -s /bin/bash \
    -g phpgroup \
    -G sudo \
    -u $PUID \
    phpuser

# RUN chown -R phpuser:phpgroup ./findrightIngredients

USER phpuser

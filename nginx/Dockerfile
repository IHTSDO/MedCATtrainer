FROM nginx
# Add configuration
RUN rm /etc/nginx/conf.d/default.conf
ADD nginx.conf /etc/nginx/nginx.conf
# Add site
RUN mkdir /etc/nginx/sites-enabled/
ADD sites-enabled/ /etc/nginx/sites-enabled

RUN mkdir -p /etc/nginx/logs
RUN mkdir -p /etc/ssl/private
RUN mkdir -p /etc/ssl/certs
ADD ssl/nginx-letsencrypt.crt /etc/ssl/private/nginx-letsencrypt.crt
ADD ssl/nginx-letsencrypt.crt /etc/ssl/certs/nginx-letsencrypt.crt

FROM nginx
# Add configuration
RUN rm /etc/nginx/conf.d/default.conf
ADD nginx.conf /etc/nginx/nginx.conf
# Add site
RUN mkdir /etc/nginx/sites-enabled/
ADD sites-enabled/ /etc/nginx/sites-enabled

RUN mkdir -p /etc/ssl/private
ADD ssl/fullchain.pem /etc/ssl/private/fullchain.pem
ADD ssl/privkey.pem /etc/ssl/private/privkey.pem


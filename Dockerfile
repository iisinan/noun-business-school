FROM dunglas/frankenphp:php8.4-alpine

# Install PDO, PostgreSQL and required extensions
RUN install-php-extensions \
    pdo_pgsql \
    pgsql \
    pcntl \
    gd \
    intl \
    zip \
    bcmath \
    opcache

# Increase PHP upload limits & configure OPcache for maximum production performance
RUN echo 'upload_max_filesize = 100M' > /usr/local/etc/php/conf.d/uploads.ini && \
    echo 'post_max_size = 100M' >> /usr/local/etc/php/conf.d/uploads.ini && \
    echo 'memory_limit = 512M' >> /usr/local/etc/php/conf.d/uploads.ini && \
    echo 'opcache.enable = 1' > /usr/local/etc/php/conf.d/opcache.ini && \
    echo 'opcache.enable_cli = 1' >> /usr/local/etc/php/conf.d/opcache.ini && \
    echo 'opcache.memory_consumption = 256' >> /usr/local/etc/php/conf.d/opcache.ini && \
    echo 'opcache.interned_strings_buffer = 16' >> /usr/local/etc/php/conf.d/opcache.ini && \
    echo 'opcache.max_accelerated_files = 20000' >> /usr/local/etc/php/conf.d/opcache.ini && \
    echo 'opcache.validate_timestamps = 0' >> /usr/local/etc/php/conf.d/opcache.ini && \
    echo 'opcache.save_comments = 1' >> /usr/local/etc/php/conf.d/opcache.ini

# Copy application files
COPY . /app/
WORKDIR /app

# Copy Composer from official image
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Install Composer dependencies
RUN composer install --no-dev --optimize-autoloader --no-scripts --ignore-platform-reqs

# Run Laravel discovery
RUN php artisan package:discover --ansi

# Ensure Octane frankenphp worker exists
RUN if [ ! -f /app/public/frankenphp-worker.php ] && [ -f /app/vendor/laravel/octane/src/Commands/stubs/frankenphp-worker.php ]; then \
        cp /app/vendor/laravel/octane/src/Commands/stubs/frankenphp-worker.php /app/public/frankenphp-worker.php; \
    fi

# Set permissions
RUN chown -R www-data:www-data /app/storage /app/bootstrap/cache || true

# Install Node.js & build frontend (including Inertia SSR)
RUN apk add --no-cache nodejs npm
RUN rm -f package-lock.json && npm install
RUN npm run build

# Add startup script to handle migrations, cache, queues, SSR, and FrankenPHP Octane
RUN echo '#!/bin/sh' > /start.sh && \
    echo 'cd /app || exit 1' >> /start.sh && \
    echo 'php artisan optimize:clear || true' >> /start.sh && \
    echo 'php artisan config:cache || true' >> /start.sh && \
    echo 'php artisan route:cache || true' >> /start.sh && \
    echo 'php artisan view:cache || true' >> /start.sh && \
    echo 'php artisan event:cache || true' >> /start.sh && \
    echo 'php artisan migrate --force || true' >> /start.sh && \
    echo 'php artisan storage:link || true' >> /start.sh && \
    echo '(while true; do cd /app && php artisan queue:work redis --sleep=3 --tries=3 --max-time=3600 --memory=128; sleep 2; done) &' >> /start.sh && \
    echo '(while true; do cd /app && php artisan inertia:start-ssr; sleep 2; done) &' >> /start.sh && \
    echo '(while true; do cd /app && php artisan schedule:run --no-interaction --quiet; sleep 60; done) &' >> /start.sh && \
    echo 'exec php artisan octane:start --server=frankenphp --host=0.0.0.0 --port=${PORT:-8000} --workers=${OCTANE_WORKERS:-auto} --max-requests=500' >> /start.sh && \
    chmod +x /start.sh

EXPOSE 8000
CMD ["/start.sh"]

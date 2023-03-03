# Dockerizing Django with Postgres

Uses the default Django development server.

1. Rename .env.template to .env.
1. Set environmet variables in .env.
1. Build the images and run the containers:

   ```sh
   $ docker compose up -d
   ```

   Test it out at [http://localhost:8000](http://localhost:8000)

1. Run migrations in django container:

   ```sh
   $ docker compose exec django python manage.py migrate
   ```

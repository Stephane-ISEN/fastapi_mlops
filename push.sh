# connection au service de conteneurs
heroku container:login

# Construction de l'image docker et push sur Heroku
docker build . -t streamlit_isen

# Tag de l'image au registre Heroku
docker tag streamlit_isen registry.heroku.com/isen-mlflow-stephane/web

# Push de l'image sur Heroku
docker push registry.heroku.com/isen-mlflow-stephane/web              

# Lancement de l'application
heroku container:release web -a isen-mlflow-stephane     

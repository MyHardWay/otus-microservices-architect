# Установка

helm install otus-postgresql-api ./otus-postgresql-api/

kubectl apply -f .


# Постман коллекции

https://www.getpostman.com/collections/12b5d605be8c9cc6b3d1

# Для себя

HELM: POSTGRES

HELM - Это готовый деплоймент(всяких базок через одну команду) + параметризация

Сначала создаём папку с чартрами для нашего приложения
helm create chart-name

Затем лезем в Chart.yaml и указываем dependency и подгружаем необходимое нам приложение

dependencies: # A list of the chart requirements (optional)
  - name: postgresql
    version: 11.7.6
    repository: https://charts.bitnami.com/bitnami

Устанавливаем нужные нам чарты
helm dependency update
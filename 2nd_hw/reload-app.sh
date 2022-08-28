docker build -t myhardway/otus_microservices_arch_2nd_hw .
docker image push myhardway/otus_microservices_arch_2nd_hw
helm upgrade -i  otus-postgresql-api ./otus-postgresql-api/ --recreate-pods

# local testing
docker-compose up

* install awscli v2
* configure awscli with dummy values
* test command for local dynamodb
```
cd .\development\

aws dynamodb list-tables --endpoint-url http://localhost:8000

aws dynamodb delete-table `
    --table-name posts `
    --endpoint-url http://localhost:8000

aws dynamodb create-table `
    --table-name posts `
    --attribute-definitions AttributeName=id,AttributeType=S `
    --key-schema AttributeName=id,KeyType=HASH `
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 `
    --endpoint-url http://localhost:8000

aws dynamodb `
    batch-write-item --request-items file://item.json `
    --endpoint-url http://localhost:8000

aws dynamodb query `
    --table-name posts `
    --key-condition-expression "id = :v1" `
    --expression-attribute-values file://expression-attributes.json `
    --endpoint-url http://localhost:8000

aws dynamodb query `
    --table-name posts `
    --key-condition-expression "start_year = :y" `
    --expression-attribute-values file://expression-attributes-year.json `
    --endpoint-url http://localhost:8000

aws dynamodb get-item `
    --table-name posts `
    --key file://get-item.json `
    --endpoint-url http://localhost:8000
```

# Notes for code-engine

Build the container:
```
docker build -t quay.io/jjasghar/cloud-native-python:latest .
```

Push the container:
```
docker push quay.io/jjasghar/cloud-native-python:latest
```

Note: don't forget to make the container public.

Target the correct resource group:
```
ibmcloud target -g "Default"
```

Target the project:
```
ibmcloud ce project select -n jjtesting
```

Create the application: `-nw` will not wait
```
ibmcloud ce application create --name cloud-native-python --image quay.io/jjasghar/
cloud-native-python:latest
```

Get some info:
```
ibmcloud ce application get --name cloud-native-python
```

Spinning up "5" min instances:
```
ibmcloud ce application update --name cloud-native-python --min 5
```

Going back to zero instances:
```
ibmcloud ce application update --name cloud-native-python --min 0 -nw
```

Update the container:
```
docker build -t quay.io/jjasghar/cloud-native-python:latest .
docker push quay.io/jjasghar/cloud-native-python:latest
ibmcloud ce application update --name cloud-native-python
```

Delete the application:
```
ibmcloud ce application delete --name cloud-native-python
```

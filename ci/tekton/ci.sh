#!/bin/bash

# wget kubectl maybe

# get kubernetes creds

# load resources
kubectl apply -f resources

# load tasks

kubectl delete -f tasks || echo .
kubectl create -f tasks

# load pipeline
kubectl delete -f pipeline || echo .
kubectl create -f pipeline

# create pipeline run

kubectl create -f pipelineRun-build-and-push.yaml

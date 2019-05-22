# Bootcamp Infrastructure Project

The goal of this project is to automate the setup, lifecycle and teardown of bootcamp instances.
Instances will automatically pull down the latest project containers, and start the application.

This application can be hosted within the free tier provided by AWS.
## Services used
 - EC2
 - API Gateway
 - Lambda
 - Docker / Docker Compose

# How to Use
This project requires serverless framework (and [Node.js](https://nodejs.org/)) to deploy the lifecycle functions (Starting, stopping, checking the instance status). If you do not need them, you can skip this section. 

```
$ npm install serverless
```

### Starting the Infrastructure Stack in Cloudformation
 - Access the cloudformation console
 - Upload cloudformation.yml
 - Select application and key
 - Start the stack

The stack will have two outputs

| Output | Description |
| ------ | ------ |
| WebServerIP | Inital web server IP. If you restart the server, the IP may change. |
| WebServerID | Instance ID. Used for the lifecycle stack | 

### Lifecycle Lambda Configuration
```
$ sls deploy --instance <WebServerID>
```

Serverless framework will create an API gateway function with three endpoints
```
endpoints:
  GET - https://<ID>.execute-<region>.amazonaws.com/dev/start
  GET - https://<ID>.execute-api.<region>.amazonaws.com/dev/stop
  GET - https://<ID>.execute-api.<region>.amazonaws.com/dev/check
```

##### Start
Starts the associated web instance. Expected Output:
```
Instance Started, run /check to determine IP Address of bootcamp server
```

##### Stop
Stops the associated web instance. Expected Output
```
Instance Stopped
```

##### Check
The server is automatically configured to get an IP address when it starts up. If it has an IP, it will respond with the IP of the server.
```
Server is at 54.179.157.148
```

However, if there is no IP (probably because the instance is stopped), It will display an error message
```
Server does not have a public IP Address. Did you turn on the server with /start? If so wait a few moments for the server to start and try again.
```

# Teardown
 - Delete the cloudformation stack
 - Teardown the serverless service
 - ```
    $ sls remove --instance <WebServerID> 
    ```
 

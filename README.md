# wait-for-url
Script to wait for URL resource to be available before running command

waitURL.py is a pure python script that will wait on the availability of a URL resource. It is useful for synchronizing the spin-up of interdependent services, such as linked docker containers.

This script only depends on standard libraries, therefore no need to pull during compile time.

## Usage

```
waitURL.py URL timeout command-args
URL                         URL resource under test
TIMEOUT                     Timeout in seconds, zero for no timeout
COMMAND ARGS                Execute command with args after the test finishes
```

## Examples

Example of DockerFile where a container is waiting for Spring Cloud Configuration Server to be available in Discovery Service

```
$ git submodule add https://github.com/CalibreFinancialTechnology/wait-for-url.git
```

Dockerfile:

```
FROM java:8

EXPOSE 8080

VOLUME /tmp

ADD build/libs/service-0.0.1-SNAPSHOT.jar app.jar
RUN bash -c 'touch /app.jar'
ADD wait-for-url/waitURL.py wait.py

ENTRYPOINT python waitURL.py http://discovery:8761/eureka/apps/configserver 60 java -Djava.security.egd=file:/dev/./urandom -jar /app.jar
```


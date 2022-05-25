FROM golang:1.18-alpine

ARG DEPLOYENV
WORKDIR /app

COPY *.go /app
COPY file-${DEPLOYENV}.txt /app/file.txt

RUN go build -o server server.go

EXPOSE 8080

ENTRYPOINT [ "/app/server" ]

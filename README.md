## REFERENCE
[github](https://github.com/ALEXANDERSSONN)
## awaresome-compose 
[fastapi](https://github.com/docker/awesome-compose/tree/master/fastapi)

## wakatime project
[wakatime](https://wakatime.com/@spcn25/projects/glewvkqqyj?start=2023-02-27&end=2023-03-05)


# BUILD-IMAGE & TAG
- คำสั่งการ Build image
```
docker compose "fastapi/compose.yaml" up -d --build
```
- คำสั่งการ Tag
```
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```
# PUSH IMAGE TO DOCKER HUB 
- คำสั่งเข้าสู่ระบบ Docker ใน VSCODE
```
docker login
```
- คำสั่ง Push Image To Docker Hub
```
docker push TARGET_IMAGE[:TAG]
```

# CREATE STACK DEPLOY
- สร้างไฟล์ compose.yaml
```
version: '3.7'
services:
  api:
    image: TARGET_IMAGE[:TAG]
    networks:
     - webproxy
    environment:
     PORT: 8000
    logging:
      driver: json-file
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - app:/app
    deploy:
      replicas: 1
      labels:
        - traefik.docker.network=webproxy
        - traefik.enable=true
        - traefik.http.routers.${APPNAME}-https.entrypoints=websecure
        - traefik.http.routers.${APPNAME}-https.rule=Host("${APPNAME}.xops.ipv9.me")
        - traefik.http.routers.${APPNAME}-https.tls.certresolver=default
        - traefik.http.services.${APPNAME}.loadbalancer.server.port=8000

volumes:
  app:          
networks:
  webproxy:
    external: true

```
- นำ compose.yaml ไป Stack Deploy on local

# SWARM CLUSTER
- Revert Proxy compose.yaml
```
version: '3.7'
services:
  api:
    image: TARGET_IMAGE[:TAG]
    networks:
     - webproxy
    environment:
     PORT: 8000
    logging:
      driver: json-file
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - app:/app
    deploy:
      replicas: 1
      labels:
        - traefik.docker.network=webproxy
        - traefik.enable=true
        - traefik.http.routers.${APPNAME}-https.entrypoints=websecure
        - traefik.http.routers.${APPNAME}-https.rule=Host("${APPNAME} URL ")
        - traefik.http.routers.${APPNAME}-https.tls.certresolver=default
        - traefik.http.services.${APPNAME}.loadbalancer.server.port=8000

volumes:
  app:          
networks:
  webproxy:
    external: true
```

![image](https://user-images.githubusercontent.com/98762543/224471388-08298469-cf76-4fb7-9175-045fb0fb8a25.png)
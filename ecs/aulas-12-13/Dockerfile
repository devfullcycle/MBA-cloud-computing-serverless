FROM openjdk:17
ADD target/java-ecs-spring-0.0.1-SNAPSHOT.jar java-ecs.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","java-ecs.jar"]
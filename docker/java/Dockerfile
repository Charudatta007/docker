#base image
FROM eclipse-temurin:21-jdk

#working dir
WORKDIR /app

#copy code into continer

COPY src/Main.java /app/Main.java

#Compile code

RUN javac Main.java

#run
CMD ["java","Main"]

# Stage 1: Cache dependencies to speed up subsequent builds
FROM maven:3.9.2-eclipse-temurin-17 AS dependencies
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline

# Stage 2: Build application
FROM maven:3.9.2-eclipse-temurin-17 AS builder
WORKDIR /app
COPY --from=dependencies /app/pom.xml .
COPY src ./src
# Build the JAR, skipping tests for faster image creation (tests run in Jenkins)
RUN mvn clean package -DskipTests

# Stage 3: Lightweight Runtime
FROM eclipse-temurin:17-jre
WORKDIR /app

# Security Best Practice: Run as non-privileged user
RUN addgroup --system javauser && adduser --system javauser --ingroup javauser
USER javauser

# Copy only the final artifact from builder stage
COPY --from=builder /app/target/*.jar app.jar

# Expose Standard web port (if applicable)
EXPOSE 8080

# Start application, Use array syntax for better signal handling (SIGTERM)
ENTRYPOINT ["java", "-jar", "app.jar"]   

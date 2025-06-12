# Spring AI Embedding with PostgreSQL (pgvector)

This is a simple Spring Boot application that demonstrates how to:

- Generate embeddings using OpenAI via Spring AI  
- Store text and its vector embeddings in PostgreSQL with the pgvector extension  
- Perform similarity searches using cosine distance  

## 🧰 Requirements

- Java 17+  
- Maven  
- OpenAI API Key  
- PostgreSQL with `pgvector` extension enabled  

## 📦 Setup PostgreSQL

Enable the `pgvector` extension and create the table:

CREATE EXTENSION IF NOT EXISTS vector;  
CREATE TABLE documents (  
    id SERIAL PRIMARY KEY,  
    content TEXT NOT NULL,  
    embedding VECTOR(1536)  
);

## 🔐 Set OpenAI API Key

Export your OpenAI API key as an environment variable:

export OPENAI_API_KEY=sk-...

## ⚙️ Configure Database

Update your PostgreSQL connection settings in the Java file:

- URL: jdbc:postgresql://localhost:5432/yourdb  
- Username: youruser  
- Password: yourpassword  

## ▶️ How to Run

1. Clone the project or copy the Java file into a new Spring Boot app.  
2. Add the following dependencies to your `pom.xml`:

Group ID: org.springframework.boot  
Artifact ID: spring-boot-starter  

Group ID: org.springframework.ai  
Artifact ID: spring-ai-openai-spring-boot-starter  
Version: 0.8.0  

Group ID: org.postgresql  
Artifact ID: postgresql  
Version: 42.7.1  

3. Run the application:

mvn spring-boot:run

## 🧪 Example Output

Inserted text + embedding into DB.  
Most similar document:  
Spring AI integrates easily with LLMs. (distance=0.1234)

## 📚 References

- https://docs.spring.io/spring-ai/reference/  
- https://github.com/pgvector/pgvector  
- https://platform.openai.com/docs/guides/embeddings  

## 📌 Notes

- Embeddings use OpenAI's default model `text-embedding-ada-002`  
- Distance is calculated using the `<#>` cosine distance operator  
- Make sure the vector size in the database matches the model (e.g., VECTOR(1536))

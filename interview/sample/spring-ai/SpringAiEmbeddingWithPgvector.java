import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.boot.CommandLineRunner;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.ai.embedding.EmbeddingClient;
import org.springframework.ai.openai.OpenAiEmbeddingClient;
import org.springframework.ai.openai.api.OpenAiApi;

import javax.sql.DataSource;
import java.util.List;
import java.util.stream.Collectors;

@SpringBootApplication
public class SpringAiEmbeddingWithPgvector {

    public static void main(String[] args) {
        SpringApplication.run(SpringAiEmbeddingWithPgvector.class, args);
    }

    @Bean
    public OpenAiApi openAiApi() {
        return new OpenAiApi(System.getenv("OPENAI_API_KEY"));
    }

    @Bean
    public EmbeddingClient embeddingClient(OpenAiApi api) {
        return new OpenAiEmbeddingClient(api);
    }

    @Bean
    public DataSource dataSource() {
        var ds = new DriverManagerDataSource();
        ds.setDriverClassName("org.postgresql.Driver");
        ds.setUrl("jdbc:postgresql://localhost:5432/yourdb");
        ds.setUsername("youruser");
        ds.setPassword("yourpassword");
        return ds;
    }

    @Bean
    public CommandLineRunner run(EmbeddingClient embeddingClient, JdbcTemplate jdbcTemplate) {
        return args -> {
            // Step 1: Embed text
            String inputText = "Spring AI integrates easily with LLMs.";
            List<Double> vector = embeddingClient.embed(inputText).getEmbedding();

            // Step 2: Store in PostgreSQL
            String vectorStr = vector.stream().map(Object::toString).collect(Collectors.joining(","));
            jdbcTemplate.update("INSERT INTO documents (content, embedding) VALUES (?, ?::vector)", inputText, vectorStr);
            System.out.println("Inserted text + embedding into DB.");

            // Step 3: Similarity Search (Cosine Distance)
            String searchText = "AI framework for working with LLMs.";
            List<Double> searchVec = embeddingClient.embed(searchText).getEmbedding();
            String searchVecStr = searchVec.stream().map(Object::toString).collect(Collectors.joining(","));

            var results = jdbcTemplate.query(
                "SELECT content, embedding <#> ?::vector AS distance " +
                "FROM documents ORDER BY distance ASC LIMIT 1",
                new Object[]{searchVecStr},
                (rs, rowNum) -> rs.getString("content") + " (distance=" + rs.getDouble("distance") + ")"
            );

            System.out.println("Most similar document:");
            results.forEach(System.out::println);
        };
    }
}

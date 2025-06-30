package com.example.embabel;

import io.embabel.agent.annotation.*;
import io.embabel.boot.shell.annotation.EnableAgentShell;
import io.embabel.boot.spring.annotation.EnableAgents;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableAgentShell  // Enables interactive agent shell
@EnableAgents       // Scans for agent components
public class EmbabelApp {
    public static void main(String[] args) {
        SpringApplication.run(EmbabelApp.class, args);
    }

    @Agent(description = "Simple math agent")
    static class MathAgent {

        @Action
        @AchievesGoal(description = "Compute the sum of two numbers")
        public int add(Numbers input) {
            return input.a() + input.b();
        }
    }

    public record Numbers(int a, int b) {}
}

import java.util.Set;

// Write a Spring Application to find the unique characters within a given string.You will also need to find the total count of the unique characters found.
// Please write a controller and a service class.
// Example: Input:“AAAABBBBBVVVVVDDDDDSAAAA” Output:A B V D S,5

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

@SpringBootApplication
public class Solve1905 {
    public static void main(String[] args) {
        SpringApplication.run(Solve1905.class, args);
    }
}

@RestController
@RequestMapping("api/characters")
class CharacterController {

    private final CharacterService characterService;

    @Autowired
    public CharacterController(CharacterService characterService) {
        this.characterService = characterService;
    }

    @GetMapping("/counting/{input}")
    public CountResult getCounts(@PathVariable("input") String input) {
        return characterService.getCounts(input);
    }
}

@Service
class CharacterService {
    public CountResult getCounts(String input) {
        Set<Character> set = new HashSet<>();
        for (char c : input.toCharArray()) {
            set.add(c);
        }

        String uniqueCharacters = set.stream()
                                     .map(String::valueOf)
                                     .collect(Collectors.joining(" "));
        return new CountResult(uniqueCharacters, set.size());
    }
}

// Using Java 17 record for CountResult
record CountResult(String result, int count) {}

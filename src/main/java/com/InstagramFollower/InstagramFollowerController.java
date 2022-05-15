package com.InstagramFollower;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

@RestController
public class InstagramFollowerController {
    @RequestMapping
    public String helloWorld() {
        return "Hello World from Spring Boot";
    }

    @RequestMapping("/goodbye")
    public String goodbye() {
        return "Goodbye from Spring Boot";
    }

    @RequestMapping("/pythoncall")
    public String createUserScript() throws IOException {
        ProcessBuilder builder = new ProcessBuilder("python", System.getProperty("user.dir") + "\\scripts\\helloworld.py", "1");
        Process process = builder.start();

        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

        String lines = null;
        String result = "";
        while((lines=reader.readLine()) != null) {
            result = lines;
        }

        return result;
    }

}

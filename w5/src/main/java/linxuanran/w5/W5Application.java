package linxuanran.w5;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;

@SpringBootApplication
public class W5Application {
    @RequestMapping(value = "/*")
    public String hello(){
        return "hello world";
    }

    public static void main(String[] args) {
        SpringApplication.run(W5Application.class, args);
    }
}

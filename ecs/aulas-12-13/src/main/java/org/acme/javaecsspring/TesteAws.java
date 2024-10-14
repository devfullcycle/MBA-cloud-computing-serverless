package org.acme.javaecsspring;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("teste-aws")
public class TesteAws {

    @GetMapping
    @ResponseBody
    @ResponseStatus(HttpStatus.OK)
    public String get(@RequestParam("nome") String name) {
        return "Bem vindo ".concat(name).concat("!");
    }
}

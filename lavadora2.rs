use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::{digit1, space0},
    combinator::map_res,
    sequence::{delimited, tuple},
    IResult,
};
use std::str::FromStr;

// Estructura de la lavadora
#[derive(Debug)]
struct Lavadora {
    encendida: bool,
    nivel_agua: u8,
    temperatura: u8,
    duracion_ciclo: u8,
}

impl Lavadora {
    fn new() -> Self {
        Lavadora {
            encendida: false,
            nivel_agua: 0,
            temperatura: 30,
            duracion_ciclo: 30,
        }
    }

    fn encender(&mut self) {
        self.encendida = true;
        println!("Lavadora encendida");
    }

    fn apagar(&mut self) {
        self.encendida = false;
        println!("Lavadora apagada");
    }

    fn set_nivel_agua(&mut self, nivel: u8) {
        if nivel <= 100 {
            self.nivel_agua = nivel;
            println!("Nivel de agua establecido a {}%.", nivel);
        } else {
            println!("Nivel de agua no válido.");
        }
    }

    fn set_temperatura(&mut self, temperatura: u8) {
        if temperatura >= 30 && temperatura <= 90 {
            self.temperatura = temperatura;
            println!("Temperatura establecida a {}°C.", temperatura);
        } else {
            println!("Temperatura no válida.");
        }
    }

    fn iniciar_ciclo_lavado(&mut self) {
        if !self.encendida {
            println!("La lavadora está apagada. Enciéndela primero.");
            return;
        }

        println!("Iniciando ciclo de lavado...");
        self.llenar_agua();
        self.calentar_agua();
        self.lavar();
        self.enjuagar();
        self.centrifugar();
        println!("Ciclo de lavado completado.");
    }

    fn llenar_agua(&self) {
        println!("Llenando la lavadora con agua...");
        std::thread::sleep(std::time::Duration::from_secs(2));
        println!("Lavadora llena al {}%.", self.nivel_agua);
    }

    fn calentar_agua(&self) {
        println!("Calentando el agua a {}°C...", self.temperatura);
        std::thread::sleep(std::time::Duration::from_secs(2));
        println!("Agua calentada a {}°C.", self.temperatura);
    }

    fn lavar(&self) {
        println!("Lavando la ropa...");
        std::thread::sleep(std::time::Duration::from_secs(self.duracion_ciclo as u64));
        println!("Lavado completado.");
    }

    fn enjuagar(&self) {
        println!("Enjuagando la ropa...");
        std::thread::sleep(std::time::Duration::from_secs(2));
        println!("Enjuague completado.");
    }

    fn centrifugar(&self) {
        println!("Centrifugando la ropa...");
        std::thread::sleep(std::time::Duration::from_secs(2));
        println!("Centrifugado completado.");
    }
}

// Analizador léxico y sintáctico

// Tokens
#[derive(Debug)]
enum Token {
    Encender,
    Apagar,
    SetAgua(u8),
    SetTemperatura(u8),
    Iniciar,
}

// Función para parsear un número
fn parse_numero(input: &str) -> IResult<&str, u8> {
    map_res(digit1, |s: &str| u8::from_str(s))(input)
}

// Función para parsear el comando "encender"
fn parse_encender(input: &str) -> IResult<&str, Token> {
    let (input, _) = tag("encender")(input)?;
    Ok((input, Token::Encender))
}

// Función para parsear el comando "apagar"
fn parse_apagar(input: &str) -> IResult<&str, Token> {
    let (input, _) = tag("apagar")(input)?;
    Ok((input, Token::Apagar))
}

// Función para parsear el comando "set agua <número>"
fn parse_set_agua(input: &str) -> IResult<&str, Token> {
    let (input, _) = tuple((tag("set"), space0, tag("agua"), space0))(input)?;
    let (input, nivel) = parse_numero(input)?;
    Ok((input, Token::SetAgua(nivel)))
}

// Función para parsear el comando "set temperatura <número>"
fn parse_set_temperatura(input: &str) -> IResult<&str, Token> {
    let (input, _) = tuple((tag("set"), space0, tag("temperatura"), space0))(input)?;
    let (input, temp) = parse_numero(input)?;
    Ok((input, Token::SetTemperatura(temp)))
}

// Función para parsear el comando "iniciar"
fn parse_iniciar(input: &str) -> IResult<&str, Token> {
    let (input, _) = tag("iniciar")(input)?;
    Ok((input, Token::Iniciar))
}

// Función principal para parsear un comando
fn parse_comando(input: &str) -> IResult<&str, Token> {
    alt((
        parse_encender,
        parse_apagar,
        parse_set_agua,
        parse_set_temperatura,
        parse_iniciar,
    ))(input)
}

// Función para ejecutar un comando en la lavadora
fn ejecutar_comando(lavadora: &mut Lavadora, comando: &str) {
    match parse_comando(comando) {
        Ok((_, token)) => match token {
            Token::Encender => lavadora.encender(),
            Token::Apagar => lavadora.apagar(),
            Token::SetAgua(nivel) => lavadora.set_nivel_agua(nivel),
            Token::SetTemperatura(temp) => lavadora.set_temperatura(temp),
            Token::Iniciar => lavadora.iniciar_ciclo_lavado(),
        },
        Err(_) => println!("Comando no válido: {}", comando),
    }
}

fn main() {
    let mut lavadora = Lavadora::new();

    // Ejemplos de comandos
    let comandos = [
        "encender",
        "set agua 80",
        "set temperatura 40",
        "iniciar",
        "apagar",
    ];

    for comando in comandos.iter() {
        println!("Ejecutando comando: {}", comando);
        ejecutar_comando(&mut lavadora, comando);
        println!();
    }
}
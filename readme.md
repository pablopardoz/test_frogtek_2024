# Test Python Frogtek 2024

## Consideraciones generales:
- Se ha creado un repositorio público con 3 scripts, así como una clase City, un archivo de utils y uno de tests.
- Se ha creado una carpeta data en la que están los datos del ejercicio 3
- Se incluye el .env con la API keay al ser un ejercicio de ejemplo, pero lo ideal seria no subir este archivo a github.
- Se ha creado un entorno virtual de Python

## Ejercicio 1:
```
Escribe un script que sume todos los números de una cadena de texto pasada por parámetros.
```
La manera más simple y  directa que he visto para afrontarlo ha sido:
- Dividir el texto por los espacios
- Para cada elemento de la lista resultante, aplicarle la función de convertir palabra. Esta función símplemente convierte lo que entra a número, y devuelve un 0 si no es número.
También controla un posible error de números con decimales, permitiendo que pueda leer tanto números con `.` decimal como con `,`


## Ejercicio 2
```
Escribe un script que borre los ceros por la izquierda de una dirección IP pasada por parámetros.
```
Además de borrar los ceros a la izquierda, he añadido un pequeño validador para saber si la IP está bien formada cumpliendo símplemente que esté separada en 4 octetos, y que esos octetos sean números entre 0 y 255.

Para borrar el 0 a la izquierda simplemente he convertido cada octeto a numéro entero, así puedo gestionar más fácilmente que borre todos los ceros en caso de tener más de uno.
También puedo controlar que si es el octeto `.0.` lo deje igual.


## Ejercicio 3:
```
Escribe un script que tome como entrada un fichero con una lista de ciudades españolas (por ejemplo: "Huesca, Frogtek, Jaca, Guadalajara")
, una por línea. Por cada una de las ciudades el script hará dos queries a la API de OpenWeather
 (https://openweathermap.org, puedes usar la key 2b2c54bd4f822b146e23fc28a5e1c1e6) y guardará en el fichero original los datos que pedimos, separados por una coma (,):

Petición 1) Usando el nombre de la ciudad, consulta y guarda la temperatura,
la velocidad del viento y sus coordenadas geográficas (longitud y latitud).

Petición 2) Usando las coordenadas del punto anterior, consulta y guarda la hora del amanecer y anochecer
y valida que el nombre de la ciudad devuelto por la petición usando coordenadas
devuelve el mismo nombre de la ciudad del listado.

Si en el punto 1), hay algún tipo de error, se rellenarán los valores con 0 y no se hará la petición 2).

Por ejemplo, si el listado inicial fuera de dos ciudades de nombre EXISTE y NOEXISTE, el fichero final quedaría así:
EXISTE,23.21,2.54,-0.7499,40.560,06:45:12,21:45:12
NOEXISTE,0,0,0,0
```

- Se ha usado la clase dataclass de Python para encapsular el objeto Cty y que sea más cómodo trabajar.
- Se ha sacado tanto la API key como la url base a un .env, que se carga con la librería dotenv
Para ejecutar todo el flujo de datos se ha intentado simplificar al máximo, ciñendome en el enunciado:
- Se leen las ciudades de txt inicial.
- Se itera entre las ciudades y se crea una primera versión del objeto solo con el nombre y el país, el resto a 0.
- Se hace una primera petición a la API con el nombre y el país.
- Si es correcto, se rellenan los campos de coordenadas, temperatura y velocidad del viento. Si no es correcto, se queda todo a 0.
- En caso de que haya sido correcto, se hace una segunda llamada pasandole las coordenadas.
- Si también es correcto, se rellenan los datos de sunset y sunrise, y se valida el nombre.
- Si no es correcto, no  se hace nada (no está especificado en el enunciado qué hacer)
- Finalmente se sobreescribe el fichero original con los datos obtenidos.

Notas:
- Se han hecho dos llamadas como se especificaba, pero se pdría optimizar haciendo solo una, ya que la API trae todos los datos en el mismo json
- Se ha decidido guardar todos los datos el final para evitar abrir y cerrar el archivo muchas veces, pero este método no sería muy escalable pues guarda en una variable todo el contenido para luego imprimirlo. Lo ideal habría sido guardar linea a linea, y para mi gusto, habría dejado el archivo de entrada como estaba, y habría guardado todo en un archivo diferente `output.txt`. Esto permite tener constancia de lo que entra y de lo que sale en el caso de tener que debugar.

## Tests


##Instalación

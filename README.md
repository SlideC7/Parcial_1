# Parcial_1

Este código es un juego básico de Asteroids en el que el jugador controla una nave espacial y dispara a asteroides en movimiento. El jugador puede moverse con las teclas de dirección y disparar con la tecla de espacio. El objetivo es golpear los asteroides para acumular puntos, mientras se esquiva las balas de los enemigos y los asteroides que se mueven por la pantalla. El juego termina cuando el jugador ha perdido todas sus vidas.

El código importa los módulos necesarios: math, random, arcade y el archivo game_object.py que contiene la clase Player.

Las variables SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCALING, SPEED y BULLET_SPEED se utilizan para definir las dimensiones de la pantalla, el título del juego, la escala de las imágenes de los objetos del juego y las velocidades de la nave y las balas.

La clase App hereda de arcade.Window y se utiliza para definir y actualizar los objetos del juego. El constructor de la clase define una serie de variables, entre ellas una lista de sprites, una instancia de la clase Player, una lista de balas, una lista de asteroides, una puntuación, un número de vidas y un enfriamiento para los enemigos. El método add_enemy se llama cada medio segundo para crear un enemigo y una bala. Los métodos on_key_press y on_key_release se utilizan para detectar cuándo se han presionado o soltado las teclas de dirección y la barra espaciadora. El método on_update se llama en cada cuadro y se encarga de actualizar los objetos del juego. El método on_draw se encarga de dibujar los objetos en la pantalla.

Los métodos update_bullets y update_enemies se encargan de actualizar las listas de balas y asteroides. El método update_enemies_attack se utiliza para mover las balas de los enemigos y detectar colisiones con la nave del jugador. Si la nave es alcanzada, se pierde una vida y si se pierden todas las vidas, se muestra un mensaje de "Game Over".



¿Cómo ejecutar el juego?
1. Para ejecutar el problema entra al archivo Parcial_1
2. Doble clic izquierdo sobre el archivo build 
3. Doble clic izquierdo sobre el archivo exe.win-amd64-3.10
4. Doble clic izquierdo sobre mainAsteroids.exe


El juego nace con la idea de asteroids, pero lo convertí a mi versión de juego, es un tipo asteroids de que sobrevive sí te mueves 

Tenemos 3 personajes: 
Nave enemiga: se mueven de arriba hacía abajo y disparan una vez de manera vertical, sus balas te hacen daño pero la nave no, pero tu mente pensará que sí asi que tratarás de evitarlas, ahí esta el truco del juego.
Meteorito:
A diferencia de la nave enemiga sí te chocas con esta morirás. Mi intención fue hacerlas del mismo tamaño para engañar la mente del jugador. 
Nave principal: Dispara balas, tiene tres vidas, y puede moverse hacia arriba, abajo, derecha izquierda, dar vuelta de 360 grados. 



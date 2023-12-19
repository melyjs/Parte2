Carolina Celeste Fotografía

Bienvenido al repositorio de la web de Carolina Celeste Fotografía. Este proyecto es un sitio web diseñado para mostrar el trabajo de una fotógrafa especializada en eventos, familia, retratos y productos. Centrado en la cobertura de eventos de quince años. En la segunda etapa se ha incorporado la opcion de tomar cursos de fotografia. Este archivo README proporciona una descripción general del proyecto y cómo funciona.
Contenido

    Descripción
    Objetivos y motivación
    Planificación
    Uso
    Tecnologías Utilizadas
    Autor

Descripción

Se decidió hacer una web de fotografía enfocada en las fiestas de 15 años. El objetivo principal es proporcionar a los visitantes un vistazo al trabajo de una fotógrafa especializada en eventos, familia, retratos y productos, centrándose en la cobertura de eventos de quince años. Proporciona información sobre sus servicios de fotografía, así como una forma de contacto. Quienes esten interesados en tomar un curso de fotografia tienen la opción de pedir información del curso de su interés, informando disponibilidad para poder realizarlo. A continuación, se describen las secciones clave del sitio web:

    Navbar: Navegación que te permite moverte por el sitio web, incluyendo enlaces a la página de inicio, la sección "Acerca de", los paquetes de servicios y el formulario de contacto.

    Carrousel: Una sección de presentación en la página de inicio que muestra una selección de imágenes destacadas.

    Acerca de: Información sobre Carolina Celeste, su experiencia y su enfoque en la fotografía.

    Paquetes de Servicios: Una sección que describe los diferentes paquetes de servicios de fotografía que ofrece, junto con imágenes ilustrativas y descripciones detalladas de cada paquete.

    Formulario de Contacto: Un formulario interactivo que permite a los visitantes del sitio web ponerse en contacto con Carolina Celeste para solicitar presupuestos o hacer consultas.

    Cursos: Una sección interactiva donde los potenciales alumnos pueden proponer su disponibilidad para realizar cursos, donde se les permite crear cursos, visualizarlos, editarlos e incluso borrar los cursos que no podrá realizar para poder crearlos nuevamente cuando tenga disponibilidad

Objetivos y motivación

Consultamos a qué se dedicaba cada integrante del grupo para buscar una persona que le pueda dar una utilidad real al proyecto, se vieron dos posibilidades y se eligió la que nos pareció más posible. Se decidió centrarse en una parte específica del trabajo, en este caso la fotografía de fiestas de 15 años. Para poder incorporar una base de datos con CRUD se habia contemplado una opción de inspiraciones para fiestas, pero se optó por incorporar cursos de fotografía, donde el alumno puede completar sus datos, el curso de su interés, su disponibilidad horaria y en cantidad de meses. Puede crear varios cursos, así como editar o borrar sus propuestas.
Planificación

Realizamos varias reuniones por meet para decidir la maquetación del proyecto, diseño, vimos varias páginas de la temática en busca de inspiración, destacamos estas tres:

    Ejemplo 1
    Ejemplo 2
    Ejemplo 3

Inicialmente, decidimos crear una página única con desplazamiento (scroll) que comenzara con un carrusel de imágenes. Para las secciones "packs" y "about", optamos por utilizar el diseño en cuadrícula (grid) para organizar el contenido en tres y dos columnas respectivamente. Además, implementamos un formulario de contacto utilizando Formspree. Incorporamos los conocimientos de CRUD vistos en clase y los adaptamos al contenido de la pagina para que tuviera coherencia En mi caso preparé distintas galerías de fotos y los textos para las secciones.

A medida que avanzamos decidimos la tipografía, los colores de fuente y una gama clásica para el diseño general. La animación esta puesta en el carrousel de fotos del inicio. También utilizamos hovers para el navbar y los botones de formularios. Las secciones son responsive, comentamos el inicio de cada sección tanto en el archivo HTML principal como en el CSS para una mejor lectura.

Al ser scrolleable decidimos poner un botón al final de la página para volver al inicio. En la sección “packs” elegimos un diseño en tarjetas.

Finalmente, implementamos un formulario de contacto con la ayuda de la API de SheetDB. Este formulario se encuentra en una página separada a la que se puede acceder desde el enlace en el footer. El footer también incluye un enlace para regresar a la página de inicio, y el logo del sitio web también sirve como un acceso directo para volver a la parte superior de la página.

Se utilizó un modelo de plantillas de Django por lo que hubo que incorporar archivos estáticos y modificar rutas de acceso.

Con PythonAnyWere deployamos la pagina web integrando Python y Django, ejes centrales de este curso Full Stack
Uso

Puedes navegar por las diferentes secciones y utilizar el formulario de contacto según sea necesario. Con Python definimos modelos de datos para poder ejecutar las consultas a una base de datos MySQL y modificar sus registros.
Tecnologías Utilizadas

El proyecto utiliza las siguientes tecnologías:

    - HTML5 y CSS3 para la estructura y diseño del sitio web.
    - JavaScript para la funcionalidad interactiva del menú de navegación.
    - Formspree para el manejo del formulario de contacto.
    - Formulario con API en SheetDB
    - Python, Django y SQLite para realizar operacions CRUD en la opcion de Cursos de Fotografia

Autor

Este proyecto fue desarrollado por Carolina Coria.
En la segunda etapa incorporando a Melina Soto para el desarrollo Back-End

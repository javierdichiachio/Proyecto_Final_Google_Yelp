<p align="center"><img src="src\henry_logo.png" height=100></p>

<h1 align=center>PROYECTO GOOGLE - YELP</h1>
<p align="center">
<img src="src\44a8dac5-94bb-4363-a2d7-61b8c6b6959e.jpg"  height=300>
</p>

# Descripción
DataSolutions, es una empresa líder en el campo de análisis de datos, se posiciona como una empresa pionera en la transformación de información en conocimiento accionable. Nuestro enfoque se centra en proporcionar soluciones integrales que aprovechan la ciencia de datos para potenciar la toma de decisiones empresariales.

# Equipo encargado del proyecto

<p align="center">
<img src="src\integrantes2.png" height=250>
</p>

# Indice


- [Planteamiento del Proyecto ](#Planteamiento-del-Proyecto)
- [Objetivo y alcance del proyecto](#Objeto-y-alcance-del-Proyecto)
- [Indicadores Clave de Desempeño (KPIs)](#Indicadores-Clave-de-Desempeño (KPIs))
- [Metodologías](#Metodologías)
- [Stack Tecnológico ](#Stack-Tecnológico)
- [DataPipeline del proceso de ETL](#datapipeline-del-proceso-de-etl)
- [Carga Incremental](#carga-incremental)
- [Producto Machine Learning (ML)](#producto-machine-learning-ml)
- [Dashboard](#dashboard)
- [Conclusión](#conclusión)
- [Autores](#autores)

# Planteamiento del Proyecto

En el mundo digital actual, las plataformas Yelp y Google Maps han emergido como referentes clave en la toma de decisiones cotidianas. Yelp, un espacio global de reseñas,democratiza la retroalimentación del consumidor, ofreciendo testimonios que van más allá de simples puntuaciones. Desde restaurantes hasta servicios locales, las experiencias compartidas proporcionan una visión auténtica de la calidad percibida.

Google Maps, conocida por su funcionalidad de navegación, se ha transformado en un indispensable directorio de recomendaciones. Integrada con reseñas, esta herramienta no solo guía a los usuarios hacia su destino, sino que también les ofrece una visión detallada de la calidad de los negocios locales. Más que simples estrellas, las opiniones proporcionan narrativas ricas, destacando aspectos clave que definen la experiencia del usuario.

En conclusión, la transformación de plataformas como Yelp y Google Maps va más allá de ser directorios digitales; se han convertido en auténticos narradores de historias, donde las experiencias de los consumidores y los negocios se entrelazan. Al explorar estas plataformas, los usuarios no solo encuentran información, sino testimonios valiosos que les permiten tomar decisiones informadas. Estas narrativas colectivas sirven como faros digitales, guiando a los usuarios hacia elecciones fundamentadas y experiencias gratificantes en un mundo cada vez más centrado en la voz compartida.


# Objetivo y alcance del proyecto:
Como parte de la consultora DataSolutions de data, hemos sido contratados para realizar un análisis del mercado de restaurantes en California.

Nuestro cliente es una destacada agencia de viajes que ofrece tours en español en el estado de California, busca obtener una visión detallada de la opinión de los usuarios en plataformas clave como Yelp y Google Maps con respecto a los diferentes restaurantes de comida latinoamericana. El objetivo principal es proporcionar recomendaciones a sus usuarios basadas en las mismas. 

En este proyecto, nos proponemos montar la infraestructura necesaria y establecer un flujo de datos eficiente para lograr dos productos clave:

>Dashboard Interactivo: Desarrollaremos un dashboard interactivo que presentará información actualizada sobre el sector de restaurantes en California. Este recurso será una herramienta valiosa para que nuestro cliente acceda y visualice de manera intuitiva las tendencias, patrones y datos relevantes del mercado.

>API Funcional en un Servicio Web: Implementaremos una API funcional alojada en un servicio web que proporcionará recomendaciones de restaurantes a los usuarios. Estas recomendaciones podrán basarse en la categoría de los restaurantes o en características similares, utilizando datos recopilados de plataformas de reseñas populares.

Nuestro enfoque se centrará en brindar a nuestro cliente las herramientas necesarias para tomar decisiones informadas, aprovechando la gran cantidad de datos disponibles en estas plataformas de reseñas. Este análisis permitirá a la agencia de viajes ofrecer experiencias gastronómicas excepcionales a sus clientes, respaldadas por la voz auténtica de la comunidad.


# Indicadores Clave de Desempeño (KPIs):

En el ámbito empresarial y analítico, los **Indicadores Clave de Desempeño (KPIs)** desempeñan un papel fundamental al ofrecer una medida cuantificable del rendimiento de una organización o proyecto. Estos indicadores permiten evaluar el progreso hacia objetivos específicos, identificar áreas de mejora y tomar decisiones informadas.

En este contexto, en nuestro tablero incluiremos los siguientes KPIs:

* **Rating Promedio (estrellas) - Evolución:**
La valoración o rating promedio cuantifica la percepción general del público en relación con un producto o servicio. La misma se expresa en estrellas, en una escala de 1 a 5, y sirve como medida visual rápida de la calidad percibida; por tal motivo resulta indispensable realizar un seguimiento de la evolución del mismo a través de los años. El **objetivo** propuesto es que el indicador **incremente un 2% como mínimo** respecto del mismo período del año anterior y su fórmula de cálculo es la siguiente:

  > **Evolución_rating = (Rating promedio / Rating promedio año anterior - 1) * 100**

<br>

* **Satisfacción del cliente (% Reviews Positivas):**
La satisfacción del cliente se convierte en un KPI vital al evaluar el éxito de una iniciativa. Se calcula como la proporción de reseñas con expresión de sentimiento positivo (sentiment_score mayor a 0.5) con respecto al total de reseñas, y se establece como **objetivo** para este indicador un valor de **50% como mínimo** en el período de análisis. La fórmula es la siguiente:

   > **Satisfacción_cliente = Cantidad de reseñas con expresión de sentimiento positivo / Total reseñas * 100**

<br>

* **Satisfacción del Cliente - Evolución:**
La evolución de la satisfacción del cliente es una métrica dinámica que compara la satisfacción actual con la del año anterior. Este KPI ofrece perspectivas sobre las tendencias a lo largo del tiempo, permitiendo a las organizaciones entender cómo ha evolucionado la percepción del cliente y adaptarse en consecuencia. El **objetivo** propuesto es que el índice de satisfacción **incremente un 5%** de un año a otro.
La fórmula es la siguiente:

   > **Evolución_Satisfacción_cliente = Satisfacción_cliente / Satisfacción_cliente año anterior.**

<br>

* **Evolución Checkin - Anual:**
Este indicador evalúa la variación en la cantidad de accesos de clientes en un establecimiento o ubicación específica a lo largo del tiempo, por lo que el mismo permite realizar un seguimiento de la popularidad del local y planificar la necesidad de personal en distintos momentos del año. El **objetivo** propuesto es un **10% de crecimiento** en la cantidad de accesos respecto del mismo período del año anterior. La fórmula de cálculo es la siguiente: 

   > **Evolución_Checkin = Numero total de accesos en el período actual / Numero total de accesos en el mismo período del año anterior.**

## Metodologías
Este proyecto se basa en la metodología Scrum, la cual es altamente eficaz en entornos dinámicos y colaborativos. Scrum se destaca por su enfoque iterativo e incremental, dividiendo el proyecto en sprints manejables con entregables tangibles al final de cada iteración. Esto no solo permite una entrega temprana de valor, sino que también facilita la adaptabilidad a medida que los requisitos evolucionan.

## Stack Tecnológico 
<p align="center">
<img src="src\Stack_nuevo.PNG" height=400>
</p>

El stack tecnológico seleccionado para este proyecto se compone de herramientas y plataformas líderes que han sido cuidadosamente elegidas para maximizar la eficiencia y la calidad en el desarrollo. Aquí hay una descripción de cada componente y las razones detrás de su elección:

**Google Cloud**: Utilizamos Google Cloud como nuestra plataforma de nube principal debido a su escalabilidad, confiabilidad y conjunto integral de servicios. Google Cloud proporciona un entorno robusto para implementar, gestionar y escalar nuestras aplicaciones y servicios de manera eficiente.

**GitHub**: GitHub es una plataforma esencial para el control de versiones y la colaboración en desarrollo de software. Facilita la colaboración entre miembros del equipo, permitiendo la revisión de código, la gestión de problemas y el seguimiento de cambios. GitHub asegura un flujo de trabajo fluido y una integración continua efectiva.

**Python**: Python se ha convertido en el lenguaje de programación elegido debido a su simplicidad, legibilidad y versatilidad. Es una herramienta poderosa para el análisis de datos, la manipulación de datos y el desarrollo de aplicaciones, lo que lo hace ideal para nuestros propósitos.

**Mage**: es una herramienta de orquestación de contenedores que se utiliza para automatizar la implementación, el escalado y la administración de cargas de trabajo y servicios en contenedores. La orquestación de contenedores es la automatización y gestión del ciclo de vida de contenedores y servicios. Es un proceso de gestión y organización de múltiples contenedores y arquitectura de microservicios a escala.

**NLTK (Natural Language Toolkit)**: NLTK es una biblioteca de Python utilizada para procesar y analizar texto. Su inclusión en el stack tecnológico se debe a su capacidad para trabajar con procesamiento de lenguaje natural (NLP), lo que es esencial para comprender y analizar las reseñas y comentarios en nuestro proyecto.

Cada componente de este stack ha sido seleccionado cuidadosamente para contribuir a la eficacia, escalabilidad y calidad del proyecto, garantizando así una implementación exitosa y resultados sobresalientes.

## DataPipeline del proceso de ETL

<p align="center">
<img src="src\procesoETL.PNG" height=300>
</p>

El proceso de ETL es un proceso fundamental en el mundo de la gestión de datos y la informática, ya que permite obtener información significativa y utilizable a partir de múltiples fuentes de datos. Facilita la preparación de datos para su análisis, reporting o para alimentar sistemas que requieren información actualizada y precisa. Este Pipeline describe las diferentes etapas del proceso ETL utilizando herramientas de Google Cloud Platform (GCP).

* `Data soucers:` Durante esta fase, se extraen los datos desde múltiples fuentes. El propósito es almacenar esta información en un entorno de almacenamiento en la nube, comúnmente denominado 'data lake', que proporciona un espacio seguro y escalable para preservar los datos en su forma original. Esta estrategia busca mantener la integridad de los datos brutos, ofreciendo un lugar óptimo para su almacenamiento.

* `Transform (Transformar):` Una vez extraídos los datos, se someten a una serie de transformaciones. Estas pueden incluir limpieza de datos, filtrado, normalización, conversión de formatos, agregación o cualquier proceso que permita preparar los datos para el análisis o el almacenamiento en un repositorio final.

* `Load (Cargar):` En la etapa final, los datos transformados y procesados se cargan en "Google Big Query" definida como nuestro destino. Este destino lo vamos a denominar como nuestro data warehouse. El objetivo es almacenar los datos de manera que sean accesibles y útiles para su posterior análisis o uso.

## Carga Incremental

<p align="center">
<img src="src\carga_incremental.PNG" height=400>
</p>

La carga incremental es esencial en nuestro proyecto para mantener actualizados nuestros modelos con los nuevos datos de manera eficiente. Este proceso consta de varias etapas automatizadas:


+ La primera etapa implica la definición de nuestra orquestación mediante la herramienta 'MAGE' para ejecutar nuestro pipeline automáticamente.


+ Una vez definida la orquestación, llevamos a cabo nuestro datapipeline de ETL automatizado utilizando disparadores, también conocidos como triggers, programados previamente. Este proceso comienza extrayendo fuentes de nuestro almacenamiento de datos (Google Storage), las cuales pasan por el proceso de ETL para finalmente ser almacenadas en nuestro Data Warehouse (Google BigQuery).


+ Con los triggers programados, podemos actualizar nuestros datos mediante una nueva carga de datos, siguiendo nuestra orquestación. Esta carga almacena los datos nuevos en una nueva tabla en BigQuery, conocida como tabla auxiliar. Esta tabla es útil para comparar la información con datos anteriores y evitar duplicados, asegurándonos de sumar únicamente datos nuevos y únicos.


+ En la etapa final, ejecutamos una consulta en BigQuery cuya función principal es insertar la información de la tabla auxiliar en las tablas originales, evitando la duplicación de datos. Una vez completada esta operación, eliminamos las tablas auxiliares. Es importante destacar que esta consulta puede realizarse manualmente o automáticamente mediante un disparador previamente programado.

## Producto Machine Learning (ML)
En nuestro enfoque innovador de análisis de opiniones de usuarios, aprovechamos técnicas avanzadas de Procesamiento de Lenguaje Natural (PLN) y Machine Learning (ML) con la destacada herramienta NLTK, una biblioteca de Python especializada en el análisis y procesamiento del lenguaje natural.

Utilizando NLTK, llevamos a cabo tareas fundamentales como la tokenización, dividendo el texto en unidades más pequeñas llamadas tokens, lo que resulta crucial para comprender la estructura gramatical y semántica de las opiniones.

En nuestra metodología, la categorización de la importancia desempeña un papel central, donde técnicas avanzadas de ML asignan pesos a términos y frases específicas en las reseñas. Estos pesos se vinculan directamente con las estrellas asignadas a un restaurante, basándonos en el análisis de sentimiento y la asociación de términos con aspectos clave de la experiencia del usuario, como la calidad de la comida o el servicio.

La integración de NLTK y la categorización de importancia nos permite generar un rating compuesto más preciso y representativo, considerando no solo la calificación numérica de las estrellas, sino también la ponderación contextualizada de elementos específicos. Este enfoque refinado captura la complejidad de las opiniones, incluyendo la intensidad emocional asociada a diferentes aspectos, proporcionando a los usuarios una evaluación más matizada y detallada de cada restaurante.

En resumen, la combinación de NLTK, el análisis de sentimiento y la categorización de importancia en nuestro enfoque innovador de análisis de opiniones garantiza una comprensión más profunda y precisa de las reseñas de usuarios, brindando recomendaciones más informadas y personalizadas.

## Dashboard

## Conclusión
En el universo de Viajes Expedition, las reseñas se tornan en pilares fundamentales que guían a los usuarios en la elección de los mejores restaurantes durante sus viajes. Este componente esencial se argumenta por diversas razones que reflejan la importancia que estas opiniones tienen en la experiencia gastronómica de los viajeros.

Las reseñas actúan como una guía confiable en la selección de restaurantes, destacando aquellos lugares que han dejado una impresión positiva en otros viajeros. Este componente social de las reseñas no solo influye en la elección de un restaurante en particular, sino que también contribuye a la creación de una experiencia gastronómica compartida entre los usuarios de Viajes Expedition.

En resumen, en el contexto de Viajes Expedition, las reseñas no son solo comentarios aislados, sino herramientas esenciales que moldean las elecciones gastronómicas de los usuarios. Estas opiniones no solo informan, sino que también enriquecen la experiencia de viaje al conectar a los usuarios con los mejores restaurantes, contribuyendo así a una vivencia culinaria memorable durante sus expediciones.
## Autores

Los enlaces los llevaran a sus perfiles de LinkedIn.

+ [Francisco Angulo](https://www.linkedin.com/in/franciscomanuelangulo/)
+ [Javier Dichiachio](https://www.linkedin.com/in/javier-dichiachio-34104857/)
+ [Kathiuska Mangones](https://www.linkedin.com/in/kathiuska-mangones-ramos-1b494913b/)
+ [Luis Laurence](https://www.linkedin.com/in/luis-alberto-laurence-salas-036a32187/)
+ [Mariano Baigorria](https://www.linkedin.com/in/mariano-baigorria-b85004282/)

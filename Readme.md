<p align="center"><img src="src\henry_logo.png" height=100></p>

<h1 align=center>PROYECTO GOOGLE - YELP</h1>
<p align="center">
<img src="src\44a8dac5-94bb-4363-a2d7-61b8c6b6959e.jpg"  height=300>
</p>

# Descripción
DataSolutions, es una empresa líder en el campo de análisis de datos, se posiciona como una empresa pionera en la transformación de información en conocimiento accionable. Nuestro enfoque se centra en proporcionar soluciones integrales que aprovechan la ciencia de datos para potenciar la toma de decisiones empresariales.

# Equipo encargado del proyecto

<p align="center">
<img src="src\integrantes3.png" height=250>
</p>

# Indice (README)

- [Planteamiento del Proyecto](#planteamiento-del-proyecto)
- [Objetivo y alcance del proyecto](#objetivo-y-alcance-del-proyecto)
- [Metodologías](#metodologías)
- [Stack Tecnológico ](#stack-tecnológico)
- [DataPipeline del proceso de ETL](#datapipeline-del-proceso-de-etl)
- [Carga Incremental](#carga-incremental)
- [Producto Machine Learning (ML): Sistema de recomendación de restaurantes de comida latinoamericana](#producto-machine-learning-ml-sistema-de-recomendación-de-restaurantes-de-comida-latinoamericana)
- [Dashboard interactivo en Power BI](#dashboard-interactivo-en-power-bi)
- [Indicadores Clave de Desempeño (KPIs)](#indicadores-clave-de-desempeño-kpis)
- [Conclusión](#conclusión)
- [Índice de Archivos del Repositorio](#índice-de-archivos-del-repositorio)
- [Autores](#autores)

# Planteamiento del Proyecto

En el mundo digital actual, las plataformas Yelp y Google Maps han emergido como referentes clave en la toma de decisiones cotidianas. Yelp, un espacio global de reseñas, democratiza la retroalimentación del consumidor, ofreciendo testimonios que van más allá de simples puntuaciones. Desde restaurantes hasta servicios locales, las experiencias compartidas proporcionan una visión auténtica de la calidad percibida.

Google Maps, conocida por su funcionalidad de navegación, se ha transformado en un indispensable directorio de recomendaciones. Integrada con reseñas, esta herramienta no solo guía a los usuarios hacia su destino, sino que también les ofrece una visión detallada de la calidad de los negocios locales. Más que simples estrellas, las opiniones proporcionan narrativas ricas, destacando aspectos clave que definen la experiencia del usuario.

En conclusión, la transformación de plataformas como Yelp y Google Maps va más allá de ser directorios digitales; se han convertido en auténticos narradores de historias, donde las experiencias de los consumidores y los negocios se entrelazan. Al explorar estas plataformas, los usuarios no solo encuentran información, sino testimonios valiosos que les permiten tomar decisiones informadas. Estas narrativas colectivas sirven como faros digitales, guiando a los usuarios hacia elecciones fundamentadas y experiencias gratificantes en un mundo cada vez más centrado en la voz compartida.


# Objetivo y alcance del proyecto:
Como parte de la consultora DataSolutions, hemos sido contratados para realizar un análisis del mercado de restaurantes en California.

Nuestro cliente es una destacada agencia de viajes que ofrece tours en español en el estado de California, busca **obtener una visión detallada** de la **opinión de los usuarios** en plataformas clave como Yelp y Google Maps con respecto a los diferentes **restaurantes de comida latinoamericana**. El **objetivo principal** es **proporcionar recomendaciones a sus usuarios** basadas en las mismas. 

En este proyecto, nos proponemos montar la infraestructura necesaria y establecer un flujo de datos eficiente para lograr dos productos clave:

>**Dashboard Interactivo**: Desarrollaremos un dashboard interactivo en Power BI que presentará información actualizada sobre el sector de restaurantes en California. Este recurso será una herramienta valiosa para que nuestro cliente acceda y visualice de manera intuitiva las tendencias, patrones y datos relevantes del mercado.

>**Sistema de recomendación de restaurantes en un Servicio Web**: Implementaremos un programa alojado en un servicio web (Streamlit) que proporcionará recomendaciones de restaurantes de comida latinoamericana a los usuarios a traves de un bot de inteligencia artificial. Estas recomendaciones se realizarán en base a una valoración que contempla tanto el rating ingresado por el usuario, como el puntaje obtenido a través del análisis de sentimiento de las reseñas de los usuarios realizado por la biblioteca de procesamiento de lenguaje natural (NLTK).

Nuestro enfoque se centrará en brindar a nuestro cliente las herramientas que le permitan ofrecer experiencias gastronómicas excepcionales a sus clientes, respaldadas por la voz auténtica de la comunidad.


## Metodologías
Para la realización de este proyecto implementaremos la **metodología Scrum**, la cual es altamente eficaz en entornos dinámicos y colaborativos. Scrum se destaca por su enfoque **iterativo e incremental, dividiendo el proyecto en sprints** manejables con entregables tangibles al final de cada iteración. Esto no solo permite una entrega temprana de valor, sino que también facilita la adaptabilidad a medida que los requisitos evolucionan.

## Stack Tecnológico 
<p align="center">
<img src="src\Stack_final.png" height=400>
</p>

El stack tecnológico seleccionado para este proyecto se compone de herramientas y plataformas líderes que han sido cuidadosamente elegidas para maximizar la eficiencia y la calidad en el desarrollo. Aquí hay una descripción de cada componente y las razones detrás de su elección:

**Google Cloud**: Utilizamos Google Cloud como nuestra plataforma de nube principal debido a su escalabilidad, confiabilidad y conjunto integral de servicios. Google Cloud proporciona un entorno robusto para implementar, gestionar y escalar nuestras aplicaciones y servicios de manera eficiente.

**GitHub**: GitHub es una plataforma esencial para el control de versiones y la colaboración en desarrollo de software. Facilita la colaboración entre miembros del equipo, permitiendo la revisión de código, la gestión de problemas y el seguimiento de cambios. GitHub asegura un flujo de trabajo fluido y una integración continua efectiva.

**Python**: Python se ha convertido en el lenguaje de programación elegido debido a su simplicidad, legibilidad y versatilidad. Es una herramienta poderosa para el análisis de datos, la manipulación de datos y el desarrollo de aplicaciones, lo que lo hace ideal para nuestros propósitos.

**Mage**: es una herramienta de orquestación de contenedores que se utiliza para automatizar la implementación, el escalado y la administración de cargas de trabajo y servicios en contenedores. La orquestación de contenedores implica la automatización y gestión del ciclo de vida de los mismos. 

**NLTK (Natural Language Toolkit)**: NLTK es una biblioteca de Python utilizada para procesar y analizar texto. Su inclusión en el stack tecnológico se debe a su capacidad para trabajar con procesamiento de lenguaje natural (NLP), lo que es esencial para comprender y analizar las reseñas y comentarios en nuestro proyecto.

**LangChain**: LangChain es un framework para construir aplicaciones con modelos de lenguaje de gran tamaño (LLMs)2. También es un framework que utiliza LLMs para crear aplicaciones de inteligencia artificial, tales como chatbots similares al famoso ChatGPT, sistemas de preguntas sobre documentos, análisis automatizado de datos, sistemas de recomendación, asistentes virtuales personalizados y más. 
Las Cadenas son el núcleo vital de LangChain. Estas conexiones lógicas entre uno o más LLMs son la columna vertebral de la funcionalidad de LangChain1. Las Cadenas pueden ser simples o complejas, según las necesidades y los LLMs involucrados.

**Folium**: Folium es una biblioteca de Python que se utiliza para crear mapas interactivos. Su inclusión en el stack tecnológico se debe a su capacidad para trabajar con mapas interactivos, lo que es esencial para comprender y analizar las reseñas y comentarios en nuestro proyecto.

**Streamlit**: es un marco de desarrollo de código abierto para crear aplicaciones web interactivas con Python: permite de manera sencilla e integrada desarrollar aplicaciones gracias a la interacción con otras librerías para su empleo en campos de la teledetección, ciencia de datos, etc.

Cada componente de este stack ha sido seleccionado cuidadosamente para contribuir a la eficacia, escalabilidad y calidad del proyecto, garantizando así una implementación exitosa y resultados sobresalientes.

## DataPipeline del proceso de ETL

<p align="center">
<img src="src\procesoETL.PNG" height=300>
</p>

El **proceso de ETL** es un proceso fundamental en el mundo de la gestión de datos y la informática, ya que permite obtener información significativa y utilizable a partir de múltiples fuentes de datos. **Facilita la preparación de datos para su análisis**, reporting o para alimentar sistemas que requieren información actualizada y precisa. Este Pipeline describe las diferentes etapas del proceso ETL utilizando herramientas de **Google Cloud Platform (GCP)** y el orquestador **Mage**.

* `Data soucers:` Durante esta fase, se extraen los datos desde múltiples fuentes. El propósito es almacenar esta información en un entorno de almacenamiento en la nube, comúnmente denominado 'data lake', que proporciona un espacio seguro y escalable para preservar los datos en su forma original. Esta estrategia busca mantener la integridad de los datos brutos, ofreciendo un lugar óptimo para su almacenamiento.

* `Transform (Transformar):` Una vez extraídos los datos, se someten a una serie de transformaciones mediante una carga de trabajo automatizada a través de Mage. Esta pueden incluir limpieza de datos, filtrado, normalización, conversión de formatos, agregación o cualquier proceso que permita preparar los datos para el análisis o el posterior almacenamiento en una base de datos.

* `Load (Cargar):` En la etapa final, los datos transformados y procesados se cargan en "Google Big Query" definida como nuestra base de datos principal o data warehouse. El objetivo es almacenar los datos de manera que sean accesibles y útiles para su posterior análisis o uso.

## Carga Incremental

<p align="center">
<img src="src\carga_incremental.PNG" height=400>
</p>

La carga incremental es esencial en nuestro proyecto para mantener una base con información actualizada en función a los datos más recientes. Este proceso consta de varias etapas automatizadas:

+ La primera etapa implica la **definición de nuestra orquestación** mediante la herramienta 'MAGE' para ejecutar nuestro pipeline. La misma se compone de distintos segmentos en los cuales se van realizando distintas transformaciones sobre los datos y se conectan entre sí estableciendo un flujo de trabajo: cada segmento tiene entradas y salidas, que pueden depender de otros segmentos.

+ Una vez definida la orquestación, se **programan los disparadores o triggers** que darán inicio a nuestro datapipeline de ETL de manera automatizada. Este proceso comienza extrayendo fuentes de nuestro almacenamiento de datos (Google Cloud Storage), las cuales pasan por el proceso de ETL establecido en Mage para finalmente ser almacenadas en nuestro Data Warehouse (Google BigQuery).

+ Los datos procesados a traves de Mage **se cargan en una nueva tabla en BigQuery**, conocida como **tabla auxiliar**. Esta tabla es útil para comparar la información con los datos almacenados en nuestra base y evitar duplicados, asegurándonos de sumar únicamente datos nuevos y únicos.

+ En la etapa final, **ejecutamos una consulta programada** en BigQuery cuya función principal es **comparar** la información de la tabla auxiliar **con la base original**, e **insertarlos en la misma** en caso de no existir, evitando la duplicación de datos. 

+ Una vez completada esta operación, la misma consulta programada descripta anteriomente **vacía las tablas auxiliares**, dando finalización al proceso. 

<br>

# Productos finales del Proyecto:


## Producto Machine Learning (ML): Sistema de recomendación de restaurantes de comida latinoamericana
En nuestro enfoque innovador de análisis de opiniones de usuarios, aprovechamos técnicas avanzadas de Procesamiento de Lenguaje Natural (NLP) y Machine Learning (ML) con la destacada herramienta NLTK, una biblioteca de Python especializada en el análisis y procesamiento del lenguaje natural.

A traves de una función llamada **SentimentIntensityAnalyzer()**, llevamos a cabo un análisis de la intensidad del sentimiento contenido en las reseñas de usuarios de las plataformas de Google Maps y Yelp: la función utiliza recursos léxicos internos para asignar puntuaciones a las palabras en función de su carga sentimental, obteniendo como **resultado** una **puntuación numérica** que indica la **intensidad del sentimiento** en el texto. Esta puntuación puede variar **desde -1 (muy negativo) hasta 1 (muy positivo)**; **valores cercanos a 0** indican una **intensidad baja o neutral**. 

La integración de NLTK y el análisis de sentimiento nos **permite generar un rating compuesto** más preciso y representativo, **considerando** no sólo la **calificación numérica de las estrellas** incluida en la **reseña**, sino también la **puntuación numérica de intensidad de sentimiento** descripta anteriormente. Este enfoque refinado captura la complejidad de las opiniones, incluyendo la intensidad emocional asociada a diferentes aspectos, proporcionando a los usuarios una evaluación más matizada y detallada de cada restaurante.

Posteriormente, el **rating compuesto** obtenido en el proceso anterior se utiliza como **criterio base** para establecer un **ranking de recomendaciones más preciso** que se utilizará en el sistema de recomendación de restaurantes alojado en Streamlit y explicado a continuación.

LangChain es una biblioteca diseñada para simplificar la interacción con varios proveedores de grandes modelos de lenguaje (LLMs) como OpenAI. En el contexto de un proyecto de recomendación de restaurantes, LangChain se utiliza para analizar y procesar reseñas de restaurantes y otros datos relacionados con el lenguaje.

En nuestro caso, se crea un sistema que toma las reseñas de los clientes de varios restaurantes en California, las procesa utilizando **LangChain** y luego utiliza los resultados para hacer recomendaciones personalizadas a los usuarios. Este sistema tiene en cuenta factores como las preferencias con ratings del usuario, su ubicación, el tipo de comida que le gusta, tambien utiliza el análisis de sentimiento de las reseñas de los usuarios y la ubicación de los restaurantes para hacer recomendaciones y muestra en el mapa los restaurantes de la respuesta y los muestra en el mapa:

<p align="center">
<img src="src\Streamlit.png" height=300>
</p>

Es importante mencionar que la implementación de un proyecto de este tipo requeriría un conocimiento sólido de la programación y el procesamiento del lenguaje natural, así como acceso a una base de datos de restaurantes y reseñas.

### Chatbot de recomendaciones - Deploy en Streamlit
> La aplicación se encuentra disponible en la siguiente [ubicación](https://apprestaurantes-mumgsqtzxzqsbvrq6gynxo.streamlit.app/).


## Dashboard interactivo en Power BI
El dashboard desarrollado tiene como **objetivo principal** ofrecer una **visión rápida y detallada de las valoraciones de restaurantes** realizadas por los usuarios.

Se organiza en **3 páginas o tableros**:

> 1. **Portada**: Se presenta el tablero e incluye accesos directos a las demás páginas.

> 2. **Google Maps**: Incluye información referente a las reseñas sobre restaurantes de comida latinoamericana realizadas por los usuarios de la plataforma Google Maps.
El mismo incluye:

+ **3 Segmentadores (filtros)**: por **año, mes** y por **categoría de restaurant**.
+ **Mapa** que incluye la **localización de los restaurantes** y la **clasificación de los mismos** en función a la **cantidad de estrellas**.
+ **Tabla** que incluye el **nombre del restaurante**, la **valoración o rating promedio de las reseñas** y la **cantidad de reviews** en el período.
+ **3 KPIs**: **evolución del rating promedio, satisfacción del cliente y evolución de la satisfacción del cliente** (a desarrollar en el punto siguiente).

> 3. **Yelp**: Incluye información referente a las reseñas sobre restaurantes de comida latinoamericana realizadas por los usuarios de la plataforma Yelp.
El mismo incluye:

+ **4 Segmentadores (filtros)**: por **año, mes, ciudad** y por **categoría de restaurant**.
+ **Mapa** que incluye la **localización de los restaurantes** y la **clasificación de los mismos** en función a la **cantidad de estrellas**.
+ **Tabla** que incluye el **nombre del restaurante** y la **valoración o rating promedio de las reseñas** en el período.
+ **3 KPIs**: **evolución del rating promedio, satisfacción del cliente y evolución de los accesos o checkin** (a desarrollar en el punto siguiente).

### Vista previa del dashboard:
<p align="center">
<img src="src\dashboard_powerbi.gif" height=400>
</p>

> Se puede **acceder** a una **versión online** del **dashboard** ingresando en el siguiente [link](https://app.powerbi.com/view?r=eyJrIjoiNzU3OTVkNTEtNWQzNC00ZDhkLThiN2QtM2VhZTE1NzQ1ZWYyIiwidCI6IjQyNzViZDI3LTVmYjktNDEyNy1hZmE1LWVmZDU3OTdmMTNhOSIsImMiOjR9).

### Indicadores Clave de Desempeño (KPIs):

En el ámbito empresarial y analítico, los **Indicadores Clave de Desempeño (KPIs)** desempeñan un papel fundamental al ofrecer una medida cuantificable del rendimiento de una organización o proyecto. Estos indicadores permiten evaluar el progreso hacia objetivos específicos, identificar áreas de mejora y tomar decisiones informadas.

En este contexto, en nuestro tablero se incluyeron los siguientes KPIs:

* **Rating Promedio (estrellas) - Evolución:**
La valoración o rating promedio cuantifica la percepción general del público en relación con un producto o servicio, en este caso, los restaurantes. La misma se expresa en estrellas, en una escala de 1 a 5, y sirve como medida visual rápida de la calidad percibida; por tal motivo resulta indispensable realizar un seguimiento de la evolución del mismo a través de los años. El **objetivo** propuesto es que el indicador **incremente un 2% como mínimo** respecto del mismo período del año anterior y su fórmula de cálculo es la siguiente:

  > **Evolución_rating = (Rating promedio / Rating promedio año anterior - 1) * 100**


* **Satisfacción del cliente (% Reviews Positivas):**
La satisfacción del cliente se convierte en un KPI vital al evaluar el éxito de una iniciativa. Se calcula como la proporción de reseñas con expresión de sentimiento positivo (sentiment_score mayor a 0.5) con respecto al total de reseñas, y se establece como **objetivo** para este indicador un valor de **50% como mínimo** en el período de análisis. La fórmula es la siguiente:

   > **Satisfacción_cliente = Cantidad de reseñas con expresión de sentimiento positivo / Total reseñas * 100**


* **Satisfacción del Cliente - Evolución:**
La evolución de la satisfacción del cliente es una métrica dinámica que compara la satisfacción actual con la del año anterior. Este KPI ofrece perspectivas sobre las tendencias a lo largo del tiempo, permitiendo a las organizaciones entender cómo ha evolucionado la percepción del cliente y adaptarse en consecuencia. El **objetivo** propuesto es que el índice de satisfacción **incremente un 5%** de un año a otro.
La fórmula es la siguiente:

   > **Evolución_Satisfacción_cliente = (Satisfacción_cliente / Satisfacción_cliente año anterior - 1) * 100**


* **Evolución Checkin - Anual:**
Este indicador evalúa la variación en la cantidad de accesos de clientes en un establecimiento o ubicación específica a lo largo del tiempo, por lo que el mismo permite realizar un seguimiento de la popularidad del local y planificar la necesidad de personal en distintos momentos del año. El **objetivo** propuesto es un **10% de crecimiento** en la cantidad de accesos respecto del mismo período del año anterior. La fórmula de cálculo es la siguiente: 

   > **Evolución_Checkin = (Numero total de accesos en el período actual / Numero total de accesos año anterior - 1) * 100**

<br>

## Conclusión
En el universo de Viajes Expedition, las reseñas se tornan en pilares fundamentales que guían a los usuarios en la elección de los mejores restaurantes durante sus viajes. Este componente esencial se argumenta por diversas razones que reflejan la importancia que estas opiniones tienen en la experiencia gastronómica de los viajeros.

Las reseñas actúan como una guía confiable en la selección de restaurantes, destacando aquellos lugares que han dejado una impresión positiva en otros viajeros. Este componente social de las reseñas no solo influye en la elección de un restaurante en particular, sino que también contribuye a la creación de una experiencia gastronómica compartida entre los usuarios de Viajes Expedition.

En resumen, en el contexto de Viajes Expedition, las reseñas no son solo comentarios aislados, sino herramientas esenciales que moldean las elecciones gastronómicas de los usuarios. Estas opiniones no solo informan, sino que también enriquecen la experiencia de viaje al conectar a los usuarios con los mejores restaurantes, contribuyendo así a una vivencia culinaria memorable durante sus expediciones.



# Índice de Archivos del Repositorio

## Carpeta Data

+ Incluye los archivos parquet que contienen toda la información de reviews y restaurantes luego del proceso de ETL. Es la misma información que está almacenada en Big Query.

## Carpeta EDA-ETL

+ Incluye los archivos donde se realizan los procesos de Análisis Exploratorio de Datos (EDA) y Extracción, Transformación y Carga (ETL), que luego se automatizan a través de Mage y se almacena en Big Query.

## Carpeta Power BI

+ Incluye el Dashboard desarrollado en Power BI Desktop y que fue subido a Power BI Service.

## Carpeta Streamlit

+ Incluye los archivos necesarios para montar el chatbot de recomendaciones de restaurantes en Streamlit.

## Carpeta raíz del repositorio

+ [Diccionario de Datos](Diccionario_de_datos.pdf)


## Autores

Haciendo click en los enlaces se podrá ingresar a sus perfiles de LinkedIn:

+ [Francisco Angulo](https://www.linkedin.com/in/franciscomanuelangulo/)
+ [Javier Dichiachio](https://www.linkedin.com/in/javier-dichiachio-34104857/)
+ [Kathiuska Mangones](https://www.linkedin.com/in/kathiuska-mangones-ramos-1b494913b/)
+ [Luis Laurence](https://www.linkedin.com/in/luis-alberto-laurence-salas-036a32187/)
+ [Mariano Baigorria](https://www.linkedin.com/in/mariano-baigorria-b85004282/)

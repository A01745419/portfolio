import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import Imagen from './components/Imagen';
import jolo from "./images/jolo.jpg"
import idiomas from "./images/idiomas.jpg"
import coursera from "./images/coursera.png"
import github from './images/github.png'

function App() {
  return (
    <div className="App">
      <Header 
        user = "ITESM"
        title = "Portafolio"
        score = "ITC"/>
      <h1>José Luis Madrigal Sánchez</h1>
      <div className='info'>
        <Imagen img={jolo}/>
        <div>
        <p>Perseverante y apasionado por realizar
        actividades con un alto nivel de calidad.
        Enfocado en el trabajo colaborativo, tolerancia y
        la ética profesional. Interesado en hablar en
        público y técnicas de persuasión. Experiencia
        con el sistema operativo Windows, así como con
        analítica de datos y programación orientada a objetos.
        </p>
        <h3>Habilidades</h3>
        <li>Resolución de problemas</li>
        <li>Comunicación activa</li>
        <li>Gestión del tiempo</li>
          </div>
      </div>
      <div className='certificados'>
        <div className='cursos'>
          <div>
          <h4>Cursos</h4>
          <li>IT Security: Defense against the digital dark
            arts de Google</li>
          <li>Market Research and Consumer Behavior de
            IE Business School</li>
          <li>Cybersecurity Roles, Processes & Operating
            System Security de IBM</li>
          <li>Innovations in Investment Technology:
            Artificial Intelligence de la Universidad de
            Michigan</li>
          <li>Blockchain Business Models de la
            Universidad de Duke University</li>
            </div>
          <Imagen img={coursera} />
        </div>
        <div className='idiomas'>
          <Imagen img={idiomas} />
          <div>
          <h4>Idiomas</h4>
          <li>Español: Nativo</li>
          <li>Ingles: TOEFL ITP 600</li>
          <li>Aleman: Goethe A1</li>
          </div>
        </div>
      </div>
      <div className='universidad'>
          <h3>Estudios</h3>
          <p>Licenciatura en Ingeniería en Tecnologías
          Computacionales en Tecnologico
          de Monterrey Campus Estado de Mexico/ 2020-actual</p>
          <h3>Participaciones relevantes</h3>
          <li>Migración de plataforma de HagamosCine a Django</li>
          <li>Generación de aplicación para Instituto Irapuatense Down</li>
          <h3>Premios</h3>
          <li>Beca al talento académico 2021</li>
          <li>2do lugar Winter Games 2020: desafíos físicos intelectuales y físicos entre comunidades</li>
          <li>1er lugar HackMx 2021: Detección de fraudes bancarios con redes neuronales</li>
      </div>
      <div className='github'>
        <Imagen img={github} />
        <h3>Proyectos importantes</h3>
        <li>Python / jugador estratégico para el marco del juego Dagor de Caterpillars que utiliza la función minimax.</li>
        <li>Python / análisis de datos de expedientes de COVID México.</li>
        <li>Python / estadísticas y regresión lineal con aprendizaje automático básico para un archivo de registro de alimentos.</li>
        <li>Python / C# / sistema multiagente con biblioteca Mesa basado en sincronización eficiente del tráfico vehicular que se simula en un proyecto 3D de Unity.</li>
        <li>Python / reto HackMx NDS Cognitive Labs, detección de fraude bancario con machine learning.</li>
        <li>Python / análisis de información de Twitter con cuenta de desarrollador.</li>
        <li>R / análisis biológico con dataset de GEO y recursos bioinformáticos.</li>
      </div>
      <div className='github'>
        <a className='git' href="https://github.com/A01745419/portfolio"><span class="fa-container text-center    mr-2"><i class="fa fa-linkedin-square"></i></span>Ir a Github</a>
      </div>
      <div className='contactos'>
        <h3>Contactos</h3>
        <p>Correo: jlmadrigal1917@gmail.com</p>
        <p>Teléfono: 5534325251</p>
        <a className='link' href="https://www.linkedin.com/in/jose-luis-madrigals-31201/"><span class="fa-container text-center    mr-2"><i class="fa fa-linkedin-square"></i></span>LinkedIn</a>
      </div>
      <p className='leyenda'>App de React "PORTFOLIO-WEBPAGE": creada por Jose Luis Madrigal Sanchez 2023</p>
    </div>
  );
}

export default App;

// Autor: Jose Luis Madrigal
// App con perfiles de linkedin
import './App.css';
import paulo from "./images/paulo.jpg";
import angel from "./images/angel.jpg";
import pablo from "./images/pablo.jpg";
import lalo from "./images/lalo.jpg";
import Titulo from './components/Titulo';
import Perfil from './components/Perfil';

function App() {
  return (
    <div className="App">
      <Titulo texto="LinkedIn ITCs"/>
      <Perfil perfil={{
        imagen: paulo,
        nombre: "Paulo Ogando Gulias",
        info: "Especializado en videojuegos",
        btn_conectar: "+ Conectar"
      }} />
      <Perfil perfil={{
        imagen: angel,
        nombre: "Jose Angel Garcia Gomez",
        info: "Especializado en desarrollo web",
        btn_conectar: "+ Conectar"
      }} />
      <Perfil perfil={{
        imagen: pablo,
        nombre: "Pablo Gonzalez de la Parra",
        info: "Especializado en IA avanzada",
        btn_conectar: "+ Conectar"
      }} />
      <Perfil perfil={{
        imagen: lalo,
        nombre: "Eduardo Joel Cortez Valente",
        info: "Especializado en BD avanzada",
        btn_conectar: "+ Conectar"
      }} />
    </div>
  );
}

export default App;

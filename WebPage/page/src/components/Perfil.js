// Autor: Jose Luis Madrigal
// Perfil con componentes de datos de persona en App
import "../styles/Perfil.css";
import Nombre from "./Nombre";
import Info from "./Info";
import BotonConectar from "./BotonConectar";
import Imagen from "./Imagen";

const Perfil = (props) => {
    return <div className="perfil">
        <Imagen img={props.perfil.imagen}/>
        <Nombre nombre = {props.perfil.nombre}/>
        <Info info = {props.perfil.info}/>
        <BotonConectar btn_conectar = {props.perfil.btn_conectar}/>
        </div>;

};

export default Perfil
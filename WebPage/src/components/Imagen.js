// Autor: Jose Luis Madrigal
// Una imagen que se importa desde el proyecto

const Imagen = (props) => {
    return <img src={props.img} alt="Foto" width="320" height="320"/>;
};

export default Imagen
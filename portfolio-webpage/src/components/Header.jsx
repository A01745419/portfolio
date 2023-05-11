import React from 'react'
import '../styles/Header.css'

const Header = (props) => {
  return (
    <div className='header'>
        <h1>{props.user ? props.user : '---'}</h1>
        <h1>{props.title ? props.title : 'Quiz App'}</h1>
        <h1>{props.score ? props.score : '0'}</h1>
    </div>
  )
}

export default Header

import './button.css';
import React  from 'react';


function NumBtn(property) {

    return (
        
            <button className='one_button' onClick={() =>property.func(property.digt)}>{property.digt}</button>
    );
};
  
export default NumBtn;
  


import React, { useEffect, useState } from 'react';
import './calculator.css';
import NumBtn from './button.js';


const num_list = ['ac', '+/-','%', '/',7,8,9,'x',4,5,6,'-',1,2,3,'+','<',0,'.','=']


function Calculator() {
    const [temp, setTemp] = useState('')
   
    function innerInput (num) {
        // const line = document.getElementById('input');
        if (num === "="){
            setTemp(eval(temp.replace('x','*')))
            // setTemp(eval(temp))
        }
        else if (num === '+/-'){
            setTemp((-1*eval(temp)).toString())
            
        }
        else if(num==="ac"){
            setTemp("")
        }
        // else if(num=="x"){
        //     setTemp(temp + '*')
        // }
        else if(num==='<'){
            setTemp(temp[temp.length - 1])
            // setTemp(temp.slice(0,-1))

        }
        else if(0<=temp[-1]<=9){
            setTemp(temp + num)
        }

    }

    return (
        <div className="calculator">
            <div className='screen_button'>
                <h2 className="_input">{temp}</h2>
                <div className="buttons">
                    {num_list.map((item) => <NumBtn digt={item} func={innerInput}/>)}
                </div>
            </div>
        </div>
    );
};


  
export default Calculator;
  



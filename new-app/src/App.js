import React from 'react';
import './App.css';
import { useState,useEffect } from 'react';

function App() {
  const[preState,setPreState] = useState('')
  const[curState,setCurState] = useState('')
  const[operator,setOperator] = useState(null)
  const[total,setTotal] = useState(false)

  const inputNum = (e) => {
    if (total) return
    // If it's point after point, leave it like that
    if (curState.includes('.') && e.target.innerText === '.') return;
    
    curState  
      // If there was a number before in curState, add with the number of curState, if not, then insert a letter into curState  curState
    ? setCurState((pre) => pre + e.target.innerText)
    : setCurState(e.target.innerText);
  };

  const operatorType = (e) => {
    // Checks if a number is ever entered or if it's a blank screen
    if ((curState === '') && (preState === '')) return
    setOperator(e.target.innerText)
    // in case it's after (=)
    setTotal(false)
    // that I do an operator after a full calculation, so I calculate and add an operator
    if(preState !== '') { 
        equals()
        return
    }
    // In case it is a single number then substitute between the variables
    setPreState(curState)
    setCurState('')
  };
    
  const equals = (e) => {

    if (e.target.innerText === '='){
      setOperator('')
      setTotal(true)
    };

    let cal
    switch ( (operator)) {
      case '/':
        cal = String(parseFloat(preState) / parseFloat(curState)
        );    
        break;
      case '+':
        cal = String(parseFloat(preState) + parseFloat(curState)
        );    
        break;
      case 'x':
        cal = String(parseFloat(preState) * parseFloat(curState)
        );    
        break;
      case '-':
        cal = String(parseFloat(preState) - parseFloat(curState)
        );    
        break;
        default:
          return
      }
      setPreState(cal)
      setCurState('')
  }
  
  const minusPlos = () => {
    curState
    ?setCurState((pre) => -pre)
    :setPreState((pre) => -pre);
  };


  const percent = () => {
    if(operator === '+'||operator === '-'){
      setCurState(preState*curState/100)
    }
    else{
      curState
      ?setCurState((pre) => pre/100)
      :setPreState((pre) => pre/100); 
    }

  };

  const reset = () => {
    setOperator('');
    setPreState('');
    setCurState('');
    setTotal(false)
  };


  return (
  <div className="head_app">
    <div className='App'>
      <div className='wrapper'>
      <div className='screen'>{(preState || '') + (operator || '') + (curState || '') || 0}</div>
        <div className='button light-gray' onClick={reset}>AC</div>
        <div className='button light-gray' onClick={minusPlos}>+/-</div>
        <div className='button light-gray' onClick={percent}>%</div>
        <div className='button orange' onClick={operatorType}>/</div>
        <div className='button' onClick={inputNum}>7</div>
        <div className='button' onClick={inputNum}>8</div>
        <div className='button' onClick={inputNum}>9</div>
        <div className='button orange' onClick={operatorType}>x</div>
        <div className='button' onClick={inputNum}>4</div>
        <div className='button' onClick={inputNum}>5</div>
        <div className='button' onClick={inputNum}>6</div>
        <div className='button orange' onClick={operatorType}>+</div>
        <div className='button' onClick={inputNum}>1</div>
        <div className='button' onClick={inputNum}>2</div>
        <div className='button' onClick={inputNum}>3</div>
        <div className='button orange' onClick={operatorType}>-</div>
        <div className='zero button' onClick={inputNum}>0</div>
        <div className='button' onClick={inputNum}>.</div>
        <div className='button equals' onClick={equals}>=</div>
      </div>
    </div>
  </div>
  );
}

export default App;
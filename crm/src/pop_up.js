import React, { useState } from "react";
import './pop_up.css'


function Login(props) {
    const [username, setUsername] = useState("")
    const [lestname, setLestname] = useState("")
    const [phonenumber, setPhoneNumber] = useState("")
    const [email, setEmail] = useState("")
    const [class_n, setClass_n] = useState("")

    function handleLogin(e) {
        e.preventDefault()
        // Code to handle login goes here
        props.toggle()
        props.addrow({firstName: username,
            lastName: lestname,
            phoneNumber:phonenumber,
            email:email,
            class_student:class_n
        })
    }
    

    return (
        <div className="popup">
            <div className="popup-inner">
                <h2>add student</h2>
                <form onSubmit={handleLogin} >
                    <label>
                        firstName:
                        <input required='true' type="text" value={username} onChange={e => setUsername(e.target.value)} maxLength={10} pattern="[a-zA-Z]{1,100}" />
                    </label>
                    <label>
                        lestname:
                        <input required='true' type="text" value={lestname} onChange={e => setLestname(e.target.value)} />
                    </label>
                    <label>
                        phoneNumber:
                        <input required='true' type="phonenumber" value={phonenumber} onChange={e => setPhoneNumber(e.target.value)} maxLength={10}/>
                    </label> 
                    <label>
                        e- mail:
                        <input required='true' type="email" value={email} onChange={e => setEmail(e.target.value)} pattern='[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[.]{1}[a-zA-Z]{2,}$'/>
                    </label>                    
                    <label>
                        class:
                        <input required='true' type="number" value={class_n} onChange={e => setClass_n(e.target.value)} />
                    </label>
                    <button type="submit">add</button>
                </form> 
                <button onClick={props.toggle}>cancel</button>
            </div>
        </div>
    )
}
export default Login
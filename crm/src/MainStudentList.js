import React, { useEffect,useState } from 'react';
import './Student_list.css';
import student_list_all from './adapter.js';
import Student from './Student.js';
import './Main_student.css';
import Login from './pop_up.js';





function MainStudentList (){
    const [lsStudent, setLsStudent] = useState([])

    const [seen, setSeen] = useState(false)
    
    function togglePop () {
      setSeen(!seen);
    };
    // function addRow (x) {
    //   setLsStudent([...lsStudent, x]);
    // };
    function del_s(index){
      setLsStudent(lsStudent.filter((_ , ind) => ind !== index));
    };
    const url = "http://localhost:8000/api/data/"

    const delete_student = (id) => {
      fetch(url+id,{
        method:"DELETE",
      })
      .then(fetchUserData)
    };  

    const add_student = (new_student) => {
      fetch(url,{
        method:"POST",
        body:JSON.stringify(new_student),
        headers: {'Content-Type': 'application/json'}
        
    })
    .then(fetchUserData)
  };

    const fetchUserData = () => {
      fetch(url,{
       method: "GET",
      })
      .then((response) => response.json())
      .then((data) => {setLsStudent(data)});
      
    }
    useEffect(() => {
      fetchUserData()

    }, [])
    return (
      
      <div className="page">
        <table>
          <thead className="head title">
            <tr className="">
              List of students
            </tr>
            <tr>
              <th>
                name
              </th>
              <th>
                lest name
              </th>
              <th>
                phoneNumber
              </th>
              <th>
                e- mail
              </th>
              <th>
                class
              </th>
            </tr>        
          </thead>
          <tbody className='body table'>
            {lsStudent.map((oneStudent) => <Student ar_student={oneStudent} del={() => delete_student(oneStudent.id)} edit={() => edit(index)}  />)}
            <td>
              <button onClick={togglePop}>add</button>
              {seen ? <Login toggle={togglePop} addrow={add_student} /> : null}
            </td>
          </tbody>
        </table>
      </div>
    )   
  };


export default MainStudentList;

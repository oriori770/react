import React from "react";
import './adapter.js';
// import delete_item from './adapter.js';



function Student ({ar_student, del, edit}) {
    return(
        <tr className="main">
            <td className="st_f_name">
                {ar_student.firstName}
            </td>
            <td className="st_l_name">
                {ar_student.lastName}
            </td>
            <td className="st_phoneNumber">
                {ar_student.phoneNumber}
            </td>
            <td className="st_email">
                {ar_student.email}
            </td>
            <td className="st_class">
                {ar_student.class_student}
            </td>
            <td>
                <img src="IMG_6345.PNG"   width={20} height={30} className="delete_button" onClick={del}/>
            </td>
            {/* <td>
                <img src="IMG_6345.PNG"   width={20} height={30} className="edit_button" onClick={edit}/>
            </td> */}

        </tr>

    
    )

};

export default Student;




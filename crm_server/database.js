// let student_list_all = [
//     {firstName:"shneor",
//     lastName:"rainitz",
//     phoneNumber:"0587705258",
//     email:"oriori770@gmail.com",
//     class_student:"8"
//     },

    // {firstName:"moshenko",
    // lastName:"rainkkkitz",
    // phoneNumber:"058798258",
    // email:"oriori770@gmail.com",
    // class_student:"6"
    // },

//     {firstName:'shmulik',
//     lastName:'rainitz',
//     phoneNumber:'0578837485',
//     email:'oriori770@gmail.com',
//     class_student:"10"
//     },

//     {firstName:'yakov',
//     lastName:'greenshot',
//     phoneNumber:'0548830375',
//     email:'or@walla.co.il',
//     class_student:"6"
//     }

// ]

// module.exports = student_list_all

var sqlite3 = require('sqlite3').verbose()

const DBSOURCE = "student_list_all.sqlite"

let student_list_all = new sqlite3.Database(DBSOURCE, (err) => {
    if (err) {
      // Cannot open database
      console.error(err.message)
      throw err
    }else{
        console.log('Connected to the SQLite database.')
        student_list_all.run(`CREATE TABLE student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName text, 
            lastName text,
            phoneNumber numeric,
            email text UNIQUE, 
            class_student numeric, 
            CONSTRAINT email_unique UNIQUE (email)
            )`,
        (err) => {
            if (err) {
                // Table already created
            }else{
                // Table just created, creating some rows
                var insert = 'INSERT INTO student (firstName,lastName, phoneNumber, email,class_student) VALUES (?,?,?,?,?)'
                student_list_all.run(insert, ["yakov","greenshot","0548830375","or@walla.co.il","6"])
                student_list_all.run(insert, ["shmulik","rainit","057883748","oriori770@gmail.com","10"])
                student_list_all.run(insert, ["moshenko","rainitz","058798258","oriri770@gmail.co.il","6"])
                student_list_all.run(insert, ["shneor","rainitz","0587705258","770@gmail.com","8"])
                student_list_all.run(insert, ["ori","rainitz","0587705258","770770gg@gmail.com","8"])
            }
        });  
    }
});


module.exports = student_list_all

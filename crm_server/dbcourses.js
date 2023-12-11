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
            name text,
            
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

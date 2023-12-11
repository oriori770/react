
// Create express app
var express = require("express")
var app = express()
var cors = require('cors')
var student_list_all = require("./database.js")
var bodyParser = require('body-parser')


app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))
app.use(cors())
// Server port
var HTTP_PORT = 8000 
// Start server
app.listen(HTTP_PORT, () => {
    console.log("Server running on port %PORT%".replace("%PORT%",HTTP_PORT))
});

app.get("/api/data/:id", (req, res, next) => {
    var sql = "select * from student where id = ?"
    var params = [req.params.id]
    student_list_all.get(sql, params, (err, row) => {
        if (err) {
          res.status(400).json({"error":err.message});
          return;
        }
        res.send({
            "message":"success",
            "data":row
        })
      });
});

app.get("/api/data",(req, res,) => {
    var sql = "select * from student"
    var params = []
    student_list_all.all(sql, params, (err, rows) => {
        if (err) {
          res.status(400).json({"error":err.message});
          return;
        }
        res.send(
            rows
        )
      });
});


app.post("/api/data",(req, res, next) => {
    console.log(req.body)
    var data = {
        firstName:req.body.firstName,
        lastName: req.body.lastName,
        phoneNumber:req.body.phoneNumber,
        email:req.body.email,
        class_student:req.body.class_student
    }

    var sql ='INSERT INTO student (firstName,lastName, phoneNumber, email,class_student) VALUES (?,?,?,?,?)'
    var params =[data.firstName, data.lastName, data.phoneNumber, data.email, data.class_student]
    student_list_all.run(sql, params, function (err, result) {
        if (err){
            res.status(400).json({"error": err.message})
            return;
        }
        res.json({
            "message": "success",
        })
    });
})

app.delete("/api/data/:id", (req, res, next) => {
    student_list_all.run(
        'DELETE FROM student WHERE id = ?',
        req.params.id,  
        console.log(req.params.id),
        function (err, result) {
            if (err){
                res.status(400).json({"error": res.message})
                return;
            }
            res.send({"message":"deleted", changes: this.changes})
    });
})


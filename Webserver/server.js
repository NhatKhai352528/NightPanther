const express = require('express')
const app = express()
const fileUpload = require('express-fileupload')
const net = require('net')

app.use(fileUpload())
app.set('view engine', 'ejs')

const client = net.createConnection({port: '2020'}, () => {})

client.on('data', (data) => {
  if (data.toString() == "reset") {
    printing_code = 0
  }else {
    printing_code = data.toString()
  }
})

printing_code = 0
print_success = 0

app.get('/', function (req, res) {
  if (printing_code != 0) {
    res.render('upload', {printing_code: printing_code})
  }else {
    res.render('waiting_for_rasp', {print_sucess: print_success})
  }
  if (print_success == 1) {
    print_success = 0
  }
})

app.post('/upload', function(req, res) {
    client.write(req.files.customer_file.name)
    req.files.customer_file.mv(__dirname + '/user_file.pdf')
    // res.end()
    printing_code = 0
    print_success = 1
    res.redirect('/')
});

app.listen(3000)

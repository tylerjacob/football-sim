console.log('Hello')
const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const morgan = require('morgan')

const app = express()
app.use(morgan('combine'))
app.use(bodyParser.json())
app.use(cors())

app.get('/status', (req, res) => {
  res.send({
    message: 'hello world!'
  })
})

app.post('/register', (req, res) => {
  res.send({
    message: 'register page!'
  })
})

console.log('listening on port 8081!')
app.listen(process.env.PORT || 8081)

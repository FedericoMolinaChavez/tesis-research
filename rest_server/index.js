const express = require('express')
const bodyParser = require('body-parser')
const path = require('path')
const app = express()
app.use(bodyParser.json())
app.use(express.static(path.join(__dirname, 'public')))
app.use('/uploads', express.static('uploads'))
app.use('/upload', require('./src/up') )

app.listen(8000, () => console.log('Server running on http://localhost:8000/'));
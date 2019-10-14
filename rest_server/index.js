const express = require('express')
const bodyParser = require('body-parser')
const path = require('path')
const users = require('./src/users')
const app = express()
require('dotenv').config();
const moongose = require('mongoose')
moongose.connect('mongodb+srv://isabelmorales:'+process.env.mongoPassword+'@cluster0-blgex.mongodb.net/test?retryWrites=true&w=majority')
app.use(bodyParser.json())
app.use(express.static(path.join(__dirname, 'public')))
app.use('/uploads', express.static('uploads'))
app.use('/upload', require('./src/up') )
app.use('/login', users)
app.listen(8000, () => console.log('Server running on http://localhost:8000/'));
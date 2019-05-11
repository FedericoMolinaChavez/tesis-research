const express = require('express')
const multer = require('multer')
const fs = require("fs");
let router = express.Router()
let spawn = require("child_process").spawn
var ps = require(`python-shell`)
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, './uploads/')
    },
    filename: function (req, file, cb) {
        cb(null, file.originalname)
    }
})
const upload = multer({
    storage: storage
})


router.post('/', upload.single('File'), (req, res, next) => {
   res.json({'message' : 'correctly uploaded'})
})

router.get('/', (req, res, next) => {
    console.log('request done')
    
    let process = spawn('python', ["-u","../../testLoad.py"])
    process.stdout.on('data', function (data){
        console.log(data.toString())
    })
    res.send('puta')
})


module.exports = router
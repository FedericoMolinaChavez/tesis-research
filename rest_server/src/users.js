const express = require('express')
const router = express.Router();
const bcrypt = require('bcryptjs')
const passport = require('passport')
const User = require('../model/User')
const jwt = require('jsonwebtoken')
const {
  ensureAuthenticated
} = require('../config/auth')

/**
 * @module api/user
 * @desc module for managing users password creation and password related operations
 */

 /**
  * This function handles updates for passwords
  * @memberof module:api/user
  * @param {String} email - name of user
  * @param {String} password - password
  * @param {String} password2 - password repeat
  * @returns {JSON} - ans
  */
router.put('/', (req, res, next) => {
  const {
    email,
    password,
    password2
  } = req.body
  let errors = []
  if (!email || !password || !password2) {
    errors.push({
      msg: "please fill in all fields"
    })
  }
  if (password !== password2) {
    errors.push({
      msg: "Passwords do not match"
    })
  }
  if (password.length < 6) {
    errors.push({
      msg: "Password should be at least 6 characters"
    })
  }
  if (errors.length > 0) {
    res.send(errors)
  } else {
    User.findOne({
        email: email
      })
      .then(user => {
        if (!user) {
          res.json({
            'error': 'User doesnt exist'
          })
        } else {
          // Hash Passwords
          console.log(user.email)
          bcrypt.genSalt(12, (err, salt) =>
            bcrypt.hash(password, salt, (err, hash) => {
              console.log(hash)
              User.findOneAndUpdate({email : email},{password: hash}, function (err) {
                if (!err) {
                    res.status(201).json({
                        'message': 'update succesful'
                    })
                } else {
                    res.status(500).json({
                        'message': 'error' + err
                    })
                }
            })
            })
          )
        }
      })
  }
})
/**
 * This function handles the original validation and saving of a new user in the application
 * @memberof module:api/user
 * @param {String} name - name of user
 * @param {String} email - email of user
 * @param {String} password - password
 * @param {String} password2 - repeat password
 * @returns {JSON} - msg
 */
router.post('/', (req, res) => {
  const {
    name,
    email,
    password,
    password2
  } = req.body;
  let errors = []
  console.log(password)
  if (!name || !email || !password || !password2) {
    errors.push({
      msg: "please fill in all fields"
    })
  }
  if (password !== password2) {
    errors.push({
      msg: "Passwords do not match"
    })
  }
  if (password.length < 6) {
    errors.push({
      msg: "Password should be at least 6 characters"
    })
  }

  if (errors.length > 0) {
    res.send(errors)
  } else {
    User.findOne({
        email: email
      })
      .then(user => {
        console.log('aquí')
        if (user) {
          errors.push({
            msg: 'Email already in use'
          })
          res.send(errors)
        } else {
          console.log('si entra')
          const newUser = new User({
            name,
            email,
            password,

          })
          // Hash Passwords
          bcrypt.genSalt(12, (err, salt) =>
            bcrypt.hash(newUser.password, salt, (err, hash) => {
              if (err) throw err;
              //Set password to hashed
              newUser.password = hash;
              newUser.save()
                .then(user => {
                  console.log(user)
                  res.json({
                    msg: 'succesfull'
                  })
                })
                .catch(err => console.log(err))
            }))
        }
      })
      .catch(err => console.log(err))
    //res.send('pass')
  }
})
/**
 * Basic functionality to assert a login
 * @memberof module:api/user 
 * @param {String} email - users email 
 * @param {String} password - password of user
 * @returns {jwt} - token 
 */
router.post('/login', passport.authenticate('local', {
  session: false
}), (req, res, next) => {
  console.log(req.user)
  const token = jwt.sign(req.user.toJSON(), 'your_jwt_secret')
  const user = req.user.toJSON()
  return res.json({
    user,
    token
  })
})
/**
 * function to validate jwt
 * @memberof module:api/user
 * @param {jwt} token - jwt token
 * @returns {JSON} - msg
 */
router.get('/', passport.authenticate('jwt', {
  session: false
}), (req, res, next) => {
  console.log('tried')
  res.json({
    msg: 'it validates'
  })
})

module.exports = router
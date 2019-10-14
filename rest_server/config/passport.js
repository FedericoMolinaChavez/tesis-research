const passport = require('passport');
const localStrategy = require('passport-local').Strategy
const mongoose = require('mongoose')
const bcrypt = require('bcryptjs')
var JwtStrategy = require('passport-jwt').Strategy,
    ExtractJwt = require('passport-jwt').ExtractJwt;

//load user model
const User = require('../model/User');


  passport.use(
    new localStrategy({ usernameField: 'email'}, (email, password, done) => {
      User.findOne({email: email})
        .then(user => {
          if(!user){
            return done(null, false, {message: 'that email is not registered'});
          }
          bcrypt.compare(password, user.password, (err, isMatch) => {
            console.log(isMatch)
            console.log(password)
            console.log(user.password)
            if(err) throw err;
            if(isMatch){
              return done(null, user)
            }
            else{
              return done(null, false, {message: 'password incorrect'})
            }
          })
        })
        .catch(err => console.log(err))
    })
  )
  passport.use(new JwtStrategy({
        jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
        secretOrKey   : 'your_jwt_secret'
    },
    function (jwtPayload, done) {

      User.findOne({id: jwtPayload.sub}, function(err, user) {
        if (err) {
            return done(err, false);
        }
        if (user) {
            return done(null, user);
        } else {
            return done(null, false);
            // or you could create a new account
        }
    });
    }
));

  passport.serializeUser((user, done) => {
      done(null, user.id);
  });
  passport.deserializeUser((id, done) => {
    User.findById(id, (err, user) => {
      done(err, user)
    })})
module.exports = passport

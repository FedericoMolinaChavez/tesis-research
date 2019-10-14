module.exports = {
  ensureAuthenticated: function(req, res, next){
    if(req.isAuthenticated()){
      console.log('enters')
      return next()
    }
    console.log('authenticate')
    res.json({mess : 'authenticate'})
  }
}

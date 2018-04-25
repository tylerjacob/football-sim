const {User} = require('../models')
const config = require('../config/config')

module.exports = {
  async register (req, res) {
    try {
      const user = await User.create(req.body)
      res.send(user.toJSON())
    } catch (err) {
      res.status(400).send({
        error: 'email already in use'
      })
    }
  },
  async login (req, res){
    try {
      console.log(req.body)
      const {email, password} = req.body
      const user = await User.findOne({
        where: {
          email: email
        }
      })
      console.log(user)
      if (!user){
        return res.status(403).send({
          error: "The User login information was incorrect"
        })
      }
      console.log("AHHHHHHHHHHHHHHHHH")
      const isPasswordValid = password === user.password
      console.log(isPasswordValid)
      if (!isPasswordValid){
        return res.status(403).send({
          error: "The Password login information was incorrect"
        })
      }
      const userJson = user.toJSON()
      res.send({
        user: userJson
      })  
  } catch (err) {
    res.status(500).send({
      error: 'An error has occured while trying to login'
      })
    }
  }
}


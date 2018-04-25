const Joi = require('joi')

module.exports = {
  register (req, res, next) {
    const schema = {
      email: Joi.string().email(),
      password: Joi.string().regex(
        new RegExp('^[a-zA-Z0-9]{8,32}$')
      )
    }

    const {error} = Joi.validate(req.body, schema)

    if (error) {
      switch (error.details[0].context.key) {
        case 'email':
          res.status(400).send({
            error: 'Must be a valid email address'
          })
          break
        case 'password':
          res.status(400).send({
            error: `The password failed to meet the following requirements
                <br>
                1. must contain at least 6 charecters
                <br>
                2. must ONLY contain the following charecters: lowercase, uppercase, numeric values of 0-9
               `
          })
          break
        default:
          res.status(400).send({
            error: 'Invalid registration information'
        })
      }
    } else {
      next()
    }
  }
}

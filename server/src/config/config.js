const path = require('path')

module.exports = {
  port: process.env.PORT || 8082,
  db: {
    database: process.env.DB_NAME || 'football-sim',
    user: process.env.DB_USER || 'football-sim',
    password: process.env.DB_PASS || 'football-sim',
    options: {
      dialect: process.env.DIALECT || 'sqlite',
      host: process.env.HOST || 'localhost',
      storage: path.resolve(__dirname, '../../football-sim.sqlite')
    }
  }
}

<template>

  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs10>
            <v-card flat class="elevation-10">
              <v-toolbar dark color="cyan">
                <v-spacer></v-spacer>
                <v-toolbar-title dark>Enter Login Information</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-tooltip bottom>
                </v-tooltip>
              </v-toolbar>
                <div class="pr-4 pl-4 pt-2 pb-2">
                    <input
                    type="email"
                    name="email"
                    v-model="email"
                    placeholder="email" >
                    <br>
                    <input
                    type="password"
                    name="password"
                    v-model="password"
                    placeholder="password" >
                    <br>
                    <div class="error" v-html="error"/>
                    <br>
                    <v-spacer></v-spacer>
                  <v-btn @click="register" color="cyan">Login</v-btn>
                </div>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>

</template>

<script>
import AuthenticationService from '@/services/authenticationService.js'
export default {
  data () {
    return {
      email: 'abc@gmail.com',
      password: 'password',
      error: null
    }
  },
  methods: {
    async register () {
      try {
        await AuthenticationService.register({
          email: this.email,
          password: this.password
        })
      } catch (error) {
        this.error = error.response.data.error
      }
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.error {
  color: red;
}
.cards {
  padding: 0 0 10em 10em
}
</style>

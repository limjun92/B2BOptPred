<template>
  <!-- <div class="container"> -->
    <!-- <div class="col-lg-12 col-md-6 ml-auto mr-auto"> -->
      <form @submit.prevent="login">
        <card class="card-login card-white">
          <template slot="header">
            <img src="img/card-primary.png" alt="" />
            <h1 class="card-title">Log in</h1>
          </template>

          <div>
            <base-input
              v-validate="'required|email'"
              name="email"
              :error="getError('email')"
              v-model="model.email"
              placeholder="Email"
              addon-left-icon="tim-icons icon-email-85"
            >
            </base-input>

            <base-input
              v-validate="'required|min:5'"
              name="password"
              :error="getError('password')"
              v-model="model.password"
              type="password"
              placeholder="Password"
              addon-left-icon="tim-icons icon-lock-circle"
            >
            </base-input>
          </div>

          <div slot="footer">
            <base-button native-type="submit" type="primary" class="mb-3" size="lg" block>
              Get Started
            </base-button>
            <div class="pull-left">
                <div v-on:click = "openRegiModals">
                  Create Account
                </div>
            </div>
          </div>
        </card>
      </form>
</template>
<script>
export default {
  data() {
    return {
      model: {
        email: '',
        password: '',
        subscribe: true
      }
    };
  },
  methods: {
    getError(fieldName) {
      return this.errors.first(fieldName);
    },
    async login() {
      let isValidForm = await this.$validator.validateAll();
      if (isValidForm) {
        // TIP use this.model to send it to api and perform login call
      }
    },
    openRegiModals(){
      this.$store.commit('openRegiModal', true);
      this.$store.commit('openLoginModal', false);
    }
  }
};
</script>
<style>
.navbar-nav .nav-item p {
  line-height: inherit;
  margin-left: 5px;
}
</style>

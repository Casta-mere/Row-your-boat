<template>
  <view class="content">
    <v-card>
      <image :src="src"> </image>
      <v-card-title>You are now renting boat #{{ id }}</v-card-title>

      <v-card-subtitle class="pb-0">Renting time is {{ time }}</v-card-subtitle>

      <v-card-text class="text--primary">
        <div>Rented for {{ minute }} minute(s) {{ second }} second(s)</div>
      </v-card-text>

      <v-card-actions>
        <v-btn class="button" rounded @click="returnboat()">Return</v-btn>
      </v-card-actions>
      <v-card-title v-if="paging ^ warning" class="pb-2"
        >Reply in 2 min!</v-card-title
      >
      <v-card-title v-if="warning" class="pb-3">Reply in 2 min!</v-card-title>
      <v-card-actions>
        <v-btn class="button" v-if="paging" rounded @click="answer()"
          >Copy!</v-btn
        >
      </v-card-actions>
    </v-card>
  </view>
</template>

<script>
export default {
  data() {
    return {
      id: "",
      src: "",
      time: "",
      rent_time: 0,
      minute: 0,
      second: 0,
      paging: false,
      warning: false,
    };
  },
  onShow() {
    this.id = this.$route.query.id;
    this.rent_time = this.$route.query.rent_time;
    this.src = "/static/img/boats/Boat" + this.id + ".png";
    if (this.$route.query.type == 1) this.time = this.nowtime();
    else this.time = this.$route.query.time;
    if (this.id != 2) {
      let timer = setTimeout(() => {
        clearTimeout(timer);
        this.paging = true;
      }, 10000);
    }
  },

  mounted() {
    let _this = this;
    let timer = setInterval(() => {
      _this.rent_time = _this.rent_time + 1;
      _this.second = _this.rent_time % 60;
      _this.minute = (_this.rent_time - _this.second) / 60;
    }, 1000);
    let timer2 = setInterval(() => {
      if (!this.paging) {
        this.warning = false;
      }
      if (this.paging) {
        let timer3 = setTimeout(() => {
          clearTimeout(timer3);
          if (this.paging) this.warning = true;
        }, 10000);
      }
      if (this.paging && this.warning) {
        let timer4 = setTimeout(() => {
          clearTimeout(timer4);
          if (this.paging & this.warning)
            // console.log("You have not replied in 2 minutes!");
            clearInterval(timer2);
          this.$router.push({
            path: "/pages/404/404",
          });
        }, 10000);
      }
    }, 1000);
  },
  onunload() {
    clearInterval(timer2);
    console.log("leave");
  },
  methods: {
    nowtime() {
      var date = new Date();
      var year = date.getFullYear();
      var month = date.getMonth() + 1;
      var day = date.getDate();
      var hour = date.getHours();
      var minute = date.getMinutes();
      var second = date.getSeconds();
      this.timeunix = Date.parse(date);
      return (
        year +
        "-" +
        month +
        "-" +
        day +
        " " +
        hour +
        ":" +
        minute +
        ":" +
        second
      );
    },
    returnboat() {
      this.$axios
        .post("http://10.96.229.74:8888/", {
          message: this.id + " " + "U",
        })
        .then((res) => {
          const { status, data } = res;
          if (status === 200) {
            console.log(data);
          } else console.log("not success");
        });
      this.$router.push({
        path: "/pages/Me/Me",
      });
    },
    answer() {
      this.paging = false;
      let timer = setTimeout(() => {
        clearTimeout(timer);
        this.paging = true;
      }, 10000);
    },
  },
};
</script>

<style>
.content {
  display: flex;
  /* flex-direction: column; */
  /* align-items: center; */
  justify-content: center;
}

.logo {
  height: 500rpx;
  width: 500rpx;
  margin-top: 100rpx;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 50rpx;
}

.text-area {
  display: flex;
  justify-content: center;
}

.title {
  font-size: 36rpx;
  color: #8f8f94;
}

.question {
  font-size: 50rpx;
  color: brown;
}

.button {
  border-radius: 4px;
  background-color: #f4511e;
  border: none;
  color: black;
  text-align: center;
  font-size: 10px;
  padding: 15px;
  width: 150px;
  transition: all 0.5s;
  cursor: pointer;
  margin: auto;
}
.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

.button span:after {
  content: "\00bb";
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}

.button:hover span {
  padding-right: 25px;
}

.button:hover span:after {
  opacity: 1;
  right: 0;
}

.button:active {
  background-color: #0e5390;
  color: white;
  box-shadow: 0 5px #666;
  transform: translateY(5px);
}
.pb-2 {
  color: red;
  text-align: center;
  margin: auto;
  /* background-color: red; */
}
.pb-3 {
  color: black;
  text-align: center;
  margin: auto;
  background-color: red;
}
</style>

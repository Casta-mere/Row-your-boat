<template>
  <view class="content">
    <v-card>
      <image :src="src"> </image>
      <v-card-title>You are now renting boat #{{ id }}</v-card-title>

      <v-card-subtitle class="pb-0">Renting time is {{ time }}</v-card-subtitle>

      <v-card-text class="text--primary">
        <div>Rented for {{ minute }} minute(s) {{second}} second(s) </div>
      </v-card-text>

      <v-card-actions>
        <v-btn class="button" rounded @click=returnboat()>Return</v-btn>
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
      minute:0,
      second:0,
    };
  },
  onShow() {
    this.id = this.$route.query.id;
    this.src = "/static/img/boats/Boat" + this.id + ".png";
    this.time = this.nowtime();
  },
  mounted() {
    let _this = this;
    this.timer = setInterval(() => {
      _this.rent_time = _this.rent_time + 1;
      _this.second = _this.rent_time%60;
      _this.minute = (_this.rent_time-_this.second)/60;
    }, 1000);
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
    returnboat(){
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
    }
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
  color: #4caf50;
  outline: none;
  text-align: center;
  margin: auto;
}
</style>

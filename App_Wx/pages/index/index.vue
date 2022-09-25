<template>
  <!-- <view class="content">
    <image class="logo" src="/static/logo.png"></image>
    <view class="text-area">
      <text class="title">{{ title }} is Crazy \n</text>
    </view>
    <navigator :url="url">to 404</navigator>
    <view class="question">
      <navigator url="/subPackages/Question_1/Question_1">前往问题1</navigator>
      <button @click="getuserList()">114514</button>
    </view>
  </view> -->

  <v-data-table
    data-app="true"
    :headers="headers"
    :items="desserts"
    :sort-by="['calories', 'fat']"
    :sort-desc="[false, true]"
    multi-sort
    align="center"
  ></v-data-table>
</template>

<script>
export default {
  data() {
    return {
      title: "Crazy frog",
      url: "/pages/404/404",
      dialog: false,
      msg: [],
      headers: [
        {
          text: "Boat Number",
          sortable: false,
          value: "name",
        },
        { text: "AM/PM", value: "AP" },
        { text: "Rent Times", value: "RT" },
        { text: "Total time(min)", value: "TT" },
        { text: "Average time(min)", value: "AT" },
        { text: "Max time(min)", value: "MT" },
        { text: "Status", value: "s" },
      ],
      desserts: [],
    };
  },
  mounted() {
    this.timer = setInterval(() => {
      this.$axios
        .post("http://10.96.229.74:8888/", {
          message: "1 " + "D",
        })
        .then((res) => {
          const { status, data } = res;
          if (status === 200) {
            var string = data.toString();
            // console.log(string);
            var ans = [];
            ans = string.split(", '*'], [");
            ans[0] = ans[0].split("[[")[1];
            ans[ans.length - 1] = ans[ans.length - 1].split(", '*']]")[0];
            this.desserts=[];
            for (let i = 0; i < ans.length; i++) {
              var value = ans[i].split(",");
              var item1 = {};
              item1.name = "Boat#" + value[0];
              item1.AP = "Total";
              if (value[1] == 0) item1.s = "Available";
              else if (value[1] == 1) item1.s = "Unavailable";
              else if(value[1]==2) item1.s="Lost";
              item1.RT = value[2];
              item1.TT = value[3];
              item1.AT = value[4];
              item1.MT = value[5];

              var item2 = {};
              item2.name = "Boat#" + value[0];
              item2.AP = "AM";
              item2.s = "-";
              item2.RT = value[6];
              item2.TT = value[7];
              item2.AT = value[8];
              item2.MT = value[9];
              var item3 = {};
              item3.name = "Boat#" + value[0];
              item3.AP = "PM";
              item3.s = "-";
              item3.RT = value[10];
              item3.TT = value[11];
              item3.AT = value[12];
              item3.MT = value[13];

              this.desserts.push(item1);
              this.desserts.push(item2);
              this.desserts.push(item3);
            }
          } else console.log("not success");
        });
    }, 10000);
  },
  onShow() {
    console.log("Index page show");
  },

  onPullDownRefresh() {
    console.log("Index page onPullDownRefresh");
    let timer = setTimeout(() => {
      clearTimeout(timer);
      console.log("back to index");
      uni.switchTab({
        url: "/pages/index/index",
        animationType: "pop-in",
        animationDuration: 300,
      });
    }, 2000);
  },

  methods: {
    getuserList() {
      this.$axios
        .post("http://10.96.229.74:8888/", { message: "hell" })
        .then((res) => {
          const { status, data } = res;
          if (status === 200) {
            this.userList = data;
            console.log(this.userList);
          } else console.log("not success");
        });
    },
  },
};
</script>

<style>
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.logo {
  height: 200rpx;
  width: 200rpx;
  margin-top: 200rpx;
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
</style>

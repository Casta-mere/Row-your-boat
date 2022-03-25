<template>
  <view class="content">
    <image class="logo" src="/static/logo.png"></image>
    <view class="text-area">
      <text class="title">{{ title }} is Crazy \n</text>
    </view>
    <navigator :url="url">to 404</navigator>
    <view class="question">
      <navigator url="/subPackages/Question_1/Question_1"
        >前往问题1</navigator
      ></view
    >
  </view>
</template>

<script>
export default {
  data() {
    return {
      title: "Crazy frog",
      url: "/pages/404/404",
    };
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
  methods: {},
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

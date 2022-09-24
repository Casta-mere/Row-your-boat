<template>
  <view class="content">
    <image class="logo" src="/static/warning.png"></image>
    <text>Boat is not Available!</text>
  </view>
</template>

<script>
export default {
  data() {
    return {
      title: "Warning!",
    };
  },
  onShow() {
    let timer = setTimeout(() => {
      clearTimeout(timer);
      console.log("back to index");
      uni.switchTab({
        url: "/pages/Me/Me",
        animationType: "pop-in",
        animationDuration: 300
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
  font-size: 50rpx;
  color: red;
}
.logo {
  height: 480rpx;
  width: 520rpx;
  margin-top: 100rpx;
  margin-left: auto;
  margin-right: auto;
  /* margin-bottom: 50rpx; */
}
</style>

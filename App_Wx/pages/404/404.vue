<template>
  <view class="content">
    <text>404 not found!</text>
  </view>
</template>

<script>
export default {
  data() {
    return {
      title: "404 not found!",
    };
  },
  onShow() {
    let timer = setTimeout(() => {
      clearTimeout(timer);
      console.log("back to index");
      uni.switchTab({
        url: "/pages/index/index",
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
}
</style>

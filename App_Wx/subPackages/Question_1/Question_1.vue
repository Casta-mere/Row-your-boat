<template>
  <scroll-view class="main">
    <view
      ><image class="img" src="/static/Question/Q1/Question.png"></image>
    </view>
    <text class="Front"> 延安革命纪念馆 </text>
    <text>
      位于陕西省延安市宝塔区西北延河东岸，为国家AAAA级景区。整个纪念馆外观朴素大方，结构紧凑，高大宏伟，具有传统的民族风格，展馆正门上方悬挂着红色匾牌，上有郭沫若1971年来延参观时题写的馆名。\n
      馆内主要介绍1937年10月至1948年3月将近12年间，党中央和毛泽东同志在延安和陕甘宁边区领导中国人民英勇斗争的光辉历史，同时介绍了毛泽东、刘少奇、周恩来、朱德等老一辈与无产阶级革命家的丰功伟绩，介绍了马克思列宁主义和中国革命具体实践相结合的毛泽东思想。
    </text>
    <text>
      位于陕西省延安市宝塔区西北延河东岸，为国家AAAA级景区。整个纪念馆外观朴素大方，结构紧凑，高大宏伟，具有传统的民族风格，展馆正门上方悬挂着红色匾牌，上有郭沫若1971年来延参观时题写的馆名。\n
      馆内主要介绍1937年10月至1948年3月将近12年间，党中央和毛泽东同志在延安和陕甘宁边区领导中国人民英勇斗争的光辉历史，同时介绍了毛泽东、刘少奇、周恩来、朱德等老一辈与无产阶级革命家的丰功伟绩，介绍了马克思列宁主义和中国革命具体实践相结合的毛泽东思想。 </text
    ><view>
      <button class="button" @click="back">◀返回首页</button>
      <button class="button" @click="back" style="right: 20px">
        下一关卡▶
      </button>
    </view>
  </scroll-view>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    back: function () {
      let timer = setTimeout(() => {
        clearTimeout(timer);
        console.log("back to index");
        uni.switchTab({
          url: "/pages/index/index",
          animationType: "pop-in",
          animationDuration: 300,
        });
      }, 500);
    },
  },
};
</script>

<style>
.main {
  background-color: #e47676;
  font-size: 20px;
  height: auto;
  width: auto;
  padding-left: 20px;
  padding-right: 20px;
}
.Front {
  font-size: 30px;
}

.img {
  margin-top: 10px;
  border-radius: 8px;
  display: block;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}

.button {
  position: fixed;
  bottom: 0;
  bottom: constant(safe-area-inset-bottom);
  bottom: env(safe-area-inset-bottom);
  display: inline-block;
  border-radius: 20px;
  background-color: #504e4e;
  border: none;
  color: #ffffff;
  text-align: center;
  font-size: 20px;
  width: 150px;
  transition: all 0.2s;
  cursor: pointer;
  margin: 5px;
}

.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.2s;
}

.button span:after {
  content: "\00bb";
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.2s;
}

.button:hover span {
  padding-right: 25px;
}

.button:hover span:after {
  opacity: 1;
  right: 0;
}

.button:active {
  background-color: #3e8e41;
  box-shadow: 0 5px #666;
  transform: translateY(5px);
}
</style>

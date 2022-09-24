<template>
  <view class="content">
    <image class="logo" :src="src"></image>
    <view class="title">My rent {{ id }}</view>

    <v-card class="mx-auto" max-width="400">
      <v-img
        class="white--text align-end"
        height="200px"
        :src=src
      >
        <v-card-title>Top 10 Australian beaches</v-card-title>
      </v-img>

      <v-card-subtitle class="pb-0">Number 10</v-card-subtitle>

      <v-card-text class="text--primary">
        <div>Whitehaven Beach</div>

        <div>Whitsunday Island, Whitsunday Islands</div>
      </v-card-text>

      <v-card-actions>
        <v-btn color="orange" text> Share </v-btn>

        <v-btn color="orange" text> Explore </v-btn>
      </v-card-actions>
    </v-card>
  </view>
</template>

<script>
// import { VCard, VImg, VCardTitle, VCardSubtitle, VCardText, VCardActions, VBtn } from "vuetify/lib";
export default {
  data() {
    return {
      id: "",
      src: "",
    };
  },
  onShow() {
    this.id = this.$route.query.id;
    this.src = "/static/img/boats/Boat" + this.id + ".png";
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
</style>

<template>
  <view class="content">
    <image class="logo" :src="src"></image>
    <view class="title">My rent {{ id }}</view>

    <el-card>
      <div slot="header" class="clearfix">
        <i class="el-icon-user" /><span style="margin-left: 5px">123</span>
        <div
          style="display: inline-block; float: right; cursor: pointer"
          @click="doEdit(id)"
        >
          <el-tooltip effect="dark" content="编辑角色" placement="top">
            <i class="el-icon-edit-outline" style="margin-left: 15px" />
          </el-tooltip>
        </div>
      </div>
      <div>
        <ul class="role-info">
          <li>
            <div class="role-left">描述信息：</div>
          </li>
          <li>
            <div class="role-left">
              创建时间：{{ src }}
            </div>
          </li>
        </ul>
      </div>
    </el-card>
  </view>
</template>

<script>
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

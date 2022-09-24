<template>
  <view class="uni-product-list">
    <view
      class="uni-product"
      v-for="(product, index) in productList"
      :key="index"
    >
      <view class="image-view">
        <image
          v-if="renderImage"
          class="uni-product-image"
          :src="product.image"
          @click="func(product)"
        ></image>
      </view>
      <view class="uni-product-title">{{ product.title }}</view>
      <view class="uni-product-price">
        <text class="uni-product-price-favour">{{ product.status }}</text>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      url: "/pages/index/index",
      title: "product-list",
      productList: [],
      renderImage: false,
    };
  },
  methods: {
    loadData(action = "add") {
      const data = [
        {
          image: "/static/img/boats/Boat1.png",
          title: "Boat#1",
          status: "Available",
        },
        {
          image: "/static/img/boats/Boat2.png",
          title: "Boat#2",
          status: "Available",
        },
        {
          image: "/static/img/boats/Boat3.png",
          title: "Boat#3",
          status: "Available",
        },
        {
          image: "/static/img/boats/Boat4.png",
          title: "Boat#4",
          status: "Available",
        },
        {
          image: "/static/img/boats/Boat5.png",
          title: "Boat#5",
          status: "Available",
        },
        {
          image: "/static/img/boats/Boat6.png",
          title: "Boat#6",
          status: "Available",
        },
      ];

      if (action === "refresh") {
        this.productList = [];
      }

      data.forEach((item) => {
        this.productList.push(item);
      });
    },
    func(product) {
      console.log(product.title);
      this.$axios
        .post("http://10.96.229.74:8888/", { message: product.title+" "+product.status[0] })
        .then((res) => {
          const { status, data } = res;
          if (status === 200) {
            this.userList = data;
            console.log(this.userList);
          } else console.log("not success");
        });
      if (product.status == "Available") {
        product.status = "Unavailable";
        product.image = "/static/img/boats2/Boat"+product.title[5]+".png";
      } else {
        product.status = "Available";
        product.image = "/static/img/boats/Boat"+product.title[5]+".png";
      }
      this.$router.push({
        path: "/pages/Me/boat",
        query: {
          id: product.title[5],
        },
      });
    },
  },
  onLoad() {
    this.loadData();
    setTimeout(() => {
      this.renderImage = true;
    }, 300);
  },
  onPullDownRefresh() {
    this.loadData("refresh");
    // 实际开发中通常是网络请求，加载完数据后就停止。这里仅做演示，加延迟为了体现出效果。
    setTimeout(() => {
      uni.stopPullDownRefresh();
    }, 2000);
  },
  // onReachBottom() {
  //     this.loadData();
  // }
};
</script>

<style>
/* product */
page {
  background: #f8f8f8;
}

view {
  font-size: 28upx;
}

.uni-product-list {
  display: flex;
  width: 100%;
  flex-wrap: wrap;
  flex-direction: row;
}

.uni-product {
  padding: 20upx;
  display: flex;
  flex-direction: column;
}

.image-view {
  height: 330upx;
  width: 330upx;
  margin: 12upx 0;
}

.uni-product-image {
  height: 330upx;
  width: 330upx;
}

.uni-product-title {
  width: 300upx;
  word-break: break-all;
  display: -webkit-box;
  overflow: hidden;
  line-height: 1.5;
  text-overflow: ellipsis;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}

.uni-product-price {
  margin-top: 10upx;
  font-size: 28upx;
  line-height: 1.5;
  position: relative;
}

.uni-product-price-original {
  color: #e80080;
}

.uni-product-price-favour {
  color: #0b0404;
}

.uni-product-tip {
  position: absolute;
  right: 10upx;
  background-color: #ff3333;
  color: #ffffff;
  padding: 0 10upx;
  border-radius: 5upx;
}
</style>

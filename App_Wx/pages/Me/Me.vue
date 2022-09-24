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
      states: [],
    };
  },
  methods: {
    refresh() {
      this.$axios
        .post("http://10.96.229.74:8888/", { message: "0 L" })
        .then((res) => {
          const { status, data } = res;
          if (status === 200) {
            var string = data.toString();

            this.states = string.split(",");
            console.log(this.states);
          } else console.log("not success");
        });
    },
    loadData(action = "add") {
      this.productList = [];
      const data = [
        {
          image: "/static/img/boats/Boat1.png",
          title: "Boat#1",
          status: "",
        },
        {
          image: "/static/img/boats/Boat2.png",
          title: "Boat#2",
          status: "",
        },
        {
          image: "/static/img/boats/Boat3.png",
          title: "Boat#3",
          status: "",
        },
        {
          image: "/static/img/boats/Boat4.png",
          title: "Boat#4",
          status: "",
        },
        {
          image: "/static/img/boats/Boat5.png",
          title: "Boat#5",
          status: "",
        },
        {
          image: "/static/img/boats/Boat6.png",
          title: "Boat#6",
          status: "",
        },
      ];
      for (let i = 0; i < 6; i++) {
        if (this.states[i] == 0) data[i].status = "Available";
        else {
          data[i].status = "Unavailable";
          data[i].image = "/static/img/boats2/Boat" + (i + 1) + ".png";
        }
      }
      if (action === "refresh") {
        this.productList = [];
      }

      data.forEach((item) => {
        this.productList.push(item);
      });
    },
    func(product) {
      console.log(product.title);

      if (product.status == "Available") {
        this.$axios
          .post("http://10.96.229.74:8888/", {
            message: product.title + " " + product.status[0],
          })
          .then((res) => {
            const { status, data } = res;
            if (status === 200) {
              console.log(data);
            } else console.log("not success");
          });
        product.status = "Unavailable";
        product.image = "/static/img/boats2/Boat" + product.title[5] + ".png";
        this.$router.push({
          path: "/pages/Me/boat",
          query: {
            id: product.title[5],
          },
        });
      } else {
        // this.$router.push({
        //   path: "/pages/Me/boat",
        //   query: {
        //     id: product.title[5],
        //   },
        // });
        // product.status = "Available";
        // product.image = "/static/img/boats/Boat" + product.title[5] + ".png";
      }
    },
  },
  onLoad() {
    this.onShow();
  },
  onPullDownRefresh() {
    this.$axios
      .post("http://10.96.229.74:8888/", { message: "0 L" })
      .then((res) => {
        const { status, data } = res;
        if (status === 200) {
          this.states = data;
          console.log(this.states);
        } else console.log("not success");
      });
  },
  onShow() {
    setTimeout(() => {
      this.refresh();
    }, 50);
    console.log(this.states);

    setTimeout(() => {
      this.loadData();
    }, 100);
    setTimeout(() => {
      this.renderImage = true;
    }, 150);
  },
};
</script>

<style>
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

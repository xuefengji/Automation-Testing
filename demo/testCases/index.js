/*
author: xuefengji
describe: 从首页进入单次商品详情页，再从商品详情页进入定单结算页
*/
const getOneProduct = require('../handle/getProduct')
const singleBuy = require('../handle/singleBuy')
const orderPay = require('../handle/orderPay')
async function indexToOrder(miniProgram){
     //获取首页或全部商品页的任意商品
      await getOneProduct(miniProgram)
      //从商品详情页进入订单结算页
      await singleBuy(miniProgram)
      //进入支付页
      await orderPay(miniProgram)
      const currentPage = await miniProgram.currentPage()
      console.log(await currentPage.path)
      if(await currentPage.path == 'pages/payCenter/index'){
            console.log('生成订单成功，用例结束')
      }
      
}
module.exports = indexToOrder


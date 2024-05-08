export interface IProduct {
  product_id: string;
  product_type: string;
  product_name: string;
  price: number;
  sale_price: number;
  blurb: string;
  stock_quantity: number;
  image_url: string;
}

export class Product implements IProduct {
  product_id: string;
  product_type: string;
  product_name: string;
  sale_price: number;
  price: number;
  blurb: string;
  stock_quantity: number;
  image_url: string;

  constructor(product: IProduct) {
    this.product_id = product.product_id;
    this.product_type = product.product_type;
    this.product_name = product.product_name;
    this.price = product.price;
    this.sale_price = product.sale_price;
    this.blurb = product.blurb;
    this.stock_quantity = product.stock_quantity;
    this.image_url = product.image_url;
  }
}

export interface IOrderItem {
  id: number;
  order_id: number;
  product_id: number;
  quantity: number;
}

export interface IOrder {
  id: number;
  user_id: number;
  created_at: Date;
  items: IOrderItem[];
}

export interface IReview {
  id: number;
  product_id: number;
  author_id: number;
  content: string;
  rating: number;
}

export interface IUser {
  id: number;
  username: string;
  email: string;
  is_active?: boolean; // Optional
}

export default {};

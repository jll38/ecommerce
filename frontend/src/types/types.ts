export interface IProduct {
  product_id: string;
  product_type: string;
  product_name: string;
  price: number;
  description?: string; // Optional
  stock_quantity: number;
  image_url?: string; // Optional
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
  
  
  
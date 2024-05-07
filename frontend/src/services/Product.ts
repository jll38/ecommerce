import { BACKEND_URL } from "../constants";

export const getProductInfo = async (productID: string) => {
  try {
    const product = await fetch(`${BACKEND_URL}/products/${productID}`).then(
      (res) => res.json()
    );
    return product;
  } catch (err) {
    console.error("Error fetching product information");
  }
};

interface IGetProductList {
  page: Number;
  limit: Number;
  type: string;
}

export const getProductList = async ({page, limit, type} : IGetProductList) => {
    
};

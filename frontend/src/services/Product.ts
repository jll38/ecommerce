import { BACKEND_URL } from "../constants";

export const getProductInfo = async (productID: string) => {
  const product = await fetch(`${BACKEND_URL}/products/${productID}`).then(
    (res) => res.json()
  );
  return product;
};
